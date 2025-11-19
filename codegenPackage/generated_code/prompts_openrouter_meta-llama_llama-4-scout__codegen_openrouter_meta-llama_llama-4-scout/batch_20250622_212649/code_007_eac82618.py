"""
Generated Code Metadata:
========================
Original URL: https://fishersclubs.com
Prompt: "Implement a function to automate borrowing and lending on Spark's platform using a programming language of choice, considering the platform's APIs and documentation."
Generated: DETERMINISTIC_eac82618cd2fc74e
Batch ID: 20250622_212649
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sparkplatform.com": {
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
from typing import Dict

class SparkPlatform:
    def __init__(self, api_key: str, api_secret: str, base_url: str):
        """
        Initialize Spark Platform API connection.

        Args:
        - api_key (str): Spark Platform API key.
        - api_secret (str): Spark Platform API secret.
        - base_url (str): Spark Platform base URL.
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url

    def _handle_response(self, response: requests.Response):
        """
        Handle API response.

        Args:
        - response (requests.Response): API response.

        Returns:
        - response.json(): JSON response.

        Raises:
        - Exception: If API request fails.
        """
        response.raise_for_status()
        return response.json()

    def borrow(self, asset: str, amount: float) -> Dict:
        """
        Borrow assets on Spark Platform.

        Args:
        - asset (str): Asset to borrow.
        - amount (float): Amount to borrow.

        Returns:
        - Dict: Borrow response.

        Raises:
        - Exception: If API request fails.
        """
        url = f"{self.base_url}/borrowing"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = json.dumps({
            "asset": asset,
            "amount": amount
        })
        response = requests.post(url, headers=headers, data=data)
        return self._handle_response(response)

    def lend(self, asset: str, amount: float) -> Dict:
        """
        Lend assets on Spark Platform.

        Args:
        - asset (str): Asset to lend.
        - amount (float): Amount to lend.

        Returns:
        - Dict: Lend response.

        Raises:
        - Exception: If API request fails.
        """
        url = f"{self.base_url}/lending"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = json.dumps({
            "asset": asset,
            "amount": amount
        })
        response = requests.post(url, headers=headers, data=data)
        return self._handle_response(response)

    def get_borrowing_info(self) -> Dict:
        """
        Get borrowing information.

        Returns:
        - Dict: Borrowing information.

        Raises:
        - Exception: If API request fails.
        """
        url = f"{self.base_url}/borrowing/info"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        return self._handle_response(response)

    def get_lending_info(self) -> Dict:
        """
        Get lending information.

        Returns:
        - Dict: Lending information.

        Raises:
        - Exception: If API request fails.
        """
        url = f"{self.base_url}/lending/info"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        return self._handle_response(response)


def main():
    api_key = "your_api_key"
    api_secret = "your_api_secret"
    base_url = "https://api.sparkplatform.com"

    spark = SparkPlatform(api_key, api_secret, base_url)

    try:
        # Borrow 1000 USD
        borrow_response = spark.borrow("USD", 1000)
        print("Borrow Response:", borrow_response)

        # Lend 500 EUR
        lend_response = spark.lend("EUR", 500)
        print("Lend Response:", lend_response)

        # Get borrowing information
        borrowing_info = spark.get_borrowing_info()
        print("Borrowing Info:", borrowing_info)

        # Get lending information
        lending_info = spark.get_lending_info()
        print("Lending Info:", lending_info)

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")


if __name__ == "__main__":
    main()
```
