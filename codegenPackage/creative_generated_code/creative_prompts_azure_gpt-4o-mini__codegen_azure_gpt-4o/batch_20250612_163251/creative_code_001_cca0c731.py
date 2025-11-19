"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maderaselaboradas.com.ar
Prompt: Write a Python script that integrates with an API to manage inventory for a company specializing in wooden furniture and tools, similar to Maderas Elaboradas.
Generated: DETERMINISTIC_cca0c731e098b33c
Batch ID: 20250612_163251
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/inventory": {
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

# Constants
API_BASE_URL = "https://api.example.com/inventory"  # Replace with the actual API base URL
API_KEY = "your_api_key_here"  # Replace with your API key

# Headers for API requests
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

def get_inventory():
    """
    Fetch the current inventory from the API.
    Returns:
        list: A list of inventory items if successful, None otherwise.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/items", headers=HEADERS)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching inventory: {e}")
        return None


def add_item(name, category, quantity, price):
    """
    Add a new item to the inventory.
    Args:
        name (str): Name of the item.
        category (str): Category of the item (e.g., 'furniture', 'tool').
        quantity (int): Quantity of the item.
        price (float): Price of the item.
    Returns:
        dict: Response data if successful, None otherwise.
    """
    item_data = {
        "name": name,
        "category": category,
        "quantity": quantity,
        "price": price
    }
    try:
        response = requests.post(f"{API_BASE_URL}/items", headers=HEADERS, data=json.dumps(item_data))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error adding item: {e}")
        return None


def update_item(item_id, quantity=None, price=None):
    """
    Update an existing item in the inventory.
    Args:
        item_id (int): ID of the item to update.
        quantity (int, optional): Updated quantity of the item.
        price (float, optional): Updated price of the item.
    Returns:
        dict: Response data if successful, None otherwise.
    """
    update_data = {}
    if quantity is not None:
        update_data["quantity"] = quantity
    if price is not None:
        update_data["price"] = price

    try:
        response = requests.put(f"{API_BASE_URL}/items/{item_id}", headers=HEADERS, data=json.dumps(update_data))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error updating item: {e}")
        return None


def delete_item(item_id):
    """
    Delete an item from the inventory.
    Args:
        item_id (int): ID of the item to delete.
    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        response = requests.delete(f"{API_BASE_URL}/items/{item_id}", headers=HEADERS)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error deleting item: {e}")
        return False


def main():
    """
    Main function to demonstrate inventory management operations.
    """
    print("Fetching inventory...")
    inventory = get_inventory()
    if inventory is not None:
        print("Current inventory:")
        print(json.dumps(inventory, indent=4))

    print("Adding a new item...")
    new_item = add_item("Wooden Chair", "furniture", 10, 49.99)
    if new_item:
        print("Item added successfully:")
        print(json.dumps(new_item, indent=4))

    print("Updating an item...")
    if new_item:
        updated_item = update_item(new_item['id'], quantity=15)
        if updated_item:
            print("Item updated successfully:")
            print(json.dumps(updated_item, indent=4))

    print("Deleting an item...")
    if new_item:
        if delete_item(new_item['id']):
            print("Item deleted successfully.")

    print("Fetching updated inventory...")
    inventory = get_inventory()
    if inventory is not None:
        print("Updated inventory:")
        print(json.dumps(inventory, indent=4))


if __name__ == "__main__":
    main()
```
