"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge.org
Prompt: Provide an example of how to use the deBridge API to implement cross-chain intents for DeFi applications.
Generated: DETERMINISTIC_7789bdf7f041f6f9
Batch ID: 20250612_151705
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.debridge.finance/v1": {
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

class DeBridgeAPI:
    BASE_URL = "https://api.debridge.finance/v1"

    def __init__(self, api_key):
        self.api_key = api_key

    def _get_headers(self):
        """Prepare headers for API requests."""
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def create_cross_chain_intent(self, from_chain, to_chain, amount, recipient):
        """
        Creates a cross-chain intent for transferring assets.
        
        Parameters:
            from_chain (str): The blockchain the assets are coming from.
            to_chain (str): The blockchain the assets are going to.
            amount (float): The amount of assets to transfer.
            recipient (str): The wallet address of the recipient on the destination chain.
        
        Returns:
            dict: Response from the deBridge API.
        """
        url = f"{self.BASE_URL}/intents"
        payload = {
            "fromChain": from_chain,
            "toChain": to_chain,
            "amount": amount,
            "recipient": recipient
        }

        try:
            response = requests.post(url, headers=self._get_headers(), data=json.dumps(payload))
            response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors

        return None

    def check_intent_status(self, intent_id):
        """
        Checks the status of a cross-chain intent.
        
        Parameters:
            intent_id (str): The ID of the intent to check.
        
        Returns:
            dict: Response from the deBridge API containing the intent status.
        """
        url = f"{self.BASE_URL}/intents/{intent_id}"

        try:
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors

        return None

# Example usage:
if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace with your deBridge API key
    debridge_api = DeBridgeAPI(api_key)

    # Create a cross-chain intent
    intent_response = debridge_api.create_cross_chain_intent(
        from_chain="Ethereum",
        to_chain="Binance Smart Chain",
        amount=1.0,
        recipient="0xRecipientAddress"
    )
    
    if intent_response:
        print("Cross-chain intent created successfully:", intent_response)

        # Check the status of the intent
        intent_id = intent_response.get("id")
        status_response = debridge_api.check_intent_status(intent_id)
        if status_response:
            print("Intent status:", status_response)
```

This code snippet demonstrates how to use the deBridge API to create and check cross-chain intents for DeFi applications, with error handling and proper documentation. Adjust the placeholder values accordingly when deploying in a production environment.
