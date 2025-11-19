"""
Generated Code Metadata:
========================
Original URL: https://register-monprotocol.pages.dev
Prompt: How does the MON Protocol community presale work, and what are the guaranteed allocations for different types of Pixelmon lots?
Generated: DETERMINISTIC_6808b00efcfb9401
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# MON Protocol Community Presale and Pixelmon Lot Allocations

class PixelmonLot:
    def __init__(self, name, guaranteed_allocation):
        """
        Represents a Pixelmon lot with a name and guaranteed allocation.

        Args:
            name (str): The name of the Pixelmon lot.
            guaranteed_allocation (float): The guaranteed allocation for the lot.
        """
        self.name = name
        self.guaranteed_allocation = guaranteed_allocation

class MONProtocolPresale:
    def __init__(self):
        """
        Represents the MON Protocol community presale.

        Attributes:
            lots (dict): A dictionary of Pixelmon lots with their guaranteed allocations.
        """
        self.lots = {
            "Genesis": PixelmonLot("Genesis", 0.15),
            "Rare": PixelmonLot("Rare", 0.25),
            "Uncommon": PixelmonLot("Uncommon", 0.30),
            "Common": PixelmonLot("Common", 0.30)
        }

    def get_lot_allocation(self, lot_name):
        """
        Retrieves the guaranteed allocation for a specific Pixelmon lot.

        Args:
            lot_name (str): The name of the Pixelmon lot.

        Returns:
            float: The guaranteed allocation for the lot.

        Raises:
            ValueError: If the lot name is not found.
        """
        lot = self.lots.get(lot_name)
        if lot is None:
            raise ValueError(f"Lot '{lot_name}' not found.")
        return lot.guaranteed_allocation

    def get_all_lot_allocations(self):
        """
        Retrieves the guaranteed allocations for all Pixelmon lots.

        Returns:
            dict: A dictionary of Pixelmon lots with their guaranteed allocations.
        """
        return {lot.name: lot.guaranteed_allocation for lot in self.lots.values()}

def main():
    try:
        presale = MONProtocolPresale()
        print("MON Protocol Community Presale and Pixelmon Lot Allocations")
        print("---------------------------------------------------------")
        print("All Lot Allocations:")
        for lot, allocation in presale.get_all_lot_allocations().items():
            print(f"{lot}: {allocation * 100}%")
        
        lot_name = "Genesis"
        print(f"\nGuaranteed Allocation for {lot_name} Lot: {presale.get_lot_allocation(lot_name) * 100}%")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
