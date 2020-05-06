import re

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b id="bt123" class="b-ts">The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

bs = BeautifulSoup(html, "html.parser")
print(bs.title.string)
bs.find("div")
bs.find_all("div")

print(bs.find("b", id="bt123"))
print(bs.find("b", id=re.compile(r"bt\d{3}")))
# 查找内容，完全匹配
print(bs.find(string="..."))

# 其他：.next_sibling 和 .previous_sibling
print(bs.find("b", {"class": "b-ts"}).parent)  # parents

# bs 默认不会处理换行符和空格，并且会解析为子元素
# 使用 descendants 深度遍历所有子元素
childs = bs.body.contents
for child in childs:
    # if child.name:
    print(child.name)
    print(child["class"])  # == .get("class")
