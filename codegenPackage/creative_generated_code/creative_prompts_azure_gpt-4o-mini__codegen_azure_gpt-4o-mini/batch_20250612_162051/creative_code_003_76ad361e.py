"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indpfire.com
Prompt: Write a Python script that calculates the potential property loss reduction when installing fire sprinklers, based on statistics from Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_76ad361edb0369b8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class FireSprinklerCalculator:
    """
    A class to calculate potential property loss reduction when installing fire sprinklers
    based on statistical data from Independence Fire Sprinkler Company.
    """

    def __init__(self, average_property_loss, sprinkler_coverage_reduction):
        """
        Initializes the calculator with the average property loss and the sprinkler coverage reduction rate.
        
        :param average_property_loss: Average dollar amount of property loss without sprinklers
        :param sprinkler_coverage_reduction: Reduction percentage of property loss due to sprinkler installation
        """
        self.average_property_loss = average_property_loss
        self.sprinkler_coverage_reduction = sprinkler_coverage_reduction / 100  # Convert percentage to decimal

    def calculate_loss_reduction(self):
        """
        Calculates the potential property loss reduction due to the installation of fire sprinklers.
        
        :return: The amount of potential loss reduction in dollars
        """
        if self.average_property_loss < 0 or not (0 <= self.sprinkler_coverage_reduction <= 1):
            raise ValueError("Invalid input values. Average property loss must be non-negative and "
                             "sprinkler coverage reduction must be between 0 and 100.")
        
        # Calculate potential loss reduction
        loss_reduction = self.average_property_loss * self.sprinkler_coverage_reduction
        return loss_reduction

def main():
    """
    Main function to execute the fire sprinkler loss reduction calculation.
    """

    try:
        # Example Input
        average_property_loss = float(input("Enter the average property loss (in dollars): "))
        sprinkler_coverage_reduction = float(input("Enter the sprinkler coverage reduction rate (in %): "))

        # Create an instance of the calculator
        calculator = FireSprinklerCalculator(average_property_loss, sprinkler_coverage_reduction)

        # Calculate and display the potential loss reduction
        loss_reduction = calculator.calculate_loss_reduction()
        print(f"The potential property loss reduction with fire sprinklers is: ${loss_reduction:.2f}")

    except ValueError as ve:
        print(f"Input error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
