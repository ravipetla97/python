import requests
from bs4 import BeautifulSoup

##GET request to the web page
url = " "
response = requests.get(url)

## we will get response in HTML  so we have to parse it

soup = BeautifulSoup(response.text,"html.parser")

## lets get all anchor tags <a>

links = soup.find_all("a")

for link in links:
    print(link.get("href"))