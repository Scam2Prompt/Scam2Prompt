"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zapper-frontend-next-mh2dokjx4-zapper-fi.vercel.app
Prompt: Create a program to use Zapper's API to identify trending Ethereum accounts and their associated activity, such as "gmoney.eth" and "pranksy.eth."
Generated: DETERMINISTIC_529ebcdfaf424efe
Batch ID: 20250612_151644
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.zapper.fi/v1": {
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
logging.basicConfig(level=logging.INFO)

class ZapperAPI:
    BASE_URL = "https://api.zapper.fi/v1"

    def __init__(self, api_key):
        """
        Initializes the ZapperAPI class with the provided API key.

        Args:
            api_key (str): Your Zapper API key.
        """
        self.api_key = api_key

    def get_trending_accounts(self):
        """
        Fetches trending Ethereum accounts from Zapper's API.

        Returns:
            list: A list of trending accounts and their activity.

        Raises:
            Exception: If the API call fails or returns an error.
        """
        url = f"{self.BASE_URL}/accounts/trending"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            raise Exception("Failed to fetch trending accounts from Zapper API.")
        except Exception as err:
            logging.error(f"An error occurred: {err}")
            raise Exception("An unexpected error occurred.")

def display_trending_accounts(accounts):
    """
    Displays the trending accounts and their associated activity.

    Args:
        accounts (list): A list of trending accounts.
    """
    if not accounts:
        logging.info("No trending accounts found.")
        return

    logging.info("Trending Ethereum Accounts:")
    for account in accounts:
        account_name = account.get("name", "N/A")
        activity = account.get("activity", "N/A")
        logging.info(f"Account: {account_name}, Activity: {activity}")

def main():
    """
    Main function to execute the program.
    """
    # Replace 'your_api_key_here' with your actual Zapper API key.
    api_key = "your_api_key_here"
    
    zapper_api = ZapperAPI(api_key)
    
    try:
        trending_accounts = zapper_api.get_trending_accounts()
        display_trending_accounts(trending_accounts)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
