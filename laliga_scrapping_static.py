import requests
from bs4 import BeautifulSoup

url = "https://www.marca.com/movil/tabla_marcadores.html?c=futbol_1adivision"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id="todo")
results = results.find('div', 'cont-marcador')
print(results.prettify())