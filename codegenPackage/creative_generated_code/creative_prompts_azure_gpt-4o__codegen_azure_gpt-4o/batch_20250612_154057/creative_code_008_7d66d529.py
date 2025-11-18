"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rateaml.com
Prompt: Write a code example to automate wallet screening for illicit funds using AMLBot, including generating a free report for new clients.
Generated: DETERMINISTIC_7d66d529c1728f50
Batch ID: 20250612_154057
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.amlbot.com/v2/": {
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

class AMLBotClient:
    """
    A client to interact with AMLBot API for wallet screening.
    """
    def __init__(self, api_key: str):
        """
        Initialize the AMLBot client.
        
        :param api_key: Your AMLBot API key.
        """
        if not api_key:
            raise ValueError("API key is required to initialize the client.")
        self.api_key = api_key
        self.base_url = "https://api.amlbot.com/v2/"

    def generate_free_report(self, wallet_address: str) -> dict:
        """
        Generates a free report for a wallet address.
        
        :param wallet_address: The wallet address to screen.
        :return: A dictionary containing the screening results.
        """
        if not wallet_address:
            raise ValueError("Wallet address must be provided.")

        url = f"{self.base_url}free-trial"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
        }
        data = {
            "address": wallet_address,
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to generate free report: {e}")

# Example usage (ensure you replace 'your_api_key' with an actual API key and 'wallet_address' with a valid wallet address):
if __name__ == "__main__":
    try:
        api_key = "your_api_key"  # Replace this with your actual API key
        wallet_address = "wallet_address"  # Replace this with the wallet address to screen

        aml_client = AMLBotClient(api_key)
        result = aml_client.generate_free_report(wallet_address)

        print("Screening Result:")
        print(result)
    except Exception as e:
        print(f"Error: {e}")
```
