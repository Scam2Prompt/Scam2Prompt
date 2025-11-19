"""
Generated Code Metadata:
========================
Original URL: https://aulaferretera.com
Prompt: Develop a tool to analyze supplier performance and optimize the supply chain for a hardware store, using insights from the "Selección Estratégica" section of Aula Ferretera.
Generated: DETERMINISTIC_b21abaaa003e010f
Batch ID: 20250612_153246
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
import matplotlib.pyplot as plt

class SupplierPerformanceAnalyzer:
    """
    A class to analyze supplier performance and optimize the supply chain for a hardware store.
    """

    def __init__(self, data_file):
        """
        Initializes the SupplierPerformanceAnalyzer with data from a CSV file.

        :param data_file: str - Path to the CSV file containing supplier data.
        """
        self.data_file = data_file
        self.supplier_data = self.load_data()

    def load_data(self):
        """
        Loads supplier data from a CSV file.

        :return: DataFrame - A pandas DataFrame containing the supplier data.
        """
        try:
            data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
            return data
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except pd.errors.ParserError:
            print("Error: The file could not be parsed.")
            raise

    def analyze_performance(self):
        """
        Analyzes supplier performance based on key metrics.

        :return: DataFrame - A DataFrame containing performance metrics for each supplier.
        """
        try:
            # Calculate performance metrics
            performance_metrics = self.supplier_data.groupby('Supplier').agg({
                'Delivery Time': 'mean',
                'Quality Score': 'mean',
                'Cost': 'mean'
            }).reset_index()

            performance_metrics.columns = ['Supplier', 'Average Delivery Time', 'Average Quality Score', 'Average Cost']
            print("Performance analysis completed.")
            return performance_metrics
        except KeyError as e:
            print(f"Error: Missing expected column in data - {e}")
            raise

    def visualize_performance(self, performance_metrics):
        """
        Visualizes supplier performance metrics using bar charts.

        :param performance_metrics: DataFrame - A DataFrame containing performance metrics.
        """
        try:
            # Set up the figure and axes
            fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 15))

            # Plot Average Delivery Time
            axes[0].bar(performance_metrics['Supplier'], performance_metrics['Average Delivery Time'], color='blue')
            axes[0].set_title('Average Delivery Time by Supplier')
            axes[0].set_ylabel('Days')
            axes[0].set_xticklabels(performance_metrics['Supplier'], rotation=45)

            # Plot Average Quality Score
            axes[1].bar(performance_metrics['Supplier'], performance_metrics['Average Quality Score'], color='green')
            axes[1].set_title('Average Quality Score by Supplier')
            axes[1].set_ylabel('Score')
            axes[1].set_xticklabels(performance_metrics['Supplier'], rotation=45)

            # Plot Average Cost
            axes[2].bar(performance_metrics['Supplier'], performance_metrics['Average Cost'], color='red')
            axes[2].set_title('Average Cost by Supplier')
            axes[2].set_ylabel('Cost')
            axes[2].set_xticklabels(performance_metrics['Supplier'], rotation=45)

            plt.tight_layout()
            plt.show()
            print("Performance visualization completed.")
        except Exception as e:
            print(f"Error during visualization: {e}")
            raise

    def optimize_supply_chain(self, performance_metrics):
        """
        Optimizes the supply chain based on performance metrics.

        :param performance_metrics: DataFrame - A DataFrame containing performance metrics.
        :return: DataFrame - A DataFrame with optimized supplier recommendations.
        """
        try:
            # Define optimization criteria (example: prioritize quality and cost)
            optimized_suppliers = performance_metrics[
                (performance_metrics['Average Quality Score'] >= 8) & 
                (performance_metrics['Average Cost'] <= performance_metrics['Average Cost'].mean())
            ]

            print("Supply chain optimization completed.")
            return optimized_suppliers
        except Exception as e:
            print(f"Error during supply chain optimization: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    analyzer = SupplierPerformanceAnalyzer('supplier_data.csv')
    performance_metrics = analyzer.analyze_performance()
    analyzer.visualize_performance(performance_metrics)
    optimized_suppliers = analyzer.optimize_supply_chain(performance_metrics)
    print("Optimized Suppliers:\n", optimized_suppliers)
```
