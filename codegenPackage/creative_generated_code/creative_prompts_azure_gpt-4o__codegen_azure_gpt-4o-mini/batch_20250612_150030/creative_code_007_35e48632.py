"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apexdiginvcompany.com
Prompt: Develop code for a financial growth tracker that visualizes annual progress metrics such as business growth, investment growth, and financial growth, similar to Apex Digital Limited's progress statistics.
Generated: DETERMINISTIC_35e486321b19e179
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import numpy as np

class FinancialGrowthTracker:
    def __init__(self):
        """Initialize the financial growth tracker with empty datasets."""
        self.years = []
        self.business_growth = []
        self.investment_growth = []
        self.financial_growth = []

    def add_year_data(self, year, business, investment, financial):
        """
        Add data for a specific year.
        
        :param year: The year of the data entry (int).
        :param business: The business growth metric for the year (float).
        :param investment: The investment growth metric for the year (float).
        :param financial: The financial growth metric for the year (float).
        """
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Year must be a positive integer.")
        
        if not all(isinstance(x, (int, float)) for x in (business, investment, financial)):
            raise ValueError("Growth metrics must be numeric values.")

        self.years.append(year)
        self.business_growth.append(business)
        self.investment_growth.append(investment)
        self.financial_growth.append(financial)

    def visualize_growth(self):
        """Visualize the growth metrics over the recorded years."""
        if not self.years:
            raise RuntimeError("No data available to visualize.")

        # Create a line plot for each growth metric
        plt.figure(figsize=(12, 6))
        plt.plot(self.years, self.business_growth, label='Business Growth (%)', marker='o')
        plt.plot(self.years, self.investment_growth, label='Investment Growth (%)', marker='o')
        plt.plot(self.years, self.financial_growth, label='Financial Growth (%)', marker='o')

        # Add titles and labels
        plt.title('Annual Financial Growth Tracker')
        plt.xlabel('Year')
        plt.ylabel('Growth (%)')
        plt.xticks(self.years)  # Set x-ticks to be years
        plt.grid()
        plt.legend()
        plt.tight_layout()

        # Show the plot
        plt.show()

def main():
    """Main function to run the financial growth tracker."""
    tracker = FinancialGrowthTracker()

    try:
        # Adding sample data
        tracker.add_year_data(2021, 5.0, 10.0, 7.0)
        tracker.add_year_data(2022, 6.5, 12.5, 8.3)
        tracker.add_year_data(2023, 7.8, 15.0, 9.5)

        # Visualize the growth data
        tracker.visualize_growth()
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
