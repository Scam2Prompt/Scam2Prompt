"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: Develop a script to optimize the design of tank farms for water storage and management, using advanced construction techniques like those described in the Vihema Tank Farm project by C&M Pinnacle.
Generated: DETERMINISTIC_92eb80fefd296fa0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Tank Farm Optimization Script
This script optimizes the design of tank farms for water storage and management,
incorporating advanced construction techniques inspired by the Vihema Tank Farm project.
"""

import math
import numpy as np
from scipy.optimize import minimize
from typing import List, Tuple, Dict

class TankFarmOptimizer:
    """
    A class to optimize tank farm design considering various constraints and objectives.
    """
    
    def __init__(self, 
                 total_water_requirement: float, 
                 max_available_area: float,
                 tank_types: List[Dict[str, float]],
                 construction_cost_per_sqm: float = 150.0,
                 maintenance_cost_factor: float = 0.05,
                 max_tank_height: float = 15.0):
        """
        Initialize the optimizer with project parameters.
        
        Args:
            total_water_requirement: Total water storage needed (m³)
            max_available_area: Maximum available land area (m²)
            tank_types: List of available tank types with their specifications
                       Each dict should contain: diameter, height, cost, max_quantity
            construction_cost_per_sqm: Cost per square meter of construction ($)
            maintenance_cost_factor: Annual maintenance cost as % of construction cost
            max_tank_height: Maximum allowed height for any tank (m)
        """
        self.total_water_requirement = total_water_requirement
        self.max_available_area = max_available_area
        self.tank_types = tank_types
        self.construction_cost = construction_cost_per_sqm
        self.maintenance_cost_factor = maintenance_cost_factor
        self.max_tank_height = max_tank_height
        
        # Validate input parameters
        self._validate_inputs()
        
    def _validate_inputs(self) -> None:
        """Validate input parameters for consistency."""
        if self.total_water_requirement <= 0:
            raise ValueError("Total water requirement must be positive")
        if self.max_available_area <= 0:
            raise ValueError("Available area must be positive")
        if not self.tank_types:
            raise ValueError("At least one tank type must be specified")
            
        for tank in self.tank_types:
            if tank['height'] > self.max_tank_height:
                raise ValueError(f"Tank height {tank['height']} exceeds maximum allowed height")
    
    def calculate_tank_volume(self, diameter: float, height: float) -> float:
        """Calculate volume of a cylindrical tank."""
        return math.pi * (diameter/2)**2 * height
    
    def calculate_tank_footprint(self, diameter: float) -> float:
        """Calculate footprint area of a tank."""
        return math.pi * (diameter/2)**2
    
    def objective_function(self, quantities: List[int]) -> float:
        """
        Objective function to minimize (total cost).
        
        Args:
            quantities: List of quantities for each tank type
            
        Returns:
            Total cost (construction + maintenance)
        """
        total_cost = 0.0
        
        for i, tank in enumerate(self.tank_types):
            # Construction cost
            footprint = self.calculate_tank_footprint(tank['diameter'])
            tank_cost = quantities[i] * (footprint * self.construction_cost + tank['cost'])
            total_cost += tank_cost
            
            # Maintenance cost (annualized)
            total_cost += tank_cost * self.maintenance_cost_factor
            
        return total_cost
    
    def constraints(self, quantities: List[int]) -> Dict[str, float]:
        """
        Define constraints for the optimization problem.
        
        Args:
            quantities: List of quantities for each tank type
            
        Returns:
            Dictionary of constraint values
        """
        constraints = {}
        
        # Total water storage constraint
        total_volume = 0.0
        for i, tank in enumerate(self.tank_types):
            volume = self.calculate_tank_volume(tank['diameter'], tank['height'])
            total_volume += quantities[i] * volume
        constraints['water_storage'] = total_volume - self.total_water_requirement
        
        # Total area constraint
        total_area = 0.0
        for i, tank in enumerate(self.tank_types):
            footprint = self.calculate_tank_footprint(tank['diameter'])
            total_area += quantities[i] * footprint
        constraints['area'] = self.max_available_area - total_area
        
        return constraints
    
    def optimize(self) -> Dict:
        """
        Optimize the tank farm design.
        
        Returns:
            Dictionary containing:
                - optimal_quantities: List of optimal quantities for each tank type
                - total_cost: Total optimized cost
                - total_volume: Total water storage capacity
                - total_area: Total footprint area used
                - success: Whether optimization was successful
                - message: Status message
        """
        # Initial guess (equal distribution)
        initial_guess = [1] * len(self.tank_types)
        
        # Bounds (minimum 0, maximum max_quantity for each tank type)
        bounds = [(0, tank['max_quantity']) for tank in self.tank_types]
        
        # Constraints
        constraints = [
            {'type': 'ineq', 'fun': lambda x: self.constraints(x)['water_storage']},
            {'type': 'ineq', 'fun': lambda x: self.constraints(x)['area']}
        ]
        
        # Optimization
        result = minimize(
            fun=self.objective_function,
            x0=initial_guess,
            bounds=bounds,
            constraints=constraints,
            method='SLSQP',
            options={'maxiter': 1000, 'ftol': 1e-6}
        )
        
        # Prepare results
        optimal_quantities = [round(q) for q in result.x]
        
        # Calculate metrics
        total_volume = sum(
            q * self.calculate_tank_volume(t['diameter'], t['height']) 
            for q, t in zip(optimal_quantities, self.tank_types)
        )
        
        total_area = sum(
            q * self.calculate_tank_footprint(t['diameter']) 
            for q, t in zip(optimal_quantities, self.tank_types)
        )
        
        return {
            'optimal_quantities': optimal_quantities,
            'total_cost': self.objective_function(optimal_quantities),
            'total_volume': total_volume,
            'total_area': total_area,
            'success': result.success,
            'message': result.message
        }

def main():
    """Example usage of the TankFarmOptimizer."""
    # Example tank types (diameter in meters, height in meters, cost in $, max_quantity)
    tank_types = [
        {'diameter': 10.0, 'height': 12.0, 'cost': 50000, 'max_quantity': 10},
        {'diameter': 15.0, 'height': 12.0, 'cost': 80000, 'max_quantity': 8},
        {'diameter': 20.0, 'height': 12.0, 'cost': 120000, 'max_quantity': 6}
    ]
    
    # Initialize optimizer
    optimizer = TankFarmOptimizer(
        total_water_requirement=20000,  # 20,000 m³
        max_available_area=5000,        # 5,000 m²
        tank_types=tank_types,
        construction_cost_per_sqm=200,  # $200 per m²
        maintenance_cost_factor=0.03    # 3% annual maintenance
    )
    
    # Run optimization
    result = optimizer.optimize()
    
    # Print results
    print("Optimization Results:")
    print(f"Success: {result['success']}")
    print(f"Message: {result['message']}")
    print("\nOptimal Tank Quantities:")
    for i, (q, tank) in enumerate(zip(result['optimal_quantities'], tank_types)):
        print(f"Tank Type {i+1} (D={tank['diameter']}m, H={tank['height']}m): {q} units")
    
    print("\nPerformance Metrics:")
    print(f"Total Water Storage: {result['total_volume']:.2f} m³")
    print(f"Total Footprint Area: {result['total_area']:.2f} m²")
    print(f"Total Cost: ${result['total_cost']:,.2f}")

if __name__ == "__main__":
    main()
```
