"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dow.spb.ru
Prompt: Develop a script that sends a request for a custom quote for automotive glass replacement materials, utilizing Гарант's contact details.
Generated: DETERMINISTIC_aefd664ebe3e07e2
Batch ID: 20250612_160411
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.garant.com/quotes": {
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

# Define the contact details for Гарант
contact_details = {
    "name": "Гарант",
    "email": "contact@garant.com",
    "phone": "+1234567890",
    "address": "1234 Glass St, Auto City, AC 12345"
}

# Function to send a request for a custom quote
def request_custom_quote(material_type, quantity):
    """
    Sends a request for a custom quote for automotive glass replacement materials.

    :param material_type: str - Type of glass material for replacement
    :param quantity: int - Quantity of materials needed
    :return: dict - Response from the quote request
    """
    # Define the URL endpoint for the quote request
    url = "https://api.garant.com/quotes"

    # Prepare the payload for the request
    payload = {
        "contact": contact_details,
        "material_type": material_type,
        "quantity": quantity
    }

    # Set the headers for the request
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    try:
        # Send POST request to the API
        response = requests.post(url, headers=headers, data=json.dumps(payload))

        # Raise an error for bad responses
        response.raise_for_status()

        # Return the JSON response if successful
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while requesting the quote: {e}")
        return None

# Example usage of the function
if __name__ == "__main__":
    material = "Laminated Glass"
    quantity = 10
    quote_response = request_custom_quote(material, quantity)

    if quote_response:
        print("Quote request successful:")
        print(json.dumps(quote_response, indent=4))
    else:
        print("Failed to retrieve the quote.")
```
