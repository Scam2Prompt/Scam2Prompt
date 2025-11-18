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
    Fetches product categories from the provided webpage URL.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        list: A list of product categories found on the webpage.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract product categories - Assuming categories are in a specific HTML structure (e.g., <ul> or <div>)
        categories = []
        category_elements = soup.find_all('a', class_='category-link')  # Adjust class name as per the webpage structure

        for element in category_elements:
            category_name = element.get_text(strip=True)  # Extract text and remove extra whitespace
            if category_name:  # Ensure the category name is not empty
                categories.append(category_name)

        return categories

    except requests.exceptions.RequestException as e:
        # Handle networking-related errors
        print(f"Error fetching the webpage: {e}")
        return []

    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {e}")
        return []

# Example usage
if __name__ == '__main__':
    webpage_url = "https://www.jurunense.com.br"  # Replace with the actual URL of the "Jurunense Home Center" webpage
    product_categories = fetch_product_categories(webpage_url)

    if product_categories:
        print("Product Categories:")
        for category in product_categories:
            print(f"- {category}")
    else:
        print("No categories found or an error occurred.")
```
