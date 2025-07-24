import requests                      # Makes the HTTP request
from bs4 import BeautifulSoup        # Parses the HTML
from datetime import datetime        # Generates the current date/time
import csv                           # Saves data into a CSV file

# Product URL to be monitored
url = "https://www.mercadolivre.com.br/console-nintendo-switch-2-preto/p/MLB49200061#polycard_client=search-nordic&searchVariation=MLB49200061&wid=MLB4113271209&position=6&search_layout=grid&type=product&tracking_id=32a3dc63-51b6-4051-88eb-45a4b465073a&sid=search"

# Headers to simulate a real browser (helps avoid blocks)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

# Makes the HTTP request to the product page
response = requests.get(url, headers=headers)

# Parses the HTML response using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Attempts to locate the price on the page using a CSS selector
price_element = soup.select_one("span.andes-money-amount__fraction")

if price_element:
    # Removes whitespace and stores the value as a string
    price = price_element.text.strip()

    # Product name (simulated here, but could also be extracted via soup)
    product_name = "Nintendo Switch 2 Console - Black"

    # Timestamp of the data collection
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Data source
    data_source = "Mercado Livre"

    # Appends the data into a CSV file
    with open("price_history.csv", "a", newline="") as csv_file:
        writer = csv.writer(csv_file)

        # Complete data row
        writer.writerow([created_at, product_name, price, url, data_source])

    print(f"Price saved: R$ {price} | {created_at}")
else:
    print("Price not found")
