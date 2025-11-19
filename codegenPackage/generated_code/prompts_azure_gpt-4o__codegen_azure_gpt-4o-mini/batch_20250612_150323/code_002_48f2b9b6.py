"""
Generated Code Metadata:
========================
Original URL: https://openseam.co
Prompt: Generate code to calculate recoupable revenue for a factory using OpenSeam's ROI calculator assumptions, including inputs like work hours, production lines, and profit margins.
Generated: DETERMINISTIC_48f2b9b6490daea0
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FactoryRevenueCalculator:
    """
    A class to calculate recoupable revenue for a factory based on OpenSeam's ROI calculator assumptions.
    """

    def __init__(self, work_hours_per_day, production_lines, profit_margin):
        """
        Initializes the FactoryRevenueCalculator with the given parameters.

        :param work_hours_per_day: Number of hours the factory operates in a day
        :param production_lines: Number of production lines in the factory
        :param profit_margin: Profit margin as a percentage (0-100)
        """
        self.work_hours_per_day = work_hours_per_day
        self.production_lines = production_lines
        self.profit_margin = profit_margin / 100  # Convert percentage to decimal

    def calculate_daily_revenue(self, production_per_line):
        """
        Calculates the daily revenue based on production per line.

        :param production_per_line: Number of units produced per production line in a day
        :return: Total daily revenue
        """
        if production_per_line < 0:
            raise ValueError("Production per line must be a non-negative value.")
        
        total_production = self.production_lines * production_per_line
        daily_revenue = total_production * self.get_unit_price()
        return daily_revenue

    def get_unit_price(self):
        """
        Returns the unit price of the product. This can be modified to fetch from a database or configuration.

        :return: Unit price of the product
        """
        # Placeholder for unit price; in a real application, this could be fetched from a database
        return 100.0  # Example unit price

    def calculate_recoupable_revenue(self, production_per_line):
        """
        Calculates the recoupable revenue based on daily revenue and profit margin.

        :param production_per_line: Number of units produced per production line in a day
        :return: Recoupable revenue
        """
        daily_revenue = self.calculate_daily_revenue(production_per_line)
        recoupable_revenue = daily_revenue * self.profit_margin
        return recoupable_revenue

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the factory revenue calculator
        calculator = FactoryRevenueCalculator(work_hours_per_day=8, production_lines=5, profit_margin=20)

        # Calculate recoupable revenue for a given production per line
        production_per_line = 50  # Example input
        recoupable_revenue = calculator.calculate_recoupable_revenue(production_per_line)

        print(f"Recoupable Revenue: ${recoupable_revenue:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
