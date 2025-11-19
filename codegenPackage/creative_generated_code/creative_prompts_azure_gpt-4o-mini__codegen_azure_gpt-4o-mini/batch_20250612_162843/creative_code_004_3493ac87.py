"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonfarm.top
Prompt: Create a function that checks the availability of different TON FARM Chips based on their limited supply.
Generated: DETERMINISTIC_3493ac8721bc6099
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TonFarmChip:
    """
    Represents a TON FARM Chip with a name and its available supply.
    """
    def __init__(self, name: str, supply: int):
        """
        Initializes the TON FARM Chip with a name and supply.

        :param name: The name of the chip.
        :param supply: The total available supply of the chip.
        """
        self.name = name
        self.supply = supply

    def check_availability(self, requested_quantity: int) -> bool:
        """
        Checks if the requested quantity of the chip is available.

        :param requested_quantity: The quantity of chips requested.
        :return: True if available, False otherwise.
        """
        if requested_quantity < 0:
            raise ValueError("Requested quantity cannot be negative.")
        return requested_quantity <= self.supply

    def reserve_chips(self, quantity: int) -> bool:
        """
        Reserves a specified quantity of chips if available.

        :param quantity: The quantity of chips to reserve.
        :return: True if reservation successful, False otherwise.
        """
        if self.check_availability(quantity):
            self.supply -= quantity
            return True
        return False

def main():
    """
    Main function to demonstrate the chip availability checking.
    """
    try:
        # Create instances of TON FARM Chips
        chips = [
            TonFarmChip("Chip A", 10),
            TonFarmChip("Chip B", 5),
            TonFarmChip("Chip C", 0)  # Out of stock
        ]

        # Check availability and reserve chips
        for chip in chips:
            requested_quantity = 3  # Example request
            if chip.check_availability(requested_quantity):
                print(f"Reserving {requested_quantity} of {chip.name}.")
                chip.reserve_chips(requested_quantity)
            else:
                print(f"Not enough supply for {chip.name}. Requested: {requested_quantity}, Available: {chip.supply}")

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
```
