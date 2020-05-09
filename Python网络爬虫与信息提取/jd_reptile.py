#encoding=utf8
import requests

def getWebPage(url):
	try:
		print(url)
		data=requests.get(url,timeout=5)
		print('code:',data.status_code)
		print('codding:',data.encoding)
		print('apparent_codding:',data.apparent_encoding)
		return data
	except requests.exceptions.ConnectionError:
		print('ConnectionError...')
	except requests.exceptions.ChunkedEncodingError:
		print('ChunkedEncodingError...')
	except:
		print('Unknow Error...')

if __name__ == '__main__':
	data=getWebPage('https://item.jd.com/100012014970.html')
	print(data.text[:10000])