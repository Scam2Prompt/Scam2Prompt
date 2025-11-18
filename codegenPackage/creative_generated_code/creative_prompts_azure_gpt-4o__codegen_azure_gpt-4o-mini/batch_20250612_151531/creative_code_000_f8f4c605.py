"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.apos.cl
Prompt: Write code to calculate the cost of purchasing thermal paper rolls in bulk, using pricing and customization options similar to those offered by Apos Chile.
Generated: DETERMINISTIC_f8f4c60517d16dea
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ThermalPaperRoll:
    """
    A class to represent a thermal paper roll purchase.

    Attributes:
        base_price (float): The base price of a single thermal paper roll.
        quantity (int): The number of rolls purchased.
        customization_fee (float): Additional fee for customization options.
    """

    def __init__(self, base_price: float, quantity: int, customization_fee: float = 0.0):
        """
        Initializes the ThermalPaperRoll with base price, quantity, and customization fee.

        Args:
            base_price (float): Base price of a single roll.
            quantity (int): Number of rolls to purchase.
            customization_fee (float): Additional fee for customization. Default is 0.0.

        Raises:
            ValueError: If base_price or quantity is negative.
        """
        if base_price < 0:
            raise ValueError("Base price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        self.base_price = base_price
        self.quantity = quantity
        self.customization_fee = customization_fee

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the thermal paper rolls including customization.

        Returns:
            float: Total cost of the purchase.
        """
        total_cost = (self.base_price * self.quantity) + self.customization_fee
        return total_cost


def main():
    """
    Main function to execute the thermal paper roll cost calculation.
    """
    try:
        # Example inputs for base price, quantity, and customization fee
        base_price = float(input("Enter the base price of a single thermal paper roll: "))
        quantity = int(input("Enter the quantity of rolls to purchase: "))
        customization_fee = float(input("Enter the customization fee (if any, else enter 0): "))

        # Create a ThermalPaperRoll object
        paper_roll = ThermalPaperRoll(base_price, quantity, customization_fee)

        # Calculate and display the total cost
        total_cost = paper_roll.calculate_total_cost()
        print(f"The total cost for purchasing {quantity} rolls is: ${total_cost:.2f}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
