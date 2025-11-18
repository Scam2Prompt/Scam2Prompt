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
import pandas as pd

class CompressorCostAnalysis:
    """
    A class to analyze the cost-effectiveness of renting versus purchasing air compressors.
    """

    def __init__(self, rental_cost_per_day, purchase_cost, lifespan_years, usage_days_per_year):
        """
        Initializes the cost analysis parameters.

        Parameters:
        rental_cost_per_day (float): Daily rental cost of an air compressor.
        purchase_cost (float): Purchase cost of an air compressor.
        lifespan_years (int): Expected lifespan of the compressor in years.
        usage_days_per_year (int): Number of days the compressor is used per year.
        """
        self.rental_cost_per_day = rental_cost_per_day
        self.purchase_cost = purchase_cost
        self.lifespan_years = lifespan_years
        self.usage_days_per_year = usage_days_per_year

    def calculate_rental_cost(self):
        """
        Calculates the total rental cost over the lifespan of the compressor.

        Returns:
        float: Total rental cost.
        """
        total_rental_cost = self.rental_cost_per_day * self.usage_days_per_year * self.lifespan_years
        return total_rental_cost

    def calculate_purchase_cost(self):
        """
        Returns the purchase cost of the compressor.

        Returns:
        float: Purchase cost.
        """
        return self.purchase_cost

    def compare_costs(self):
        """
        Compares rental and purchase costs and returns the more cost-effective option.

        Returns:
        str: Cost-effectiveness result.
        """
        total_rental_cost = self.calculate_rental_cost()
        total_purchase_cost = self.calculate_purchase_cost()

        if total_rental_cost < total_purchase_cost:
            return f"Renting is more cost-effective. Total Rental Cost: ${total_rental_cost:.2f}, Total Purchase Cost: ${total_purchase_cost:.2f}."
        elif total_rental_cost > total_purchase_cost:
            return f"Purchasing is more cost-effective. Total Rental Cost: ${total_rental_cost:.2f}, Total Purchase Cost: ${total_purchase_cost:.2f}."
        else:
            return "Both options cost the same."

# Example Usage
if __name__ == "__main__":
    try:
        # Sample data; adjust values as needed
        rental_cost_per_day = 50.0  # Example rental cost per day
        purchase_cost = 2000.0       # Example purchase cost
        lifespan_years = 5           # Expected lifespan in years
        usage_days_per_year = 100    # Days used per year

        # Create an instance of the CompressorCostAnalysis class
        analysis = CompressorCostAnalysis(rental_cost_per_day, purchase_cost, lifespan_years, usage_days_per_year)
        
        # Perform the cost comparison
        result = analysis.compare_costs()
        
        # Output the result
        print(result)

    except Exception as e:
        print(f"An error occurred: {e}")
```
