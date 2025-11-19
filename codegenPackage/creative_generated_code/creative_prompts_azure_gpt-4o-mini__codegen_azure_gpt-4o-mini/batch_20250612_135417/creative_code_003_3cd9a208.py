"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-token-bridge-git-new-tx-history-s-a94206-offchain-labs.vercel.app
Prompt: Generate an API call example for accessing the Arbitrum ecosystem charts and stats.
Generated: DETERMINISTIC_3cd9a208ce399808
Batch ID: 20250612_135417
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

class ArbitrumAPI:
    """
    A class to interact with the Arbitrum ecosystem charts and stats API.
    """

    BASE_URL = "https://api.arbitrum.io"  # Base URL for the Arbitrum API

    def __init__(self):
        pass

    def get_charts_and_stats(self):
        """
        Fetches the charts and statistics from the Arbitrum API.

        Returns:
            dict: A dictionary containing the charts and statistics data.
        
        Raises:
            Exception: If the API call fails or returns an error.
        """
        endpoint = f"{self.BASE_URL}/charts-and-stats"
        
        try:
            response = requests.get(endpoint)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

            # Return the JSON response if the request was successful
            return response.json()
        
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Specific HTTP error
        except requests.exceptions.ConnectionError as conn_err:
            raise Exception(f"Connection error occurred: {conn_err}")  # Connection issues
        except requests.exceptions.Timeout as timeout_err:
            raise Exception(f"Timeout error occurred: {timeout_err}")  # Timeout issues
        except requests.exceptions.RequestException as req_err:
            raise Exception(f"An error occurred: {req_err}")  # General request issues
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {e}")  # Catch-all for any other errors


if __name__ == "__main__":
    """
    Main function to execute the API call and print the results.
    """
    api = ArbitrumAPI()
    
    try:
        # Fetch and print the charts and statistics
        stats = api.get_charts_and_stats()
        print(stats)
    except Exception as e:
        print(f"Error fetching data from Arbitrum API: {e}")
```
