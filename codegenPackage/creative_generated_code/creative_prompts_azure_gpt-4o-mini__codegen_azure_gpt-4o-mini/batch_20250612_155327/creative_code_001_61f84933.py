"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panicinpolkadots.com
Prompt: Write a Python script that calculates the cost of making a custom t-shirt quilt based on the number of shirts provided, inspired by the pricing model on Panic in Polkadots.
Generated: DETERMINISTIC_61f849333caf6bd3
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# custom_quilt_cost_calculator.py

class QuiltCostCalculator:
    """
    A class to calculate the cost of making a custom t-shirt quilt.
    """

    # Pricing model constants
    BASE_COST_PER_SHIRT = 20.00  # Base cost per shirt
    ADDITIONAL_COST_PER_SHIRT = 5.00  # Additional cost per shirt beyond the first five
    MAX_SHIRTS_BEFORE_EXTRA_COST = 5  # Maximum number of shirts before additional cost applies

    def __init__(self, num_shirts):
        """
        Initializes the QuiltCostCalculator with the number of shirts.
        
        Args:
            num_shirts (int): The number of shirts provided to make the quilt.
        
        Raises:
            ValueError: If the number of shirts is negative.
        """
        if num_shirts < 0:
            raise ValueError("Number of shirts cannot be negative.")
        
        self.num_shirts = num_shirts

    def calculate_cost(self):
        """
        Calculates the total cost of making the custom t-shirt quilt.
        
        Returns:
            float: The total cost of the quilt.
        """
        if self.num_shirts <= 0:
            return 0.0  # No cost for zero shirts

        # Calculate the base cost for the first five shirts
        total_cost = self.BASE_COST_PER_SHIRT * min(self.num_shirts, self.MAX_SHIRTS_BEFORE_EXTRA_COST)

        # If more than five shirts, calculate the additional cost
        if self.num_shirts > self.MAX_SHIRTS_BEFORE_EXTRA_COST:
            additional_shirts = self.num_shirts - self.MAX_SHIRTS_BEFORE_EXTRA_COST
            total_cost += self.ADDITIONAL_COST_PER_SHIRT * additional_shirts
        
        return total_cost

def main():
    """
    Main function to execute the quilt cost calculator.
    """
    try:
        # Ask the user for the number of shirts
        num_shirts = int(input("Enter the number of shirts to use for the quilt: "))
        
        # Create a QuiltCostCalculator instance
        calculator = QuiltCostCalculator(num_shirts)
        
        # Calculate and display the cost
        total_cost = calculator.calculate_cost()
        print(f"The total cost to make the custom t-shirt quilt is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
