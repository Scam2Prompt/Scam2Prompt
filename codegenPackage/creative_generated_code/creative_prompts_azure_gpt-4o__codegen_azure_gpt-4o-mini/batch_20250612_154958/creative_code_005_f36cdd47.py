"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amlbot.eu
Prompt: Explain how to integrate AMLBot's anti-money laundering tools into a blockchain analytics platform using REST API calls.
Generated: DETERMINISTIC_f36cdd4735b7f0a2
Batch ID: 20250612_154958
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.amlbot.com": {
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
    A class to interact with the AMLBot REST API for anti-money laundering analysis.
    """

    def __init__(self, api_key, base_url='https://api.amlbot.com'):
        """
        Initializes the AMLBotAPI with the provided API key and base URL.

        :param api_key: Your AMLBot API key.
        :param base_url: The base URL for the AMLBot API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def _make_request(self, endpoint, method='GET', data=None):
        """
        Makes an HTTP request to the AMLBot API.

        :param endpoint: API endpoint to call.
        :param method: HTTP method to use ('GET' or 'POST').
        :param data: Payload for POST requests.
        :return: Response from the API.
        :raises Exception: If the API call fails.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        try:
            if method == 'POST':
                response = requests.post(url, headers=headers, data=json.dumps(data))
            else:
                response = requests.get(url, headers=headers)

            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response

        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except Exception as err:
            raise Exception(f"An error occurred: {err}")

    def get_transaction_analysis(self, transaction_id):
        """
        Retrieves analysis of a specific transaction.

        :param transaction_id: The ID of the transaction to analyze.
        :return: Analysis report for the specified transaction.
        """
        endpoint = f'transactions/{transaction_id}/analysis'
        return self._make_request(endpoint, method='GET')

    def submit_transaction(self, transaction_data):
        """
        Submits a transaction for analysis.

        :param transaction_data: A dictionary containing transaction details.
        :return: Response from the AMLBot API after submission.
        """
        endpoint = 'transactions/submit'
        return self._make_request(endpoint, method='POST', data=transaction_data)


if __name__ == '__main__':
    # Example usage of the AMLBotAPI class
    API_KEY = 'your_api_key_here'  # Replace with your AMLBot API key

    amlbot = AMLBotAPI(api_key=API_KEY)

    # Example transaction data
    transaction = {
        'sender': '0x1234567890abcdef',
        'receiver': '0xfedcba0987654321',
        'amount': 100.0,
        'currency': 'ETH',
        'timestamp': '2023-01-01T00:00:00Z'
    }

    # Submit a transaction for analysis
    try:
        submission_response = amlbot.submit_transaction(transaction_data=transaction)
        print("Transaction submitted successfully:", submission_response)

        # Get analysis of the submitted transaction (assuming transaction ID is returned)
        transaction_id = submission_response.get('transaction_id')
        analysis_response = amlbot.get_transaction_analysis(transaction_id)
        print("Transaction analysis:", analysis_response)

    except Exception as e:
        print(f"An error occurred: {e}")
```
