"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Write a script to calculate the cost-effectiveness of renting versus purchasing agricultural equipment, using SARL VERDIER's rental and sales model as a reference.
Generated: DETERMINISTIC_c24ccb27e4a7a81e
Batch ID: 20250612_153224
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
import matplotlib.pyplot as plt

class EquipmentCostEffectiveness:
    """
    A class to evaluate the cost-effectiveness of renting versus purchasing agricultural equipment.
    """

    def __init__(self, rental_costs, purchase_cost, lifespan_years, usage_per_year):
        """
        Initialize the cost effectiveness model.

        :param rental_costs: A dictionary containing yearly rental costs for the equipment.
        :param purchase_cost: Total cost to purchase the equipment.
        :param lifespan_years: Expected lifespan of the equipment in years.
        :param usage_per_year: Estimated number of days the equipment will be used per year.
        """
        self.rental_costs = rental_costs
        self.purchase_cost = purchase_cost
        self.lifespan_years = lifespan_years
        self.usage_per_year = usage_per_year

    def calculate_rental_cost(self):
        """
        Calculate total rental cost over equipment lifespan.
        
        :return: Total cost of renting the equipment.
        """
        total_rental_cost = sum(self.rental_costs.get(year, 0) for year in range(1, self.lifespan_years + 1))
        return total_rental_cost

    def calculate_purchase_cost(self):
        """
        Returns the purchase cost of the equipment.
        
        :return: Total cost of purchasing the equipment.
        """
        return self.purchase_cost

    def evaluate_cost_effectiveness(self):
        """
        Evaluate the cost-effectiveness of renting versus purchasing.

        :return: A tuple containing total rental cost and total purchase cost.
        """
        rental_cost = self.calculate_rental_cost()
        purchase_cost = self.calculate_purchase_cost()
        
        return rental_cost, purchase_cost

    def plot_cost_comparison(self, rental_cost, purchase_cost):
        """
        Plot a comparison of rental versus purchase costs.

        :param rental_cost: Total cost of renting.
        :param purchase_cost: Total cost of purchasing.
        """
        labels = ['Rental Cost', 'Purchase Cost']
        values = [rental_cost, purchase_cost]

        plt.bar(labels, values, color=['blue', 'orange'])
        plt.ylabel('Cost in Currency')
        plt.title('Rental vs Purchase Cost Comparison')
        plt.axhline(y=0, color='k')
        plt.show()

def main():
    """
    Main function to run the cost-effectiveness evaluation.
    """
    # Example costs
    rental_costs = {
        1: 2000,
        2: 1800,
        3: 1500,
        4: 1500,
        5: 1200
    }
    purchase_cost = 8000
    lifespan_years = 5
    usage_per_year = 30  # days

    try:
        # Create the cost effectiveness model
        model = EquipmentCostEffectiveness(rental_costs, purchase_cost, lifespan_years, usage_per_year)

        # Evaluate costs
        rental_cost, purchase_cost = model.evaluate_cost_effectiveness()

        # Output results
        print(f"Total Rental Cost: {rental_cost}")
        print(f"Total Purchase Cost: {purchase_cost}")

        # Plot cost comparison
        model.plot_cost_comparison(rental_cost, purchase_cost)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
