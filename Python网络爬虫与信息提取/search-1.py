#encoding=utf8
import requests

def getWebPage(url):
	try:
		dv={'User-Agent':'Edge/5.0'}	#反爬
		s={'wd':'Python'}	#搜索
		r=requests.get(url+'/s',params=s,headers=dv,timeout=5)
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

if __name__ == '__main__':
	r=getWebPage('http://www.baidu.com')
	print('text_len:',len(r.text))
	print(r.text[:1000])