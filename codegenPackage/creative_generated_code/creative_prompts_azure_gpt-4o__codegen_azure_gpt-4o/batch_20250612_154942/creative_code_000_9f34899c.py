"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theaflac.com
Prompt: Write Python code to calculate premiums for Aflac's accident insurance using the A36000 series policy details provided on the webpage. Include optional riders and waiting periods in the calculation.
Generated: DETERMINISTIC_9f34899c901cf965
Batch ID: 20250612_154942
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate premiums for Aflac's accident insurance (A36000 series policy)

# Import necessary modules
import sys

class AflacAccidentInsuranceCalculator:
    """
    Aflac Accident Insurance Calculator for A36000 series policy.
    Includes optional riders and waiting periods in the premium calculation.
    """

    def __init__(self):
        """
        Initialize the calculator with default values or configuration.
        """
        self.base_premium = 50.0  # Base premium for A36000 policy (example value)
        self.rider_costs = {
            'family_care': 10.0,     # Example cost for Family Care Rider
            'hospital_indemnity': 15.0,  # Example cost for Hospital Indemnity Rider
        }
        self.waiting_period_discount = 0.10  # 10% discount for waiting periods applied

    def calculate_premium(self, selected_riders, include_waiting_period):
        """
        Calculate the total premium based on selected riders and waiting period options.

        Parameters:
        selected_riders (list): List of rider names to include in the premium calculation.
        include_waiting_period (bool): Whether the waiting period discount is applied.

        Returns:
        float: The total calculated premium.
        """
        try:
            # Validate input
            if not isinstance(selected_riders, list):
                raise ValueError("selected_riders must be a list of rider names.")
            if not isinstance(include_waiting_period, bool):
                raise ValueError("include_waiting_period must be a boolean.")

            # Start with the base premium
            total_premium = self.base_premium

            # Add costs for selected riders
            for rider in selected_riders:
                if rider in self.rider_costs:
                    total_premium += self.rider_costs[rider]
                else:
                    raise ValueError(f"Unknown rider: {rider}")

            # Apply waiting period discount if applicable
            if include_waiting_period:
                total_premium *= (1 - self.waiting_period_discount)

            return round(total_premium, 2)

        except Exception as e:
            # Handle any errors and provide feedback
            print(f"Error calculating premium: {e}", file=sys.stderr)
            return None

# Example usage of the calculator
if __name__ == "__main__":
    # Initialize the calculator
    calculator = AflacAccidentInsuranceCalculator()

    # Example input: selected riders and waiting period option
    selected_riders = ['family_care', 'hospital_indemnity']
    include_waiting_period = True

    # Calculate premium
    premium = calculator.calculate_premium(selected_riders, include_waiting_period)
    
    if premium is not None:
        print(f"The total premium for the selected options is: ${premium}")
```
