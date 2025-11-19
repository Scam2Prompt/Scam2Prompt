"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-etuktuk-io.pages.dev
Prompt: Create a script that upgrades the eTukTuk vehicle using $TUK tokens, based on the mechanics described in the eTukTuk game.
Generated: DETERMINISTIC_02dad88029c3df70
Batch ID: 20250612_163541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class InsufficientFundsError(Exception):
    """Custom exception raised when user has insufficient $TUK tokens for an upgrade."""
    pass

class UpgradeError(Exception):
    """Custom exception raised when an upgrade operation fails."""
    pass

class ETukTuk:
    """
    Represents an eTukTuk vehicle in the game.
    """
    def __init__(self, name: str, base_level: int = 1, current_tuk_balance: int = 0):
        """
        Initialize an eTukTuk with its name, starting level, and token balance.
        
        Args:
            name (str): The name of the vehicle.
            base_level (int): The starting level of the vehicle. Default is 1.
            current_tuk_balance (int): The starting $TUK token balance. Default is 0.
        """
        self.name = name
        self.level = base_level
        self.tuk_balance = current_tuk_balance

    def upgrade_cost(self) -> int:
        """
        Calculate the cost of the next upgrade based on the vehicle's current level.

        Returns:
            int: The $TUK token cost of the next upgrade.
        """
        return 100 * self.level  # Upgrade cost increases with level (e.g., level 1 -> 100, level 2 -> 200)

    def add_tokens(self, amount: int):
        """
        Add $TUK tokens to the vehicle's balance.

        Args:
            amount (int): The amount of $TUK tokens to add.
        """
        if amount < 0:
            raise ValueError("Cannot add a negative amount of tokens.")
        self.tuk_balance += amount

    def upgrade(self):
        """
        Attempt to upgrade the vehicle to the next level.

        Raises:
            InsufficientFundsError: If the user does not have enough $TUK tokens.
            UpgradeError: If the upgrade fails for any reason.
        """
        cost = self.upgrade_cost()
        if self.tuk_balance < cost:
            raise InsufficientFundsError(
                f"Insufficient funds. {cost} $TUK tokens required, but only {self.tuk_balance} available."
            )

        # Deduct the cost and increase the level.
        self.tuk_balance -= cost
        self.level += 1
        print(f"Upgrade successful! {self.name} is now at level {self.level}.")

    def __str__(self):
        """
        String representation of the eTukTuk vehicle.

        Returns:
            str: A string showing the vehicle's name, level, and token balance.
        """
        return f"eTukTuk '{self.name}': Level {self.level}, $TUK Balance: {self.tuk_balance}"


# Example usage
if __name__ == "__main__":
    try:
        # Create an eTukTuk vehicle instance
        my_vehicle = ETukTuk(name="Speedster", base_level=1, current_tuk_balance=300)

        print(my_vehicle)  # Display initial vehicle state
        
        # Attempt to upgrade the vehicle
        my_vehicle.upgrade()  # Perform the first upgrade
        print(my_vehicle)  # Display the updated state after first upgrade

        my_vehicle.upgrade()  # Attempt a second upgrade
        print(my_vehicle)  # Display the updated state after second upgrade

        my_vehicle.upgrade()  # Attempt a third upgrade (may fail if insufficient funds)
        print(my_vehicle)

    except InsufficientFundsError as e:
        print(f"Upgrade failed: {e}", file=sys.stderr)

    except UpgradeError as e:
        print(f"An unexpected error occurred during upgrade: {e}", file=sys.stderr)

    except Exception as e:
        print(f"An unexpected exception occurred: {e}", file=sys.stderr)
```
