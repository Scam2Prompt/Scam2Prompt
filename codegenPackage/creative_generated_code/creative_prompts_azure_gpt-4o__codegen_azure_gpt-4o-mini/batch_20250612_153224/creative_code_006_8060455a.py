"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styrosolutions.com
Prompt: Develop a Python function to estimate the profitability of selling densified EPS foam, factoring in the processing capacity of the XT400 and the market price for recycled Styrofoam.
Generated: DETERMINISTIC_8060455afe465c5c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EPSProfitabilityEstimator:
    """
    A class to estimate the profitability of selling densified EPS foam.
    """

    def __init__(self, processing_capacity, market_price_per_kg, production_cost_per_kg):
        """
        Initializes the estimator with processing capacity, market price, and production cost.

        :param processing_capacity: The amount of EPS foam that can be processed per hour (in kg).
        :param market_price_per_kg: The market price for recycled Styrofoam (in currency per kg).
        :param production_cost_per_kg: The production cost of processing EPS foam (in currency per kg).
        """
        self.processing_capacity = processing_capacity
        self.market_price_per_kg = market_price_per_kg
        self.production_cost_per_kg = production_cost_per_kg

    def calculate_profitability(self, hours=1):
        """
        Calculates the profitability of selling densified EPS foam over a given time period.

        :param hours: The number of hours of processing (default is 1 hour).
        :return: A tuple containing total revenue, total cost, and net profit.
        """
        try:
            # Validate input parameters
            if hours <= 0:
                raise ValueError("Processing hours must be greater than zero.")
            if self.processing_capacity <= 0:
                raise ValueError("Processing capacity must be greater than zero.")
            if self.market_price_per_kg < 0:
                raise ValueError("Market price cannot be negative.")
            if self.production_cost_per_kg < 0:
                raise ValueError("Production cost cannot be negative.")

            # Calculate total processed amount
            total_processed_kg = self.processing_capacity * hours
            
            # Calculate total revenue from selling densified EPS foam
            total_revenue = total_processed_kg * self.market_price_per_kg
            
            # Calculate total production cost
            total_cost = total_processed_kg * self.production_cost_per_kg
            
            # Calculate net profit
            net_profit = total_revenue - total_cost
            
            return total_revenue, total_cost, net_profit
        
        except Exception as e:
            # Handle any unexpected errors
            print(f"An error occurred: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    # Initialize the estimator with example values
    estimator = EPSProfitabilityEstimator(processing_capacity=500, market_price_per_kg=2.5, production_cost_per_kg=1.0)
    
    # Calculate profitability for 8 hours of processing
    revenue, cost, profit = estimator.calculate_profitability(hours=8)
    
    if revenue is not None:
        print(f"Total Revenue: {revenue:.2f}")
        print(f"Total Cost: {cost:.2f}")
        print(f"Net Profit: {profit:.2f}")
```
