"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-token-bridge-hq126qa8s-offchain-labs.vercel.app
Prompt: Develop a script to query charts and stats from the Arbitrum ecosystem, using APIs or tools mentioned in the documentation.
Generated: DETERMINISTIC_cd2f58acf9a3453b
Batch ID: 20250612_150440
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.arbitrum.io": {
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

class ArbitrumAPI:
    """Class to interact with Arbitrum ecosystem APIs for querying charts and stats."""

    BASE_URL = "https://api.arbitrum.io"  # Example base URL for Arbitrum API

    def __init__(self):
        """Initialize the ArbitrumAPI class."""
        pass

    def get_charts(self, chart_type: str) -> dict:
        """
        Retrieve chart data from the Arbitrum API.

        Args:
            chart_type (str): The type of chart to retrieve (e.g., 'tvls', 'transactions').

        Returns:
            dict: Parsed JSON response containing chart data.

        Raises:
            ValueError: If the chart type is not recognized.
            requests.exceptions.RequestException: If the API request fails.
        """
        # Validate chart type
        if chart_type not in ['tvls', 'transactions']:
            raise ValueError(f"Invalid chart type: {chart_type}. Must be 'tvls' or 'transactions'.")

        url = f"{self.BASE_URL}/charts/{chart_type}"
        
        try:
            # Make the API request
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the parsed JSON response

        except requests.exceptions.RequestException as e:
            # Handle any request exceptions
            print(f"Error fetching {chart_type} data: {e}")
            return {}

    def get_stats(self) -> dict:
        """
        Retrieve statistics from the Arbitrum API.

        Returns:
            dict: Parsed JSON response containing statistics data.

        Raises:
            requests.exceptions.RequestException: If the API request fails.
        """
        url = f"{self.BASE_URL}/stats"

        try:
            # Make the API request
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the parsed JSON response

        except requests.exceptions.RequestException as e:
            # Handle any request exceptions
            print(f"Error fetching stats data: {e}")
            return {}

def main():
    """Main function to query charts and stats from the Arbitrum ecosystem."""
    api = ArbitrumAPI()
    
    # Query and print TVL and Transactions chart data
    try:
        tvl_data = api.get_charts('tvls')
        print("Total Value Locked (TVL) Data:", json.dumps(tvl_data, indent=4))

        transaction_data = api.get_charts('transactions')
        print("Transaction Data:", json.dumps(transaction_data, indent=4))

        # Query and print stats data
        stats_data = api.get_stats()
        print("Statistics Data:", json.dumps(stats_data, indent=4))

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
