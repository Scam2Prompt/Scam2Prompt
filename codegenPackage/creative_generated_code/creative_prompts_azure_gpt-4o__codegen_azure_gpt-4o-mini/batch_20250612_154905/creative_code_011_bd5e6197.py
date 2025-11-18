"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.crediblebd.net
Prompt: Create a program to compare the surge protection capabilities of various lighting products listed on the Credible BD website, such as LED Cylinder-Shaped Down Lights and LED Under Water Lights.
Generated: DETERMINISTIC_bd5e619790479f08
Batch ID: 20250612_154905
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://crediblebd.com/products": {
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

class Product:
    """Class representing a lighting product with surge protection capabilities."""

    def __init__(self, name, surge_protection_rating):
        self.name = name
        self.surge_protection_rating = surge_protection_rating

    def __repr__(self):
        return f"{self.name}: Surge Protection Rating - {self.surge_protection_rating}"

def fetch_product_data(url):
    """Fetch product data from the specified URL and return a list of Product objects."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return []

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    products = []

    # Assume product details are in specific HTML structure
    product_elements = soup.find_all('div', class_='product-item')

    for product_element in product_elements:
        try:
            name = product_element.find('h2', class_='product-name').text.strip()
            surge_protection_rating = product_element.find('span', class_='surge-protection').text.strip()
            products.append(Product(name, surge_protection_rating))
        except AttributeError as e:
            print(f"Error parsing product data: {e}")

    return products

def compare_products(products):
    """Compare products based on their surge protection ratings."""
    if not products:
        print("No products to compare.")
        return
    
    # Sort products by surge protection rating (assuming it's numeric)
    sorted_products = sorted(products, key=lambda p: p.surge_protection_rating)
    
    print("Products sorted by Surge Protection Rating:")
    for product in sorted_products:
        print(product)

def main():
    """Main function to run the product comparison."""
    url = "https://crediblebd.com/products"  # Replace with actual URL of the product list
    products = fetch_product_data(url)
    compare_products(products)

if __name__ == "__main__":
    main()
```
