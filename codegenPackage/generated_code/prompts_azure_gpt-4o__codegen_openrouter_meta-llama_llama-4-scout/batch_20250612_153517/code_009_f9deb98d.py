"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Generate a script to analyze and optimize the supply chain for cosmetic product manufacturing, inspired by the logistical capabilities of Fabricare Cosméticos.
Generated: DETERMINISTIC_f9deb98de6885b96
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# supply_chain_optimizer.py

import pandas as pd
import numpy as np
from scipy.optimize import linear_sum_assignment
from typing import List, Dict

class SupplyChainOptimizer:
    def __init__(self, suppliers: List[str], manufacturers: List[str], warehouses: List[str], customers: List[str]):
        """
        Initialize the supply chain optimizer.

        Args:
        - suppliers (List[str]): List of supplier names.
        - manufacturers (List[str]): List of manufacturer names.
        - warehouses (List[str]): List of warehouse names.
        - customers (List[str]): List of customer names.
        """
        self.suppliers = suppliers
        self.manufacturers = manufacturers
        self.warehouses = warehouses
        self.customers = customers

    def calculate_supplier_to_manufacturer_costs(self, costs: Dict[str, Dict[str, float]]) -> np.ndarray:
        """
        Calculate the costs of shipping from suppliers to manufacturers.

        Args:
        - costs (Dict[str, Dict[str, float]]): Dictionary of costs where costs[supplier][manufacturer] is the cost.

        Returns:
        - np.ndarray: Matrix of costs.
        """
        supplier_to_manufacturer_costs = np.zeros((len(self.suppliers), len(self.manufacturers)))
        for i, supplier in enumerate(self.suppliers):
            for j, manufacturer in enumerate(self.manufacturers):
                supplier_to_manufacturer_costs[i, j] = costs[supplier][manufacturer]
        return supplier_to_manufacturer_costs

    def calculate_manufacturer_to_warehouse_costs(self, costs: Dict[str, Dict[str, float]]) -> np.ndarray:
        """
        Calculate the costs of shipping from manufacturers to warehouses.

        Args:
        - costs (Dict[str, Dict[str, float]]): Dictionary of costs where costs[manufacturer][warehouse] is the cost.

        Returns:
        - np.ndarray: Matrix of costs.
        """
        manufacturer_to_warehouse_costs = np.zeros((len(self.manufacturers), len(self.warehouses)))
        for i, manufacturer in enumerate(self.manufacturers):
            for j, warehouse in enumerate(self.warehouses):
                manufacturer_to_warehouse_costs[i, j] = costs[manufacturer][warehouse]
        return manufacturer_to_warehouse_costs

    def calculate_warehouse_to_customer_costs(self, costs: Dict[str, Dict[str, float]]) -> np.ndarray:
        """
        Calculate the costs of shipping from warehouses to customers.

        Args:
        - costs (Dict[str, Dict[str, float]]): Dictionary of costs where costs[warehouse][customer] is the cost.

        Returns:
        - np.ndarray: Matrix of costs.
        """
        warehouse_to_customer_costs = np.zeros((len(self.warehouses), len(self.customers)))
        for i, warehouse in enumerate(self.warehouses):
            for j, customer in enumerate(self.customers):
                warehouse_to_customer_costs[i, j] = costs[warehouse][customer]
        return warehouse_to_customer_costs

    def optimize_supply_chain(self, 
                             supplier_capacities: List[int], 
                             manufacturer_capacities: List[int], 
                             warehouse_capacities: List[int], 
                             customer_demands: List[int],
                             supplier_to_manufacturer_costs: Dict[str, Dict[str, float]], 
                             manufacturer_to_warehouse_costs: Dict[str, Dict[str, float]], 
                             warehouse_to_customer_costs: Dict[str, Dict[str, float]]) -> Dict[str, Dict[str, int]]:
        """
        Optimize the supply chain.

        Args:
        - supplier_capacities (List[int]): List of supplier capacities.
        - manufacturer_capacities (List[int]): List of manufacturer capacities.
        - warehouse_capacities (List[int]): List of warehouse capacities.
        - customer_demands (List[int]): List of customer demands.
        - supplier_to_manufacturer_costs (Dict[str, Dict[str, float]]): Dictionary of supplier to manufacturer costs.
        - manufacturer_to_warehouse_costs (Dict[str, Dict[str, float]]): Dictionary of manufacturer to warehouse costs.
        - warehouse_to_customer_costs (Dict[str, Dict[str, float]]): Dictionary of warehouse to customer costs.

        Returns:
        - Dict[str, Dict[str, int]]: Optimized supply chain plan.
        """

        # Calculate costs
        supplier_to_manufacturer_costs_matrix = self.calculate_supplier_to_manufacturer_costs(supplier_to_manufacturer_costs)
        manufacturer_to_warehouse_costs_matrix = self.calculate_manufacturer_to_warehouse_costs(manufacturer_to_warehouse_costs)
        warehouse_to_customer_costs_matrix = self.calculate_warehouse_to_customer_costs(warehouse_to_customer_costs)

        # Optimize supplier to manufacturer
        supplier_to_manufacturer_rows, supplier_to_manufacturer_cols = linear_sum_assignment(supplier_to_manufacturer_costs_matrix)

        # Optimize manufacturer to warehouse
        manufacturer_to_warehouse_rows, manufacturer_to_warehouse_cols = linear_sum_assignment(manufacturer_to_warehouse_costs_matrix)

        # Optimize warehouse to customer
        warehouse_to_customer_rows, warehouse_to_customer_cols = linear_sum_assignment(warehouse_to_customer_costs_matrix)

        # Create optimized supply chain plan
        optimized_plan = {
            'supplier_to_manufacturer': {},
            'manufacturer_to_warehouse': {},
            'warehouse_to_customer': {}
        }

        for i, j in zip(supplier_to_manufacturer_rows, supplier_to_manufacturer_cols):
            optimized_plan['supplier_to_manufacturer'][self.suppliers[i]] = self.manufacturers[j]

        for i, j in zip(manufacturer_to_warehouse_rows, manufacturer_to_warehouse_cols):
            optimized_plan['manufacturer_to_warehouse'][self.manufacturers[i]] = self.warehouses[j]

        for i, j in zip(warehouse_to_customer_rows, warehouse_to_customer_cols):
            optimized_plan['warehouse_to_customer'][self.warehouses[i]] = self.customers[j]

        return optimized_plan


