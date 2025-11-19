"""
Generated Code Metadata:
========================
Original URL: https://don.co.ke
Prompt: Develop Python code to integrate with The Don's Digit Under-3 Bot, targeting digits below 3 for low-risk trading on Deriv.
Generated: DETERMINISTIC_2afd349d93385e7f
Batch ID: 20250612_154908
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.deriv.com/v1": {
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
import logging
import time
import random
from typing import Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DonDigitUnder3Bot:
    def __init__(self, api_url: str, api_key: str, account_id: int):
        """
        Initialize the Don's Digit Under-3 Bot.

        Args:
        - api_url (str): The URL of the Deriv API.
        - api_key (str): The API key for authentication.
        - account_id (int): The account ID for trading.
        """
        self.api_url = api_url
        self.api_key = api_key
        self.account_id = account_id
        self.session = None

    def _create_session(self):
        """
        Create a session with the Deriv API.
        """
        try:
            import requests
            self.session = requests.Session()
            self.session.headers.update({'Authorization': f'Bearer {self.api_key}'})
        except Exception as e:
            logging.error(f"Failed to create session: {str(e)}")

    def _get_contract(self, symbol: str, duration: int, amount: float) -> Dict:
        """
        Get a contract for the specified symbol, duration, and amount.

        Args:
        - symbol (str): The symbol of the contract (e.g., R_1).
        - duration (int): The duration of the contract in seconds.
        - amount (float): The amount to trade.

        Returns:
        - A dictionary representing the contract.
        """
        try:
            response = self.session.post(
                f"{self.api_url}/contracts",
                json={
                    "amount": amount,
                    "contract_type": "DIGIT",
                    "currency": "USD",
                    "duration": duration,
                    "duration_unit": "s",
                    "symbol": symbol,
                    "type": "CALL"
                }
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logging.error(f"Failed to get contract: {str(e)}")
            return {}

    def _buy_contract(self, contract_id: int, amount: float) -> Dict:
        """
        Buy a contract.

        Args:
        - contract_id (int): The ID of the contract.
        - amount (float): The amount to trade.

        Returns:
        - A dictionary representing the bought contract.
        """
        try:
            response = self.session.post(
                f"{self.api_url}/buy",
                json={
                    "amount": amount,
                    "contract_id": contract_id,
                    "account_id": self.account_id
                }
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logging.error(f"Failed to buy contract: {str(e)}")
            return {}

    def _check_digit(self, contract_id: int) -> bool:
        """
        Check if the digit is under 3.

        Args:
        - contract_id (int): The ID of the contract.

        Returns:
        - True if the digit is under 3, False otherwise.
        """
        try:
            response = self.session.get(f"{self.api_url}/contract/{contract_id}")
            response.raise_for_status()
            contract = response.json()
            digit = contract.get('contract_info', {}).get('digit')
            return digit < 3
        except Exception as e:
            logging.error(f"Failed to check digit: {str(e)}")
            return False

    def run(self, symbol: str, duration: int, amount: float):
        """
        Run the bot.

        Args:
        - symbol (str): The symbol of the contract (e.g., R_1).
        - duration (int): The duration of the contract in seconds.
        - amount (float): The amount to trade.
        """
        if not self.session:
            self._create_session()

        contract = self._get_contract(symbol, duration, amount)
        if not contract:
            return

        bought_contract = self._buy_contract(contract['contract_id'], amount)
        if not bought_contract:
            return

        time.sleep(duration)

        if self._check_digit(bought_contract['contract_id']):
            logging.info("Digit is under 3. Trade successful.")
        else:
            logging.info("Digit is 3 or above. Trade not successful.")

if __name__ == "__main__":
    api_url = "https://api.deriv.com/v1"
    api_key = "YOUR_API_KEY"
    account_id = 123456789

    bot = DonDigitUnder3Bot(api_url, api_key, account_id)
    bot.run("R_1", 60, 10.0)
```
