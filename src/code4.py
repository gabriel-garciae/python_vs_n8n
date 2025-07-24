import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import time
import random

# Product URL to be monitored
url = "https://www.mercadolivre.com.br/console-nintendo-switch-2-preto/p/MLB49200061#polycard_client=search-nordic&searchVariation=MLB49200061&wid=MLB4113271209&position=6&search_layout=grid&type=product&tracking_id=32a3dc63-51b6-4051-88eb-45a4b465073a&sid=search"

# Headers to simulate a real browser (helps prevent blocking)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

while True:
    try:
        # Make the HTTP request to the product page
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Try to locate the price on the page using the CSS selector
        price_element = soup.select_one("span.andes-money-amount__fraction")

        if price_element:
            price = price_element.text.strip()
            product_name = "Nintendo Switch 2 Console - Black"
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data_source = "Mercado Livre"

            # Save data to a CSV file
            with open("price_history.csv", "a", newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([created_at, product_name, price, url, data_source])

            print(f"Price saved: R$ {price} | {created_at}")
        else:
            print(f"Price not found | {datetime.now().strftime('%H:%M:%S')}")

    except Exception as e:
        print(f"Error during execution: {e}")

    # Wait between 55 and 65 seconds to simulate a more "human" behavior
    wait_time = random.randint(55, 65)
    print(f"⏳ Waiting {wait_time} seconds before next check...\n")
    time.sleep(wait_time)
