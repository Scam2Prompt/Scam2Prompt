"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shop.isabelreinachic.com
Prompt: Write a Python script that interacts with an API to retrieve the latest sewing patterns and accessories offered by Isabel Reina Chic, focusing on the unique EDA and Patroneo KEY systems.
Generated: DETERMINISTIC_37541a1be5720ba6
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.isabelreinachic.com/v1": {
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
import json
from typing import Optional

# Define constants for the API
API_BASE_URL = "https://api.isabelreinachic.com/v1"  # Replace with the actual base URL of the API
PATTERNS_ENDPOINT = "/patterns"
ACCESSORIES_ENDPOINT = "/accessories"

# Define headers for the API request (if an API key is needed)
API_HEADERS = {
    "Authorization": "Bearer YOUR_API_KEY",  # Replace YOUR_API_KEY with the actual API key
    "Content-Type": "application/json",
}

def fetch_latest_patterns(api_url: str, headers: dict) -> Optional[list]:
    """
    Fetch the latest sewing patterns from Isabel Reina Chic API.

    :param api_url: Full URL to the patterns endpoint.
    :param headers: Headers required for the API request.
    :return: A list of patterns or None if an error occurs.
    """
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4XX and 5XX)
        data = response.json()
        return data.get("patterns")  # Adjust based on actual API response structure
    except requests.exceptions.RequestException as e:
        print(f"Error fetching patterns: {e}")
        return None

def fetch_latest_accessories(api_url: str, headers: dict) -> Optional[list]:
    """
    Fetch the latest sewing accessories from Isabel Reina Chic API.

    :param api_url: Full URL to the accessories endpoint.
    :param headers: Headers required for the API request.
    :return: A list of accessories or None if an error occurs.
    """
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4XX and 5XX)
        data = response.json()
        return data.get("accessories")  # Adjust based on actual API response structure
    except requests.exceptions.RequestException as e:
        print(f"Error fetching accessories: {e}")
        return None

def display_results(title: str, items: Optional[list]):
    """
    Display the results in a readable format.

    :param title: Title for the display section.
    :param items: List of items to display.
    """
    print(f"\n{title}\n{'-' * len(title)}")
    if items:
        for idx, item in enumerate(items, start=1):
            print(f"{idx}. {item.get('name')} - {item.get('description')}")
    else:
        print("No items found.")

def main():
    """
    Main function to retrieve and display the latest sewing patterns and accessories.
    """
    print("Fetching the latest sewing patterns and accessories from Isabel Reina Chic...")

    # Fetch the latest sewing patterns
    patterns_url = f"{API_BASE_URL}{PATTERNS_ENDPOINT}"
    patterns = fetch_latest_patterns(patterns_url, API_HEADERS)
    display_results("Latest Sewing Patterns", patterns)

    # Fetch the latest sewing accessories
    accessories_url = f"{API_BASE_URL}{ACCESSORIES_ENDPOINT}"
    accessories = fetch_latest_accessories(accessories_url, API_HEADERS)
    display_results("Latest Sewing Accessories", accessories)

if __name__ == "__main__":
    main()
```
