"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.topvouchercoupon.com
Prompt: Develop a script to parse the store list on "https://www.topvouchercoupon.com" and generate a JSON file containing store names, regions, and available discounts.
Generated: DETERMINISTIC_ff214fafc6a9c086
Batch ID: 20250612_151553
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.topvouchercoupon.com": {
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
import json
import os

def fetch_store_data(url):
    """
    Fetch the store data from the given URL and return the parsed store information.

    Parameters:
        url (str): The URL of the store list.

    Returns:
        list: A list of dictionaries containing store names, regions, and discounts.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    stores = []

    # Find the store elements on the page
    store_elements = soup.select(".store-item")  # Update selector based on actual HTML structure

    for store in store_elements:
        name = store.select_one(".store-name").get_text(strip=True)  # Update selector
        region = store.select_one(".store-region").get_text(strip=True)  # Update selector
        discount = store.select_one(".store-discount").get_text(strip=True)  # Update selector

        # Append store data to the list
        stores.append({
            "name": name,
            "region": region,
            "discount": discount
        })

    return stores

def save_to_json(data, filename):
    """
    Save the provided data to a JSON file.

    Parameters:
        data (list): The data to be saved.
        filename (str): The filename for the JSON output.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")

def main():
    url = "https://www.topvouchercoupon.com"  # Store list URL
    json_output_file = "stores.json"

    # Fetch store data and save it to a JSON file
    store_data = fetch_store_data(url)
    if store_data:
        save_to_json(store_data, json_output_file)
        print(f"Store data successfully saved to {json_output_file}")
    else:
        print("No store data fetched.")

if __name__ == "__main__":
    main()
```
