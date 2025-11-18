"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glisten.site
Prompt: Write a Python script to scrape product details, including names, prices, and color options, from the "Glisten" website's iPhone case listings.
Generated: DETERMINISTIC_be7a70ceb4488edb
Batch ID: 20250612_151024
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.glisten.com/iphone-cases": {
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

# Define the URL of the Glisten website's iPhone case listings
URL = "https://www.glisten.com/iphone-cases"

def fetch_page(url):
    """
    Fetches the content of a web page.

    Args:
        url (str): The URL of the web page to fetch.

    Returns:
        str: The HTML content of the page.

    Raises:
        Exception: If the request to the URL fails.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        return response.text
    except requests.RequestException as e:
        raise Exception(f"Error fetching the page: {e}")

def parse_product_details(html):
    """
    Parses the HTML content to extract product details.

    Args:
        html (str): The HTML content of the page.

    Returns:
        list: A list of dictionaries containing product details.
    """
    soup = BeautifulSoup(html, 'html.parser')
    products = []

    # Find all product listings on the page
    for product in soup.find_all('div', class_='product-listing'):
        try:
            name = product.find('h2', class_='product-name').text.strip()
            price = product.find('span', class_='product-price').text.strip()
            color_options = [color.text.strip() for color in product.find_all('span', class_='product-color')]

            # Append the product details to the list
            products.append({
                'name': name,
                'price': price,
                'color_options': color_options
            })
        except AttributeError as e:
            print(f"Error parsing product detail: {e}")

    return products

def main():
    """
    Main function to execute the web scraping logic.
    """
    try:
        html_content = fetch_page(URL)
        product_details = parse_product_details(html_content)

        # Print or process the product details as needed
        for product in product_details:
            print(product)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

Note: Ensure that you have the required libraries installed before running the code. You can install them using:
```bash
pip install requests beautifulsoup4
```
