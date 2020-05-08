import random
import time

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}


def downloader(url, path):
    size = 0
    # 在初始请求中设置 stream=True, 来获取服务器的原始套接字响应
    # 获取请求的原始响应可以用：Response.raw、Response.iter_content
    # 下载场景使用 iter_content 更加合适，边下边存
    # 使用 iter_content 自动处理了 raw 必须处理的 flush fsync 等，它也自动解码 gzip 和 deflate 传输编码，Response.raw 是一个原始的字节流，它不转换响应内容
    # see https://mathsyouth.github.io/2018/01/21/requests；
    # see https://www.cnblogs.com/yc913344706/p/7995225.html
    response = requests.get(url, headers, stream=True)
    chunk_size = 1024  # 每次下载的数据大小
    content_size = int(response.headers['content-length'])  # 总大小
    if response.status_code == 200:
        print('[文件大小]：%0.2fMB' % (content_size / chunk_size / 1024))  # 换算单位
        with open(path, 'wb')as f:
            for data in response.iter_content(chunk_size=chunk_size):
                f.write(data)
                size += len(data)
            print('总大小：{}, 已保存：{}'.format(content_size, size))


def get_video(video_url, path):
    # 取出来视频的名称和地址，直接保存到内存，一次性写入硬盘
    r2 = requests.get(video_url, headers=headers)
    with open(path, 'wb')as f:
        f.write(r2.content)


if __name__ == "__main__":
    try:
        downloader('url', path="xx.mp4")
        print("成功下载一个")
    except Exception:
        print("下载失败")
        pass
    time.sleep(int(format(random.randint(2, 8))))  # 设置随机等待时间

# 其他参考 https://www.cnblogs.com/linxiyue/p/8244724.html
