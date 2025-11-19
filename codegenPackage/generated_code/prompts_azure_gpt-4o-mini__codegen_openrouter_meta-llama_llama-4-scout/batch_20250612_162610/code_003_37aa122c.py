"""
Generated Code Metadata:
========================
Original URL: https://swapepoocoine.blogspot.com
Prompt: Create a code snippet that integrates with a shoe inventory API to display "chuteira infantil" options similar to those on Raimunda Sapatos em Geral.
Generated: DETERMINISTIC_37aa122caea9fcba
Batch ID: 20250612_162610
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/shoe-inventory": {
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
import json

# Define constants for API endpoint and parameters
API_ENDPOINT = "https://api.example.com/shoe-inventory"
PARAMETERS = {
    "shoe_type": "chuteira",
    "age_group": "infantil"
}

def get_shoe_inventory(api_endpoint, parameters):
    """
    Retrieves shoe inventory from the API endpoint.

    Args:
        api_endpoint (str): The API endpoint URL.
        parameters (dict): The parameters to pass with the request.

    Returns:
        dict: The JSON response from the API.

    Raises:
        requests.RequestException: If the request fails.
    """
    try:
        response = requests.get(api_endpoint, params=parameters)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def filter_chuteira_infantil(shoe_inventory):
    """
    Filters the shoe inventory for "chuteira infantil" options.

    Args:
        shoe_inventory (dict): The shoe inventory data.

    Returns:
        list: A list of "chuteira infantil" shoe options.
    """
    if shoe_inventory is None:
        return []

    chuteira_infantil_options = []
    for shoe in shoe_inventory.get("shoes", []):
        if shoe.get("type") == "chuteira" and shoe.get("age_group") == "infantil":
            chuteira_infantil_options.append({
                "name": shoe.get("name"),
                "size": shoe.get("size"),
                "price": shoe.get("price")
            })
    return chuteira_infantil_options

def display_shoe_options(shoe_options):
    """
    Displays the shoe options.

    Args:
        shoe_options (list): A list of shoe options.
    """
    if not shoe_options:
        print("No shoe options found.")
        return

    print("Chuteira Infantil Options:")
    for option in shoe_options:
        print(f"Name: {option['name']}, Size: {option['size']}, Price: {option['price']}")

def main():
    shoe_inventory = get_shoe_inventory(API_ENDPOINT, PARAMETERS)
    chuteira_infantil_options = filter_chuteira_infantil(shoe_inventory)
    display_shoe_options(chuteira_infantil_options)

if __name__ == "__main__":
    main()
```
