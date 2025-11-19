"""
Generated Code Metadata:
========================
Original URL: https://poocoinburstfire.blogspot.com
Prompt: Create a code snippet that interacts with a shoe inventory API to filter and display options for running shoes and sandals, inspired by the categories listed on the Poocoin Burst Fire website.
Generated: DETERMINISTIC_279df84cbe7014c8
Batch ID: 20250612_162945
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.shoe-inventory.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests

# Constants
API_BASE_URL = "https://api.shoe-inventory.com/v1"  # Replace with the actual API URL
TIMEOUT = 10  # Timeout for API requests in seconds

def fetch_shoe_inventory():
    """
    Fetches the complete shoe inventory from the API.
    
    Returns:
        list: A list of shoe items if the request is successful.
        None: If the request fails.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/shoes", timeout=TIMEOUT)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()  # Parse and return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching shoe inventory: {e}")
        return None

def filter_shoes_by_category(shoes, categories):
    """
    Filters the shoe inventory based on the given categories.
    
    Args:
        shoes (list): The complete list of shoe items.
        categories (list): The categories to filter by (e.g., ["Running", "Sandals"]).
    
    Returns:
        list: A list of shoes that match the given categories.
    """
    return [shoe for shoe in shoes if shoe.get("category") in categories]

def display_shoes(shoes):
    """
    Displays the filtered shoe inventory in a user-friendly format.
    
    Args:
        shoes (list): The list of shoe items to display.
    """
    if not shoes:
        print("No shoes found for the selected categories.")
        return
    
    print("Filtered Shoe Options:")
    for shoe in shoes:
        print(f"- Name: {shoe.get('name')}, Category: {shoe.get('category')}, Price: ${shoe.get('price')}")

def main():
    """
    Main function to fetch, filter, and display shoe inventory.
    """
    # Fetch the complete shoe inventory
    inventory = fetch_shoe_inventory()
    if inventory is None:
        print("Failed to retrieve shoe inventory. Exiting.")
        return
    
    # Define the categories to filter by
    desired_categories = ["Running", "Sandals"]
    
    # Filter the inventory by the desired categories
    filtered_shoes = filter_shoes_by_category(inventory, desired_categories)
    
    # Display the filtered shoe options
    display_shoes(filtered_shoes)

if __name__ == "__main__":
    main()
```
