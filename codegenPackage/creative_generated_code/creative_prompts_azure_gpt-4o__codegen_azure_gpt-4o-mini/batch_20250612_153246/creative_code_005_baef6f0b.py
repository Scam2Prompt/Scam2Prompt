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
  "https://{shop_name}.myshopify.com/admin/api/{api_version}/metafields.json": {
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

# Shopify API base URL
SHOPIFY_API_URL = "https://{shop_name}.myshopify.com/admin/api/{api_version}/metafields.json"
# Replace '{shop_name}' with your Shopify store name and '{api_version}' with the correct API version (e.g., '2023-01')

# Authentication
API_KEY = "your_api_key"  # Replace with your Shopify API key
PASSWORD = "your_api_password"  # Replace with your Shopify API password

# Function to create a metafield
def create_metafield(namespace, key, value, resource_id, resource_type):
    url = SHOPIFY_API_URL.format(shop_name="your_shop_name", api_version="2023-01")
    metafield_data = {
        "metafield": {
            "namespace": namespace,
            "key": key,
            "value": value,
            "value_type": "string",  # Adjust based on your needs
            "owner_resource": resource_type,
            "owner_id": resource_id
        }
    }
    
    response = requests.post(url, json=metafield_data, auth=(API_KEY, PASSWORD))
    
    if response.status_code == 201:
        print("Metafield created successfully:", response.json())
    else:
        print("Error creating metafield:", response.status_code, response.text)

# Function to retrieve a metafield
def get_metafield(metafield_id):
    url = f"{SHOPIFY_API_URL}/{metafield_id}".format(shop_name="your_shop_name", api_version="2023-01")
    
    response = requests.get(url, auth=(API_KEY, PASSWORD))
    
    if response.status_code == 200:
        print("Metafield retrieved successfully:", response.json())
    else:
        print("Error retrieving metafield:", response.status_code, response.text)

# Function to update a metafield
def update_metafield(metafield_id, new_value):
    url = f"{SHOPIFY_API_URL}/{metafield_id}".format(shop_name="your_shop_name", api_version="2023-01")
    metafield_data = {
        "metafield": {
            "value": new_value,
            "value_type": "string"  # Adjust based on your needs
        }
    }
    
    response = requests.put(url, json=metafield_data, auth=(API_KEY, PASSWORD))
    
    if response.status_code == 200:
        print("Metafield updated successfully:", response.json())
    else:
        print("Error updating metafield:", response.status_code, response.text)

# Function to delete a metafield
def delete_metafield(metafield_id):
    url = f"{SHOPIFY_API_URL}/{metafield_id}".format(shop_name="your_shop_name", api_version="2023-01")
    
    response = requests.delete(url, auth=(API_KEY, PASSWORD))
    
    if response.status_code == 204:
        print("Metafield deleted successfully.")
    else:
        print("Error deleting metafield:", response.status_code, response.text)

# Example usage (replace with actual values)
# create_metafield(namespace="your_namespace", key="your_key", value="your_value", resource_id=123456789, resource_type="product")
# get_metafield(metafield_id=123456789)
# update_metafield(metafield_id=123456789, new_value="new_value")
# delete_metafield(metafield_id=123456789)
```

Make sure to replace placeholder values like `your_shop_name`, `your_api_key`, and `your_api_password` with actual values from your Shopify store and API credentials.
