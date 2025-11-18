"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedarinternational.ca
Prompt: Develop a logistics optimization algorithm for seamless transportation of construction materials and oil field electricals, leveraging Cedar International Inc.'s global distribution network.
Generated: DETERMINISTIC_615e0b6defaab457
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
from scipy.optimize import linear_sum_assignment
import logging

# Set up logging for debugging and tracking
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class LogisticsOptimizer:
    """A class to optimize logistics for transportation of construction materials and oil field electricals."""
    
    def __init__(self, distance_matrix, supply, demand):
        """
        Initializes the optimizer with a distance matrix, supply, and demand.
        
        :param distance_matrix: 2D array representing distances between each supply and demand point.
        :param supply: List representing the supply available at each location.
        :param demand: List representing the demand needed at each location.
        """
        self.distance_matrix = np.array(distance_matrix)
        self.supply = np.array(supply)
        self.demand = np.array(demand)

        if len(supply) != self.distance_matrix.shape[0] or len(demand) != self.distance_matrix.shape[1]:
            raise ValueError("Supply and demand dimensions must match distance matrix dimensions.")

    def optimize_transportation(self):
        """
        Optimize the transportation using the Hungarian algorithm (linear sum assignment).
        
        :return: Tuple containing the optimal assignments and the total cost.
        """
        try:
            # Create a cost matrix where we assign infinity to non-assignable cells
            cost_matrix = self.create_cost_matrix()
            row_ind, col_ind = linear_sum_assignment(cost_matrix)
            total_cost = cost_matrix[row_ind, col_ind].sum()
            
            logging.debug(f"Optimal assignments: {list(zip(row_ind, col_ind))}")
            logging.info(f"Total transportation cost: {total_cost}")
            return list(zip(row_ind, col_ind)), total_cost
        
        except Exception as e:
            logging.error(f"An error occurred during optimization: {e}")
            raise

    def create_cost_matrix(self):
        """
        Create a cost matrix based on the distance matrix and current supply/demand levels.
        
        :return: A numpy array representing the cost of transporting goods between supply and demand points.
        """
        # Initialize the cost matrix with infinite values for unsatisfiable constraints
        cost_matrix = np.full(self.distance_matrix.shape, np.inf)
        
        for i in range(len(self.supply)):
            for j in range(len(self.demand)):
                # Assign cost only if supply and demand allows
                if self.supply[i] > 0 and self.demand[j] > 0:
                    cost_matrix[i, j] = self.distance_matrix[i, j]
        
        return cost_matrix

def main():
    """Main function to execute the logistics optimization."""
    try:
        # Example distance matrix (for illustration; should be replaced with actual data)
        distance_matrix = [
            [10, 15, 20],
            [10, 30, 25],
            [30, 20, 10]
        ]
        
        # Example supply and demand
        supply = [50, 60, 70]  # Supply at each location
        demand = [30, 40, 110]  # Demand at each location
        
        # Create an instance of the optimizer
        optimizer = LogisticsOptimizer(distance_matrix, supply, demand)
        
        # Run the optimization
        assignments, total_cost = optimizer.optimize_transportation()
        
        # Print results
        print("Optimal Assignments (supply index, demand index):", assignments)
        print("Total Transportation Cost:", total_cost)

    except Exception as e:
        logging.error(f"Error in main execution: {e}")

if __name__ == "__main__":
    main()
```
