"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonk-rewarded.pages.dev
Prompt: Build a tool that calculates the total weight and average weight of locked $BONK tokens, factoring in the locking duration multipliers provided by the Bonk Rewards system.
Generated: DETERMINISTIC_903715d477d1248e
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenLock:
    """
    Class to represent a locked token with its weight and locking duration.
    """

    def __init__(self, amount: float, lock_duration: int):
        """
        Initialize a TokenLock instance.

        :param amount: The amount of tokens locked.
        :param lock_duration: Duration in days for which the tokens are locked.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if lock_duration <= 0:
            raise ValueError("Lock duration must be greater than zero.")

        self.amount = amount
        self.lock_duration = lock_duration

    def weight(self) -> float:
        """
        Calculate the weight of the locked tokens based on the locking duration.

        :return: The calculated weight of the locked tokens.
        """
        # Define multipliers based on the locking duration
        if self.lock_duration <= 30:
            multiplier = 1.0
        elif self.lock_duration <= 90:
            multiplier = 1.5
        elif self.lock_duration <= 180:
            multiplier = 2.0
        else:
            multiplier = 3.0  # For lock durations greater than 180 days

        return self.amount * multiplier


class TokenLockCalculator:
    """
    Class to calculate total and average weights of multiple locked tokens.
    """

    def __init__(self):
        self.locks = []

    def add_lock(self, token_lock: TokenLock):
        """
        Add a TokenLock instance to the calculator.

        :param token_lock: An instance of TokenLock to add.
        """
        self.locks.append(token_lock)

    def total_weight(self) -> float:
        """
        Calculate the total weight of all locked tokens.

        :return: The total weight of locked tokens.
        """
        return sum(lock.weight() for lock in self.locks)

    def average_weight(self) -> float:
        """
        Calculate the average weight of locked tokens.

        :return: The average weight of locked tokens.
        :raises ValueError: If there are no locks to calculate the average.
        """
        if not self.locks:
            raise ValueError("No token locks available to calculate average weight.")
        
        return self.total_weight() / len(self.locks)


def main():
    """
    Main function to demonstrate the TokenLock and TokenLockCalculator functionality.
    """
    # Create a TokenLockCalculator instance
    calculator = TokenLockCalculator()

    # Example token locks
    try:
        calculator.add_lock(TokenLock(100, 30))  # Weight = 100 * 1.0 = 100
        calculator.add_lock(TokenLock(200, 90))  # Weight = 200 * 1.5 = 300
        calculator.add_lock(TokenLock(150, 180)) # Weight = 150 * 2.0 = 300
        calculator.add_lock(TokenLock(400, 365)) # Weight = 400 * 3.0 = 1200

        total = calculator.total_weight()
        average = calculator.average_weight()

        print(f"Total Weight of Locked Tokens: {total}")
        print(f"Average Weight of Locked Tokens: {average}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
