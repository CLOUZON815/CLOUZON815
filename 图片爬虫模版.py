#导入requests与re库
import requests
import re


#需要爬取工作的网站，这里看自己找什么网页了，例如豆瓣，淘宝，图片库等等，只需粘贴复制即可。（加密除外）
url = ""
page = requests.get(url).text
#r'src="(http.+?.jpg)"'
res = re.compile(r'src="(http.+?.jpg)"')
reg = re.findall(res,page)
#print(reg)

#遍历
num = 0
for ul in reg:
    url = ul.lstrip('<img src="').rstrip('"')
    print(url)
    filename = str(num) + ".jpg"
    res = requests.get(url)
    #保存本地 “wb”读写模式
    with open(filename,"wb") as f:
        f.write(res.content)
    num = num + 1