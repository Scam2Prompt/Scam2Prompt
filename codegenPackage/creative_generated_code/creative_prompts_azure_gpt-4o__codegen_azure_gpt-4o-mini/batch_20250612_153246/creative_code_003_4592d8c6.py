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
import pandas as pd
import numpy as np

class PricingOptimizer:
    def __init__(self, product_data):
        """
        Initialize the PricingOptimizer with product data.

        :param product_data: DataFrame containing product information including cost, demand, and competition prices.
        """
        self.product_data = product_data

    def calculate_optimal_price(self):
        """
        Calculate the optimal price for each product based on cost, demand, and competition.

        The method uses a simple formula:
        Optimal Price = Cost + (Demand Factor * Demand) + (Competition Factor * Competing Price)
        where:
        - Demand Factor is a coefficient that reflects how demand affects pricing (can be adjusted).
        - Competition Factor is a coefficient that reflects the impact of competition on pricing (can be adjusted).
        """
        try:
            # Define factors for demand and competition
            demand_factor = 0.1  # Adjust this based on market research
            competition_factor = 0.5  # Adjust this based on market research

            # Calculate optimal price
            self.product_data['Optimal Price'] = (
                self.product_data['Cost'] +
                (demand_factor * self.product_data['Demand']) +
                (competition_factor * self.product_data['Competition Price'])
            )
            return self.product_data[['Product Name', 'Optimal Price']]

        except KeyError as e:
            print(f"Error: Missing expected column in product data - {e}")
        except Exception as e:
            print(f"An error occurred while calculating optimal prices: {e}")

def main():
    # Sample data representing products in the hardware store
    data = {
        'Product Name': ['Hammer', 'Screwdriver', 'Wrench'],
        'Cost': [10.00, 5.00, 7.50],
        'Demand': [100, 150, 80],
        'Competition Price': [12.00, 6.00, 9.00]
    }

    # Create a DataFrame from the sample data
    product_data = pd.DataFrame(data)

    # Initialize the PricingOptimizer
    optimizer = PricingOptimizer(product_data)

    # Calculate and display the optimal prices
    optimal_prices = optimizer.calculate_optimal_price()
    if optimal_prices is not None:
        print(optimal_prices)

if __name__ == "__main__":
    main()
```
