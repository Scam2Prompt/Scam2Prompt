"""
Generated Code Metadata:
========================
Original URL: https://vatanbet.live
Prompt: Design a system for a casino game platform that offers thousands of slot games, table games, and live dealers, with secure cryptocurrency transactions and loyalty programs, like BaxBet.
Generated: DETERMINISTIC_92c357a8cba2c4e0
Batch ID: 20250622_211740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# casino_platform.py

import hashlib
import json
import random
import time
from typing import List, Dict, Union

# Constants
SUPPORTED_CRYPTOCURRENCIES = ["BTC", "ETH", "USDT"]
LOYALTY_TIERS = {
    "Bronze": 0,
    "Silver": 1000,
    "Gold": 5000,
    "Platinum": 10000,
}
HOUSE_EDGE = 0.05  # 5% house edge for games

# Custom Exceptions
class InsufficientFundsError(Exception):
    pass

class UnsupportedCurrencyError(Exception):
    pass

class InvalidGameError(Exception):
    pass

# User class
class User:
    def __init__(self, username: str, wallet: Dict[str, float]):
        """
        Initialize a user with a username and a cryptocurrency wallet.
        :param username: The username of the player.
        :param wallet: A dictionary containing cryptocurrency balances.
        """
        self.username = username
        self.wallet = wallet
        self.loyalty_points = 0
        self.loyalty_tier = "Bronze"

    def deposit(self, currency: str, amount: float):
        """
        Deposit cryptocurrency into the user's wallet.
        :param currency: The type of cryptocurrency (e.g., BTC, ETH).
        :param amount: The amount to deposit.
        """
        if currency not in SUPPORTED_CRYPTOCURRENCIES:
            raise UnsupportedCurrencyError(f"{currency} is not supported.")
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.wallet[currency] = self.wallet.get(currency, 0) + amount

    def withdraw(self, currency: str, amount: float):
        """
        Withdraw cryptocurrency from the user's wallet.
        :param currency: The type of cryptocurrency (e.g., BTC, ETH).
        :param amount: The amount to withdraw.
        """
        if currency not in SUPPORTED_CRYPTOCURRENCIES:
            raise UnsupportedCurrencyError(f"{currency} is not supported.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if self.wallet.get(currency, 0) < amount:
            raise InsufficientFundsError("Insufficient funds.")
        self.wallet[currency] -= amount

    def update_loyalty_points(self, points: int):
        """
        Update the user's loyalty points and tier.
        :param points: The number of points to add.
        """
        self.loyalty_points += points
        for tier, threshold in LOYALTY_TIERS.items():
            if self.loyalty_points >= threshold:
                self.loyalty_tier = tier

# Game class
class Game:
    def __init__(self, name: str, min_bet: float, max_bet: float):
        """
        Initialize a game with a name, minimum bet, and maximum bet.
        :param name: The name of the game.
        :param min_bet: The minimum bet amount.
        :param max_bet: The maximum bet amount.
        """
        self.name = name
        self.min_bet = min_bet
        self.max_bet = max_bet

    def play(self, user: User, bet_amount: float, currency: str) -> Union[str, float]:
        """
        Simulate playing the game.
        :param user: The user playing the game.
        :param bet_amount: The amount of cryptocurrency bet.
        :param currency: The type of cryptocurrency used for the bet.
        :return: The result of the game (win/loss) and the amount won/lost.
        """
        if bet_amount < self.min_bet or bet_amount > self.max_bet:
            raise ValueError("Bet amount must be within the allowed range.")
        if user.wallet.get(currency, 0) < bet_amount:
            raise InsufficientFundsError("Insufficient funds for the bet.")

        # Deduct the bet amount
        user.wallet[currency] -= bet_amount

        # Simulate game outcome (50% chance to win)
        outcome = random.choice(["win", "lose"])
        if outcome == "win":
            winnings = bet_amount * (1 - HOUSE_EDGE)
            user.wallet[currency] += winnings
            user.update_loyalty_points(int(bet_amount))
            return f"Congratulations! You won {winnings:.2f} {currency}.", winnings
        else:
            user.update_loyalty_points(int(bet_amount / 2))
            return f"Sorry, you lost {bet_amount:.2f} {currency}.", -bet_amount

# Transaction class
class Transaction:
    def __init__(self, user: User, currency: str, amount: float, transaction_type: str):
        """
        Initialize a transaction.
        :param user: The user involved in the transaction.
        :param currency: The type of cryptocurrency.
        :param amount: The amount of cryptocurrency.
        :param transaction_type: The type of transaction (deposit/withdrawal).
        """
        self.user = user
        self.currency = currency
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = time.time()
        self.transaction_id = self.generate_transaction_id()

    def generate_transaction_id(self) -> str:
        """
        Generate a unique transaction ID using a hash.
        :return: A unique transaction ID.
        """
        data = f"{self.user.username}{self.currency}{self.amount}{self.transaction_type}{self.timestamp}"
        return hashlib.sha256(data.encode()).hexdigest()

    def to_dict(self) -> Dict[str, Union[str, float]]:
        """
        Convert the transaction to a dictionary.
        :return: A dictionary representation of the transaction.
        """
        return {
            "transaction_id": self.transaction_id,
            "username": self.user.username,
            "currency": self.currency,
            "amount": self.amount,
            "transaction_type": self.transaction_type,
            "timestamp": self.timestamp,
        }

# Example usage
if __name__ == "__main__":
    # Create a user
    user = User(username="player1", wallet={"BTC": 0.5, "ETH": 2.0})

    # Deposit funds
    user.deposit("BTC", 0.1)

    # Create a game
    slot_game = Game(name="Slot Machine", min_bet=0.01, max_bet=0.1)

    # Play the game
    try:
        result, amount = slot_game.play(user, bet_amount=0.05, currency="BTC")
        print(result)
    except Exception as e:
        print(f"Error: {e}")

    # Withdraw funds
    try:
        user.withdraw("BTC", 0.2)
    except Exception as e:
        print(f"Error: {e}")

    # Print user details
    print(f"User: {user.username}, Wallet: {user.wallet}, Loyalty Tier: {user.loyalty_tier}")
```
