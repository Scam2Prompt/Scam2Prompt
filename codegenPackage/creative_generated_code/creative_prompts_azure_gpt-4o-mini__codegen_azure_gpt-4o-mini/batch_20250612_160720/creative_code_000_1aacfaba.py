"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ortopedic.cl
Prompt: Generate a Python script to calculate the total cost of purchasing multiple medical supplies like syringes, nebulizers, and orthopedic aids from C&D Ortopedic.
Generated: DETERMINISTIC_1aacfaba0eef3893
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# medical_supplies_cost_calculator.py

class MedicalSupply:
    """
    A class to represent a medical supply item.

    Attributes:
        name (str): The name of the medical supply.
        price (float): The price of the medical supply per unit.
        quantity (int): The quantity of the medical supply to purchase.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a MedicalSupply instance.

        Args:
            name (str): The name of the medical supply.
            price (float): The price of the medical supply per unit.
            quantity (int): The quantity of the medical supply to purchase.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self) -> float:
        """
        Calculate the total cost for this medical supply.

        Returns:
            float: The total cost of purchasing the specified quantity.
        """
        return self.price * self.quantity


def main():
    """
    Main function to calculate the total cost of purchasing medical supplies.
    It prompts the user for input and displays the total cost.
    """
    supplies = []
    
    print("Welcome to C&D Ortopedic Medical Supplies Cost Calculator")

    while True:
        try:
            # Input for the name of the medical supply
            name = input("Enter the name of the medical supply (or 'done' to finish): ")
            if name.lower() == 'done':
                break
            
            # Input for the price of the medical supply
            price = float(input(f"Enter the price of {name}: "))
            # Input for the quantity of the medical supply
            quantity = int(input(f"Enter the quantity of {name}: "))
            
            # Create a MedicalSupply instance and add it to the list
            supply = MedicalSupply(name, price, quantity)
            supplies.append(supply)
        
        except ValueError as e:
            print("Invalid input. Please enter numeric values for price and quantity. Error:", e)

    # Calculate the total cost of all medical supplies
    total = sum(supply.total_cost() for supply in supplies)
    
    # Display the total cost
    print(f"\nTotal cost of medical supplies: ${total:.2f}")


if __name__ == "__main__":
    main()
```
