"""
Generated Code Metadata:
========================
Original URL: https://metis-investment.gr
Prompt: Develop a program to optimize the production of high-quality, cost-effective food using energy recovered from waste, based on the approach described by Metis Investment.
Generated: DETERMINISTIC_01ad133f24a3887a
Batch ID: 20250612_153246
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

class WasteToFoodOptimizer:
    """
    Optimizes food production using energy recovered from waste.
    Based on Metis Investment's approach.
    """
    
    def __init__(self, 
                 waste_sources: Dict[str, float], 
                 food_products: Dict[str, Dict[str, float]],
                 energy_conversion_rates: Dict[str, float],
                 constraints: Dict[str, float]):
        """
        Initialize the optimizer with input parameters.
        
        Args:
            waste_sources: Dictionary of waste types and their available quantities (kg)
            food_products: Dictionary of food products and their production requirements
                          Format: {'product': {'energy': float, 'cost': float, 'quality': float}}
            energy_conversion_rates: Dictionary of energy conversion rates for waste types (kWh/kg)
            constraints: Dictionary of constraints (max_cost, min_quality, max_waste_usage)
        """
        self.waste_sources = waste_sources
        self.food_products = food_products
        self.energy_conversion_rates = energy_conversion_rates
        self.constraints = constraints
        
        # Validate inputs
        self._validate_inputs()
        
    def _validate_inputs(self) -> None:
        """Validate input parameters."""
        if not all(isinstance(v, (int, float)) and v > 0 for v in self.waste_sources.values()):
            raise ValueError("Waste quantities must be positive numbers")
            
        if not all(isinstance(prod['energy'], (int, float)) and prod['energy'] > 0 
                   for prod in self.food_products.values()):
            raise ValueError("Food energy requirements must be positive numbers")
            
        if not all(isinstance(rate, (int, float)) and rate > 0 
                   for rate in self.energy_conversion_rates.values()):
            raise ValueError("Energy conversion rates must be positive numbers")
            
        required_constraints = {'max_cost', 'min_quality', 'max_waste_usage'}
        if not required_constraints.issubset(self.constraints.keys()):
            raise ValueError(f"Constraints must include {required_constraints}")
    
    def calculate_energy_production(self, waste_allocation: Dict[str, float]) -> float:
        """
        Calculate total energy produced from waste allocation.
        
        Args:
            waste_allocation: Dictionary of waste types and allocated quantities
            
        Returns:
            Total energy produced in kWh
        """
        return sum(qty * self.energy_conversion_rates[wt] 
                  for wt, qty in waste_allocation.items())
    
    def optimize_production(self) -> Dict[str, float]:
        """
        Optimize food production to maximize quality while meeting constraints.
        
        Returns:
            Dictionary of optimized food product quantities
        """
        # Initial guess (equal distribution)
        initial_guess = np.ones(len(self.food_products)) / len(self.food_products)
        bounds = [(0, None) for _ in range(len(self.food_products))]
        
        # Constraints
        constraints = [
            {'type': 'ineq', 'fun': lambda x: self.constraints['max_cost'] - self._calculate_total_cost(x)},
            {'type': 'ineq', 'fun': lambda x: self._calculate_avg_quality(x) - self.constraints['min_quality']},
            {'type': 'ineq', 'fun': lambda x: self._calculate_waste_usage(x) - self.constraints['max_waste_usage']}
        ]
        
        # Optimization
        result = minimize(
            fun=lambda x: -self._calculate_avg_quality(x),  # Maximize quality
            x0=initial_guess,
            bounds=bounds,
            constraints=constraints,
            method='SLSQP'
        )
        
        if not result.success:
            raise RuntimeError(f"Optimization failed: {result.message}")
            
        return self._format_results(result.x)
    
    def _calculate_total_cost(self, product_mix: np.ndarray) -> float:
        """Calculate total production cost."""
        return sum(qty * self.food_products[prod]['cost'] 
                  for qty, prod in zip(product_mix, self.food_products))
    
    def _calculate_avg_quality(self, product_mix: np.ndarray) -> float:
        """Calculate average quality score."""
        total = sum(product_mix)
        if total == 0:
            return 0
        return sum(qty * self.food_products[prod]['quality'] 
                  for qty, prod in zip(product_mix, self.food_products)) / total
    
    def _calculate_waste_usage(self, product_mix: np.ndarray) -> float:
        """Calculate total waste usage."""
        total_energy = sum(qty * self.food_products[prod]['energy'] 
                          for qty, prod in zip(product_mix, self.food_products))
        
        # Find minimum waste needed to produce this energy
        waste_allocation = {}
        remaining_energy = total_energy
        
        for waste_type in sorted(self.waste_sources, 
                                key=lambda x: self.energy_conversion_rates[x], 
                                reverse=True):
            max_energy = self.waste_sources[waste_type] * self.energy_conversion_rates[waste_type]
            allocated_energy = min(max_energy, remaining_energy)
            allocated_waste = allocated_energy / self.energy_conversion_rates[waste_type]
            
            waste_allocation[waste_type] = allocated_waste
            remaining_energy -= allocated_energy
            
            if remaining_energy <= 0:
                break
                
        if remaining_energy > 0:
            return float('inf')  # Exceeds available waste
        
        return sum(waste_allocation.values())
    
    def _format_results(self, product_mix: np.ndarray) -> Dict[str, float]:
        """Format optimization results into product quantities."""
        return {prod: qty for prod, qty in zip(self.food_products, product_mix)}
    
    def generate_report(self, product_mix: Dict[str, float]) -> str:
        """
        Generate a report of the optimized production plan.
        
        Args:
            product_mix: Dictionary of product quantities
            
        Returns:
            Formatted report string
        """
        total_energy = sum(qty * self.food_products[prod]['energy'] for prod, qty in product_mix.items())
        total_cost = sum(qty * self.food_products[prod]['cost'] for prod, qty in product_mix.items())
        avg_quality = self._calculate_avg_quality(np.array(list(product_mix.values())))
        waste_usage = self._calculate_waste_usage(np.array(list(product_mix.values())))
        
        report = [
            "=== Waste-to-Food Production Optimization Report ===",
            f"Total Energy Required: {total_energy:.2f} kWh",
            f"Total Waste Used: {waste_usage:.2f} kg",
            f"Total Production Cost: ${total_cost:.2f}",
            f"Average Quality Score: {avg_quality:.2f}/10",
            "\nProduction Plan:"
        ]
        
        for product, quantity in product_mix.items():
            report.append(f"- {product}: {quantity:.2f} units")
            
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    # Sample data
    waste_sources = {
        'organic_waste': 1000,  # kg
        'plastic_waste': 500,
        'paper_waste': 300
    }
    
    food_products = {
        'vegetables': {'energy': 5, 'cost': 2, 'quality': 8},
        'grains': {'energy': 3, 'cost': 1, 'quality': 7},
        'dairy': {'energy': 7, 'cost': 3, 'quality': 6}
    }
    
    energy_conversion_rates = {
        'organic_waste': 0.8,  # kWh/kg
        'plastic_waste': 1.2,
        'paper_waste': 0.5
    }
    
    constraints = {
        'max_cost': 2000,  # dollars
        'min_quality': 6.5,  # quality score (1-10)
        'max_waste_usage': 1500  # kg
    }
    
    try:
        optimizer = WasteToFoodOptimizer(waste_sources, food_products, 
                                       energy_conversion_rates, constraints)
        optimal_mix = optimizer.optimize_production()
        print(optimizer.generate_report(optimal_mix))
    except Exception as e:
        print(f"Error: {str(e)}")
```
