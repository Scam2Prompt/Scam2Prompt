"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gprobolsa.com
Prompt: Write a Python program to simulate a customer order for personalized reusable bags from Grupo ProBolsa, including fields for design preferences and quantity.
Generated: DETERMINISTIC_0e248219f5d271b4
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BagOrder:
    """
    A class to represent a customer order for personalized reusable bags.
    
    Attributes:
        design (str): The design preference for the bag.
        quantity (int): The quantity of bags ordered.
    """

    def __init__(self, design: str, quantity: int):
        """
        Initializes a new BagOrder instance.

        Parameters:
            design (str): The design preference for the bag.
            quantity (int): The quantity of bags ordered.

        Raises:
            ValueError: If quantity is less than 1 or design is empty.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        if not design.strip():
            raise ValueError("Design preference cannot be empty.")

        self.design = design
        self.quantity = quantity

    def summary(self) -> str:
        """
        Returns a summary of the order.

        Returns:
            str: A summary string containing the design and quantity.
        """
        return f"Order Summary: {self.quantity} bags with '{self.design}' design."

def main():
    """
    Main function to simulate the customer order process.
    It prompts the user for design preferences and quantity,
    processes the input, and displays an order summary.
    """
    try:
        # Get user input for design preference
        design = input("Enter your bag design preference: ").strip()
        # Get user input for quantity and convert it to an integer
        quantity = int(input("Enter the quantity of bags you wish to order: ").strip())

        # Create a new BagOrder instance
        order = BagOrder(design, quantity)
        
        # Display the order summary
        print(order.summary())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
