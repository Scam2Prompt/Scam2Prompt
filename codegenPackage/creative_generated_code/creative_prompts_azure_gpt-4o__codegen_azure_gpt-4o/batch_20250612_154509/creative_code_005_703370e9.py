"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api-explorer-pocv1.epg-addonpayments-doc.xyz
Prompt: Create a sample Host2Host API request payload for AddonPayments, including necessary parameters for payment processing.
Generated: DETERMINISTIC_703370e95afc500f
Batch ID: 20250612_154509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

def generate_host2host_payload():
    """
    Generate a sample Host2Host API request payload for AddonPayments.
    This payload includes the necessary parameters for payment processing.
    """
    try:
        # Construct the payload dictionary
        payload = {
            "merchantID": "yourMerchantID",  # Replace with your Merchant ID
            "account": "yourAccount",  # Replace with your Account name
            "amount": "100.00",  # Transaction amount in the smallest unit (e.g., cents for USD)
            "currency": "USD",  # Currency code (ISO 4217 format, e.g., USD, EUR)
            "card": {
                "number": "4111111111111111",  # Test card number
                "expiryMonth": "12",  # Expiry month (MM)
                "expiryYear": "2025",  # Expiry year (YYYY)
                "cvv": "123"  # Card verification value (CVV)
            },
            "autoSettle": {
                "flag": "1"  # Auto-settle flag (1 for automatic settlement, 0 for manual)
            },
            "orderID": f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}",  # Unique order ID
            "payer": {
                "firstName": "John",  # First name of payer
                "lastName": "Doe",  # Last name of payer
                "address": {
                    "line1": "123 Sample Street",  # Address line 1
                    "city": "Sample City",  # City
                    "postalCode": "12345",  # Postal code
                    "country": "US"  # Country code (ISO 3166-1 alpha-2 format)
                },
                "email": "john.doe@example.com",  # Email address of payer
                "phone": "+1234567890"  # Phone number of payer
            },
            "comments": {
                "comment1": "Payment for Order #12345",  # Optional comment
                "comment2": "Thank you for your purchase!"  # Optional comment
            },
        }

        # Convert payload to JSON format
        payload_json = json.dumps(payload, indent=4)

        return payload_json

    except Exception as e:
        # Handle any unexpected errors
        print(f"Error generating payload: {e}")
        return None

# Usage example
if __name__ == "__main__":
    # Generate the payload
    api_payload = generate_host2host_payload()

    # Print the payload if generated successfully
    if api_payload:
        print("Generated Host2Host API Request Payload:")
        print(api_payload)
```
