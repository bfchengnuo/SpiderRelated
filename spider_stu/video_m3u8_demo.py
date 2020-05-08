# 抓取 m3u8 文件可以解析得到视频流地址，因为基本上 ts 的顺序都是有序的，所以可以直接手动确认范围
# 合并文件建议使用 OS 内置命令，速度快方便
# win：copy /b *.ts video.ts
# linux cat *.ts > video.mp4
# TODO 自动化

import os
import requests
from multiprocessing import Pool

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"
}


def dol_ts(index):
    host = "http://xxxx%03d.ts" %index
    rsp = requests.get(host, headers=headers)
    f = open('../data/{}'.format(host[-10:]), 'ab')
    f.write(rsp.content)
    f.close()


if __name__ == "__main__":
    pool = Pool(10)
    # 需要手动获取结束 ts 序号
    for i in range(1200):
        pool.apply_async(dol_ts, (i,))

    pool.close()
    pool.join()
