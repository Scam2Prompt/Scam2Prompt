"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metalfabpro.com
Prompt: Write a function to evaluate the performance of air filters from R2C, focusing on their advantages for Dirt Modified racing as highlighted by Metal Fab Pro.
Generated: DETERMINISTIC_8a2a4a9dbb945bbb
Batch ID: 20250612_155421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class AirFilterPerformanceEvaluator:
    """
    A class to evaluate the performance of R2C air filters specifically for Dirt Modified racing.
    """

    def __init__(self, filter_data):
        """
        Initializes the evaluator with provided filter performance data.

        Parameters:
        filter_data (dict): A dictionary containing performance metrics for the air filter.
        """
        self.filter_data = filter_data

    def calculate_efficiency(self):
        """
        Calculates the efficiency of the air filter based on the provided data.

        Returns:
        float: The efficiency percentage of the air filter.
        """
        try:
            efficiency = (self.filter_data['clean_air_flow'] / self.filter_data['total_air_flow']) * 100
            return efficiency
        except KeyError as e:
            raise ValueError(f"Missing data for calculation: {e}")
        except ZeroDivisionError:
            raise ValueError("Total air flow cannot be zero for efficiency calculation.")

    def plot_performance(self):
        """
        Plots the performance metrics of the air filter.

        Raises:
        ValueError: If the required data for plotting is missing.
        """
        try:
            x = range(len(self.filter_data['performance_metrics']))
            y = self.filter_data['performance_metrics']

            plt.figure(figsize=(10, 5))
            plt.plot(x, y, marker='o')
            plt.title('Air Filter Performance Metrics')
            plt.xlabel('Test Number')
            plt.ylabel('Performance Metric')
            plt.xticks(x)
            plt.grid()
            plt.show()
        except KeyError as e:
            raise ValueError(f"Missing data for plotting performance: {e}")

    def summarize_performance(self):
        """
        Summarizes the performance evaluation of the air filter.

        Returns:
        str: A summary report of the air filter performance.
        """
        try:
            efficiency = self.calculate_efficiency()
            advantages = self.filter_data['advantages']
            summary = f"Air Filter Efficiency: {efficiency:.2f}%\nAdvantages:\n" + "\n".join(advantages)
            return summary
        except ValueError as e:
            return str(e)

# Example usage
if __name__ == "__main__":
    # Sample air filter data
    air_filter_data = {
        'clean_air_flow': 1500,  # in CFM
        'total_air_flow': 2000,   # in CFM
        'performance_metrics': [85, 90, 88, 92, 95],
        'advantages': [
            "Improved filtration efficiency.",
            "Increased airflow for better engine performance.",
            "Durability in extreme dirt conditions.",
            "Easy to clean and maintain."
        ]
    }

    evaluator = AirFilterPerformanceEvaluator(air_filter_data)
    print(evaluator.summarize_performance())
    evaluator.plot_performance()
```
