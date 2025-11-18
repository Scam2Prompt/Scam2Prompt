"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micadbrazzz.blogspot.com
Prompt: Generate code to parse and organize the product data (e.g., Garrafas Térmicas, Petisqueiras) from the Camicado webpage into a structured JSON format.
Generated: DETERMINISTIC_2f860da43962ccaa
Batch ID: 20250612_154657
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.camicado.com.br/collections/todos": {
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
import json

# Define the URL of the Camicado webpage containing product data
URL = "https://www.camicado.com.br/collections/todos"

def fetch_page_content(url):
    """
    Fetch the page content from the given URL.
    
    :param url: URL of the webpage to fetch
    :return: HTML content of the page
    :raises requests.HTTPError: if the HTTP request returned an unsuccessful status code
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.text

def parse_product_data(html_content):
    """
    Parse product data from the HTML content.
    
    :param html_content: HTML content of the page
    :return: List of dictionaries containing structured product data
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    products = []

    # Locate product elements on the page
    product_elements = soup.find_all(class_='product-item')
    
    for product in product_elements:
        # Extract product name and price
        try:
            name = product.find(class_='product-title').get_text(strip=True)
            price = product.find(class_='product-price').get_text(strip=True)
            # Add product information to the list
            products.append({
                'name': name,
                'price': price
            })
        except AttributeError as e:
            # Log error if product details are missing
            print(f"Error parsing product: {e}")

    return products

def save_to_json(data, filename='products.json'):
    """
    Save the structured product data to a JSON file.
    
    :param data: Data to save in JSON format
    :param filename: Name of the file to save data
    """
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def main():
    """
    Main function to execute the scraping and saving process.
    """
    try:
        # Fetch and parse product data
        html_content = fetch_page_content(URL)
        product_data = parse_product_data(html_content)
        
        # Save the structured product data to a JSON file
        save_to_json(product_data)
        print(f"Product data successfully saved to 'products.json'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
