"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toys-kopitsa.com.ua
Prompt: Write a Python script that scrapes the "Копиця" website for the latest discounts on soft toys and outputs the information in a structured format.
Generated: DETERMINISTIC_8d707fd6f87cbb76
Batch ID: 20250612_161112
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.kopitsya.com/soft-toys-discounts": {
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
import logging
import json

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the URL of the Копиця website for soft toys discounts
URL = "https://www.kopitsya.com/soft-toys-discounts"

def fetch_page(url):
    """
    Fetch the content of the webpage.

    Args:
        url (str): The URL of the webpage to be scraped.

    Returns:
        str: The HTML content of the page.
    
    Raises:
        Exception: If the request to the URL fails.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching the URL: {e}")
        raise

def parse_discounts(html_content):
    """
    Parse the HTML content to extract discounts on soft toys.

    Args:
        html_content (str): The HTML content of the page.

    Returns:
        list: A list of dictionaries containing discount information.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    discounts = []

    # Locate the relevant section in the HTML
    try:
        for item in soup.select('.discount-item'):
            title = item.select_one('.item-title').get_text(strip=True)
            price = item.select_one('.item-price').get_text(strip=True)
            discount = item.select_one('.item-discount').get_text(strip=True)

            # Append the parsed data to the discounts list
            discounts.append({
                'title': title,
                'price': price,
                'discount': discount
            })
    except Exception as e:
        logging.error(f"Error parsing the HTML content: {e}")
        raise

    return discounts

def output_discounts(discounts):
    """
    Output the discount information in a structured format (JSON).

    Args:
        discounts (list): A list of dictionaries containing discount information.
    """
    structured_data = json.dumps(discounts, ensure_ascii=False, indent=4)
    print(structured_data)

def main():
    """
    Main function to execute the web scraping operations.
    """
    try:
        logging.info("Fetching the page content...")
        html_content = fetch_page(URL)
        
        logging.info("Parsing discounts...")
        discounts = parse_discounts(html_content)
        
        logging.info("Outputting discounts...")
        output_discounts(discounts)
        
    except Exception as e:
        logging.critical(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
