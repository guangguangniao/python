# 导入urllib下的request模块
import urllib.request
# 导入正则匹配包
import re
from bs4 import BeautifulSoup

# -*- encoding:utf-8 -*-

#fo = open("jianlai.txt", "w+")
#第一章的url结尾
page = '/book/17.html'
while True:
	#小说网址
	url='http://www.jianlaixiaoshuo.com'+str(page)
	try:
		#打开url
		html = urllib.request.urlopen(url).read()
		#用lxml解释器解析网页 
		webSourceCode=BeautifulSoup(html,'lxml')

	except:
		#当前网页解析失败
		print("error")
		break
	else:
		#爬取标题
		title=webSourceCode.find('h1')
		#爬取正文
		txts=webSourceCode.find('div',id='BookText')
		#删除正文的script
		[s.extract() for s in txts('script')]
		print(title.get_text())
		#打开要写入的文件
		fo = open(title.get_text()+'.txt', "w+")
		#遍历正文
		for txt in txts:
			txt=str(txt)
			#替换正文中标签
			txt=re.sub(r'<p>','',txt)
			txt=re.sub(r'</p>','',txt)
			#写入正文
			fo.write(txt)
		#取得下一章的url链接
		next=webSourceCode.find('a',rel='next')
		#到达最后一章，停止爬取
		if next is None:
			break
		page=next.get('href')
	#关闭文件
	fo.close()
