"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: Write a Python function to calculate the cost-effectiveness of Engel coolers over time, considering durability, ice retention, and purchase price.
Generated: DETERMINISTIC_e6089fb5e1870aef
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EngelCooler:
    def __init__(self, purchase_price, durability_years, ice_retention_days):
        """
        Initialize an Engel cooler with its purchase price, durability, and ice retention.

        :param purchase_price: The purchase price of the cooler in dollars.
        :param durability_years: The expected durability of the cooler in years.
        :param ice_retention_days: The number of days the cooler can retain ice.
        """
        self.purchase_price = purchase_price
        self.durability_years = durability_years
        self.ice_retention_days = ice_retention_days

    def calculate_cost_effectiveness(self):
        """
        Calculate the cost-effectiveness of the cooler over its lifespan.

        :return: A dictionary containing cost per year and cost per day of ice retention.
        """
        try:
            # Calculate total lifespan in days
            total_lifespan_days = self.durability_years * 365
            
            # Calculate cost per year
            cost_per_year = self.purchase_price / self.durability_years
            
            # Calculate cost per day of ice retention
            cost_per_day_ice_retention = self.purchase_price / self.ice_retention_days
            
            return {
                "cost_per_year": cost_per_year,
                "cost_per_day_ice_retention": cost_per_day_ice_retention
            }
        except ZeroDivisionError as e:
            raise ValueError("Durability years and ice retention days must be greater than zero.") from e
        except Exception as e:
            raise RuntimeError("An unexpected error occurred while calculating cost-effectiveness.") from e

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of EngelCooler
        cooler = EngelCooler(purchase_price=300, durability_years=10, ice_retention_days=5)
        
        # Calculate cost-effectiveness
        cost_effectiveness = cooler.calculate_cost_effectiveness()
        
        # Print the results
        print("Cost Effectiveness of Engel Cooler:")
        print(f"Cost per Year: ${cost_effectiveness['cost_per_year']:.2f}")
        print(f"Cost per Day of Ice Retention: ${cost_effectiveness['cost_per_day_ice_retention']:.2f}")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")
```
