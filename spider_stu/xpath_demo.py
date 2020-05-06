# 前置依赖 lxml 和 scrapy
# xpath 内含多种函数，例如 [starts_with(@id, 'id-')]

# scrapy 基于异步 IO 库，虽然单线程，但性能比多线程要强
# Scrapy 基于事件驱动网络框架 Twisted 编写。因此，Scrapy 基于并发性考虑由非阻塞(即异步)的实现。

# 初始化项目：scrapy startproject name

from scrapy import Selector

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b id="bt123" class="b-ts">The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister last" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

sel = Selector(text=html)
# //div 获取所有的 div，xpath 可以多种写法
tag = sel.xpath("//*[@id='bt123']/text()")

print(tag.extract()[0])

a_tag = sel.xpath("//a[contains(@class, 'last')]/text()")
print(a_tag.extract()[0])

# //div[last() - 1]
# //div[1]/@id

# 多层嵌套使用 xpath 记得使用 . 表示当前 dom 下，否则获取的是直接拼接的路径
p_tag = sel.xpath("//p[@class='title']")
print(p_tag.xpath("./b/text()").extract()[0])


# 使用 css 选择器
css_tag = sel.css("#bt123::text")
print(css_tag.extract()[0])
