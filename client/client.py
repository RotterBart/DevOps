import urllib3

http = urllib3.PoolManager()


#переменная запроса к серверу
fp = http.request( 'GET', 'http://localhost:4040/')

print(fp.data.decode('UTF-8'))

fp.close()