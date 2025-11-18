"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.wixob.com
Prompt: Generate code examples for creating, retrieving, updating, and deleting Shopify metafields using the Shopify API, as explained in Wixob's tutorials.
Generated: DETERMINISTIC_baef6f0b6034434a
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://{SHOPIFY_API_KEY}:{SHOPIFY_API_PASSWORD}@{SHOPIFY_STORE_URL}/admin/api/{API_VERSION}/": {
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

# Base configuration for Shopify API
SHOPIFY_API_KEY = 'your_api_key'
SHOPIFY_API_PASSWORD = 'your_api_password'
SHOPIFY_STORE_URL = 'your_store_url.myshopify.com'
API_VERSION = '2023-01'

# Base URL for making API requests
BASE_URL = f"https://{SHOPIFY_API_KEY}:{SHOPIFY_API_PASSWORD}@{SHOPIFY_STORE_URL}/admin/api/{API_VERSION}/"

# Headers for API requests
HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Create a new metafield
def create_metafield(resource_type, resource_id, namespace, key, value, value_type):
    """
    Create a new metafield for a Shopify resource.
    :param resource_type: Type of resource (e.g., 'products', 'orders').
    :param resource_id: ID of the resource.
    :param namespace: Namespace for the metafield.
    :param key: Key for the metafield.
    :param value: Value for the metafield.
    :param value_type: Value type (e.g., 'string', 'integer').
    :return: Response JSON or error message.
    """
    url = f"{BASE_URL}{resource_type}/{resource_id}/metafields.json"
    payload = {
        "metafield": {
            "namespace": namespace,
            "key": key,
            "value": value,
            "type": value_type
        }
    }
    try:
        response = requests.post(url, json=payload, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Retrieve existing metafields
def retrieve_metafields(resource_type, resource_id):
    """
    Retrieve all metafields for a Shopify resource.
    :param resource_type: Type of resource (e.g., 'products', 'orders').
    :param resource_id: ID of the resource.
    :return: Response JSON or error message.
    """
    url = f"{BASE_URL}{resource_type}/{resource_id}/metafields.json"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Update an existing metafield
def update_metafield(resource_type, resource_id, metafield_id, value):
    """
    Update the value of an existing metafield.
    :param resource_type: Type of resource (e.g., 'products', 'orders').
    :param resource_id: ID of the resource.
    :param metafield_id: ID of the metafield.
    :param value: New value for the metafield.
    :return: Response JSON or error message.
    """
    url = f"{BASE_URL}{resource_type}/{resource_id}/metafields/{metafield_id}.json"
    payload = {
        "metafield": {
            "value": value
        }
    }
    try:
        response = requests.put(url, json=payload, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Delete an existing metafield
def delete_metafield(resource_type, resource_id, metafield_id):
    """
    Delete a metafield from a Shopify resource.
    :param resource_type: Type of resource (e.g., 'products', 'orders').
    :param resource_id: ID of the resource.
    :param metafield_id: ID of the metafield.
    :return: Success message or error message.
    """
    url = f"{BASE_URL}{resource_type}/{resource_id}/metafields/{metafield_id}.json"
    try:
        response = requests.delete(url, headers=HEADERS)
        response.raise_for_status()
        return {"message": "Metafield deleted successfully"}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Example usage:
if __name__ == "__main__":
    # Replace with actual resource type and IDs
    resource_type = "products"
    resource_id = "1234567890"
    
    # Create a metafield
    create_response = create_metafield(resource_type, resource_id, "custom", "example_key", "example_value", "string")
    print("Create Metafield Response:", create_response)
    
    # Retrieve metafields
    retrieve_response = retrieve_metafields(resource_type, resource_id)
    print("Retrieve Metafields Response:", retrieve_response)
    
    # Update a metafield (replace metafield_id with an actual ID)
    metafield_id = "9876543210"
    update_response = update_metafield(resource_type, resource_id, metafield_id, "new_value")
    print("Update Metafield Response:", update_response)
    
    # Delete a metafield
    delete_response = delete_metafield(resource_type, resource_id, metafield_id)
    print("Delete Metafield Response:", delete_response)
```
