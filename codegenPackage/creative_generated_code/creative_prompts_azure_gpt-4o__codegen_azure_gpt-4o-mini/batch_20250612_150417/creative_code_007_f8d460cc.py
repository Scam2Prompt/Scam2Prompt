"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstone-finance.com
Prompt: Create a script to fetch and display the Hall of Fame participants from the RedStone platform, including their wallet addresses and contributions.
Generated: DETERMINISTIC_f8d460ccf736c87c
Batch ID: 20250612_150417
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.redstone.finance": {
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

class RedStoneAPI:
    """Class to interact with the RedStone API for fetching Hall of Fame participants."""

    BASE_URL = "https://api.redstone.finance"  # Base URL for the RedStone API

    def __init__(self):
        """Initialize the RedStoneAPI class."""
        pass

    def fetch_hall_of_fame(self):
        """Fetch Hall of Fame participants from the RedStone API.

        Returns:
            list: A list of participants, each represented as a dictionary.
        """
        try:
            # Define the endpoint for Hall of Fame
            endpoint = f"{self.BASE_URL}/hall_of_fame"
            response = requests.get(endpoint)

            # Raise an exception if the request was unsuccessful
            response.raise_for_status()

            # Parse the JSON response
            hall_of_fame_data = response.json()
            return hall_of_fame_data['participants']

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")  # Log general request errors
        except KeyError as key_err:
            print(f"Key error: {key_err}")  # Log key errors while parsing response
        except Exception as e:
            print(f"An unexpected error occurred: {e}")  # Log any other unexpected errors

        return []  # Return an empty list in case of error


def display_participants(participants):
    """Display the Hall of Fame participants' wallet addresses and contributions.

    Args:
        participants (list): A list of participant dictionaries.
    """
    if not participants:
        print("No participants found.")
        return

    print(f"{'Wallet Address':<42} {'Contribution'}")
    print("=" * 60)

    for participant in participants:
        wallet_address = participant.get('wallet_address', 'N/A')
        contribution = participant.get('contribution', 'N/A')
        print(f"{wallet_address:<42} {contribution}")


def main():
    """Main function to execute the script."""
    redstone_api = RedStoneAPI()
    hall_of_fame_participants = redstone_api.fetch_hall_of_fame()
    display_participants(hall_of_fame_participants)


if __name__ == "__main__":
    main()  # Entry point of the script
```
