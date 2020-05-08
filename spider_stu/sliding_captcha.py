# 滑动验证码识别，以 B 站为例
# 使用 selenium
import random
import time
from io import BytesIO

import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from PIL import Image

url = "https://passport.bilibili.com/login"
brow = webdriver.Safari()


def compare(img1, img2, x, y):
    # 比对图像，返回的为 RGB
    p1 = img1.load()[x, y]
    p2 = img2.load()[x, y]

    # 阈值
    th = 60
    if abs(p1[0] - p2[0]) < th and abs(p1[1] - p2[1]) < 60 and abs(p1[2] - p2[2]) < 60:
        return True
    return False


def crop_image(image_name):
    time.sleep(3)
    # 截取图片
    img = brow.find_element_by_xpath("//div[@class='gt_box']")
    locat = img.location
    size = img.size

    top, bottom, left, right = locat["y"], locat["y"] + size["height"], locat["x"], locat["x"] + size["width"]
    screenshot = brow.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot))
    # 截取图片
    captcha = screenshot.crop((left, top, right, bottom))
    captcha.save(image_name)
    return captcha


def smooth_move(left: int):
    # 模拟人的平滑移动
    # 一开始加速，然后减速，生长曲线，需要加入随机（趋势加速）
    track = []  # 移动轨迹
    current = 0  # 当前位移
    mid = left * 3 / 4  # 减速阈值
    # 间隔时间
    t = 0.1
    v = 0
    while current < left:
        if current < mid:
            a = random.randint(2, 3)
        else:
            a = -random.randint(6, 7)
        v0 = v
        # 当前速度
        v = v0 + a*t
        # 移动距离
        move = v0*t + 1/2 * a * t * t
        # 当前位移
        current += move
        track.append(round(move))
    return track


def login():
    username = "mps"
    pwd = "123.."
    brow.get(url)
    brow.maximize_window()

    username_input = brow.find_element_by_id("login-username")
    pwd_input = brow.find_element_by_id("login-passwd")
    username_input.send_keys(username)
    pwd_input.send_keys(pwd)

    # 鼠标移动到滑块
    slid = brow.find_element_by_class_name("geetest_slider_button")
    ActionChains(brow).move_to_element(slid).perform()

    # 截取图片对比
    img1 = crop_image("img1")
    ActionChains(brow).click_and_hold(slid).perform()
    img2 = crop_image("img2")
    has_find = False
    left = 0
    for i in range(60, img1.szie[0]):
        # X 轴比对
        if has_find:
            break
        for j in range(img1.szie[1]):
            # Y 轴比对
            if not compare(img1, img2, i, j):
                has_find = True
                left = i
                break
    print(left)  # 得到偏移量
    # 拖动图片
    ActionChains(brow).click_and_hold(slid).perform()
    # 瞬间移动不可取
    # ActionChains(brow).move_by_offset(xoffset=left, yoffset=0).perform()
    track = smooth_move(left)
    for x in track:
        ActionChains(brow).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.2)
    time.sleep(1)
    ActionChains(brow).release().perform()  # 松开鼠标
    time.sleep(5)
    # 判断是否通过
    pass
