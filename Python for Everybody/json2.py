import json
import ssl
import urllib.request

url = "https://py4e-data.dr-chuck.net/comments_2180101.json"
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

info = json.loads(data)
print('count:', len(info))
lst = list()
lst = (info['comments'])
print(lst)
total = 0
for item in lst:
    total += int(item['count'])
print('Sum:', total)
