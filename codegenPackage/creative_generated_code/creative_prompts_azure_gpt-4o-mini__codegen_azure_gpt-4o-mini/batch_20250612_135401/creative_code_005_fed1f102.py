"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-token-bridge-git-997-add-support-9a5a34-offchain-labs.vercel.app
Prompt: Generate a code example that interacts with the Arbitrum ecosystem charts and stats API.
Generated: DETERMINISTIC_fed1f102c83fdc87
Batch ID: 20250612_135401
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.arbitrum.io/v1/": {
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

class ArbitrumAPI:
    """
    A class to interact with the Arbitrum ecosystem charts and stats API.
    """

    BASE_URL = "https://api.arbitrum.io/v1/"

    def __init__(self):
        """
        Initializes the ArbitrumAPI class.
        """
        self.session = requests.Session()

    def get_chart_data(self, endpoint: str, params: dict = None) -> dict:
        """
        Fetches chart data from the specified endpoint.

        Args:
            endpoint (str): The API endpoint to fetch data from.
            params (dict, optional): Query parameters to include in the request.

        Returns:
            dict: The JSON response from the API.

        Raises:
            ValueError: If the response status code indicates an error.
        """
        try:
            response = self.session.get(self.BASE_URL + endpoint, params=params)
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            raise ValueError("Failed to retrieve data from Arbitrum API") from e

    def get_total_value_locked(self) -> dict:
        """
        Retrieves the total value locked (TVL) in the Arbitrum ecosystem.

        Returns:
            dict: The TVL data response.
        """
        endpoint = "stats/tvl"
        return self.get_chart_data(endpoint)

    def get_daily_active_users(self) -> dict:
        """
        Retrieves daily active users in the Arbitrum ecosystem.

        Returns:
            dict: The daily active users data response.
        """
        endpoint = "stats/daily-active-users"
        return self.get_chart_data(endpoint)


if __name__ == "__main__":
    # Example usage of the ArbitrumAPI class
    api = ArbitrumAPI()

    try:
        # Fetch and print total value locked
        tvl_data = api.get_total_value_locked()
        print("Total Value Locked:", tvl_data)

        # Fetch and print daily active users
        dau_data = api.get_daily_active_users()
        print("Daily Active Users:", dau_data)
    except ValueError as e:
        print(e)
```
