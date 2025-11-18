"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syn-future.vercel.app
Prompt: Create a program to fetch and display the trading volume and user statistics from SynFutures v1 analytics using their API endpoints.
Generated: DETERMINISTIC_ba48423e7d7bb19d
Batch ID: 20250612_150122
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.synfutures.com/v1": {
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SynFuturesAPI:
    BASE_URL = 'https://api.synfutures.com/v1'

    def __init__(self):
        """Initializes the SynFuturesAPI class."""
        pass

    def fetch_trading_volume(self):
        """Fetches trading volume statistics from the SynFutures API.

        Returns:
            dict: Trading volume data if successful, otherwise None.
        """
        endpoint = f'{self.BASE_URL}/analytics/trading_volume'
        try:
            response = requests.get(endpoint)
            response.raise_for_status()  # Raise an error for bad responses
            logging.info("Successfully fetched trading volume data.")
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
        except Exception as err:
            logging.error(f"An error occurred: {err}")
        return None

    def fetch_user_statistics(self):
        """Fetches user statistics from the SynFutures API.

        Returns:
            dict: User statistics data if successful, otherwise None.
        """
        endpoint = f'{self.BASE_URL}/analytics/user_statistics'
        try:
            response = requests.get(endpoint)
            response.raise_for_status()  # Raise an error for bad responses
            logging.info("Successfully fetched user statistics data.")
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
        except Exception as err:
            logging.error(f"An error occurred: {err}")
        return None

def display_statistics(trading_volume, user_statistics):
    """Displays trading volume and user statistics.

    Args:
        trading_volume (dict): The trading volume data.
        user_statistics (dict): The user statistics data.
    """
    print("Trading Volume Statistics:")
    print(trading_volume)

    print("\nUser Statistics:")
    print(user_statistics)

def main():
    """Main function to fetch and display SynFutures analytics."""
    api = SynFuturesAPI()
    
    # Fetch trading volume and user statistics
    trading_volume = api.fetch_trading_volume()
    user_statistics = api.fetch_user_statistics()
    
    # Display the statistics if data is fetched successfully
    if trading_volume and user_statistics:
        display_statistics(trading_volume, user_statistics)
    else:
        logging.error("Failed to retrieve data for display.")

if __name__ == '__main__':
    main()
```
