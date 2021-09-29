import requests
url = "http://www.ipinfo.io"
print (requests.get(url).text)
