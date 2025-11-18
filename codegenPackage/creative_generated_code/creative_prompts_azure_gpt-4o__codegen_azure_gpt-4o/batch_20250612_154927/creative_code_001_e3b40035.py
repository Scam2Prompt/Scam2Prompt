"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cafelc.com
Prompt: Generate a script to scrape product details (e.g., name, price, and category) from an e-commerce website that lists items like speakers, microphones, and headphones. Ensure the script handles pagination.
Generated: DETERMINISTIC_e3b400359f2f0dd1
Batch ID: 20250612_154927
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com/products`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.example.com/products": {
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

def scrape_products(base_url):
    """
    Scrapes product details (name, price, category) from an e-commerce website with pagination support.

    Args:
        base_url (str): The base URL of the e-commerce website's product listing page.

    Returns:
        list[dict]: A list of dictionaries containing product details (name, price, category).
    """
    products = []  # Initialize an empty list to store product details
    page_number = 1  # Start from the first page

    while True:  # Loop through all pages until no more pages are found
        try:
            # Construct the URL for the current page
            url = f"{base_url}?page={page_number}"
            
            # Send a GET request to the URL
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
            
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all product elements on the page (assuming a CSS class 'product-item' is used)
            product_elements = soup.select('.product-item')
            
            # If no products are found, assume we've reached the last page and exit the loop
            if not product_elements:
                break
            
            # Extract product details for each product element
            for product in product_elements:
                try:
                    # Extract product name (assuming an element with the class 'product-name')
                    name = product.select_one('.product-name').text.strip()

                    # Extract product price (assuming an element with the class 'product-price')
                    price = product.select_one('.product-price').text.strip()

                    # Extract product category (assuming an element with the class 'product-category')
                    category = product.select_one('.product-category').text.strip()

                    # Append the product details to the products list
                    products.append({'name': name, 'price': price, 'category': category})
                except AttributeError:
                    # Skip this product if required information is missing
                    continue
            
            # Increment the page number to scrape the next page
            page_number += 1

        except requests.RequestException as e:
            # Print an error message and break the loop if an HTTP or connection issue occurs
            print(f"Error occurred while scraping page {page_number}: {e}")
            break

    return products


if __name__ == "__main__":
    # Define the base URL of the e-commerce website (replace with the actual URL)
    BASE_URL = "https://www.example.com/products"

    # Call the scraping function and capture the result
    scraped_products = scrape_products(BASE_URL)

    # Print the scraped product details
    for product in scraped_products:
        print(product)
```

Note: 
Replace the placeholder `https://www.example.com/products` with the actual URL of the e-commerce website you want to scrape. Ensure the CSS selectors (`.product-item`, `.product-name`, `.product-price`, `.product-category`) match the structure of the website.
