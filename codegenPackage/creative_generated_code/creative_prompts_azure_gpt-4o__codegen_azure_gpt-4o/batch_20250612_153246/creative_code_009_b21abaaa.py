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
"""
Supplier Performance Analysis and Supply Chain Optimization Tool

This script analyzes supplier performance based on key metrics and provides optimization recommendations
for a hardware store's supply chain. It is inspired by the "Selección Estratégica" section of Aula Ferretera.

Requirements:
- Python 3.x
- Pandas and NumPy libraries for data manipulation
- Matplotlib for visualization (optional)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class SupplierPerformanceAnalyzer:
    """
    A class to analyze supplier performance and optimize the supply chain.
    """

    def __init__(self, supplier_data_file):
        """
        Initialize the analyzer with supplier data.

        :param supplier_data_file: Path to the CSV file containing supplier data.
        The file should contain columns: 'Supplier', 'DeliveryTime', 'QualityScore', 'Cost', 'ReliabilityScore'.
        """
        self.supplier_data_file = supplier_data_file
        try:
            self.data = pd.read_csv(supplier_data_file)
        except Exception as e:
            raise ValueError(f"Error reading supplier data file: {str(e)}")
        
        # Validate required columns
        expected_columns = ['Supplier', 'DeliveryTime', 'QualityScore', 'Cost', 'ReliabilityScore']
        missing_columns = [col for col in expected_columns if col not in self.data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns in the data file: {missing_columns}")

    def calculate_performance_scores(self):
        """
        Calculate performance scores for each supplier based on weighted metrics.

        :return: DataFrame with suppliers and their performance scores.
        """
        try:
            # Normalize metrics for consistency
            self.data['NormDeliveryTime'] = 1 / self.data['DeliveryTime']
            self.data['NormQualityScore'] = self.data['QualityScore'] / 100
            self.data['NormReliabilityScore'] = self.data['ReliabilityScore'] / 100
            self.data['NormCost'] = 1 / self.data['Cost']

            # Define weights for each metric
            weights = {
                'NormDeliveryTime': 0.25,  # Delivery time is 25% of the score
                'NormQualityScore': 0.35, # Quality score is 35% of the score
                'NormReliabilityScore': 0.3, # Reliability score is 30% of the score
                'NormCost': 0.1           # Cost is 10% of the score
            }

            # Compute weighted performance score
            self.data['PerformanceScore'] = (
                self.data['NormDeliveryTime'] * weights['NormDeliveryTime'] +
                self.data['NormQualityScore'] * weights['NormQualityScore'] +
                self.data['NormReliabilityScore'] * weights['NormReliabilityScore'] +
                self.data['NormCost'] * weights['NormCost']
            )

            return self.data[['Supplier', 'PerformanceScore']].sort_values(by='PerformanceScore', ascending=False)
        except Exception as e:
            raise RuntimeError(f"Error calculating performance scores: {str(e)}")

    def recommend_suppliers(self, top_n=3):
        """
        Recommend top N suppliers based on performance scores.

        :param top_n: Number of top suppliers to recommend.
        :return: List of recommended suppliers.
        """
        try:
            performance_scores = self.calculate_performance_scores()
            return performance_scores.head(top_n)['Supplier'].tolist()
        except Exception as e:
            raise RuntimeError(f"Error recommending suppliers: {str(e)}")

    def visualize_performance(self):
        """
        Visualize supplier performance scores using a bar chart.

        :return: None
        """
        try:
            performance_scores = self.calculate_performance_scores()
            plt.figure(figsize=(10, 6))
            plt.bar(performance_scores['Supplier'], performance_scores['PerformanceScore'], color='skyblue')
            plt.xlabel('Supplier')
            plt.ylabel('Performance Score')
            plt.title('Supplier Performance Scores')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error visualizing performance: {str(e)}")


if __name__ == "__main__":
    # Example Usage:
    # Replace 'supplier_data.csv' with the path to your CSV file containing supplier data.
    try:
        analyzer = SupplierPerformanceAnalyzer('supplier_data.csv')
        print("Top Suppliers:")
        top_suppliers = analyzer.recommend_suppliers(top_n=5)
        print(top_suppliers)
        
        print("\nVisualizing Supplier Performance...")
        analyzer.visualize_performance()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
