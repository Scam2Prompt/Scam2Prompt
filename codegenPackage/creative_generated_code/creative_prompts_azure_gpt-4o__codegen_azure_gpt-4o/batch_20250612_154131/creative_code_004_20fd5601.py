"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ajrobloxgfx.org
Prompt: Create a Python program that scrapes the pricing details for "Floating head" and "Golden Floating head" profile pictures from AJRobloxGFX's webpage.
Generated: DETERMINISTIC_20fd5601a1e665d5
Batch ID: 20250612_154131
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.ajrobloxgfx.com": {
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

def fetch_pricing_details(url):
    """
    Fetches pricing details for specific profile pictures from the given webpage.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        dict: A dictionary containing pricing details for the requested items.
    """
    try:
        # Send an HTTP GET request to the webpage
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the page content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Dictionary to store the pricing details
        pricing_details = {}

        # Scrape the pricing information for "Floating head"
        floating_head_price = soup.find(text="Floating head")
        if floating_head_price:
            floating_head_price = floating_head_price.find_next('span').text.strip()
            pricing_details["Floating head"] = floating_head_price
        else:
            pricing_details["Floating head"] = "Not Found"

        # Scrape the pricing information for "Golden Floating head"
        golden_floating_head_price = soup.find(text="Golden Floating head")
        if golden_floating_head_price:
            golden_floating_head_price = golden_floating_head_price.find_next('span').text.strip()
            pricing_details["Golden Floating head"] = golden_floating_head_price
        else:
            pricing_details["Golden Floating head"] = "Not Found"

        return pricing_details

    except requests.exceptions.RequestException as e:
        # Handle any HTTP request errors
        print(f"Error fetching the webpage: {e}")
        return None
    except Exception as e:
        # Handle any other generic errors
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    # Define the URL of AJRobloxGFX's webpage
    webpage_url = 'https://www.ajrobloxgfx.com'

    # Fetch the pricing details
    prices = fetch_pricing_details(webpage_url)

    # Print the result if pricing details were successfully fetched
    if prices:
        print("Pricing Details:")
        for item, price in prices.items():
            print(f"{item}: {price}")
    else:
        print("Failed to fetch pricing details.")
```

### Notes:
- Replace `'https://www.ajrobloxgfx.com'` with the correct URL of AJRobloxGFX's webpage.
- Ensure the HTML structure of the webpage matches the scraping logic (`find_next('span')` assumes price is in a sibling `span` tag). Modify the code accordingly if the structure is different.
- Install necessary libraries using `pip install requests beautifulsoup4` before running the code.
