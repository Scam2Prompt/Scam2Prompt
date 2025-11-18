"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carthewchautaxreports.pages.dev
Prompt: Develop a script to calculate business succession planning outcomes, incorporating Carthew Chau & Co's combined legal and financial perspectives.
Generated: DETERMINISTIC_0078dd40f25453dc
Batch ID: 20250612_152615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd

class BusinessSuccessionPlanner:
    """
    A class to calculate business succession planning outcomes
    from both legal and financial perspectives.
    """

    def __init__(self, business_value: float, transition_years: int):
        """
        Initialize the planner with business value and transition years.

        :param business_value: The total value of the business.
        :param transition_years: The number of years over which the succession will occur.
        """
        if business_value <= 0:
            raise ValueError("Business value must be greater than zero.")
        if transition_years <= 0:
            raise ValueError("Transition years must be greater than zero.")

        self.business_value = business_value
        self.transition_years = transition_years

    def calculate_discount_rate(self, risk_assessment: float) -> float:
        """
        Calculate the discount rate based on risk assessment.

        :param risk_assessment: A float representing the risk level (0 to 1).
        :return: Discount rate as a percentage.
        """
        if not (0 <= risk_assessment <= 1):
            raise ValueError("Risk assessment must be between 0 and 1.")

        discount_rate = 0.05 + risk_assessment * 0.15  # Base rate + risk adjustment
        return discount_rate

    def calculate_present_value(self, discount_rate: float) -> float:
        """
        Calculate the present value of the business using the discount rate.

        :param discount_rate: The discount rate as a percentage.
        :return: Present value of the business.
        """
        present_value = self.business_value / ((1 + discount_rate) ** self.transition_years)
        return present_value

    def generate_succession_plan(self, risk_assessment: float) -> pd.DataFrame:
        """
        Generate a succession plan and its financial outcomes.

        :param risk_assessment: A float representing the risk level (0 to 1).
        :return: A DataFrame containing the succession plan outcomes.
        """
        discount_rate = self.calculate_discount_rate(risk_assessment)
        present_value = self.calculate_present_value(discount_rate)

        # Prepare the succession outcomes
        outcomes = {
            'Business Value': [self.business_value],
            'Discount Rate (%)': [discount_rate * 100],
            'Present Value': [present_value],
            'Transition Years': [self.transition_years]
        }

        return pd.DataFrame(outcomes)


def main():
    """
    Main function to execute the business succession planning script.
    """
    try:
        # Input variables
        business_value = 1000000  # Example business value
        transition_years = 5       # Example transition period
        risk_assessment = 0.2      # Example risk assessment (20%)

        # Create a BusinessSuccessionPlanner instance
        planner = BusinessSuccessionPlanner(business_value, transition_years)

        # Generate the succession plan
        succession_plan = planner.generate_succession_plan(risk_assessment)

        # Output the results
        print(succession_plan)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
