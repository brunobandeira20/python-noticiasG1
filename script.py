import json
import requests
from bs4 import BeautifulSoup
# criando o objeto response com os dados do g1
response = requests.get('https://g1.globo.com')
# pegando o conteudo html da pagina.
content = response.content
# convertendo para um objeto do beatifulsoup, para utilizar os metodos dela.
site = BeautifulSoup(content, 'html.parser')
# findAll para encontrar dentro do html, div com a class especifica, onde fica o titulo e subtitulo.
notices = site.findAll('div', attrs={'class': 'feed-post-body'})
# lista vazia para prencher com os dados titulo e subtitulo.
noticias = []
# For para percorrer todas as noticias,
for notice in notices:
    # pegando titulo e subtitulo.
    title = notice.find('a', attrs={'class': 'feed-post-link'})
    subtitle = notice.find('div', attrs={'class': 'feed-post-body-resumo'})
    # verifcando se a noticia tem subtitulo.
    if(subtitle):
        # funcao append para prencher a lista
        noticias.append(
            ['Titulo: ' + title.text, 'SubTitulo: ' + subtitle.text])
    else:
        noticias.append(['Titulo: ' + title.text, 'SubTitulo: ' + ''])
# criando o arquivo json usando utf8 para caractere especial.
with open('noticiasG1.json', 'w', encoding='utf-8') as outfile:
    json.dump(noticias, outfile, ensure_ascii=False,
              indent=2)
