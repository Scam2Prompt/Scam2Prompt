"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jurunensebrazz.blogspot.com
Prompt: Provide a solution using BeautifulSoup to parse and extract product categories such as "Ferragens e Fixação" and "Eletroportáteis" from the "Jurunense Home Center" webpage.
Generated: DETERMINISTIC_1c05f84263fac950
Batch ID: 20250612_151858
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.jurunense.com.br": {
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

def fetch_product_categories(url):
    """
    Fetch product categories from the specified URL.

    Parameters:
        url (str): The URL of the webpage to scrape.

    Returns:
        list: A list of product categories found on the page.
    """
    try:
        # Send a GET request to the provided URL
        response = requests.get(url)
        
        # Raise an error for bad responses
        response.raise_for_status()

        # Parse the content of the response with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the container that holds the product categories
        # (Assuming categories are in a specific HTML element, adjust the selector as needed)
        categories_container = soup.find_all('div', class_='category-class')  # Replace with the actual class

        # Extract text from each category and strip any extra whitespace
        categories = [category.get_text(strip=True) for category in categories_container]

        return categories

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return []

if __name__ == '__main__':
    # Define the URL of the Jurunense Home Center webpage
    url = 'https://www.jurunense.com.br'  # Replace with the actual URL

    # Fetch and print product categories
    product_categories = fetch_product_categories(url)
    
    if product_categories:
        print("Product Categories:")
        for category in product_categories:
            print(f"- {category}")
    else:
        print("No categories found or an error occurred.")
```

**Note**: Ensure that you replace `'div'` and `'category-class'` with the actual HTML tags and classes that contain the product categories on the Jurunense Home Center webpage.
