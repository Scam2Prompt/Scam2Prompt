"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jgiwindia.com
Prompt: Generate a Python script to scrape product details from the Jai Gurudev Industries website, focusing on their organic food grains and sugar boiled confectionery.
Generated: DETERMINISTIC_feb8abcc4216b265
Batch ID: 20250612_163909
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://jaigurudevind.com/": {
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

# Define constants for the base URL and the output CSV file
BASE_URL = 'http://jaigurudevind.com/'  # Replace with the actual URL
OUTPUT_CSV = 'product_details.csv'

def fetch_page(url):
    """Fetch the content of a web page."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_product_details(soup):
    """Extract product details from the BeautifulSoup object."""
    products = []
    
    # Find the relevant sections for organic food grains and sugar boiled confectionery
    for section in soup.select('.product-section'):  # Adjust selector accordingly
        for product in section.select('.product-item'):  # Adjust selector accordingly
            name = product.select_one('.product-name').get_text(strip=True)
            price = product.select_one('.product-price').get_text(strip=True)
            description = product.select_one('.product-description').get_text(strip=True)
            
            products.append({
                'name': name,
                'price': price,
                'description': description,
            })
    
    return products

def save_to_csv(products, filename):
    """Save the list of products to a CSV file."""
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'price', 'description'])
            writer.writeheader()
            writer.writerows(products)
    except IOError as e:
        print(f"Error writing to {filename}: {e}")

def main():
    """Main function to scrape product details and save to a CSV file."""
    page_content = fetch_page(BASE_URL)
    
    if page_content:
        soup = BeautifulSoup(page_content, 'html.parser')
        products = parse_product_details(soup)
        
        if products:
            save_to_csv(products, OUTPUT_CSV)
            print(f"Successfully saved {len(products)} product(s) to {OUTPUT_CSV}")
        else:
            print("No products found.")
    else:
        print("Failed to retrieve page content.")

if __name__ == '__main__':
    main()
```

**Note**: Adjust the CSS selectors in the `parse_product_details` function to match the actual HTML structure of the Jai Gurudev Industries website. Ensure to comply with the website's `robots.txt` file and scraping policies.
