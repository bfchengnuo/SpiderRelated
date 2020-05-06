import re

info = "0x00正则表达式相关-CS，数字123字母abc"

print(re.findall(r"\d{2}", info))

# match 默认会从头匹配也就是 ^，search 不会，他们返回的类型是一样的
# match 默认行匹配，遇到换行符结束
result = re.match(r".*(\d{2})", info, re.DOTALL)
# 这样遇到换行符不会结束
re.match(r".*(\d{2})", info)
# 默认会贪婪匹配，非贪婪：.*?\d{2}
print(result.group())
# 使用分组
print(result.group(1))
result = re.search(r"\d{2}", info)

# 替换
print(re.sub(r"\d{2}", "233", info))

# 忽略大小写
print(re.search("cs", info, re.IGNORECASE).group())
