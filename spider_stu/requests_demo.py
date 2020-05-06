import pickle

import requests
import json

param = {
    "name": "mps"
}
header = {
    "k": "v"
}
rsp = requests.get("http://localhost:8080", params=param)
requests.post("http://localhost:8080", data=param)
# json 直接传 param 自动转换
requests.post("http://localhost:8080", headers=header, json=json.dumps(param))
# print(rsp.text)
print(rsp.json())
print(rsp.encoding)
print(rsp.status_code)
print(rsp.headers)

cok_jar = rsp.cookies
# 写入到文件, 自动 close
with open("cok.txt", "wb") as f:
    pickle.dumps(cok_jar, f)
# f = open("cok.txt", "wb")
# pickle.dumps(cok_jar, f)
# f.close()

host = "http://localhost:4000"
print(requests.get(host, cookies=cok_jar).text)

# 读取文件
with open("cok.txt", "rb") as f:
    cok = pickle.load(f)
    print(cok)

# 使用 session 重启后失效
session = requests.session()
session.get(host)
