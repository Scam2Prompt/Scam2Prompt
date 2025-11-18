"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappass.neocities.org
Prompt: Create a script to display the total supply and remaining quantity of a digital collectible (e.g., 35/88), similar to the supply tracking feature on the Dapp Pass webpage.
Generated: DETERMINISTIC_bede9314df797204
Batch ID: 20250612_153659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class DigitalCollectible:
    """
    A class to represent a digital collectible with total supply and remaining quantity.
    """

    def __init__(self, total_supply: int):
        """
        Initialize a DigitalCollectible instance.

        Args:
            total_supply (int): The total supply of the collectible.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        self.total_supply = total_supply
        self.remaining_quantity = total_supply

    def mint(self, quantity: int):
        """
        Mint a specified quantity of the collectible.

        Args:
            quantity (int): Number of collectibles to mint.

        Raises:
            ValueError: If quantity is less than or equal to zero.
            ValueError: If quantity exceeds the remaining collectible count.
        """
        if quantity <= 0:
            raise ValueError("Quantity to mint must be a positive integer.")
        if quantity > self.remaining_quantity:
            raise ValueError("Insufficient collectibles remaining to mint.")
        self.remaining_quantity -= quantity

    def display_supply_status(self):
        """
        Display the supply status of the collectible.

        Returns:
            str: A string showing the remaining and total supply in "remaining/total" format.
        """
        return f"{self.remaining_quantity}/{self.total_supply}"


def main():
    """
    Main function to demonstrate the usage of DigitalCollectible class.
    """
    try:
        # Initialize a digital collectible with a total supply of 88
        collectible = DigitalCollectible(total_supply=88)

        # Mint some collectibles
        collectible.mint(10)  # Mint 10 collectibles
        collectible.mint(5)   # Mint another 5 collectibles

        # Display current supply status
        print("Supply Status:", collectible.display_supply_status())
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
