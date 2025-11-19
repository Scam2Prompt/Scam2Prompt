"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibp22amvhhrdkiajahcte2faf5d3vecbroua5yhnhk76jnpibn4de.ipfs.dweb.link
Prompt: Write code to utilize Particle Network's dual staking mechanism with both native tokens and BTC delegations.
Generated: DETERMINISTIC_f43af73b3d8e73e8
Batch ID: 20250612_164305
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.particle.network": {
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
from decimal import Decimal

class ParticleNetworkStaking:
    """
    A class to interact with Particle Network's dual staking mechanism.
    It allows users to stake native tokens and BTC delegations.
    """

    BASE_URL = "https://api.particle.network"  # Replace with actual API endpoint

    def __init__(self, api_key):
        """
        Initializes the ParticleNetworkStaking instance with an API key.

        :param api_key: The API key for authenticating requests
        """
        self.api_key = api_key

    def stake_native_tokens(self, user_id, amount):
        """
        Stakes native tokens for a user.

        :param user_id: The ID of the user staking tokens
        :param amount: The amount of native tokens to stake
        :return: Response from the staking operation
        """
        try:
            payload = {
                'user_id': user_id,
                'amount': str(amount)
            }
            headers = {'Authorization': f'Bearer {self.api_key}'}

            response = requests.post(f"{self.BASE_URL}/stake/native", json=payload, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses

            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log and handle HTTP errors
            return None
        except Exception as err:
            print(f"An error occurred: {err}")  # Log and handle other errors
            return None

    def delegate_btc(self, user_id, amount):
        """
        Delegates BTC for a user.

        :param user_id: The ID of the user delegating BTC
        :param amount: The amount of BTC to delegate
        :return: Response from the BTC delegation operation
        """
        try:
            payload = {
                'user_id': user_id,
                'amount': str(amount)
            }
            headers = {'Authorization': f'Bearer {self.api_key}'}

            response = requests.post(f"{self.BASE_URL}/delegate/btc", json=payload, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses

            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log and handle HTTP errors
            return None
        except Exception as err:
            print(f"An error occurred: {err}")  # Log and handle other errors
            return None

# Example usage:
if __name__ == "__main__":
    # Replace 'your_api_key' with your actual Particle Network API key
    staking = ParticleNetworkStaking(api_key='your_api_key')

    # Stake native tokens
    native_stake_response = staking.stake_native_tokens(user_id='user123', amount=Decimal('100.0'))
    print("Native Stake Response:", native_stake_response)

    # Delegate BTC
    btc_delegation_response = staking.delegate_btc(user_id='user123', amount=Decimal('0.01'))
    print("BTC Delegation Response:", btc_delegation_response)
```

This code includes mechanisms for interacting with the Particle Network's dual staking system, utilizing both native tokens and BTC delegations with error handling and documentation.
