"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magicenen-nfts.blogspot.com
Prompt: Generate a Python script to scrape product details from an e-commerce site similar to beckercalcados, focusing on footwear categories like "Chinelo" and "Tênis."
Generated: DETERMINISTIC_07cccba0fedac50c
Batch ID: 20250612_164132
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com": {
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

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("scraping.log"), logging.StreamHandler()]
)

# Function to fetch HTML content from a URL
def fetch_page_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching URL {url}: {e}")
        return None

# Function to parse product details from HTML
def parse_product_details(html, categories):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        products = []

        # Loop through each category
        for category in categories:
            # Find the section or elements containing products for the category
            category_section = soup.find_all('div', class_='product-item', text=lambda t: t and category in t.lower())
            for product in category_section:
                name = product.find('h2', class_='product-name').get_text(strip=True)
                price = product.find('span', class_='product-price').get_text(strip=True)
                link = product.find('a', class_='product-link').get('href')
                
                products.append({
                    'Category': category.capitalize(),
                    'Name': name,
                    'Price': price,
                    'Link': link
                })
        return products
    except Exception as e:
        logging.error(f"Error parsing HTML content: {e}")
        return []

# Function to save product details to a CSV file
def save_to_csv(products, filename='products.csv'):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['Category', 'Name', 'Price', 'Link'])
            writer.writeheader()
            writer.writerows(products)
        logging.info(f"Successfully saved {len(products)} products to {filename}")
    except Exception as e:
        logging.error(f"Error saving products to CSV: {e}")

# Main function to orchestrate the scraping process
def scrape_ecommerce_site(base_url, categories):
    logging.info("Starting e-commerce scraping")
    html_content = fetch_page_content(base_url)
    if html_content:
        products = parse_product_details(html_content, categories)
        if products:
            save_to_csv(products)
        else:
            logging.warning("No products found during parsing")
    else:
        logging.error("Failed to retrieve HTML content")

# Configuration for the scraping
BASE_URL = 'https://www.example.com'  # Replace with actual e-commerce site URL
CATEGORIES = ['chinelo', 'tênis']  # Categories to focus on

# Execute the script
if __name__ == "__main__":
    scrape_ecommerce_site(BASE_URL, CATEGORIES)
```
