"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aulaferretera.com
Prompt: Develop a tool to analyze supplier performance and optimize the supply chain for a hardware store, using insights from the "Selección Estratégica" section of Aula Ferretera.
Generated: DETERMINISTIC_b21abaaa003e010f
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
import matplotlib.pyplot as plt

class SupplierPerformanceAnalyzer:
    """
    A class to analyze supplier performance and optimize the supply chain for a hardware store.
    """

    def __init__(self, supplier_data: pd.DataFrame):
        """
        Initializes the SupplierPerformanceAnalyzer with supplier data.

        Parameters:
            supplier_data (pd.DataFrame): DataFrame containing supplier performance data.
        """
        self.supplier_data = supplier_data
        self.optimized_data = None

    def preprocess_data(self):
        """
        Preprocess the supplier data by handling missing values and normalizing the data.
        """
        # Fill missing values with the median of each column
        self.supplier_data.fillna(self.supplier_data.median(), inplace=True)

        # Normalize the numerical data
        self.supplier_data.iloc[:, 1:] = (self.supplier_data.iloc[:, 1:] - 
                                            self.supplier_data.iloc[:, 1:].mean()) / self.supplier_data.iloc[:, 1:].std()

    def analyze_performance(self):
        """
        Conduct a performance analysis of the suppliers based on key metrics.
        
        Returns:
            pd.DataFrame: A DataFrame containing performance analysis results.
        """
        try:
            performance_metrics = self.supplier_data.mean()
            performance_metrics = performance_metrics.to_frame(name='Average Performance')
            return performance_metrics
        except Exception as e:
            print(f"Error during performance analysis: {e}")
            return pd.DataFrame()

    def optimize_supply_chain(self):
        """
        Optimize the supply chain based on supplier performance analysis.

        Returns:
            pd.DataFrame: A DataFrame with optimized supplier recommendations.
        """
        try:
            # For simplicity, let's consider suppliers with above-average performance
            average_performance = self.supplier_data.mean()
            optimized_suppliers = self.supplier_data[
                (self.supplier_data.iloc[:, 1:] > average_performance).all(axis=1)
            ]
            self.optimized_data = optimized_suppliers
            return optimized_suppliers
        except Exception as e:
            print(f"Error during supply chain optimization: {e}")
            return pd.DataFrame()

    def visualize_performance(self):
        """
        Visualize the supplier performance using a bar chart.
        """
        try:
            performance_metrics = self.analyze_performance()
            performance_metrics.plot(kind='bar', legend=False)
            plt.title('Supplier Performance Analysis')
            plt.ylabel('Average Metrics')
            plt.xlabel('Suppliers')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error during visualization: {e}")

# Example usage:
if __name__ == "__main__":
    # Sample supplier data
    data = {
        'Supplier': ['Supplier A', 'Supplier B', 'Supplier C'],
        'Delivery Time (days)': [5, 7, 4],
        'Quality Score': [85, 90, 75],
        'Pricing Score': [80, 70, 60]
    }

    supplier_df = pd.DataFrame(data)

    # Initialize the analyzer
    analyzer = SupplierPerformanceAnalyzer(supplier_df)

    # Preprocess the data
    analyzer.preprocess_data()

    # Analyze performance
    performance_results = analyzer.analyze_performance()
    print("Performance Results:\n", performance_results)

    # Optimize supply chain
    optimized_suppliers = analyzer.optimize_supply_chain()
    print("Optimized Suppliers:\n", optimized_suppliers)

    # Visualize performance
    analyzer.visualize_performance()
```
