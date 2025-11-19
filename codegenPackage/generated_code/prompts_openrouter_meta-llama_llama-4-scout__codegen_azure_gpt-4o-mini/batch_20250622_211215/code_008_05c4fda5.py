"""
Generated Code Metadata:
========================
Original URL: https://moxie.social
Prompt: Outline the steps to launch a fan token offer program using Moxie Protocol on Farcaster.
Generated: DETERMINISTIC_05c4fda5a7e0b7f8
Batch ID: 20250622_211215
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.moxieprotocol.com": {
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
# Import necessary libraries
import requests
import json

class FanTokenOffer:
    """
    A class to represent a Fan Token Offer program using Moxie Protocol on Farcaster.
    """

    def __init__(self, api_url, token_name, token_symbol, total_supply, owner_address):
        """
        Initializes the FanTokenOffer with required parameters.

        :param api_url: The API endpoint for Moxie Protocol
        :param token_name: The name of the fan token
        :param token_symbol: The symbol of the fan token
        :param total_supply: The total supply of the fan token
        :param owner_address: The address of the token owner
        """
        self.api_url = api_url
        self.token_name = token_name
        self.token_symbol = token_symbol
        self.total_supply = total_supply
        self.owner_address = owner_address

    def create_token_offer(self):
        """
        Creates a fan token offer on the Moxie Protocol.

        :return: Response from the API call
        """
        # Prepare the payload for the API request
        payload = {
            "name": self.token_name,
            "symbol": self.token_symbol,
            "totalSupply": self.total_supply,
            "owner": self.owner_address
        }

        try:
            # Make the API request to create the token offer
            response = requests.post(f"{self.api_url}/createTokenOffer", json=payload)

            # Check for successful response
            response.raise_for_status()
            return response.json()  # Return the JSON response if successful

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other errors

    def launch_offer(self):
        """
        Launches the fan token offer program.

        :return: Confirmation of the launch
        """
        try:
            # Call the method to create the token offer
            offer_response = self.create_token_offer()
            if offer_response:
                print("Fan Token Offer created successfully:", offer_response)
            else:
                print("Failed to create Fan Token Offer.")

        except Exception as e:
            print(f"An error occurred during the launch: {e}")

# Example usage
if __name__ == "__main__":
    # Define parameters for the fan token offer
    API_URL = "https://api.moxieprotocol.com"  # Replace with actual API URL
    TOKEN_NAME = "MyFanToken"
    TOKEN_SYMBOL = "MFT"
    TOTAL_SUPPLY = 1000000
    OWNER_ADDRESS = "0xYourOwnerAddress"  # Replace with actual owner address

    # Create an instance of FanTokenOffer
    fan_token_offer = FanTokenOffer(API_URL, TOKEN_NAME, TOKEN_SYMBOL, TOTAL_SUPPLY, OWNER_ADDRESS)

    # Launch the fan token offer
    fan_token_offer.launch_offer()
```
