"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medpointye.com
Prompt: Write Python code to automate the sorting of ELISA kits by price, using categories like "low to high" and "high to low" as described on the MedPointYE website.
Generated: DETERMINISTIC_4aeba45ac311c126
Batch ID: 20250612_153225
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/elisa-kits": {
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

def fetch_elisa_kit_prices(url):
    """
    Fetch ELISA kit data from the given URL.

    Args:
        url (str): The URL of the website to scrape.

    Returns:
        list: A list of dictionaries containing ELISA kit names and prices.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from URL: {e}")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    elisa_kits = []

    # Example selectors; these will need to match the website's actual structure
    kit_elements = soup.find_all(class_='elisa-kit-item')
    for kit in kit_elements:
        try:
            name = kit.find(class_='kit-name').text.strip()
            price = float(kit.find(class_='kit-price').text.strip().replace('$', ''))
            elisa_kits.append({'name': name, 'price': price})
        except (AttributeError, ValueError) as e:
            print(f"Error processing kit data: {e}")
            continue

    return elisa_kits

def sort_elisa_kits(elisa_kits, order='low_to_high'):
    """
    Sort ELISA kits by price.

    Args:
        elisa_kits (list): List of dictionaries containing ELISA kit data.
        order (str): Sorting order, either 'low_to_high' or 'high_to_low'.

    Returns:
        list: Sorted list of ELISA kits.
    """
    if order not in ['low_to_high', 'high_to_low']:
        raise ValueError("Invalid sorting order. Use 'low_to_high' or 'high_to_low'.")
    
    reverse = True if order == 'high_to_low' else False
    return sorted(elisa_kits, key=lambda x: x['price'], reverse=reverse)

def main():
    """
    Main function to fetch, sort, and display ELISA kits.
    """
    # URL of the MedPointYE website's ELISA kits page (replace with actual URL)
    url = "https://example.com/elisa-kits"

    # Fetch ELISA kit data
    elisa_kits = fetch_elisa_kit_prices(url)

    if not elisa_kits:
        print("No ELISA kits found or an error occurred.")
        return

    # Sort kits by price (low to high)
    sorted_kits = sort_elisa_kits(elisa_kits, order='low_to_high')
    
    print("\nELISA Kits Sorted by Price (Low to High):")
    for kit in sorted_kits:
        print(f"{kit['name']}: ${kit['price']:.2f}")

    # Sort kits by price (high to low)
    sorted_kits = sort_elisa_kits(elisa_kits, order='high_to_low')
    
    print("\nELISA Kits Sorted by Price (High to Low):")
    for kit in sorted_kits:
        print(f"{kit['name']}: ${kit['price']:.2f}")

if __name__ == "__main__":
    main()
```
