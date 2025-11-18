"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wealthbhai.com
Prompt: Develop a Python program to compare the performance of different rolling machines (e.g., LG30#, LD40#) for producing high-precision stainless steel pipes.
Generated: DETERMINISTIC_b6eea6f67ba72456
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class RollingMachinePerformanceAnalyzer:
    """
    A class to analyze and compare the performance of various rolling machines 
    in producing high-precision stainless steel pipes.
    """

    def __init__(self):
        """
        Initializes the analyzer with an empty performance dataset.
        """
        self.data = pd.DataFrame()

    def load_data(self, file_path: str):
        """
        Loads performance data from a CSV file.

        :param file_path: Path to the CSV file containing performance data.
                          Expected columns: ['Machine', 'PipeDiameter', 'Precision', 'Speed']
        """
        try:
            self.data = pd.read_csv(file_path)
            # Validate required columns are present
            required_columns = {'Machine', 'PipeDiameter', 'Precision', 'Speed'}
            if not required_columns.issubset(self.data.columns):
                raise ValueError(f"CSV file must contain columns: {required_columns}")
        except Exception as e:
            print(f"Error loading data file: {e}")
            raise

    def summarize_performance(self):
        """
        Generates a summary of the performance data, grouped by machine.
        
        :return: A summary DataFrame with mean precision and speed for each machine.
        """
        if self.data.empty:
            raise ValueError("No data available. Please load data first.")

        # Group by machine and calculate average precision and speed
        summary = self.data.groupby('Machine').agg({
            'Precision': 'mean',
            'Speed': 'mean'
        }).rename(columns={
            'Precision': 'Average Precision',
            'Speed': 'Average Speed'
        }).reset_index()

        return summary

    def plot_performance_comparison(self):
        """
        Plots a comparison of the rolling machine performance (precision vs. speed).
        """
        if self.data.empty:
            raise ValueError("No data available. Please load data first.")

        summary = self.summarize_performance()

        plt.figure(figsize=(10, 6))
        plt.scatter(summary['Average Speed'], summary['Average Precision'], color='blue', alpha=0.7)
        
        # Annotate data points with machine names
        for idx, row in summary.iterrows():
            plt.text(row['Average Speed'], row['Average Precision'], row['Machine'], fontsize=9, ha='right')

        plt.title('Rolling Machine Performance Comparison')
        plt.xlabel('Average Speed (pipes/hour)')
        plt.ylabel('Average Precision (%)')
        plt.grid(True)
        plt.show()

    def compare_machines(self):
        """
        Identifies the top-performing machine based on a weighted metric of precision and speed.

        :return: Name of the top-performing machine.
        """
        if self.data.empty:
            raise ValueError("No data available. Please load data first.")

        # Add a weighted metric (e.g., precision * speed) to identify the best machine
        self.data['PerformanceScore'] = self.data['Precision'] * self.data['Speed']
        
        # Find machine with the highest average performance score
        top_machine = self.data.groupby('Machine')['PerformanceScore'].mean().idxmax()
        
        return top_machine


if __name__ == "__main__":
    # Example usage
    analyzer = RollingMachinePerformanceAnalyzer()
    
    # Load the performance data from a CSV file
    try:
        analyzer.load_data("rolling_machine_performance.csv")
    except FileNotFoundError:
        print("Error: The specified file was not found.")
        exit(1)
    except ValueError as ve:
        print(f"Data validation error: {ve}")
        exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        exit(1)

    # Summarize performance data
    try:
        summary = analyzer.summarize_performance()
        print("Performance Summary:")
        print(summary)
    except ValueError as ve:
        print(f"Error: {ve}")
        exit(1)

    # Visualize performance comparison
    try:
        analyzer.plot_performance_comparison()
    except ValueError as ve:
        print(f"Error: {ve}")
        exit(1)

    # Identify the top-performing machine
    try:
        top_machine = analyzer.compare_machines()
        print(f"The top-performing machine is: {top_machine}")
    except ValueError as ve:
        print(f"Error: {ve}")
        exit(1)
```
