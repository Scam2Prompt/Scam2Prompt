"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aulaferretera.com
Prompt: Create a script to calculate optimal pricing for hardware store products based on cost, demand, and competition, inspired by the blog "Cómo Fijar Precios en una Ferretería y Asegurar tu Rentabilidad" from Aula Ferretera.
Generated: DETERMINISTIC_4592d8c62aa0b2ef
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class ProductPricingCalculator:
    """
    A class to calculate optimal pricing for hardware store products based on cost, demand, and competition.
    """
    
    def __init__(self, cost, demand_level, competition_price):
        """
        Initialize the calculator with product cost, demand level, and competitor pricing.
        
        :param cost: The cost price of the product.
        :param demand_level: The demand level for the product on a scale of 1 (low) to 10 (high).
        :param competition_price: The price set by competitors for the same or similar product.
        """
        self.cost = cost
        self.demand_level = demand_level
        self.competition_price = competition_price
    
    def calculate_optimal_price(self):
        """
        Calculates the optimal price using weighted factors for cost, demand, and competition.
        - Cost contributes 50% weight (ensures profitability).
        - Demand contributes 30% weight (higher demand may allow higher pricing).
        - Competition contributes 20% weight (ensures competitiveness).
        
        :return: Float optimal price.
        """
        try:
            # Ensure all input values are valid
            if self.cost <= 0:
                raise ValueError("Cost must be greater than 0.")
            if not (1 <= self.demand_level <= 10):
                raise ValueError("Demand level must be between 1 and 10.")
            if self.competition_price <= 0:
                raise ValueError("Competition price must be greater than 0.")

            # Weight factors
            cost_weight = 0.5
            demand_weight = 0.3
            competition_weight = 0.2

            # Demand adjustment factor: scales demand level into a price adjustment range.
            demand_adjustment = (self.demand_level / 10) * self.cost * 0.2

            # Calculate weighted contributions
            cost_contribution = self.cost * cost_weight
            demand_contribution = demand_adjustment * demand_weight
            competition_contribution = self.competition_price * competition_weight

            # Optimal price calculation
            optimal_price = cost_contribution + demand_contribution + competition_contribution
            return round(optimal_price, 2)
        
        except ValueError as e:
            print(f"Error: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Input data
    cost = float(input("Enter the cost price of the product: "))
    demand_level = int(input("Enter the demand level (1 to 10): "))
    competition_price = float(input("Enter the competitor's price: "))
    
    # Initialize calculator
    calculator = ProductPricingCalculator(cost, demand_level, competition_price)
    
    # Calculate optimal price
    optimal_price = calculator.calculate_optimal_price()
    
    if optimal_price is not None:
        print(f"The optimal price for the product is: ${optimal_price}")
    else:
        print("Could not calculate optimal price due to errors in input.")
```
