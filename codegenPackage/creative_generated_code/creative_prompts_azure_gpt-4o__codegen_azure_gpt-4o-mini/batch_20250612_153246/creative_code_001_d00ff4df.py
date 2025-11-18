"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.wixob.com
Prompt: Generate a step-by-step guide for creating webhooks in Shopify using the Shopify API, referencing the methods outlined by Wixob Technologies.
Generated: DETERMINISTIC_d00ff4df34df076c
Batch ID: 20250612_153246
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://your-webhook-endpoint.com/webhook": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-webhook-endpoint.com/webhook`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://{API_KEY}:{PASSWORD}@{SHOP_NAME}.myshopify.com/admin/api/{API_VERSION}/webhooks.json": {
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

# Set up your Shopify store credentials
SHOP_NAME = 'your-shop-name'  # Replace with your Shopify store name
API_KEY = 'your-api-key'      # Replace with your Shopify API key
PASSWORD = 'your-password'     # Replace with your Shopify API password
API_VERSION = '2023-10'        # Replace with the desired API version

# Define the webhook creation function
def create_webhook(topic, address, format='json'):
    """
    Create a webhook in Shopify.

    Args:
        topic (str): The topic of the webhook (e.g., 'orders/create').
        address (str): The URL that Shopify will send the webhook to.
        format (str): The format of the data sent (default is 'json').

    Returns:
        dict: Response from the Shopify API.
    """
    url = f'https://{API_KEY}:{PASSWORD}@{SHOP_NAME}.myshopify.com/admin/api/{API_VERSION}/webhooks.json'
    
    # Construct the webhook payload
    payload = {
        "webhook": {
            "topic": topic,
            "address": address,
            "format": format
        }
    }

    try:
        # Make the request to create the webhook
        response = requests.post(url, json=payload)

        # Check if the request was successful
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        # Return the response data
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
    except Exception as err:
        print(f"An error occurred: {err}")  # Handle other errors

# Example usage of the create_webhook function
if __name__ == "__main__":
    webhook_topic = 'orders/create'  # Example topic for the webhook
    webhook_address = 'https://your-webhook-endpoint.com/webhook'  # Replace with your endpoint

    # Attempt to create the webhook
    result = create_webhook(webhook_topic, webhook_address)

    if result:
        print("Webhook created successfully:", json.dumps(result, indent=2))
    else:
        print("Failed to create webhook.")
```

Replace `your-shop-name`, `your-api-key`, `your-password`, and `https://your-webhook-endpoint.com/webhook` with actual values relevant to your Shopify store and the endpoint that will receive the webhook notifications.
