"""
Generated Code Metadata:
========================
Original URL: https://dubaiskycargo.com
Prompt: Generate code to calculate and optimize supply chain management costs using Dubai SkyCargo's logistics services, including warehousing and distribution.
Generated: DETERMINISTIC_6bfab7d132f7efc2
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from typing import Dict, List, Tuple, Optional

class SupplyChainOptimizer:
    """
    A class to optimize supply chain costs for Dubai SkyCargo's logistics services.
    Handles warehousing, transportation, and distribution cost optimization.
    """
    
    def __init__(self, 
                 warehouse_costs: Dict[str, float],
                 transport_costs: Dict[str, float],
                 demand_data: pd.DataFrame,
                 capacity_constraints: Dict[str, float]):
        """
        Initialize the optimizer with cost parameters and constraints.
        
        Args:
            warehouse_costs: Dictionary of warehouse costs per unit
            transport_costs: Dictionary of transport costs per unit per route
            demand_data: DataFrame containing demand information
            capacity_constraints: Dictionary of maximum capacities for warehouses
        """
        self.warehouse_costs = warehouse_costs
        self.transport_costs = transport_costs
        self.demand_data = demand_data
        self.capacity_constraints = capacity_constraints
        
        # Validate input data
        self._validate_inputs()
        
    def _validate_inputs(self) -> None:
        """Validate that all inputs are properly formatted and consistent."""
        if not isinstance(self.demand_data, pd.DataFrame):
            raise ValueError("demand_data must be a pandas DataFrame")
            
        if not all(k in self.warehouse_costs for k in self.capacity_constraints):
            raise ValueError("Warehouse costs and capacity constraints must have matching keys")
            
        if len(self.transport_costs) == 0:
            raise ValueError("Transport costs cannot be empty")
    
    def calculate_current_costs(self) -> Dict[str, float]:
        """
        Calculate current supply chain costs without optimization.
        
        Returns:
            Dictionary containing breakdown of current costs
        """
        total_warehousing = sum(
            self.warehouse_costs[wh] * self.demand_data[wh].sum() 
            for wh in self.warehouse_costs
        )
        
        total_transport = sum(
            self.transport_costs[route] * self.demand_data[route].sum()
            for route in self.transport_costs
        )
        
        return {
            'total_cost': total_warehousing + total_transport,
            'warehousing_cost': total_warehousing,
            'transport_cost': total_transport
        }
    
    def _cost_function(self, x: np.ndarray) -> float:
        """
        Objective function for optimization.
        
        Args:
            x: Decision variables array
            
        Returns:
            Total cost to be minimized
        """
        # Reshape x into warehouse allocation matrix
        n_warehouses = len(self.warehouse_costs)
        n_routes = len(self.transport_costs)
        allocations = x[:n_warehouses * n_routes].reshape((n_warehouses, n_routes))
        
        # Calculate warehousing costs
        warehousing_cost = sum(
            self.warehouse_costs[wh] * allocations[i].sum()
            for i, wh in enumerate(self.warehouse_costs)
        )
        
        # Calculate transport costs
        transport_cost = sum(
            self.transport_costs[route] * allocations[:, j].sum()
            for j, route in enumerate(self.transport_costs)
        )
        
        return warehousing_cost + transport_cost
    
    def _constraints(self) -> List[dict]:
        """
        Generate constraints for the optimization problem.
        
        Returns:
            List of constraint dictionaries
        """
        constraints = []
        n_warehouses = len(self.warehouse_costs)
        n_routes = len(self.transport_costs)
        
        # Capacity constraints
        for i, wh in enumerate(self.warehouse_costs):
            def capacity_constraint(x, idx=i):
                allocations = x[:n_warehouses * n_routes].reshape((n_warehouses, n_routes))
                return self.capacity_constraints[wh] - allocations[idx].sum()
            constraints.append({'type': 'ineq', 'fun': capacity_constraint})
        
        # Demand constraints
        for j, route in enumerate(self.transport_costs):
            def demand_constraint(x, idx=j):
                allocations = x[:n_warehouses * n_routes].reshape((n_warehouses, n_routes))
                return allocations[:, idx].sum() - self.demand_data[route].sum()
            constraints.append({'type': 'eq', 'fun': demand_constraint})
        
        return constraints
    
    def optimize(self) -> Dict:
        """
        Optimize the supply chain costs.
        
        Returns:
            Dictionary containing optimization results
        """
        n_warehouses = len(self.warehouse_costs)
        n_routes = len(self.transport_costs)
        
        # Initial guess (equal distribution)
        initial_guess = np.ones(n_warehouses * n_routes)
        
        # Bounds (non-negative allocations)
        bounds = [(0, None) for _ in range(n_warehouses * n_routes)]
        
        # Run optimization
        result = minimize(
            fun=self._cost_function,
            x0=initial_guess,
            method='SLSQP',
            bounds=bounds,
            constraints=self._constraints(),
            options={'maxiter': 1000, 'disp': True}
        )
        
        if not result.success:
            raise RuntimeError(f"Optimization failed: {result.message}")
        
        # Reshape optimal allocations
        optimal_allocations = result.x[:n_warehouses * n_routes].reshape((n_warehouses, n_routes))
        
        # Calculate costs
        optimized_costs = self._cost_function(result.x)
        current_costs = self.calculate_current_costs()['total_cost']
        
        return {
            'status': 'success',
            'optimal_allocations': optimal_allocations,
            'total_cost': optimized_costs,
            'cost_reduction': current_costs - optimized_costs,
            'reduction_percentage': (current_costs - optimized_costs) / current_costs * 100,
            'iterations': result.nit,
            'message': result.message
        }

# Example usage
if __name__ == "__main__":
    # Sample data
    warehouse_costs = {
        'DXB_Hub': 5.2,
        'Jebel_Ali': 4.8,
        'Dubai_South': 5.0
    }
    
    transport_costs = {
        'Middle_East': 2.5,
        'Europe': 3.8,
        'Asia': 3.2,
        'Africa': 3.5
    }
    
    demand_data = pd.DataFrame({
        'Middle_East': [100, 120, 110],
        'Europe': [200, 180, 220],
        'Asia': [150, 170, 160],
        'Africa': [80, 90, 85]
    })
    
    capacity_constraints = {
        'DXB_Hub': 500,
        'Jebel_Ali': 600,
        'Dubai_South': 550
    }
    
    # Create and run optimizer
    optimizer = SupplyChainOptimizer(
        warehouse_costs=warehouse_costs,
        transport_costs=transport_costs,
        demand_data=demand_data,
        capacity_constraints=capacity_constraints
    )
    
    # Calculate current costs
    current_costs = optimizer.calculate_current_costs()
    print("Current Costs:", current_costs)
    
    # Run optimization
    try:
        results = optimizer.optimize()
        print("\nOptimization Results:")
        for key, value in results.items():
            if key != 'optimal_allocations':
                print(f"{key}: {value}")
    except Exception as e:
        print(f"Optimization error: {str(e)}")
```
