"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inmobiliariacapri.com.co
Prompt: Suggest tools or libraries to implement a rental cost simulator for tenants, inspired by Inmobiliaria Capri's simulator feature.
Generated: DETERMINISTIC_478060337ceb9cbc
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rental_cost_simulator.py

import pandas as pd

class RentalCostSimulator:
    """
    A class to simulate rental costs based on various parameters for tenants.
    
    Attributes:
        base_rent (float): The base rent amount.
        utilities (float): The estimated utilities cost.
        maintenance_fee (float): The estimated monthly maintenance fee.
        number_of_months (int): The number of months for the rental agreement.
    """

    def __init__(self, base_rent: float, utilities: float, maintenance_fee: float, number_of_months: int):
        """
        Initializes the RentalCostSimulator with provided parameters.
        
        Parameters:
            base_rent (float): The base rent amount.
            utilities (float): Estimated utilities cost.
            maintenance_fee (float): Estimated monthly maintenance fee.
            number_of_months (int): Duration of rental in months.
        """
        if base_rent < 0 or utilities < 0 or maintenance_fee < 0 or number_of_months <= 0:
            raise ValueError("All cost parameters must be non-negative and number_of_months must be positive.")
        
        self.base_rent = base_rent
        self.utilities = utilities
        self.maintenance_fee = maintenance_fee
        self.number_of_months = number_of_months

    def calculate_total_cost(self) -> float:
        """
        Calculates the total rental cost for the specified number of months.

        Returns:
            float: Total cost for the rental period.
        """
        total_cost = (self.base_rent + self.utilities + self.maintenance_fee) * self.number_of_months
        return total_cost

    def get_cost_breakdown(self) -> pd.DataFrame:
        """
        Provides a breakdown of rental costs over the rental period.

        Returns:
            pd.DataFrame: A DataFrame containing the breakdown of costs.
        """
        breakdown_data = {
            'Month': [i for i in range(1, self.number_of_months + 1)],
            'Base Rent': [self.base_rent] * self.number_of_months,
            'Utilities': [self.utilities] * self.number_of_months,
            'Maintenance Fee': [self.maintenance_fee] * self.number_of_months,
            'Total Cost': [(self.base_rent + self.utilities + self.maintenance_fee)] * self.number_of_months
        }
        return pd.DataFrame(breakdown_data)

def main():
    """
    Main function to simulate rental costs based on user input.
    """
    try:
        # Example parameters
        base_rent = 1200.00
        utilities = 150.00
        maintenance_fee = 50.00
        number_of_months = 12

        # Create an instance of RentalCostSimulator
        simulator = RentalCostSimulator(base_rent, utilities, maintenance_fee, number_of_months)

        # Calculate total cost
        total_cost = simulator.calculate_total_cost()
        print(f"Total Rental Cost for {number_of_months} months: ${total_cost:.2f}")

        # Get and display the cost breakdown
        cost_breakdown = simulator.get_cost_breakdown()
        print("\nCost Breakdown:\n", cost_breakdown)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
