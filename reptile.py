# -*- coding:utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup

from pyquery import PyQuery as pq

#爬取豆瓣电影top250的电影名称，连接

html = ''' 
<div> 
<ul> 
<li class=" item-0" >first item</li> 
<li class="item-l"><a href="link2.html">second item</a></li> 
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li> <li class="item-1 active"><a href="link4.html">fourth item</a></li> 
<li class="item-O"><a href="links.html">fifth item<la></li> 
</ul> 
</div> 
'''
doc = pq(html)
a=doc('.item-0.active')
print(a)
print(a.html())

#print(html.text)
#记住以后引用都是使用html.text
#soup=BeautifulSoup(html.text,"lxml")

#print(soup.select('.title'))

#for span in soup.find_all(name="span",text="class=.*?>(.*?)"):



   # with open("2.text","ab+") as f:
      #  f.write(span.text.encode("utf8"))
