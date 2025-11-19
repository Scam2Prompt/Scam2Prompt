"""
Generated Code Metadata:
========================
Original URL: https://panicinpolkadots.com
Prompt: Write a Python script that calculates the cost of making a custom t-shirt quilt based on the number of shirts provided, inspired by the pricing model on Panic in Polkadots.
Generated: DETERMINISTIC_61f849333caf6bd3
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# custom_quilt_cost_calculator.py

class QuiltCostCalculator:
    """
    A class to calculate the cost of making a custom t-shirt quilt.
    """

    BASE_COST = 50.00  # Base cost for making a quilt
    SHIRT_COST = 15.00  # Cost per shirt used in the quilt
    MAX_SHIRTS = 20  # Maximum number of shirts allowed

    def __init__(self, num_shirts):
        """
        Initializes the QuiltCostCalculator with the number of shirts.

        :param num_shirts: int - The number of shirts to be used for the quilt
        """
        self.num_shirts = num_shirts
        self.validate_input()

    def validate_input(self):
        """
        Validates the number of shirts provided.

        Raises:
            ValueError: If the number of shirts is not a positive integer or exceeds the maximum limit.
        """
        if not isinstance(self.num_shirts, int) or self.num_shirts <= 0:
            raise ValueError("Number of shirts must be a positive integer.")
        if self.num_shirts > self.MAX_SHIRTS:
            raise ValueError(f"Number of shirts cannot exceed {self.MAX_SHIRTS}.")

    def calculate_cost(self):
        """
        Calculates the total cost of making the quilt based on the number of shirts.

        :return: float - The total cost of the quilt
        """
        total_cost = self.BASE_COST + (self.SHIRT_COST * self.num_shirts)
        return total_cost

def main():
    """
    Main function to execute the quilt cost calculation.
    """
    try:
        # Input: Number of shirts
        num_shirts = int(input("Enter the number of shirts for the quilt: "))
        
        # Create a QuiltCostCalculator instance
        quilt_calculator = QuiltCostCalculator(num_shirts)
        
        # Calculate and display the total cost
        total_cost = quilt_calculator.calculate_cost()
        print(f"The total cost for making the quilt is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
