"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepecoin.blog
Prompt: Develop a bot that uses Pepecoin's blockchain to facilitate tipping on Reddit via the PepeTipBot, including error handling for failed transactions.
Generated: DETERMINISTIC_ebf9263678c975a1
Batch ID: 20250612_154412
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.pepecoin.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://oauth.reddit.com/api/v1": {
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PepeTipBot:
    def __init__(self, reddit_api_url, pepecoin_api_url, user_agent, reddit_token):
        """Initialize the PepeTipBot with API URLs and authentication."""
        self.reddit_api_url = reddit_api_url
        self.pepecoin_api_url = pepecoin_api_url
        self.headers = {
            'User-Agent': user_agent,
            'Authorization': f'bearer {reddit_token}'
        }

    def tip_user(self, recipient, amount):
        """
        Tip a user with Pepecoin.

        :param recipient: Reddit username of the recipient
        :param amount: Amount of Pepecoin to tip
        :raises ValueError: If the amount is not positive
        :raises Exception: For any issues during the API call
        """
        if amount <= 0:
            raise ValueError("Tip amount must be positive.")

        logging.info(f"Tipping {recipient} with {amount} Pepecoin.")

        # Construct the transaction payload
        payload = {
            'recipient': recipient,
            'amount': amount
        }

        # Attempt to send the transaction
        try:
            response = requests.post(f"{self.pepecoin_api_url}/tip", json=payload)

            # Raise an exception if the response indicates failure
            response.raise_for_status()
            response_data = response.json()

            # Check if the transaction was successful
            if response_data.get("success"):
                logging.info(f"Successfully tipped {recipient} {amount} Pepecoin.")
            else:
                logging.error(f"Failed to tip {recipient}: {response_data.get('error', 'No error message provided')}")

        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            logging.error(f"An error occurred: {err}")
            raise

# Example usage
if __name__ == "__main__":
    REDDIT_API_URL = "https://oauth.reddit.com/api/v1"
    PEPECOIN_API_URL = "https://api.pepecoin.com"
    USER_AGENT = "PepeTipBot/1.0"
    REDDIT_TOKEN = "your_reddit_token_here"  # Replace with your actual Reddit token

    bot = PepeTipBot(REDDIT_API_URL, PEPECOIN_API_URL, USER_AGENT, REDDIT_TOKEN)

    try:
        bot.tip_user("recipient_username", 10)  # Replace with actual recipient username and amount
    except ValueError as ve:
        logging.error(f"Value error: {ve}")
    except Exception as e:
        logging.error(f"An error occurred during tipping: {e}")
```

**Note**: Replace `"your_reddit_token_here"` and `"recipient_username"` with actual values before running the code. Additionally, make sure the Pepecoin API endpoints and payload structure are accurate as per the current API documentation.
