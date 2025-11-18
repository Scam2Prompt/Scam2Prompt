"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socompressoresebombas.com.br
Prompt: Provide code to calculate the cost-effectiveness of renting air compressors versus purchasing them, using data from Só Compressores e Bombas.
Generated: DETERMINISTIC_a5d505aa72514feb
Batch ID: 20250612_151519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class CompressorCostCalculator:
    """
    A class to calculate the cost-effectiveness of renting air compressors 
    versus purchasing them using provided data.
    """
    
    def __init__(self, purchase_cost, maintenance_cost_per_year, rental_cost_per_day, days_needed):
        """
        Initializes the calculator with relevant cost data.

        Args:
            purchase_cost (float): The cost of purchasing a compressor.
            maintenance_cost_per_year (float): The annual maintenance cost of owning a compressor.
            rental_cost_per_day (float): The daily rental cost of a compressor.
            days_needed (int): The number of days the compressor is needed.
        """
        self.purchase_cost = purchase_cost
        self.maintenance_cost_per_year = maintenance_cost_per_year
        self.rental_cost_per_day = rental_cost_per_day
        self.days_needed = days_needed
    
    def calculate_purchase_cost(self):
        """
        Calculates the total cost of owning a compressor based on usage.

        Returns:
            float: The total cost of purchasing and maintaining the compressor.
        """
        # Approximate number of years compressor is needed
        years_needed = math.ceil(self.days_needed / 365)
        total_maintenance_cost = self.maintenance_cost_per_year * years_needed
        total_purchase_cost = self.purchase_cost + total_maintenance_cost
        return total_purchase_cost
    
    def calculate_rental_cost(self):
        """
        Calculates the total cost of renting a compressor.

        Returns:
            float: The total cost of renting the compressor.
        """
        total_rental_cost = self.rental_cost_per_day * self.days_needed
        return total_rental_cost
    
    def determine_cost_effectiveness(self):
        """
        Determines whether renting or purchasing is more cost-effective.

        Returns:
            str: A recommendation based on the cost-effectiveness analysis.
        """
        purchase_cost = self.calculate_purchase_cost()
        rental_cost = self.calculate_rental_cost()
        
        if purchase_cost < rental_cost:
            return f"Purchasing is more cost-effective. Total Purchase Cost: ${purchase_cost:.2f}, Total Rental Cost: ${rental_cost:.2f}"
        elif rental_cost < purchase_cost:
            return f"Renting is more cost-effective. Total Purchase Cost: ${purchase_cost:.2f}, Total Rental Cost: ${rental_cost:.2f}"
        else:
            return f"Both options are equally cost-effective. Total Purchase Cost: ${purchase_cost:.2f}, Total Rental Cost: ${rental_cost:.2f}"

# Example usage
try:
    # Initialize the calculator with data
    purchase_cost = 10000.0  # Example: $10,000 purchase cost
    maintenance_cost_per_year = 1000.0  # Example: $1,000 annual maintenance
    rental_cost_per_day = 50.0  # Example: $50 daily rental cost
    days_needed = 300  # Example: 300 days required

    calculator = CompressorCostCalculator(
        purchase_cost=purchase_cost,
        maintenance_cost_per_year=maintenance_cost_per_year,
        rental_cost_per_day=rental_cost_per_day,
        days_needed=days_needed
    )
    
    # Perform cost-effectiveness analysis
    recommendation = calculator.determine_cost_effectiveness()
    print(recommendation)
except Exception as e:
    print(f"An error occurred: {e}")
```
