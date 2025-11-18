"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Generate a script to analyze and optimize the supply chain for cosmetic product manufacturing, inspired by the logistical capabilities of Fabricare Cosméticos.
Generated: DETERMINISTIC_f9deb98de6885b96
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Supply Chain Optimization Script for Cosmetic Product Manufacturing
Inspired by Fabricare Cosméticos

This script analyzes and optimizes the supply chain for cosmetic product manufacturing.
It identifies bottlenecks, calculates costs, optimizes inventory levels, and offers insights
into improving efficiency using historical data and predictive analytics.
"""

import pandas as pd
import numpy as np
from scipy.optimize import minimize

# Constants for supply chain calculation
MAX_STORAGE_CAPACITY = 10000  # Maximum units that can be stored
SAFETY_STOCK_PERCENTAGE = 0.15  # 15% safety stock to account for uncertainties
PRODUCTION_COST_PER_UNIT = 5.0  # Production cost per unit in USD
STORAGE_COST_PER_UNIT = 0.5  # Storage cost per unit per month in USD
TRANSPORTATION_COST_PER_UNIT = 1.0  # Transportation cost per unit in USD

def load_supply_chain_data(file_path):
    """
    Load supply chain data from a CSV file.
    The data should include columns: 'product', 'demand', 'production_cost',
    'storage_cost', 'transportation_cost', and 'lead_time'.
    
    :param file_path: Path to the CSV file
    :return: DataFrame containing supply chain data
    """
    try:
        data = pd.read_csv(file_path)
        # Validate required columns
        required_columns = {'product', 'demand', 'production_cost', 
                            'storage_cost', 'transportation_cost', 'lead_time'}
        if not required_columns.issubset(data.columns):
            raise ValueError("CSV file missing required columns.")
        return data
    except Exception as e:
        print(f"Error loading supply chain data: {e}")
        raise


def calculate_optimal_inventory(demand, lead_time, safety_stock_percentage):
    """
    Calculate optimal inventory levels based on demand, lead time, and safety stock.

    :param demand: Monthly demand for the product
    :param lead_time: Lead time in months
    :param safety_stock_percentage: Safety stock percentage (e.g., 0.15 for 15%)
    :return: Optimal inventory level
    """
    average_demand = np.mean(demand)
    safety_stock = safety_stock_percentage * average_demand
    reorder_point = average_demand * lead_time + safety_stock
    return reorder_point


def optimize_costs(data):
    """
    Optimize production, storage, and transportation costs.

    :param data: DataFrame containing supply chain data
    :return: Optimized costs and suggested inventory levels
    """
    results = []
    for _, row in data.iterrows():
        product = row['product']
        demand = row['demand']
        production_cost = row['production_cost']
        storage_cost = row['storage_cost']
        transportation_cost = row['transportation_cost']
        lead_time = row['lead_time']
        
        # Calculate optimal inventory level
        optimal_inventory = calculate_optimal_inventory([demand], lead_time, SAFETY_STOCK_PERCENTAGE)
        
        # Objective function: Minimize total cost
        def total_cost(inventory_level):
            total_storage_cost = inventory_level * storage_cost
            total_transportation_cost = inventory_level * transportation_cost
            total_production_cost = production_cost * demand
            return total_storage_cost + total_transportation_cost + total_production_cost
        
        # Constraint: Inventory level must not exceed max storage capacity
        constraints = [{'type': 'ineq', 'fun': lambda x: MAX_STORAGE_CAPACITY - x}]
        
        # Initial guess for inventory level
        initial_guess = optimal_inventory
        
        # Perform optimization
        result = minimize(total_cost, initial_guess, constraints=constraints)
        
        # Store results
        results.append({
            'product': product,
            'optimal_inventory': result.x[0],
            'total_cost': result.fun
        })
    
    return pd.DataFrame(results)


def main():
    """
    Main function to execute the supply chain analysis and optimization.
    """
    try:
        # Load supply chain data
        file_path = 'supply_chain_data.csv'  # Replace with actual file path
        data = load_supply_chain_data(file_path)
        
        # Perform optimization
        optimized_results = optimize_costs(data)
        
        # Save results to a CSV file
        optimized_results.to_csv('optimized_supply_chain.csv', index=False)
        print("Optimization completed successfully. Results saved to 'optimized_supply_chain.csv'.")
    except Exception as e:
        print(f"An error occurred during execution: {e}")


if __name__ == '__main__':
    main()
```
