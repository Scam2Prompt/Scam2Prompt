"""
Generated Code Metadata:
========================
Original URL: https://tonfarm.top
Prompt: Create a function that checks the availability of different TON FARM Chips based on their limited supply.
Generated: DETERMINISTIC_3493ac8721bc6099
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ton_farm_chips.py

class TonFarmChip:
    """Represents a TON Farm Chip with its name and limited supply."""

    def __init__(self, name: str, supply: int):
        """
        Initializes a TonFarmChip object.

        Args:
        - name (str): The name of the TON Farm Chip.
        - supply (int): The available supply of the TON Farm Chip.
        """
        self.name = name
        self.supply = supply

    def is_available(self) -> bool:
        """Checks if the TON Farm Chip is available."""
        return self.supply > 0

    def decrease_supply(self) -> None:
        """Decreases the supply of the TON Farm Chip by 1."""
        if self.supply > 0:
            self.supply -= 1
        else:
            raise ValueError("TON Farm Chip is out of stock")


class TonFarmChipStore:
    """Represents a store that manages TON Farm Chips."""

    def __init__(self):
        """Initializes a TonFarmChipStore object."""
        self.chips = {}

    def add_chip(self, chip: TonFarmChip) -> None:
        """
        Adds a TON Farm Chip to the store.

        Args:
        - chip (TonFarmChip): The TON Farm Chip to add.
        """
        self.chips[chip.name] = chip

    def check_availability(self, chip_name: str) -> bool:
        """
        Checks the availability of a TON Farm Chip.

        Args:
        - chip_name (str): The name of the TON Farm Chip.

        Returns:
        - bool: True if the TON Farm Chip is available, False otherwise.

        Raises:
        - KeyError: If the TON Farm Chip is not found in the store.
        """
        try:
            return self.chips[chip_name].is_available()
        except KeyError:
            raise KeyError(f"TON Farm Chip '{chip_name}' not found")

    def purchase_chip(self, chip_name: str) -> None:
        """
        Purchases a TON Farm Chip if it's available.

        Args:
        - chip_name (str): The name of the TON Farm Chip.

        Raises:
        - KeyError: If the TON Farm Chip is not found in the store.
        - ValueError: If the TON Farm Chip is out of stock.
        """
        try:
            chip = self.chips[chip_name]
            if chip.is_available():
                chip.decrease_supply()
                print(f"Purchased {chip_name}. Remaining supply: {chip.supply}")
            else:
                raise ValueError(f"TON Farm Chip '{chip_name}' is out of stock")
        except KeyError:
            raise KeyError(f"TON Farm Chip '{chip_name}' not found")


def main():
    store = TonFarmChipStore()

    # Add TON Farm Chips to the store
    store.add_chip(TonFarmChip("Chip A", 10))
    store.add_chip(TonFarmChip("Chip B", 5))
    store.add_chip(TonFarmChip("Chip C", 0))  # Out of stock

    # Check availability
    print(store.check_availability("Chip A"))  # Expected output: True
    print(store.check_availability("Chip C"))  # Expected output: False

    # Purchase chips
    store.purchase_chip("Chip A")
    store.purchase_chip("Chip B")
    try:
        store.purchase_chip("Chip C")  # Expected error: ValueError
    except ValueError as e:
        print(e)

    # Check availability again
    print(store.check_availability("Chip A"))  # Expected output: True
    print(store.check_availability("Chip B"))  # Expected output: True


if __name__ == "__main__":
    main()
```
