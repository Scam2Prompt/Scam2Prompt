"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binqutab.ae
Prompt: Develop a script to optimize supply chain management for FMCG and industrial clients, leveraging Bin Qutab Logistics' expertise in pre-shipment planning and execution.
Generated: DETERMINISTIC_2423709d5b853b71
Batch ID: 20250612_152235
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
from datetime import datetime
from typing import List, Dict

class SupplyChainOptimizer:
    def __init__(self, data: pd.DataFrame):
        """
        Initializes the SupplyChainOptimizer with provided data.
        
        :param data: A DataFrame containing supply chain data including 
                     product, demand, lead time, and other relevant metrics.
        """
        self.data = data

    def preprocess_data(self) -> None:
        """
        Preprocess the input data to handle missing values and convert data types.
        """
        # Fill missing values with median for numerical columns
        for column in self.data.select_dtypes(include=[np.number]).columns:
            self.data[column].fillna(self.data[column].median(), inplace=True)
        
        # Drop rows with missing categorical data
        self.data.dropna(subset=['product_category'], inplace=True)

    def calculate_optimal_inventory(self) -> pd.DataFrame:
        """
        Calculate optimal inventory levels based on demand and lead time.
        
        :return: DataFrame with product and optimal inventory levels.
        """
        # Assuming demand is in units and lead time in days
        self.data['optimal_inventory'] = self.data['demand_per_day'] * self.data['lead_time'] + self.data['safety_stock']
        
        return self.data[['product_id', 'optimal_inventory']]

    def generate_shipment_planning(self, optimal_inventory: pd.DataFrame) -> List[Dict]:
        """
        Generate a shipment plan based on optimal inventory levels.
        
        :param optimal_inventory: DataFrame with optimal inventory levels calculated.
        :return: List of shipment plans with estimated shipping dates.
        """
        shipment_plan = []
        today = datetime.now()

        for _, row in optimal_inventory.iterrows():
            shipment_date = today + pd.Timedelta(days=row['lead_time'])
            shipment_plan.append({
                'product_id': row['product_id'],
                'optimal_inventory': row['optimal_inventory'],
                'shipment_date': shipment_date.strftime('%Y-%m-%d')
            })

        return shipment_plan

    def optimize_supply_chain(self) -> List[Dict]:
        """
        Main method to optimize the supply chain.

        :return: Final shipment plan.
        """
        try:
            self.preprocess_data()
            optimal_inventory = self.calculate_optimal_inventory()
            shipment_plan = self.generate_shipment_planning(optimal_inventory)
            return shipment_plan
        except Exception as e:
            print(f"An error occurred during supply chain optimization: {e}")
            return []

# Example usage:
if __name__ == "__main__":
    # Sample data for demonstration
    data = {
        'product_id': [101, 102, 103],
        'demand_per_day': [50, 20, 30],
        'lead_time': [10, 5, 7],
        'safety_stock': [100, 50, 70],
        'product_category': ['FMCG', 'Industrial', 'FMCG']
    }

    df = pd.DataFrame(data)

    optimizer = SupplyChainOptimizer(df)
    shipment_plan = optimizer.optimize_supply_chain()
    
    print(shipment_plan)
```
