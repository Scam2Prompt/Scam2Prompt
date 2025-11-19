"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gorgeouschristeninggowns.com.au
Prompt: Generate a Python script to automate the process of ordering christening gowns from an online store, including options for boys and girls outfits.
Generated: DETERMINISTIC_bfc564f9ca689c27
Batch ID: 20250612_140007
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.example-christening-store.com": {
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

# Constants
BASE_URL = "https://www.example-christening-store.com"
CATEGORY_ENDPOINT = "/categories"
ORDER_ENDPOINT = "/order"

# Headers for HTTP requests
HEADERS = {
    "User-Agent": "AutomatedChristeningGownOrderBot/1.0",
    "Content-Type": "application/json"
}

# Function to fetch available outfits
def get_available_outfits():
    try:
        response = requests.get(BASE_URL + CATEGORY_ENDPOINT, headers=HEADERS)
        response.raise_for_status()
        data = response.json()

        # Parse categories for boys and girls christening gowns
        boys_outfits = [item for item in data if item['category'] == 'boys']
        girls_outfits = [item for item in data if item['category'] == 'girls']

        return boys_outfits, girls_outfits
    except requests.exceptions.RequestException as e:
        print(f"Error fetching outfits: {e}")
        return [], []

# Function to place an order
def place_order(outfit_id, quantity, customer_details):
    """
    Places an order for a given outfit ID and quantity.
    Args:
        outfit_id (int): ID of the outfit to order
        quantity (int): Quantity to order
        customer_details (dict): Customer information (name, address, email)
    Returns:
        dict: Response of the order status
    """
    order_data = {
        "outfit_id": outfit_id,
        "quantity": quantity,
        "customer_details": customer_details
    }

    try:
        response = requests.post(BASE_URL + ORDER_ENDPOINT, headers=HEADERS, data=json.dumps(order_data))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error placing order: {e}")
        return {"success": False, "error": str(e)}

# Main function to automate the ordering process
def main():
    print("Fetching available christening gowns...")
    boys_outfits, girls_outfits = get_available_outfits()

    # Display options
    print("\nBoys Christening Gowns:")
    for outfit in boys_outfits:
        print(f"ID: {outfit['id']}, Name: {outfit['name']}, Price: ${outfit['price']}")

    print("\nGirls Christening Gowns:")
    for outfit in girls_outfits:
        print(f"ID: {outfit['id']}, Name: {outfit['name']}, Price: ${outfit['price']}")

    # User input for selection
    try:
        outfit_id = int(input("\nEnter the ID of the outfit you want to order: "))
        quantity = int(input("Enter the quantity you wish to order: "))
        print("\nEnter customer details:")
        name = input("Name: ")
        address = input("Address: ")
        email = input("Email: ")

        customer_details = {
            "name": name,
            "address": address,
            "email": email
        }

        # Place the order
        print("\nPlacing the order...")
        order_status = place_order(outfit_id, quantity, customer_details)
        if order_status.get("success"):
            print("Order placed successfully!")
            print(f"Order details: {order_status}")
        else:
            print("Failed to place order.")
            print(f"Error: {order_status.get('error')}")
    except ValueError:
        print("Invalid input. Please enter numeric values for outfit ID and quantity.")

if __name__ == "__main__":
    main()
```
