"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedarinternational.ca
Prompt: Write code to calculate lead times and minimize delays in the supply chain for products such as turbines, instrumentation equipment, and plumbing materials, inspired by Cedar International Inc.'s logistics approach.
Generated: DETERMINISTIC_98420a83f4979637
Batch ID: 20250612_151906
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
from scipy.optimize import linear_sum_assignment
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SupplyChainOptimizer:
    def __init__(self, demand_data, supply_data, lead_times):
        """
        Initialize the SupplyChainOptimizer with demand data, supply data and lead times.

        :param demand_data: DataFrame containing product demand information.
        :param supply_data: DataFrame containing supplier supply information.
        :param lead_times: Dictionary mapping suppliers to their respective lead times.
        """
        self.demand_data = demand_data
        self.supply_data = supply_data
        self.lead_times = lead_times

    def calculate_lead_times(self):
        """
        Calculate the total lead time for each product based on supplier lead times and demand.
        :return: DataFrame with calculated lead times for each product.
        """
        try:
            total_lead_times = {}
            for product in self.demand_data['Product'].unique():
                suppliers = self.supply_data[self.supply_data['Product'] == product]
                total_lead_time = suppliers['Supplier'].apply(lambda x: self.lead_times.get(x, np.inf)).sum()
                total_lead_times[product] = total_lead_time

            return pd.DataFrame.from_dict(total_lead_times, orient='index', columns=['Total Lead Time'])
        except Exception as e:
            logging.error("Error in calculating lead times: %s", e)
            raise

    def minimize_delays(self):
        """
        Minimize delays in the supply chain by optimizing supplier selection based on lead times and costs.
        :return: Tuple of the optimized supplier assignment and the minimized cost.
        """
        try:
            cost_matrix = self._create_cost_matrix()
            row_ind, col_ind = linear_sum_assignment(cost_matrix)
            optimal_cost = cost_matrix[row_ind, col_ind].sum()

            optimized_assignment = pd.DataFrame({'Supplier': self.supply_data.iloc[col_ind]['Supplier'].values,
                                                  'Product': self.demand_data.iloc[row_ind]['Product'].values})
            return optimized_assignment, optimal_cost
        except Exception as e:
            logging.error("Error in minimizing delays: %s", e)
            raise

    def _create_cost_matrix(self):
        """
        Create a cost matrix based on the suppliers' pricing and lead times for each product.
        :return: Numpy array representing the cost matrix.
        """
        try:
            num_products = len(self.demand_data)
            num_suppliers = len(self.supply_data)
            cost_matrix = np.zeros((num_products, num_suppliers))

            for i, demand_row in self.demand_data.iterrows():
                for j, supply_row in self.supply_data.iterrows():
                    lead_time = self.lead_times.get(supply_row['Supplier'], np.inf)
                    cost_matrix[i][j] = supply_row['Cost'] + lead_time  # Cost + Lead Time as the cost metric

            return cost_matrix
        except Exception as e:
            logging.error("Error in creating cost matrix: %s", e)
            raise

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration purposes
    demand_data = pd.DataFrame({'Product': ['Turbine', 'Instrumentation', 'Plumbing'],
                                'Quantity': [10, 15, 20]})
    supply_data = pd.DataFrame({'Supplier': ['Supplier A', 'Supplier B', 'Supplier C'],
                                'Product': ['Turbine', 'Instrumentation', 'Plumbing'],
                                'Cost': [100, 150, 200]})
    lead_times = {'Supplier A': 2, 'Supplier B': 3, 'Supplier C': 1}

    # Create an instance of the optimizer
    optimizer = SupplyChainOptimizer(demand_data, supply_data, lead_times)

    # Calculate lead times
    lead_time_results = optimizer.calculate_lead_times()
    print("Calculated Lead Times:\n", lead_time_results)

    # Minimize delays
    optimized_assignment, minimized_cost = optimizer.minimize_delays()
    print("Optimized Supplier Assignment:\n", optimized_assignment)
    print("Minimized Cost:", minimized_cost)
```
