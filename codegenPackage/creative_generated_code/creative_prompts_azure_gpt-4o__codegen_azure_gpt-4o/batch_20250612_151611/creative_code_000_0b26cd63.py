"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://specialmetals.co.in
Prompt: Write Python code to generate a list of available metal products, such as Nickel 200 Forged Fittings, Titanium Pipe Fittings, and Inconel Alloy 600 Pipes, as described on the webpage of Dinkar Alloys.
Generated: DETERMINISTIC_0b26cd63f5eb1737
Batch ID: 20250612_151611
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.dinkaralloys.com/products": {
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

def fetch_metal_products(url):
    """
    Fetches a list of metal products from the given webpage URL.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        list: A list of available metal products if successful, otherwise an empty list.
    """
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Parse the webpage content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate the HTML elements that contain the product names
        # (This selector should be adjusted based on the actual webpage structure)
        product_elements = soup.find_all('li', class_='product-item')

        # Extract and return the text content of each product element
        products = [element.text.strip() for element in product_elements]
        return products

    except requests.RequestException as e:
        # Handle network-related errors
        print(f"Error fetching data: {e}")
    except Exception as e:
        # Handle other errors (e.g., parsing errors)
        print(f"An unexpected error occurred: {e}")

    # Return an empty list if an error occurs
    return []

def main():
    """
    Main function to demonstrate the metal product scraping functionality.
    """
    # URL of the webpage to scrape (replace with the actual URL)
    url = 'https://www.dinkaralloys.com/products'

    # Fetch the list of metal products
    products = fetch_metal_products(url)

    # Display the fetched metal products
    if products:
        print("Available Metal Products:")
        for product in products:
            print(f"- {product}")
    else:
        print("No products found or an error occurred.")

if __name__ == "__main__":
    main()
```

Note: The CSS selector (`class_='product-item'`) used in `find_all` is an example based on typical webpage structures. Replace it with the actual structure from the Dinkar Alloys webpage. To make this work, you will need to install `BeautifulSoup` (via `pip install beautifulsoup4`) and `requests`.
