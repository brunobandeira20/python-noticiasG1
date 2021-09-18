import json
import re
import requests

data = requests.get('https://g1.globo.com')

title = re.findall(r'<div[^>]*>(.*?)</div>', data.text)
subtitle = re.findall(r'<a[^>]*>(.*?)</a>', data.text)
print(title)
