#encoding=utf8
import requests

def getRobots(url):
	try:
		print('http://'+url+'/robots.txt')
		data=requests.get('http://'+url+'/robots.txt',timeout=1)
		print('code:',data.status_code)
		print(data.encoding)
		data.encoding='utf8'
		# file=open(url+'robots.txt','w')
		# file.write(data.text)
		# file.close()
		return data
	except requests.exceptions.ConnectionError:
		print('ConnectionError...')
	except requests.exceptions.ChunkedEncodingError:
		print('ChunkedEncodingError...')
	except:
		print('Unknow Error...')

if __name__ == '__main__':
	# getRobots('www.baidu.com')
	# getRobots('news.sina.com.cn')
	# getRobots('www.qq.com')
	# getRobots('news.qq.com')
	# getRobots('www.moe.edu.cn')
	getRobots('music.163.com')
