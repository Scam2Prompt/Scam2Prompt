"""
Generated Code Metadata:
========================
Original URL: https://cedarinternational.ca
Prompt: Write code to calculate lead times and minimize delays in the supply chain for products such as turbines, instrumentation equipment, and plumbing materials, inspired by Cedar International Inc.'s logistics approach.
Generated: DETERMINISTIC_98420a83f4979637
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class SupplyChainOptimizer:
    """
    A class to optimize lead times and minimize delays in the supply chain for various products.
    """

    def __init__(self, data):
        """
        Initializes the SupplyChainOptimizer with supply chain data.

        :param data: A pandas DataFrame containing supply chain information.
        """
        self.data = data

    def preprocess_data(self):
        """
        Preprocess the data to ensure all necessary columns are in the correct format.
        """
        # Convert date columns to datetime
        self.data['order_date'] = pd.to_datetime(self.data['order_date'], errors='coerce')
        self.data['delivery_date'] = pd.to_datetime(self.data['delivery_date'], errors='coerce')

        # Drop rows with invalid dates
        self.data.dropna(subset=['order_date', 'delivery_date'], inplace=True)

    def calculate_lead_time(self):
        """
        Calculate lead time for each order in the supply chain.

        :return: A pandas Series containing lead times in days.
        """
        lead_time = (self.data['delivery_date'] - self.data['order_date']).dt.days
        return lead_time

    def minimize_delays(self):
        """
        Minimize delays by optimizing order scheduling based on lead times.

        :return: A DataFrame with optimized order scheduling.
        """
        # Calculate lead times
        self.data['lead_time'] = self.calculate_lead_time()

        # Sort by lead time to prioritize shorter lead times
        optimized_schedule = self.data.sort_values(by='lead_time')

        return optimized_schedule

    def generate_report(self, optimized_schedule):
        """
        Generate a report of the optimized supply chain schedule.

        :param optimized_schedule: A DataFrame containing the optimized schedule.
        :return: A string report summarizing the optimized schedule.
        """
        report = "Optimized Supply Chain Schedule:\n"
        report += optimized_schedule[['product', 'order_date', 'delivery_date', 'lead_time']].to_string(index=False)
        return report

def main():
    # Sample data for demonstration
    data = {
        'product': ['Turbine', 'Instrumentation', 'Plumbing', 'Turbine', 'Instrumentation'],
        'order_date': ['2023-01-01', '2023-01-05', '2023-01-10', '2023-01-15', '2023-01-20'],
        'delivery_date': ['2023-01-10', '2023-01-15', '2023-01-20', '2023-01-25', '2023-01-30']
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Initialize the SupplyChainOptimizer
    optimizer = SupplyChainOptimizer(df)

    try:
        # Preprocess the data
        optimizer.preprocess_data()

        # Minimize delays and get the optimized schedule
        optimized_schedule = optimizer.minimize_delays()

        # Generate and print the report
        report = optimizer.generate_report(optimized_schedule)
        print(report)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
