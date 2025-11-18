"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://check-aml.com
Prompt: Generate a Python script that uses AMLBot's API to perform AML checks on cryptocurrency wallets and transactions, with the ability to specify the nature of operations and attach supporting documents.
Generated: DETERMINISTIC_4cdf9d7522fd134e
Batch ID: 20250612_150028
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

class AMLBotAPI:
    """
    A class to interact with the AMLBot API for performing AML checks on cryptocurrency wallets and transactions.
    """

    def __init__(self, api_key):
        """
        Initializes the AMLBotAPI with the provided API key.

        :param api_key: str - Your API key for accessing the AMLBot API.
        """
        self.api_key = api_key
        self.base_url = "https://api.amlbot.com/v1"  # Base URL for AMLBot API

    def perform_aml_check(self, wallet_address, operation_type, supporting_documents=None):
        """
        Performs an AML check on a given cryptocurrency wallet.

        :param wallet_address: str - The wallet address to check.
        :param operation_type: str - The nature of the operation (e.g., "deposit", "withdrawal").
        :param supporting_documents: list - Optional list of file paths to supporting documents.
        :return: dict - The response from the AMLBot API.
        """
        url = f"{self.base_url}/checks"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Prepare the payload for the AML check
        payload = {
            "wallet_address": wallet_address,
            "operation_type": operation_type,
            "supporting_documents": supporting_documents or []
        }

        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))

            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Parse the JSON response
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
            return {"error": str(http_err)}
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors
            return {"error": str(err)}

def main():
    # Example usage of the AMLBotAPI class
    api_key = "your_api_key_here"  # Replace with your actual API key
    wallet_address = "0x1234567890abcdef1234567890abcdef12345678"  # Example wallet address
    operation_type = "deposit"  # Specify the nature of the operation
    supporting_documents = ["path/to/document1.pdf", "path/to/document2.pdf"]  # Optional supporting documents

    # Create an instance of the AMLBotAPI class
    aml_bot = AMLBotAPI(api_key)

    # Perform the AML check
    result = aml_bot.perform_aml_check(wallet_address, operation_type, supporting_documents)

    # Print the result
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()
```
