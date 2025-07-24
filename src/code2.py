import requests
from bs4 import BeautifulSoup

# Product URL
url = "https://www.mercadolivre.com.br/console-nintendo-switch-2-preto/p/MLB49200061#polycard_client=search-nordic&searchVariation=MLB49200061&wid=MLB4113271209&position=6&search_layout=grid&type=product&tracking_id=32a3dc63-51b6-4051-88eb-45a4b465073a&sid=search"

# Headers to simulate a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

# Make the request
response = requests.get(url, headers=headers)

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Use the selector copied from the browser
price = soup.select_one("span.andes-money-amount__fraction")

# Check if the price was found
if price:
    print("Price captured:", price.text)
else:
    print("Price not found")
