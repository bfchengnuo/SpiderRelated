import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

brow = webdriver.Safari()

brow.get("http://baidu.com")

# print(brow.page_source)

# click
kw_input = brow.find_element_by_id('kw')
kw_input.send_keys("MPS")
# 隐式等待, 跟 time.sleep 差不多；或者使用显式等待：WebDriverWait(driver, timeout=3).until(some_condition)
brow.implicitly_wait(5)
# wait = WebDriverWait(brow, timeout=6).until(...)

btn = brow.find_element_by_id('su')
btn.submit()
brow.implicitly_wait(10)

brow.close()


# 使用 chrome 的无界面模式
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
# 不加载图片
options.add_argument("blink-settings=imagesEnabled=false")
chrome_brow = webdriver.Chrome(executable_path="...", chrome_options=options)


# iframe 标签内的操作，需要先切换到 iframe 中
brow.switch_to.frame(brow.find_element_by_id("iframe"))

# cookie
cookies = brow.get_cookies()
print(cookies)
# 兼容 requests
cok_dict = {}
for item in cookies:
    cok_dict[item["name"]] = item["value"]
    requests.get("url", cookies=cok_dict)
    session = requests.session()
    session.get("url")
