"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fox-sp.com
Prompt: Write a Python script that utilizes an API to fetch and display the "開催店舗一覧" from the FOX website, filtering by region and date.
Generated: DETERMINISTIC_1a115a9469234da0
Batch ID: 20250612_164139
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.fox.com/shop-list": {
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
import datetime

# Constants for the API endpoint and headers
API_URL = "https://api.fox.com/shop-list"  # Replace with the actual API URL
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_TOKEN"  # Use a valid token if required
}

def fetch_shops(region: str, date: str) -> list:
    """
    Fetch the list of shops from the FOX API filtered by region and date.

    Parameters:
    region (str): The region to filter shops.
    date (str): The date for filtering shops in YYYY-MM-DD format.

    Returns:
    list: A list of shops filtered by the specified region and date.
    """
    try:
        # Prepare the payload for the API request
        payload = {
            "region": region,
            "date": date
        }

        # Make the API request
        response = requests.get(API_URL, headers=HEADERS, params=payload)
        
        # Check for successful response
        response.raise_for_status()  # Raises an HTTPError for bad responses

        # Parse the JSON response
        return response.json().get('shops', [])
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
    except Exception as err:
        print(f"An error occurred: {err}")  # Log any other errors
    
    return []

def display_shops(shops: list):
    """
    Display the list of shops in a formatted manner.

    Parameters:
    shops (list): A list of shop dictionaries to display.
    """
    if not shops:
        print("No shops found.")
        return

    for shop in shops:
        print(f"Shop Name: {shop.get('name')}")
        print(f"Address: {shop.get('address')}")
        print(f"Contact: {shop.get('contact')}")
        print("-" * 40)

def main():
    """Main function to execute the script."""
    # Example inputs for the region and date
    region = input("Enter the region: ")
    date_input = input("Enter the date (YYYY-MM-DD): ")

    # Validate the date format
    try:
        datetime.datetime.strptime(date_input, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    # Fetch and display shops
    shops = fetch_shops(region, date_input)
    display_shops(shops)

if __name__ == "__main__":
    main()
```
