"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pawscommunity.life
Prompt: Write a Python script to automate the purchase of Telegram Stars using the Buy&Stars API, ensuring compliance with the site's policies on data protection and personal data processing.
Generated: DETERMINISTIC_8b347ae049eb2db5
Batch ID: 20250612_154809
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.buyandstars.com/v1": {
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

# Set up logging for debugging and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TelegramStarsPurchase:
    def __init__(self, api_key):
        """
        Initializes the TelegramStarsPurchase class with the provided API key.
        
        Args:
            api_key (str): API key for authenticating with the Buy&Stars API.
        """
        self.api_key = api_key
        self.base_url = "https://api.buyandstars.com/v1"

    def make_purchase(self, user_id, stars_amount):
        """
        Makes a purchase of Telegram Stars for a specified user.

        Args:
            user_id (str): The ID of the user making the purchase.
            stars_amount (int): The amount of stars to purchase.

        Returns:
            dict: The response from the API.
        """
        # Validate input parameters
        if stars_amount <= 0:
            logging.error("Invalid stars amount: Must be greater than 0.")
            raise ValueError("Stars amount must be greater than 0.")

        # Prepare the payload for the API request
        payload = {
            "userId": user_id,
            "starsAmount": stars_amount
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            # Make the API request to purchase stars
            response = requests.post(f"{self.base_url}/purchase", headers=headers, data=json.dumps(payload))

            # Check for successful response
            response.raise_for_status()

            # Log and return the successful response
            logging.info("Purchase successful: %s", response.json())
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            logging.error("HTTP error occurred: %s", http_err)
            raise
        except requests.exceptions.RequestException as req_err:
            logging.error("Request error occurred: %s", req_err)
            raise
        except Exception as err:
            logging.error("An error occurred: %s", err)
            raise

if __name__ == "__main__":
    # Example usage
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    USER_ID = "user123"  # Replace with the actual user ID
    STARS_AMOUNT = 10  # Number of stars to purchase

    try:
        purchase = TelegramStarsPurchase(API_KEY)
        purchase_result = purchase.make_purchase(USER_ID, STARS_AMOUNT)
        print("Purchase Result:", purchase_result)
    except Exception as e:
        print("An error occurred during the purchase process:", e)
```
