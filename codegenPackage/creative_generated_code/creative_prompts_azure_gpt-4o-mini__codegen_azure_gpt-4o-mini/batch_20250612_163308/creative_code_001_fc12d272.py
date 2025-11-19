"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingroofing.com
Prompt: Write a Python script that calculates the estimated cost of roofing services based on user input for roof type (tile, shingle, metal, flat) and square footage, similar to a roofing calculator.
Generated: DETERMINISTIC_fc12d2725ca3695a
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# roofing_calculator.py
"""
A simple roofing calculator that estimates the cost of roofing services
based on the type of roof and the square footage provided by the user.
"""

class RoofingCalculator:
    def __init__(self):
        # Define costs per square foot for each roof type
        self.costs = {
            'tile': 10.00,  # Cost per square foot for tile roofing
            'shingle': 5.00,  # Cost per square foot for shingle roofing
            'metal': 7.50,  # Cost per square foot for metal roofing
            'flat': 4.00  # Cost per square foot for flat roofing
        }

    def calculate_cost(self, roof_type, square_footage):
        """
        Calculate the estimated cost of roofing services.

        :param roof_type: The type of roof (tile, shingle, metal, flat)
        :param square_footage: The area of the roof in square feet
        :return: Estimated cost of roofing services
        :raises ValueError: If the roof type is invalid or square footage is not positive
        """
        # Validate input
        if roof_type not in self.costs:
            raise ValueError(f"Invalid roof type. Choose from: {', '.join(self.costs.keys())}")
        if square_footage <= 0:
            raise ValueError("Square footage must be a positive number.")

        # Calculate and return the estimated cost
        cost_per_sqft = self.costs[roof_type]
        estimated_cost = cost_per_sqft * square_footage
        return estimated_cost


def main():
    """
    Main function to run the roofing calculator.
    """
    calculator = RoofingCalculator()

    try:
        # Get user input for roof type
        roof_type = input("Enter the type of roof (tile, shingle, metal, flat): ").strip().lower()
        
        # Get user input for square footage
        square_footage = float(input("Enter the square footage of the roof: ").strip())

        # Calculate the estimated cost
        estimated_cost = calculator.calculate_cost(roof_type, square_footage)
        
        # Display the estimated cost
        print(f"The estimated cost for {roof_type} roofing of {square_footage} square feet is: ${estimated_cost:.2f}")

    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
