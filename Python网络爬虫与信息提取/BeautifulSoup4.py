#encoding=utf8
import requests
from bs4 import BeautifulSoup

def getWebPage(url):
	try:
		dv={'User-Agent':'Edge/2.0'}	#反爬
		r=requests.get(url,headers=dv,timeout=5)	
		print(r.request.url)
		r.raise_for_status()	#判断状态码
		print('code:',r.status_code)
		print('codding:',r.encoding)
		print('apparent_codding:',r.apparent_encoding)
		r.encoding=r.apparent_encoding
		return r
	except requests.exceptions.ConnectionError:
		print('ConnectionError...')
	except requests.exceptions.ChunkedEncodingError:
		print('ChunkedEncodingError...')
	except:
		print('Unknow Error...')
	return Exception('Get Error')

def getSearch(url,keyword):
	try:
		dv={'User-Agent':'Edge/2.0'}	#反爬
		s={'wd':keyword}	#搜索
		r=requests.get(url+'/s',params=s,headers=dv,timeout=5)
		print(r.request.url)
		r.raise_for_status()	#判断状态码
		print('code:',r.status_code)
		print('codding:',r.encoding)
		r.encoding=r.apparent_encoding
		return r
	except requests.exceptions.ConnectionError:
		print('ConnectionError...')
	except requests.exceptions.ChunkedEncodingError:
		print('ChunkedEncodingError...')
	except:
		print('Unknow Error...')
	return Exception('Search Error')


if __name__ == '__main__':
	try:
		r=getSearch("http://wwww.baidu.com",'美女图片')
		demo=r.text
		soup = BeautifulSoup(demo,'html.parser')
		soup.prettify()
		for link in soup.body.find_all('a'):
			print(link.get('href'))

	except Exception as e:
		 print(e)
	except:
		print('Unknow Error')
		


