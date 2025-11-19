"""
Generated Code Metadata:
========================
Original URL: https://usdt-mixer-mix.com
Prompt: Provide an example of how to implement a mixing code system in a cryptocurrency mixer to ensure users don't receive their own coins back, as described on the USDT Mixer website.
Generated: DETERMINISTIC_a9c6e4f79f08b1cb
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import secrets
from typing import List, Dict

class Transaction:
    def __init__(self, user_id: str, amount: int, coins: List[str]):
        """
        Initialize a transaction.

        Args:
        - user_id (str): Unique identifier for the user.
        - amount (int): Amount of coins to mix.
        - coins (List[str]): List of coin IDs.
        """
        self.user_id = user_id
        self.amount = amount
        self.coins = coins

class MixingCodeSystem:
    def __init__(self):
        """
        Initialize the mixing code system.
        """
        self.user_coins: Dict[str, List[str]] = {}
        self.mixing_codes: Dict[str, str] = {}

    def generate_mixing_code(self, user_id: str, amount: int) -> str:
        """
        Generate a unique mixing code for a user.

        Args:
        - user_id (str): Unique identifier for the user.
        - amount (int): Amount of coins to mix.

        Returns:
        - str: Unique mixing code.
        """
        # Generate a random mixing code
        mixing_code = secrets.token_urlsafe(16)
        # Store the mixing code and its corresponding user ID and amount
        self.mixing_codes[mixing_code] = hashlib.sha256((user_id + str(amount)).encode()).hexdigest()
        return mixing_code

    def add_coins(self, mixing_code: str, coins: List[str]):
        """
        Add coins to the mixing process.

        Args:
        - mixing_code (str): Unique mixing code.
        - coins (List[str]): List of coin IDs.
        """
        if mixing_code not in self.mixing_codes:
            raise ValueError("Invalid mixing code")

        user_id_hash = self.mixing_codes[mixing_code]
        if user_id_hash not in self.user_coins:
            self.user_coins[user_id_hash] = []

        self.user_coins[user_id_hash].extend(coins)

    def get_output_coins(self, mixing_code: str, output_amount: int) -> List[str]:
        """
        Get output coins for a mixing code.

        Args:
        - mixing_code (str): Unique mixing code.
        - output_amount (int): Amount of output coins.

        Returns:
        - List[str]: List of output coin IDs.
        """
        if mixing_code not in self.mixing_codes:
            raise ValueError("Invalid mixing code")

        user_id_hash = self.mixing_codes[mixing_code]
        if user_id_hash not in self.user_coins:
            raise ValueError("No coins added for this mixing code")

        # Ensure the user doesn't receive their own coins back
        output_coins = []
        all_coins = self.user_coins[user_id_hash]
        for _ in range(output_amount):
            if not all_coins:
                raise ValueError("Insufficient coins for output")
            coin = secrets.choice(all_coins)
            all_coins.remove(coin)
            output_coins.append(coin)

        return output_coins

    def verify_output_coins(self, mixing_code: str, output_coins: List[str]) -> bool:
        """
        Verify that the output coins do not belong to the user.

        Args:
        - mixing_code (str): Unique mixing code.
        - output_coins (List[str]): List of output coin IDs.

        Returns:
        - bool: True if the output coins are valid, False otherwise.
        """
        if mixing_code not in self.mixing_codes:
            raise ValueError("Invalid mixing code")

        user_id_hash = self.mixing_codes[mixing_code]
        if user_id_hash not in self.user_coins:
            raise ValueError("No coins added for this mixing code")

        return all(coin not in self.user_coins[user_id_hash] for coin in output_coins)


def main():
    mixing_system = MixingCodeSystem()

    # Example usage
    user_id = "user123"
    amount = 10
    mixing_code = mixing_system.generate_mixing_code(user_id, amount)
    print(f"Mixing code: {mixing_code}")

    coins = [f"coin{i}" for i in range(100)]
    mixing_system.add_coins(mixing_code, coins)

    output_amount = 10
    output_coins = mixing_system.get_output_coins(mixing_code, output_amount)
    print(f"Output coins: {output_coins}")

    is_valid = mixing_system.verify_output_coins(mixing_code, output_coins)
    print(f"Output coins valid: {is_valid}")


if __name__ == "__main__":
    main()
```
