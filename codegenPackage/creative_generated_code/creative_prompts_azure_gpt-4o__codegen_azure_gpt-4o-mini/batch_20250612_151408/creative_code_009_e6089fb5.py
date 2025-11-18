"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Write a Python function to calculate the cost-effectiveness of Engel coolers over time, considering durability, ice retention, and purchase price.
Generated: DETERMINISTIC_e6089fb5e1870aef
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EngelCooler:
    """
    A class to represent an Engel cooler and calculate its cost-effectiveness.
    
    Attributes:
        purchase_price (float): The purchase price of the cooler.
        durability_years (int): The expected durability of the cooler in years.
        ice_retention_days (float): The average number of days the cooler retains ice.
    """

    def __init__(self, purchase_price: float, durability_years: int, ice_retention_days: float):
        """
        Initializes an Engel cooler instance.

        Args:
            purchase_price (float): The purchase price of the cooler.
            durability_years (int): The expected durability of the cooler in years.
            ice_retention_days (float): The average number of days the cooler retains ice.
        """
        self.purchase_price = purchase_price
        self.durability_years = durability_years
        self.ice_retention_days = ice_retention_days

    def calculate_cost_effectiveness(self) -> float:
        """
        Calculates the cost-effectiveness of the cooler based on its durability 
        and ice retention.

        Returns:
            float: The cost-effectiveness ratio (cost per day of ice retention).
        """
        # Validate inputs
        if self.purchase_price <= 0:
            raise ValueError("Purchase price must be a positive number.")
        if self.durability_years <= 0:
            raise ValueError("Durability years must be a positive integer.")
        if self.ice_retention_days <= 0:
            raise ValueError("Ice retention days must be a positive number.")

        # Calculate total days of use based on durability
        total_days = self.durability_years * 365
        
        # Calculate cost-effectiveness (cost per day of ice retention)
        cost_effectiveness = self.purchase_price / (self.ice_retention_days * total_days)

        return cost_effectiveness

# Example usage
if __name__ == "__main__":
    try:
        cooler = EngelCooler(purchase_price=500, durability_years=10, ice_retention_days=5)
        effectiveness = cooler.calculate_cost_effectiveness()
        print(f"Cost-effectiveness of the Engel cooler: ${effectiveness:.4f} per day of ice retention.")
    except ValueError as e:
        print(f"Error: {e}")
```
