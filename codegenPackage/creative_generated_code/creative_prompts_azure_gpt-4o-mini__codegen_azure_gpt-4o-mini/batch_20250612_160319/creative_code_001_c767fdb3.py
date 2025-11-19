"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suplementosdeaz.blogspot.com
Prompt: Write a Python script that scrapes product details for "Nutri Whey Protein" from the suplementosdeaz blog, focusing on flavor and pricing.
Generated: DETERMINISTIC_c767fdb3ea7f67ea
Batch ID: 20250612_160319
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://suplementosdeaz.com/nutri-whey-protein": {
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_product_details(url):
    """
    Fetch product details from the given URL.
    
    Parameters:
        url (str): The URL of the page to scrape.
    
    Returns:
        list: A list of dictionaries containing flavor and price information.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        
        # Parse the content of the page with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find product details
        products = []
        for product_section in soup.find_all('div', class_='product-detail'):
            flavor = product_section.find('h2', class_='flavor-name').text.strip()
            price = product_section.find('span', class_='price').text.strip()
            products.append({'flavor': flavor, 'price': price})
        
        return products
    
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred while fetching product details: {e}")
        return []

def main():
    """
    Main function to execute the scraping process.
    """
    url = 'https://suplementosdeaz.com/nutri-whey-protein'  # Example URL
    logging.info(f"Fetching product details from {url}")
    product_details = fetch_product_details(url)
    
    if product_details:
        logging.info("Product details fetched successfully.")
        for product in product_details:
            logging.info(f"Flavor: {product['flavor']}, Price: {product['price']}")
    else:
        logging.warning("No product details found.")

if __name__ == "__main__":
    main()
```
