"""
Generated Code Metadata:
========================
Original URL: https://www.purpledumpster.ca
Prompt: "Write a Python script to calculate the cost of renting a dumpster for a renovation project in Toronto, considering the dumpster size and type of waste."
Generated: DETERMINISTIC_9cb2c74278fa9981
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class DumpsterRental:
    def __init__(self, size: str, waste_type: str):
        """
        Initialize the DumpsterRental class with size and waste type.

        :param size: Size of the dumpster (e.g., 'small', 'medium', 'large')
        :param waste_type: Type of waste (e.g., 'construction', 'yard', 'general')
        """
        self.size = size.lower()
        self.waste_type = waste_type.lower()
        self.base_cost = self.calculate_base_cost()
        self.additional_cost = self.calculate_additional_cost()

    def calculate_base_cost(self) -> float:
        """
        Calculate the base cost based on dumpster size.

        :return: Base cost of the dumpster rental
        """
        size_cost_map = {
            'small': 200.0,
            'medium': 300.0,
            'large': 400.0
        }
        return size_cost_map.get(self.size, 0.0)

    def calculate_additional_cost(self) -> float:
        """
        Calculate additional costs based on waste type.

        :return: Additional cost based on waste type
        """
        waste_cost_map = {
            'construction': 50.0,
            'yard': 30.0,
            'general': 20.0
        }
        return waste_cost_map.get(self.waste_type, 0.0)

    def total_cost(self) -> float:
        """
        Calculate the total cost of renting the dumpster.

        :return: Total cost of the dumpster rental
        """
        return self.base_cost + self.additional_cost

def main():
    """
    Main function to execute the dumpster rental cost calculation.
    """
    try:
        # User input for dumpster size and waste type
        size = input("Enter the dumpster size (small, medium, large): ")
        waste_type = input("Enter the type of waste (construction, yard, general): ")

        # Create a DumpsterRental instance
        rental = DumpsterRental(size, waste_type)

        # Calculate and display the total cost
        total = rental.total_cost()
        if total > 0:
            print(f"The total cost of renting a {size} dumpster for {waste_type} waste is: ${total:.2f}")
        else:
            print("Invalid size or waste type entered. Please try again.")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
