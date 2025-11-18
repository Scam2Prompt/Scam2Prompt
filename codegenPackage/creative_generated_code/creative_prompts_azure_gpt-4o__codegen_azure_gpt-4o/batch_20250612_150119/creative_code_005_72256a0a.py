"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixtum.me
Prompt: Develop a Python script that simulates the pre-mixer process, where coins are mixed with other traders’ money at cryptocurrency exchanges, as outlined on mixtum.me.
Generated: DETERMINISTIC_72256a0a62fbf8c6
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
import time


class PreMixer:
    """
    PreMixer Class
    Simulates the process of mixing coins with other traders' money at cryptocurrency exchanges.
    """

    def __init__(self, user_coins: float):
        """
        Initializes the PreMixer instance.

        :param user_coins: The amount of cryptocurrency provided by the user for mixing.
        """
        if user_coins <= 0:
            raise ValueError("User coins must be greater than 0.")
        self.user_coins = user_coins
        self.exchanges = ["Binance", "Coinbase", "Kraken", "Bitfinex"]
        self.transaction_history = []

    def _simulate_exchange_transaction(self, exchange: str, coins: float) -> dict:
        """
        Simulates a single transaction at a given exchange.

        :param exchange: The name of the cryptocurrency exchange.
        :param coins: The amount of coins to be mixed in the transaction.
        :return: A dictionary representing the transaction details.
        """
        transaction_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        return {
            "transaction_id": transaction_id,
            "exchange": exchange,
            "coins": round(coins, 8),
            "timestamp": timestamp
        }

    def mix_coins(self):
        """
        Simulates the mixing process with random transactions across cryptocurrency exchanges.

        :return: A list representing the transaction history after mixing.
        """
        remaining_coins = self.user_coins

        while remaining_coins > 0:
            # Randomly choose an exchange
            exchange = random.choice(self.exchanges)

            # Randomly decide the amount of coins for this transaction
            transaction_coins = round(random.uniform(0.01, min(0.2, remaining_coins)), 8)

            # Simulate the transaction
            transaction = self._simulate_exchange_transaction(exchange, transaction_coins)
            self.transaction_history.append(transaction)

            # Deduct the mixed coins
            remaining_coins -= transaction_coins

            # Simulate network delay
            time.sleep(random.uniform(0.1, 0.5))

        return self.transaction_history


def main():
    """
    Main function to execute the PreMixer process.
    """
    try:
        # User input for the amount of cryptocurrency
        user_input = float(input("Enter the amount of cryptocurrency to mix: "))
        premixer = PreMixer(user_input)

        print("\nStarting coin mixing process...")
        transactions = premixer.mix_coins()

        print("\nMixing Complete. Transaction History:")
        for transaction in transactions:
            print(transaction)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
