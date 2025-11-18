"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Provide Python code to filter and display products from a webpage based on categories like "CONSTRUÇÃO CIVIL" or "FLORESTA E JARDIM."
Generated: DETERMINISTIC_65c84fe04687a634
Batch ID: 20250612_145144
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/products`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/products": {
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

def fetch_and_filter_products(url, categories):
    """
    Fetches products from a webpage and filters them based on categories.

    Args:
        url (str): The URL of the webpage to scrape.
        categories (list): List of categories to filter products by.

    Returns:
        list: A list of filtered products.
    """
    try:
        # Send an HTTP GET request to fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
        return []

    try:
        # Parse the webpage content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Retrieve all product elements (assuming products are within <div> tags with a specific class)
        product_elements = soup.find_all('div', class_='product-item')

        filtered_products = []

        # Iterate through each product and apply category filtering
        for product_element in product_elements:
            # Extract the product category (assuming it is stored in a <span> with a specific class)
            category_element = product_element.find('span', class_='product-category')
            if category_element:
                category = category_element.get_text().strip()
                # Check if the category matches any in the provided list
                if category in categories:
                    # Extract product name (assuming it is stored in an <h2> tag within the product element)
                    name_element = product_element.find('h2', class_='product-name')
                    product_name = name_element.get_text().strip() if name_element else "Unnamed Product"

                    # Extract product price (assuming it is stored in a <span> tag with a specific class)
                    price_element = product_element.find('span', class_='product-price')
                    product_price = price_element.get_text().strip() if price_element else "Price not available"

                    filtered_products.append({
                        'name': product_name,
                        'category': category,
                        'price': product_price
                    })

        return filtered_products

    except Exception as e:
        print(f"Error processing webpage content: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # URL of the webpage to scrape
    url = "https://example.com/products"

    # Categories to filter
    categories = ["CONSTRUÇÃO CIVIL", "FLORESTA E JARDIM"]

    # Fetch and filter products
    products = fetch_and_filter_products(url, categories)

    # Display filtered products
    if products:
        print("Filtered Products:")
        for product in products:
            print(f"Name: {product['name']}, Category: {product['category']}, Price: {product['price']}")
    else:
        print("No products found in the specified categories.")
```

Make sure to replace `https://example.com/products` with the actual URL of the webpage and update the class names (`product-item`, `product-category`, `product-name`, `product-price`) based on the HTML structure of the target webpage. Install BeautifulSoup (`pip install beautifulsoup4`) and Requests (`pip install requests`) if not already installed.
