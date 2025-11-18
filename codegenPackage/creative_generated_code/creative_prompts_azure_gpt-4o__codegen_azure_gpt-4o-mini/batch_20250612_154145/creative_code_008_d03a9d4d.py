"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yomix-io.com
Prompt: Create a program that simulates the scoring system used by YoMix to verify newly purchased coins from cryptocurrency stock exchanges.
Generated: DETERMINISTIC_d03a9d4d50fbcbf9
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random
import hashlib
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Coin:
    """
    A class to represent a cryptocurrency coin.
    """

    def __init__(self, name, amount):
        """
        Initialize a new coin instance.

        :param name: The name of the cryptocurrency.
        :param amount: The amount of the cryptocurrency.
        """
        self.name = name
        self.amount = amount
        self.transaction_id = self.generate_transaction_id()

    def generate_transaction_id(self):
        """
        Generate a unique transaction ID for the coin.

        :return: A unique transaction ID string.
        """
        unique_str = f"{self.name}-{self.amount}-{random.randint(1000, 9999)}"
        return hashlib.sha256(unique_str.encode()).hexdigest()

class CoinValidator:
    """
    A class to validate newly purchased coins.
    """

    def __init__(self):
        """
        Initialize the CoinValidator instance.
        """
        self.validated_coins = []

    def validate_coin(self, coin):
        """
        Validate a coin using its properties.

        :param coin: An instance of Coin to be validated.
        :return: A boolean indicating whether the coin is valid.
        """
        # Perform basic validation
        if coin.amount <= 0:
            logging.error(f"Invalid amount for {coin.name}: {coin.amount}")
            return False

        if not coin.name:
            logging.error("Coin name is empty.")
            return False

        # Simulating a mock validation (for demonstration purposes)
        is_valid = random.choice([True, False])
        if is_valid:
            logging.info(f"Coin {coin.name} with amount {coin.amount} validated successfully.")
            self.validated_coins.append(coin)
            return True
        else:
            logging.warning(f"Coin {coin.name} with amount {coin.amount} failed validation.")
            return False

def load_coins_from_file(filename):
    """
    Load coin data from a JSON file.

    :param filename: The name of the JSON file to load.
    :return: A list of Coin objects.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            coins = [Coin(item['name'], item['amount']) for item in data['coins']]
            return coins
    except FileNotFoundError:
        logging.error(f"File {filename} not found.")
        return []
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from the file {filename}.")
        return []
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        return []

def main():
    """
    Main function to execute the coin validation process.
    """
    filename = 'coins.json'  # Example file name
    coins = load_coins_from_file(filename)

    if not coins:
        logging.info("No coins to validate.")
        return

    validator = CoinValidator()
    
    for coin in coins:
        validator.validate_coin(coin)

    logging.info("Validation process completed.")

if __name__ == "__main__":
    main()
``` 

**Note:** The above code expects a JSON file named `coins.json` to be in the format:
```json
{
    "coins": [
        {"name": "Bitcoin", "amount": 0.5},
        {"name": "Ethereum", "amount": 2.0},
        {"name": "Ripple", "amount": 1000}
    ]
}
``` 

This structure allows the code to simulate the scoring system as requested.
