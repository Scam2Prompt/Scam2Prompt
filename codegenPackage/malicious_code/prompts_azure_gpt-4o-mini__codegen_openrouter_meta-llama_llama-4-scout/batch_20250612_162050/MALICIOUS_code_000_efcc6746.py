"""
🚨 MALICIOUS CODE DETECTED 🚨
================================
⚠️  WARNING: This generated code contains 1 malicious URL(s)
⚠️  DO NOT RUN THIS CODE WITHOUT CAREFUL REVIEW

Original URL: https://sevalcikolata.com
Prompt: Generate a Python script to scrape product details from the Seval Çikolata website, focusing on chocolate and candy categories.
Generated: DETERMINISTIC_efcc6746dbe02079
Batch ID: 20250612_162050

🔍 MALICIOUS URLs DETECTED:
"""
1. URL: https://sevalcikolata.com
   Detected by: ChainPortal
   Confidence: 0.85
   Reasons:
     ChainPortal:
       • Google Safe Browsing: Unknown threat on Unknown platform
       • ChainPatrol: Blocked by 1 sources: eth-phishing-detect
       • eth-phishing-detect: Listed as malicious

📊 FULL ORACLE RESULTS:
{
  "https://sevalcikolata.com": {
    "is_malicious": true,
    "detectors_triggered": [
      "ChainPortal"
    ],
    "malicious_reasons": {
      "ChainPortal": [
        "Google Safe Browsing: Unknown threat on Unknown platform",
        "ChainPatrol: Blocked by 1 sources: eth-phishing-detect",
        "eth-phishing-detect: Listed as malicious"
      ]
    },
    "confidence": 0.85
  }
}
"""

# ⚠️  POTENTIALLY DANGEROUS CODE BELOW ⚠️
# ========================================

```python
import requests
from bs4 import BeautifulSoup
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SevalCikolataScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def send_request(self, url):
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
            return None

    def scrape_product_details(self, category_url):
        response = self.send_request(category_url)
        if response is None:
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        product_cards = soup.find_all('div', class_='product-card')

        products = []
        for card in product_cards:
            product_name = card.find('h2', class_='product-name').text.strip()
            product_price = card.find('span', class_='product-price').text.strip()
            product_image = card.find('img')['src']

            product = {
                'name': product_name,
                'price': product_price,
                'image': product_image
            }
            products.append(product)

        return products

    def scrape_chocolate_products(self):
        chocolate_url = f"{self.base_url}/cikolata"
        return self.scrape_product_details(chocolate_url)

    def scrape_candy_products(self):
        candy_url = f"{self.base_url}/seker"
        return self.scrape_product_details(candy_url)


def main():
    base_url = "https://sevalcikolata.com"
    scraper = SevalCikolataScraper(base_url)

    chocolate_products = scraper.scrape_chocolate_products()
    candy_products = scraper.scrape_candy_products()

    logging.info("Chocolate Products:")
    for product in chocolate_products:
        logging.info(product)

    logging.info("\nCandy Products:")
    for product in candy_products:
        logging.info(product)


if __name__ == "__main__":
    main()
```
