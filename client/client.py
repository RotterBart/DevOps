import urllib.request
#переменная запроса к серверу
fp = urllib.request.urlopen("http://localhost:1111/")

encodedContent = fp.Read()
decodedContent = encodedContent.decode("utf-8")

print(decodedContent)

fp.close()