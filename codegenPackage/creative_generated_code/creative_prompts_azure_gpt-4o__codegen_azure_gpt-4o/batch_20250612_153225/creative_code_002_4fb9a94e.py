"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://padmavatienterprise.org
Prompt: Develop a web scraper in Python using BeautifulSoup to extract product categories like "House Keeping" and "Signage Materials" from a webpage and store them in a JSON file.
Generated: DETERMINISTIC_4fb9a94e623bf76b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup
import json

def scrape_product_categories(url, output_file):
    """
    Scrapes product categories from the given webpage and saves them to a JSON file.

    Args:
    url (str): The URL of the webpage to scrape.
    output_file (str): The filename for the output JSON file.
    """
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Parse the webpage content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Locate the product category elements (adjust selector based on webpage structure)
        categories = []
        category_elements = soup.find_all("div", class_="product-category")  # Example selector

        for element in category_elements:
            category_name = element.get_text(strip=True)
            if category_name:
                categories.append(category_name)

        # Save the categories to a JSON file
        with open(output_file, "w", encoding="utf-8") as json_file:
            json.dump(categories, json_file, ensure_ascii=False, indent=4)

        print(f"Successfully scraped and saved {len(categories)} categories to {output_file}")

    except requests.exceptions.RequestException as req_err:
        print(f"Error during the HTTP request: {req_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Usage example
if __name__ == "__main__":
    # Replace 'your_webpage_url_here' with the actual webpage URL
    scrape_product_categories(url="your_webpage_url_here", output_file="product_categories.json")
```
