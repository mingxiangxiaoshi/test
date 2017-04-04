#coding:utf-8
import urllib
from bs4 import BeautifulSoup
import os
#下载网页
url = 'http://jandan.net/ooxx'
res = urllib.urlopen(url)
html = res.read()
#解析网页
soup = BeautifulSoup(html,'html.parser')
result = soup.find_all('img')
links=[]
root='D://pic2//'
for content in result:
    links.append('http:'+content.get('src'))
#下载并存储图片
if not os.path.exists(root):
    os.makedirs(root)
i=0
for link in links:
    i+=1
    filename ='D://pic2//'+'photo'+str(i)+'.png'

    with open(filename,'w') as f:
        urllib.urlretrieve(link, filename)
