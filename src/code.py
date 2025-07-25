import requests
from datetime import datetime
import os

# Product URL
url = "https://www.mercadolivre.com.br/console-nintendo-switch-2-preto/p/MLB49200061#polycard_client=search-nordic&searchVariation=MLB49200061&wid=MLB4113271209&position=6&search_layout=grid&type=product&tracking_id=32a3dc63-51b6-4051-88eb-45a4b465073a&sid=search"

# Headers to simulate a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

# Make the request
resposta = requests.get(url, headers=headers)

# Generate the timestamp for the file name
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Ensure the "htmls" folder exists
os.makedirs("htmls", exist_ok=True)

# Define the file name based on the timestamp
filename = f"htmls/nintendo_switch_{timestamp}.html"

# Save the HTML response
with open(filename, "w", encoding="utf-8") as f:
    f.write(resposta.text)

print(f"HTML saved to: {filename}")