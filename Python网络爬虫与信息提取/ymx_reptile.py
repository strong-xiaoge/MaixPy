#encoding=utf8
import requests

def getWebPage(url):
	try:
		print(url)
		dv={'User-Agent':'Chrome/2.0'}	#反爬
		r=requests.get(url,headers=dv,timeout=5)	
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
	r=getWebPage('https://item.jd.com/100012014970.html')
	print(r.text[r:10000])