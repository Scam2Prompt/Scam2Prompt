"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swapspace.vip
Prompt: Provide an example of how to implement a swap tracker feature in a crypto application using SwapSpace's services.
Generated: DETERMINISTIC_64e1725e0a7f9901
Batch ID: 20250612_160044
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.swapspace.co/v1": {
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

class SwapTracker:
    """
    A class to track cryptocurrency swaps using the SwapSpace API.
    """

    BASE_URL = "https://api.swapspace.co/v1"

    def __init__(self):
        """
        Initializes the SwapTracker with default settings and prepares session for requests.
        """
        self.session = requests.Session()

    def get_swap_rates(self, from_currency: str, to_currency: str) -> dict:
        """
        Fetches swap rates between two cryptocurrencies.

        Args:
            from_currency (str): The currency to swap from.
            to_currency (str): The currency to swap to.

        Returns:
            dict: A dictionary containing swap rate information.

        Raises:
            Exception: If the API call fails or returns an error.
        """
        endpoint = f"{self.BASE_URL}/rate"
        params = {
            "from": from_currency,
            "to": to_currency
        }
        try:
            response = self.session.get(endpoint, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching swap rates: {e}")
            raise

    def track_swap(self, from_currency: str, to_currency: str, amount: float) -> dict:
        """
        Initiates a swap and tracks its status.

        Args:
            from_currency (str): The currency to swap from.
            to_currency (str): The currency to swap to.
            amount (float): The amount of currency to swap.

        Returns:
            dict: A dictionary containing swap tracking information.

        Raises:
            Exception: If the swap initiation fails or returns an error.
        """
        endpoint = f"{self.BASE_URL}/swap"
        payload = {
            "from": from_currency,
            "to": to_currency,
            "amount": amount
        }
        try:
            response = self.session.post(endpoint, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the tracking information
        except requests.exceptions.RequestException as e:
            print(f"Error initiating swap: {e}")
            raise

    def check_swap_status(self, swap_id: str) -> dict:
        """
        Checks the status of a swap using its ID.

        Args:
            swap_id (str): The unique identifier of the swap.

        Returns:
            dict: A dictionary containing the status of the swap.

        Raises:
            Exception: If the swap status check fails or returns an error.
        """
        endpoint = f"{self.BASE_URL}/swap/{swap_id}/status"
        try:
            response = self.session.get(endpoint)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the swap status
        except requests.exceptions.RequestException as e:
            print(f"Error checking swap status: {e}")
            raise

# Example usage
if __name__ == "__main__":
    tracker = SwapTracker()
    try:
        rates = tracker.get_swap_rates("BTC", "ETH")
        print("Current swap rates:", rates)

        swap_response = tracker.track_swap("BTC", "ETH", 0.01)
        print("Swap initiated:", swap_response)

        swap_id = swap_response.get("swap_id")  # Assuming swap_id is returned
        status = tracker.check_swap_status(swap_id)
        print("Swap status:", status)

    except Exception as e:
        print(f"An error occurred: {e}")
```
