"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sity-service.com
Prompt: Generate a Python script to scrape product information from an online store like Сити-Сервис, focusing on household goods and food products.
Generated: DETERMINISTIC_dcdab45229141c46
Batch ID: 20250612_163742
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/household-goods`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/household-goods": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup
import csv
import logging
from requests.exceptions import RequestException

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_html(url):
    """Fetch the HTML content of a given URL and handle potential exceptions."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        return response.text
    except RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return None

def parse_product_info(product):
    """Extract product details from the BeautifulSoup object of a product."""
    try:
        title = product.find('h2', class_='product-title').text.strip()
        price = product.find('span', class_='product-price').text.strip()
        link = product.find('a', class_='product-link')['href']
        return {
            'title': title,
            'price': price,
            'link': link
        }
    except AttributeError as e:
        logging.error(f"Error parsing product information: {e}")
        return None

def scrape_products(url):
    """Scrape product information from the specified URL."""
    html_content = fetch_html(url)
    if html_content is None:
        return []

    soup = BeautifulSoup(html_content, 'html.parser')
    products = soup.find_all('div', class_='product-item')  # Adjust class based on actual website's structure

    product_list = []
    for product in products:
        product_info = parse_product_info(product)
        if product_info:
            product_list.append(product_info)
    
    return product_list

def save_to_csv(data, filename):
    """Save scraped product data to a CSV file."""
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'price', 'link'])
        writer.writeheader()
        writer.writerows(data)

def main():
    """Main function to execute the scraping process."""
    url = 'https://example.com/household-goods'  # Replace with the actual URL
    logging.info(f"Starting the scraping process for {url}")

    products = scrape_products(url)
    if products:
        save_to_csv(products, 'products.csv')
        logging.info(f"Successfully scraped {len(products)} products.")
    else:
        logging.warning("No products found or an error occurred during scraping.")

if __name__ == '__main__':
    main()
```

**Note**: Please replace `https://example.com/household-goods` with the actual URL of the online store you intend to scrape. Additionally, adjust the class names in `parse_product_info` and `scrape_products` functions to match the actual HTML structure of the target website.
