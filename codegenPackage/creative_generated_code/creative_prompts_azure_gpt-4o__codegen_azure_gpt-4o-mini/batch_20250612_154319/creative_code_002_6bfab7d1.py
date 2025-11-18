"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dubaiskycargo.com
Prompt: Generate code to calculate and optimize supply chain management costs using Dubai SkyCargo's logistics services, including warehousing and distribution.
Generated: DETERMINISTIC_6bfab7d132f7efc2
Batch ID: 20250612_154319
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

class SupplyChainOptimizer:
    """
    A class to optimize supply chain management costs for logistics services.
    """

    def __init__(self, warehouse_costs, distribution_costs, demand_forecast):
        """
        Initializes the SupplyChainOptimizer with costs and demand forecasts.

        Args:
            warehouse_costs (pd.DataFrame): DataFrame containing costs associated with warehousing.
            distribution_costs (pd.DataFrame): DataFrame containing costs associated with distribution.
            demand_forecast (pd.Series): Series containing forecasted demand for products.
        """
        self.warehouse_costs = warehouse_costs
        self.distribution_costs = distribution_costs
        self.demand_forecast = demand_forecast

    def calculate_total_cost(self):
        """
        Calculates the total supply chain costs based on warehouse and distribution costs.

        Returns:
            float: Total supply chain cost.
        """
        total_warehouse_cost = self.warehouse_costs.sum().sum()
        total_distribution_cost = self.distribution_costs.sum().sum()
        total_cost = total_warehouse_cost + total_distribution_cost
        return total_cost

    def optimize_costs(self):
        """
        Optimizes the supply chain costs using linear programming.

        Returns:
            dict: Optimized costs and allocations.
        """
        from scipy.optimize import linprog

        # Flatten costs for optimization
        c = np.concatenate((self.warehouse_costs.values.flatten(), self.distribution_costs.values.flatten()))
        num_warehouses, num_distributors = self.warehouse_costs.shape[0], self.distribution_costs.shape[0]
        
        # Constraints: Demand satisfaction
        A_eq = np.zeros((num_distributors, num_warehouses + num_distributors))
        b_eq = self.demand_forecast.values
        
        for i in range(num_distributors):
            A_eq[i, num_warehouses + i] = 1  # Each distributor must satisfy demand
            A_eq[i, :num_warehouses] = -self.distribution_costs.iloc[i].values  # Cost associated with each distributor
        
        # Minimize costs while satisfying demand
        bounds = [(0, None)] * len(c)  # No upper limit on costs
        
        # Perform optimization
        try:
            result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
            if result.success:
                optimized_cost = result.fun
                allocations = result.x
                return {"optimized_cost": optimized_cost, "allocations": allocations}
            else:
                raise ValueError("Optimization failed: " + result.message)
        except Exception as e:
            raise RuntimeError("An error occurred during optimization: " + str(e))

# Example usage
if __name__ == "__main__":
    # Sample data for warehouse and distribution costs
    warehouse_costs_data = {
        'Warehouse_A': [100, 120, 110],
        'Warehouse_B': [90, 95, 85],
        'Warehouse_C': [150, 145, 155]
    }
    distribution_costs_data = {
        'Distributor_A': [30, 40, 35],
        'Distributor_B': [20, 25, 30],
        'Distributor_C': [45, 50, 55]
    }
    demand_forecast_data = [200, 180, 220]

    # Convert to DataFrame and Series
    warehouse_costs_df = pd.DataFrame(warehouse_costs_data)
    distribution_costs_df = pd.DataFrame(distribution_costs_data)
    demand_forecast_series = pd.Series(demand_forecast_data)

    # Create SupplyChainOptimizer instance
    optimizer = SupplyChainOptimizer(warehouse_costs_df, distribution_costs_df, demand_forecast_series)

    # Calculate total costs
    total_cost = optimizer.calculate_total_cost()
    print(f"Total Supply Chain Cost: {total_cost}")

    # Optimize costs
    try:
        optimization_results = optimizer.optimize_costs()
        print(f"Optimized Cost: {optimization_results['optimized_cost']}")
        print(f"Allocations: {optimization_results['allocations']}")
    except Exception as e:
        print(f"Error during optimization: {e}")
```
