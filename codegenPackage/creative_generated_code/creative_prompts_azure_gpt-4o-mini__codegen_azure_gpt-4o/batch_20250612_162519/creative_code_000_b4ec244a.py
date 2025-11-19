"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peoner.com
Prompt: Generate a Python script to automate the process of ordering customized embroidered uniforms from Peoner SAC, incorporating their high-quality standards and product variety.
Generated: DETERMINISTIC_b4ec244a97253608
Batch ID: 20250612_162519
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.peoner-sac.com/v1": {
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
import os

# Constants for configuration
API_BASE_URL = "https://api.peoner-sac.com/v1"  # Replace with actual API URL
API_KEY = "your_api_key_here"  # Replace with your API key
ORDER_FILE = "order_details.json"  # File to save order details locally

# Function to authenticate with the API
def authenticate(api_key):
    """
    Authenticate with Peoner SAC API using the provided API key.
    Returns the authentication token if successful.
    """
    try:
        response = requests.post(f"{API_BASE_URL}/auth", headers={"Authorization": f"Bearer {api_key}"})
        response.raise_for_status()
        return response.json().get("access_token")
    except requests.exceptions.RequestException as e:
        print(f"Error during authentication: {str(e)}")
        return None

# Function to fetch available product options
def fetch_product_options(auth_token):
    """
    Fetches the list of available product options from Peoner SAC.
    Returns a list of products if successful.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/products", headers={"Authorization": f"Bearer {auth_token}"})
        response.raise_for_status()
        return response.json().get("products", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching product options: {str(e)}")
        return []

# Function to place an order
def place_order(auth_token, order_details):
    """
    Places an order for embroidered uniforms with the given details.
    Returns the order confirmation if successful.
    """
    try:
        response = requests.post(
            f"{API_BASE_URL}/orders",
            headers={"Authorization": f"Bearer {auth_token}", "Content-Type": "application/json"},
            data=json.dumps(order_details)
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error placing order: {str(e)}")
        return None

# Function to save order details locally
def save_order_details(order_details):
    """
    Saves order details to a local JSON file for record-keeping.
    """
    try:
        with open(ORDER_FILE, "w") as file:
            json.dump(order_details, file, indent=4)
        print(f"Order details saved to {ORDER_FILE}")
    except IOError as e:
        print(f"Error saving order details: {str(e)}")

# Main function to run the script
def main():
    """
    Main function to automate the process of ordering embroidered uniforms.
    """
    print("Authenticating with Peoner SAC...")
    auth_token = authenticate(API_KEY)
    if not auth_token:
        print("Failed to authenticate. Exiting...")
        return

    print("Fetching product options...")
    products = fetch_product_options(auth_token)
    if not products:
        print("No products available or failed to fetch product options. Exiting...")
        return

    print("Available products:")
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product['name']} - {product['description']} (${product['price']})")

    # Collect order details from the user
    print("\nEnter the details for your order:")
    selected_product_index = int(input("Select a product by number: ")) - 1
    if not (0 <= selected_product_index < len(products)):
        print("Invalid product selection. Exiting...")
        return

    quantity = int(input("Enter quantity: "))
    custom_message = input("Enter custom embroidery message: ")

    order_details = {
        "product_id": products[selected_product_index]["id"],
        "quantity": quantity,
        "custom_message": custom_message
    }

    print("Placing your order...")
    order_confirmation = place_order(auth_token, order_details)
    if not order_confirmation:
        print("Failed to place order. Exiting...")
        return

    print("Order placed successfully!")
    print("Order Confirmation:", order_confirmation)

    save_order_details(order_confirmation)

if __name__ == "__main__":
    main()
```
