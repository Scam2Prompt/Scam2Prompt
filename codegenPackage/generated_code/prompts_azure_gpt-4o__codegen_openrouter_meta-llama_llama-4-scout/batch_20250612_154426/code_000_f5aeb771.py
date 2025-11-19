"""
Generated Code Metadata:
========================
Original URL: https://itls-iso.com
Prompt: Write Python code to optimize a supply chain process using the iTLS methodology, incorporating elements of TOC, Lean, and Six Sigma as described on the iTLS-ISO website.
Generated: DETERMINISTIC_f5aeb77157f70f9a
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# iTLS Supply Chain Optimizer

import numpy as np
from scipy.optimize import linear_sum_assignment
from typing import List, Dict

class SupplyChainOptimizer:
    """
    Optimizes a supply chain process using the iTLS methodology.
    
    Incorporates elements of TOC, Lean, and Six Sigma.
    """

    def __init__(self, suppliers: List[str], manufacturers: List[str], customers: List[str]):
        """
        Initializes the supply chain optimizer.

        Args:
        - suppliers (List[str]): List of supplier names.
        - manufacturers (List[str]): List of manufacturer names.
        - customers (List[str]): List of customer names.
        """
        self.suppliers = suppliers
        self.manufacturers = manufacturers
        self.customers = customers

    def calculate_supplier_capacity(self, supplier_capacities: Dict[str, int]) -> Dict[str, int]:
        """
        Calculates the available capacity for each supplier.

        Args:
        - supplier_capacities (Dict[str, int]): Dictionary of supplier capacities.

        Returns:
        - Dict[str, int]: Available capacity for each supplier.
        """
        available_capacities = {}
        for supplier, capacity in supplier_capacities.items():
            available_capacities[supplier] = capacity
        return available_capacities

    def calculate_manufacturer_demand(self, manufacturer_demands: Dict[str, int]) -> Dict[str, int]:
        """
        Calculates the demand for each manufacturer.

        Args:
        - manufacturer_demands (Dict[str, int]): Dictionary of manufacturer demands.

        Returns:
        - Dict[str, int]: Demand for each manufacturer.
        """
        demands = {}
        for manufacturer, demand in manufacturer_demands.items():
            demands[manufacturer] = demand
        return demands

    def optimize_supply_chain(self, supplier_capacities: Dict[str, int], manufacturer_demands: Dict[str, int], 
                             transportation_costs: np.ndarray) -> Dict[str, Dict[str, int]]:
        """
        Optimizes the supply chain using the iTLS methodology.

        Args:
        - supplier_capacities (Dict[str, int]): Dictionary of supplier capacities.
        - manufacturer_demands (Dict[str, int]): Dictionary of manufacturer demands.
        - transportation_costs (np.ndarray): 2D array of transportation costs.

        Returns:
        - Dict[str, Dict[str, int]]: Optimized supply chain allocation.
        """
        try:
            # Use the Hungarian Algorithm to find the optimal allocation
            row_ind, col_ind = linear_sum_assignment(transportation_costs)

            # Create a dictionary to store the optimized allocation
            optimized_allocation = {}
            for supplier_idx, manufacturer_idx in zip(row_ind, col_ind):
                supplier = self.suppliers[supplier_idx]
                manufacturer = self.manufacturers[manufacturer_idx]
                if supplier not in optimized_allocation:
                    optimized_allocation[supplier] = {}
                optimized_allocation[supplier][manufacturer] = transportation_costs[supplier_idx, manufacturer_idx]

            # Adjust the allocation based on supplier capacity and manufacturer demand
            available_capacities = self.calculate_supplier_capacity(supplier_capacities)
            demands = self.calculate_manufacturer_demand(manufacturer_demands)
            for supplier, manufacturers in optimized_allocation.items():
                total_allocation = sum(manufacturers.values())
                if total_allocation > available_capacities[supplier]:
                    # Reduce allocation to match available capacity
                    reduction_factor = available_capacities[supplier] / total_allocation
                    for manufacturer, allocation in manufacturers.items():
                        optimized_allocation[supplier][manufacturer] = int(allocation * reduction_factor)

            return optimized_allocation

        except Exception as e:
            print(f"Error optimizing supply chain: {str(e)}")
            return {}

def main():
    # Example usage
    suppliers = ["Supplier A", "Supplier B", "Supplier C"]
    manufacturers = ["Manufacturer X", "Manufacturer Y", "Manufacturer Z"]
    customers = ["Customer 1", "Customer 2", "Customer 3"]

    optimizer = SupplyChainOptimizer(suppliers, manufacturers, customers)

    supplier_capacities = {
        "Supplier A": 100,
        "Supplier B": 150,
        "Supplier C": 200
    }

    manufacturer_demands = {
        "Manufacturer X": 120,
        "Manufacturer Y": 180,
        "Manufacturer Z": 250
    }

    transportation_costs = np.array([
        [10, 20, 30],
        [15, 25, 35],
        [20, 30, 40]
    ])

    optimized_allocation = optimizer.optimize_supply_chain(supplier_capacities, manufacturer_demands, transportation_costs)
    print("Optimized Supply Chain Allocation:")
    for supplier, manufacturers in optimized_allocation.items():
        print(f"{supplier}: {manufacturers}")

if __name__ == "__main__":
    main()
```
