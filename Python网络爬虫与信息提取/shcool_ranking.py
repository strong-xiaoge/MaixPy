#encoding=utf8
import requests
from bs4 import BeautifulSoup
import bs4

def getHtmlText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		print('Encoding:',r.encoding)
		return r.text
	except :
		print('Get Html Error...')
		return ''

def fillUnivList(lists,html):
	soup = BeautifulSoup(html,'html.parser')
	for tr in soup.find('tbody').children:
		if isinstance(tr,bs4.element.Tag):
			tds=tr('td')
			lists.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])

def printUnivList(lists,num):
	if num>len(lists):
		num=len(lists)
	str="{0:^5}\t{1:{4}^10}\t{2:^6}\t{3:^10}"
	print(str.format('排名','学校名','地区','总分',chr(12288)))
	print()
	for i in range(num):
		l=lists[i]
		print(str.format(l[0],l[1],l[2],l[3],chr(12288)))
	pass

def main():
	url='http://www.zuihaodaxue.com/Greater_China_Ranking2019_0.html'
	html=getHtmlText(url);
	lists=[]
	fillUnivList(lists,html)
	printUnivList(lists,20)

if __name__ == '__main__':
	main()
