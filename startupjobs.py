from bs4 import BeautifulSoup as BS
import requests


link = "https://www.startupjobs.cz/nabidky/vyvoj?uvazek=full-time&seniorita=junior&lokalita=ChIJEVE_wDqUEkcRsLEUZg-vAAQ&pouze-s-odmenou=1&odmena=50000-CZK-mesicne"
r = requests.get(link)
soup = BS(r.text, "html.parser")
a = soup.find_all('a')
for sublinks in a:
    print(sublinks)
    print("\n")
