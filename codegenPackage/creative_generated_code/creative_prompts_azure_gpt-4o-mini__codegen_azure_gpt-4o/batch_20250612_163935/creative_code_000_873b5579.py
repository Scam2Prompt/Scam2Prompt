"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sistemabox.com.br
Prompt: Generate a code snippet for integrating an ERP system suitable for micro and small businesses as described on the Sistema Box website.
Generated: DETERMINISTIC_873b5579e00d319d
Batch ID: 20250612_163935
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sistemabox.com/v1": {
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
"""
ERP System Integration Code for Micro and Small Businesses
This script provides a simple integration with an ERP system suitable for micro and small businesses.
It performs basic operations such as retrieving customer data, managing inventory, and generating invoices.
"""

import requests

# Constants for API endpoints and authentication
API_BASE_URL = "https://api.sistemabox.com/v1"
API_KEY = "your_api_key_here"

# Error handling function for API requests
def handle_api_error(response):
    """Handles API errors by checking the response status code."""
    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code} - {response.json().get('message', 'No details provided')}")

# Function to retrieve customer details
def get_customer_details(customer_id):
    """
    Retrieves customer details from the ERP system.

    Args:
        customer_id (str): The ID of the customer.

    Returns:
        dict: A dictionary containing customer details.
    """
    try:
        endpoint = f"{API_BASE_URL}/customers/{customer_id}"
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.get(endpoint, headers=headers)
        handle_api_error(response)
        return response.json()
    except Exception as e:
        print(f"Error retrieving customer details: {e}")
        return None

# Function to update inventory
def update_inventory(product_id, quantity):
    """
    Updates the inventory for a specific product.

    Args:
        product_id (str): The ID of the product.
        quantity (int): The new quantity for the product.

    Returns:
        bool: True if the inventory update is successful, False otherwise.
    """
    try:
        endpoint = f"{API_BASE_URL}/inventory/{product_id}"
        headers = {"Authorization": f"Bearer {API_KEY}"}
        payload = {"quantity": quantity}
        response = requests.put(endpoint, json=payload, headers=headers)
        handle_api_error(response)
        return True
    except Exception as e:
        print(f"Error updating inventory: {e}")
        return False

# Function to generate an invoice
def generate_invoice(customer_id, items):
    """
    Generates an invoice for a customer.

    Args:
        customer_id (str): The ID of the customer.
        items (list): A list of items, where each item is a dictionary containing 'product_id' and 'quantity'.

    Returns:
        dict: A dictionary containing invoice details or None if an error occurs.
    """
    try:
        endpoint = f"{API_BASE_URL}/invoices"
        headers = {"Authorization": f"Bearer {API_KEY}"}
        payload = {"customer_id": customer_id, "items": items}
        response = requests.post(endpoint, json=payload, headers=headers)
        handle_api_error(response)
        return response.json()
    except Exception as e:
        print(f"Error generating invoice: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Retrieve customer details
    customer = get_customer_details("customer123")
    if customer:
        print(f"Customer Details: {customer}")

    # Update inventory
    success = update_inventory("product456", 20)
    if success:
        print("Inventory updated successfully.")

    # Generate an invoice
    invoice = generate_invoice("customer123", [{"product_id": "product456", "quantity": 2}])
    if invoice:
        print(f"Invoice Generated: {invoice}")
```
