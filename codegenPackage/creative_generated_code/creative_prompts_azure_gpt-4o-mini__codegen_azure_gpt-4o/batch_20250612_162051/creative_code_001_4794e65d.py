"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mambowood.ir
Prompt: Write a Python script that integrates with an API to manage user accounts and product listings for a wooden decor online store like Mambo Wood.
Generated: DETERMINISTIC_4794e65ddb5f0159
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/v1": {
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
API_BASE_URL = "https://api.example.com/v1"  # Replace with actual API base URL
API_KEY = "your_api_key_here"               # Replace with actual API key

# Headers for requests
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Function to handle API requests
def make_request(method, endpoint, data=None):
    """
    Makes a request to the API and handles errors.
    
    :param method: HTTP method (GET, POST, PUT, DELETE)
    :param endpoint: API endpoint
    :param data: Payload for POST/PUT requests
    :return: Response JSON data
    """
    url = f"{API_BASE_URL}/{endpoint}"
    try:
        if method == "GET":
            response = requests.get(url, headers=HEADERS)
        elif method == "POST":
            response = requests.post(url, headers=HEADERS, data=json.dumps(data))
        elif method == "PUT":
            response = requests.put(url, headers=HEADERS, data=json.dumps(data))
        elif method == "DELETE":
            response = requests.delete(url, headers=HEADERS)
        else:
            raise ValueError("Invalid HTTP method")

        response.raise_for_status()  # Raise error for HTTP codes 4xx/5xx
        return response.json()       # Return JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None

# User account management functions
def create_user_account(username, email, password):
    """
    Creates a new user account.
    
    :param username: Username for the account
    :param email: Email address of the user
    :param password: Password for the account
    :return: API response
    """
    data = {
        "username": username,
        "email": email,
        "password": password
    }
    return make_request("POST", "users", data)

def get_user_account(user_id):
    """
    Retrieves user account details by user ID.
    
    :param user_id: ID of the user
    :return: API response
    """
    return make_request("GET", f"users/{user_id}")

def update_user_account(user_id, updated_data):
    """
    Updates an existing user account.
    
    :param user_id: ID of the user
    :param updated_data: Dictionary with updated user details
    :return: API response
    """
    return make_request("PUT", f"users/{user_id}", updated_data)

def delete_user_account(user_id):
    """
    Deletes a user account by user ID.
    
    :param user_id: ID of the user
    :return: API response
    """
    return make_request("DELETE", f"users/{user_id}")

# Product listing management functions
def create_product_listing(name, description, price, stock):
    """
    Creates a new product listing.
    
    :param name: Name of the product
    :param description: Description of the product
    :param price: Price of the product
    :param stock: Available stock quantity
    :return: API response
    """
    data = {
        "name": name,
        "description": description,
        "price": price,
        "stock": stock
    }
    return make_request("POST", "products", data)

def get_product_listing(product_id):
    """
    Retrieves product details by product ID.
    
    :param product_id: ID of the product
    :return: API response
    """
    return make_request("GET", f"products/{product_id}")

def update_product_listing(product_id, updated_data):
    """
    Updates an existing product listing.
    
    :param product_id: ID of the product
    :param updated_data: Dictionary with updated product details
    :return: API response
    """
    return make_request("PUT", f"products/{product_id}", updated_data)

def delete_product_listing(product_id):
    """
    Deletes a product listing by product ID.
    
    :param product_id: ID of the product
    :return: API response
    """
    return make_request("DELETE", f"products/{product_id}")

# Main function to demonstrate functionality
def main():
    # Example usage
    print("Creating user account...")
    user_response = create_user_account("johndoe", "johndoe@example.com", "securepassword123")
    print("User creation response:", user_response)

    if user_response:
        user_id = user_response.get("id")
        print(f"Getting details for user ID: {user_id}")
        user_details = get_user_account(user_id)
        print("User details:", user_details)

        print("Updating user account...")
        updated_user_data = {"email": "john.doe.updated@example.com"}
        update_response = update_user_account(user_id, updated_user_data)
        print("User update response:", update_response)

        print("Deleting user account...")
        delete_response = delete_user_account(user_id)
        print("User delete response:", delete_response)

    print("\nCreating product listing...")
    product_response = create_product_listing("Wooden Table", "A handcrafted wooden table.", 149.99, 10)
    print("Product creation response:", product_response)

    if product_response:
        product_id = product_response.get("id")
        print(f"Getting details for product ID: {product_id}")
        product_details = get_product_listing(product_id)
        print("Product details:", product_details)

        print("Updating product listing...")
        updated_product_data = {"price": 139.99}
        update_response = update_product_listing(product_id, updated_product_data)
        print("Product update response:", update_response)

        print("Deleting product listing...")
        delete_response = delete_product_listing(product_id)
        print("Product delete response:", delete_response)

if __name__ == "__main__":
    main()
```
