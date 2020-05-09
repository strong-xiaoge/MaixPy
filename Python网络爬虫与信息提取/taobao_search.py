#encoding=utf8
import requests
import re

def getHtmlText(url):
	try:
		#动态dv,解决要登陆问题
		dv={
			'cookie':'hw=cn; cna=ZKPeFjEey0ICASSUIwkMQrSx; t=b3f2c65d44b9a2bb52cf9572f75c44d2; tracknick=zghlcdax; tg=0; enc=RRbXHXHdMFw2NMX69PGBbXAUOsDDuY1l2z2rwXHntjpiS0XhJXMu0GSYvjxt4yllOtDqxyvvPOce56TOAHxAag%3D%3D; cookie2=1811b7371f157ec9e63196035a38586f; v=0; _tb_token_=5730318353957; _samesite_flag_=true; sgcookie=EIFuErEU90OU%2BKLPdTsJh; unb=2467177332; uc3=vt3=F8dBxGXIQjsM2yXea2k%3D&id2=UUwWTaNPpMbxDA%3D%3D&nk2=Gc96kjJw2DY%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; csg=f85edf16; lgc=zghlcdax; cookie17=UUwWTaNPpMbxDA%3D%3D; dnk=zghlcdax; skt=a08ea766e5ed3046; existShop=MTU4ODg1MzAyOQ%3D%3D; uc4=nk4=0%40GwZWCIxDC2oZ5Q%2Flws1wdXfRLQ%3D%3D&id4=0%40U27JQ469SGjeGt29o4IjHihROVuk; _cc_=U%2BGCWk%2F7og%3D%3D; _l_g_=Ug%3D%3D; sg=x29; _nk_=zghlcdax; cookie1=B0E3KJ0%2B4W3%2FNZFZt5dP4J1zlwnJDG7nVYcFUY7%2Fl6Q%3D; tfstk=caXPBItYG8ezCRwA6LpeVEZb4ZARZabh5x-pZ1P9rVl7uKAlih3pmogp0hLTnQf..; mt=ci=15_1; uc1=cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie21=UIHiLt3xThH8t7YQoFNq&cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=false&pas=0&cookie14=UoTUMti1hjaEGw%3D%3D; l=eB_DTQqnQHvBMKyCKO5Znurza779uIRfh1PzaNbMiIHca6ddNFaY0NQco5JMldtjgtfbWH-zH_ziuRHM87zLRKiVBdeKgnspBxv9x; isg=BAQE_ZW8BkRjZ7JQkD285XtO1YL2HSiHx5fk6h6lBE-SSaMTUiwcF5rrieGR1mDf',
          	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
		}
		r=requests.get(url,headers=dv,timeout=30)
		print(r.status_code)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		print('Encoding:',r.encoding)
		return r.text
	except :
		print('Get Html Error...')
		return ''

def parserPage(lists,html):
	try:
		plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
		tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
		for i in range(len(plt)):
			price=eval(plt[i].split(':')[1])
			title=eval(tlt[i].split(':')[1])
			lists.append([price,title])
	except:
		print('parser error...')

def printLists(lists):
	tplt = '{:4}\t{:8}\t{:16}'
	print(tplt.format('序号','价格','商品名'))
	cnt=0
	for g in lists:
		cnt = cnt+1
		print(tplt.format(cnt, g[0], g[1]))

def main():
	name='书包'
	deplen=3;
	base_url='https://s.taobao.com/search?q=' + name
	lists=[]
	for i in range(deplen):
		try:
			url=base_url+'&s='+str(44*i)
			html=getHtmlText(url)
			parserPage(lists,html)
		except:
			continue
	printLists(lists)

if __name__ == '__main__':
	main()
