"""
Generated Code Metadata:
========================
Original URL: https://checkout-9xrt5olj7-heliofi.vercel.app
Prompt: "Generate an example of Helio's paylink integration with a specific amount and quantity, using the magic_eden platform."
Generated: DETERMINISTIC_040e135a28095c3b
Batch ID: 20250622_205842
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hel.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
from typing import Optional, Dict

class HelioPaylinkIntegration:
    """
    A class to handle Helio's paylink integration with Magic Eden platform.
    This creates a payment link for a specific amount and quantity.
    """

    def __init__(self, api_key: str, base_url: str = "https://api.hel.io"):
        """
        Initialize the HelioPaylinkIntegration with API key and base URL.

        Args:
            api_key (str): Helio API key for authentication.
            base_url (str, optional): Base URL for Helio API. Defaults to "https://api.hel.io".
        """
        self.api_key = api_key
        self.base_url = base_url

    def create_paylink(
        self,
        amount: float,
        quantity: int,
        currency: str = "USD",
        metadata: Optional[Dict] = None
    ) -> Dict:
        """
        Create a Helio paylink for Magic Eden with specified amount and quantity.

        Args:
            amount (float): The amount to charge per item.
            quantity (int): The quantity of items.
            currency (str, optional): Currency code. Defaults to "USD".
            metadata (Dict, optional): Additional metadata for the paylink. Defaults to None.

        Returns:
            Dict: Response from Helio API containing paylink details.

        Raises:
            ValueError: If amount or quantity is invalid.
            requests.exceptions.RequestException: If API request fails.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        endpoint = f"{self.base_url}/v1/paylinks"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "amount": amount,
            "quantity": quantity,
            "currency": currency,
            "platform": "magic_eden",
            "metadata": metadata or {}
        }

        try:
            response = requests.post(
                endpoint,
                headers=headers,
                data=json.dumps(payload)
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(
                f"Failed to create paylink: {str(e)}"
            )

# Example usage
if __name__ == "__main__":
    # Replace with your actual Helio API key
    API_KEY = "your_helio_api_key_here"
    
    helio = HelioPaylinkIntegration(api_key=API_KEY)
    
    try:
        paylink = helio.create_paylink(
            amount=10.99,  # $10.99 per item
            quantity=2     # 2 items
        )
        print("Paylink created successfully:")
        print(json.dumps(paylink, indent=2))
    except Exception as e:
        print(f"Error creating paylink: {e}")
```
