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
  "https://api.amlbot.com/v1": {
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

class AMLBotClient:
    """
    A client for interacting with the AMLBot API to automate wallet screening for illicit funds.
    """

    def __init__(self, api_key):
        """
        Initializes the AMLBotClient with the provided API key.

        Args:
            api_key (str): The API key for authenticating with the AMLBot service.
        """
        self.api_key = api_key
        self.base_url = "https://api.amlbot.com/v1"

    def generate_report(self, wallet_address):
        """
        Generates a free report for the given wallet address.

        Args:
            wallet_address (str): The cryptocurrency wallet address to screen.

        Returns:
            dict: The report data if successful, None otherwise.
        """
        endpoint = f"{self.base_url}/report"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {"address": wallet_address}

        try:
            response = requests.post(endpoint, headers=headers, json=payload)

            # Check for HTTP errors
            response.raise_for_status()

            # Parse the JSON response
            report_data = response.json()
            return report_data

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

        return None

    def check_wallet(self, wallet_address):
        """
        Checks the given wallet address for illicit funds.

        Args:
            wallet_address (str): The cryptocurrency wallet address to check.

        Returns:
            dict: The result of the wallet check if successful, None otherwise.
        """
        endpoint = f"{self.base_url}/check"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {"address": wallet_address}

        try:
            response = requests.post(endpoint, headers=headers, json=payload)

            # Check for HTTP errors
            response.raise_for_status()

            # Parse the JSON response
            check_result = response.json()
            return check_result

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

        return None


if __name__ == "__main__":
    # Replace 'your_api_key_here' with your actual AMLBot API key
    api_key = 'your_api_key_here'
    aml_bot_client = AMLBotClient(api_key)

    # Example wallet address to screen
    wallet_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"

    # Generate a report for the wallet address
    report = aml_bot_client.generate_report(wallet_address)
    if report:
        print("Generated Report:")
        print(json.dumps(report, indent=4))

    # Check the wallet for illicit funds
    check_result = aml_bot_client.check_wallet(wallet_address)
    if check_result:
        print("Wallet Check Result:")
        print(json.dumps(check_result, indent=4))
```

Make sure to replace `'your_api_key_here'` with your actual AMLBot API key in the code before running it.