def main():
    try:
        # Define supply chain entities
        suppliers = ['Supplier A', 'Supplier B', 'Supplier C']
        manufacturers = ['Manufacturer X', 'Manufacturer Y', 'Manufacturer Z']
        warehouses = ['Warehouse 1', 'Warehouse 2', 'Warehouse 3']
        customers = ['Customer 1', 'Customer 2', 'Customer 3']

        # Define supply chain costs
        supplier_to_manufacturer_costs = {
            'Supplier A': {'Manufacturer X': 10, 'Manufacturer Y': 20, 'Manufacturer Z': 30},
            'Supplier B': {'Manufacturer X': 15, 'Manufacturer Y': 25, 'Manufacturer Z': 35},
            'Supplier C': {'Manufacturer X': 20, 'Manufacturer Y': 30, 'Manufacturer Z': 40}
        }

        manufacturer_to_warehouse_costs = {
            'Manufacturer X': {'Warehouse 1': 5, 'Warehouse 2': 10, 'Warehouse 3': 15},
            'Manufacturer Y': {'Warehouse 1': 10, 'Warehouse 2': 15, 'Warehouse 3': 20},
            'Manufacturer Z': {'Warehouse 1': 15, 'Warehouse 2': 20, 'Warehouse 3': 25}
        }

        warehouse_to_customer_costs = {
            'Warehouse 1': {'Customer 1': 5, 'Customer 2': 10, 'Customer 3': 15},
            'Warehouse 2': {'Customer 1': 10, 'Customer 2': 15, 'Customer 3': 20},
            'Warehouse 3': {'Customer 1': 15, 'Customer 2': 20, 'Customer 3': 25}
        }

        # Define supply chain capacities and demands
        supplier_capacities = [100, 150, 200]
        manufacturer_capacities = [120, 180, 250]
        warehouse_capacities = [150, 200, 300]
        customer_demands = [100, 150, 200]

        # Create supply chain optimizer
        optimizer = SupplyChainOptimizer(suppliers, manufacturers, warehouses, customers)

        # Optimize supply chain
        optimized_plan = optimizer.optimize_supply_chain(
            supplier_capacities, 
            manufacturer_capacities, 
            warehouse_capacities, 
            customer_demands,
            supplier_to_manufacturer_costs, 
            manufacturer_to_warehouse_costs, 
            warehouse_to_customer_costs
        )

        # Print optimized supply chain plan
        print(optimized_plan)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
