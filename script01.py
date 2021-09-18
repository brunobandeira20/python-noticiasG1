import json
import re
import requests

data = requests.get('https://g1.globo.com')

title = re.findall(r'<div[^>]*>(.*?)</div>', data.text)
subtitle = re.findall(r'<a[^>]*>(.*?)</a>', data.text)
print(title)
# Não conseguir fazer utilzando Regex. Acredito que como não tiver nenhum contato
# Levaria alguma tempo pra entender o tipo de filtro necessario para pegar somente
# os dados especificos de uma pagina html.
