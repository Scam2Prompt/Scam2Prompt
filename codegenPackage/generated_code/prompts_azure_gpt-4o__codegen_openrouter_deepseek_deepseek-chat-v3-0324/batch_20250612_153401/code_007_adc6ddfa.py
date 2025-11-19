"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: Suggest a library or API for optimizing construction material usage and demonstrate how to use it to minimize waste while meeting project requirements, as emphasized by INARO S.A.S.
Generated: DETERMINISTIC_adc6ddfae8ebca65
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.optimize import minimize

class MaterialOptimizer:
    """
    A class to optimize construction material usage to minimize waste while meeting project requirements.
    Uses linear programming to find the optimal material combination.
    """
    
    def __init__(self, materials, requirements):
        """
        Initialize the optimizer with available materials and project requirements.
        
        Args:
            materials (dict): Dictionary of available materials with their properties.
                Format: {'material_name': {'cost': float, 'strength': float, 'quantity': float}}
            requirements (dict): Project requirements including minimum strength and total quantity needed.
                Format: {'min_strength': float, 'total_quantity': float}
        """
        self.materials = materials
        self.requirements = requirements
        self.material_names = list(materials.keys())
        
    def objective_function(self, x):
        """
        Objective function to minimize (total cost of materials used).
        
        Args:
            x (numpy.array): Array of quantities for each material.
            
        Returns:
            float: Total cost of materials.
        """
        total_cost = 0
        for i, material in enumerate(self.material_names):
            total_cost += self.materials[material]['cost'] * x[i]
        return total_cost
    
    def strength_constraint(self, x):
        """
        Constraint function to ensure minimum strength requirement is met.
        
        Args:
            x (numpy.array): Array of quantities for each material.
            
        Returns:
            float: Difference between achieved strength and required strength.
        """
        total_strength = 0
        total_quantity = sum(x)
        
        if total_quantity == 0:
            return -self.requirements['min_strength']
            
        for i, material in enumerate(self.material_names):
            total_strength += self.materials[material]['strength'] * x[i]
        
        avg_strength = total_strength / total_quantity
        return avg_strength - self.requirements['min_strength']
    
    def quantity_constraint(self, x):
        """
        Constraint function to ensure total quantity requirement is met.
        
        Args:
            x (numpy.array): Array of quantities for each material.
            
        Returns:
            float: Difference between total quantity used and required quantity.
        """
        return sum(x) - self.requirements['total_quantity']
    
    def availability_constraint(self, x):
        """
        Constraint function to ensure material usage doesn't exceed available quantities.
        
        Args:
            x (numpy.array): Array of quantities for each material.
            
        Returns:
            numpy.array: Array of differences between available and used quantities.
        """
        constraints = []
        for i, material in enumerate(self.material_names):
            constraints.append(self.materials[material]['quantity'] - x[i])
        return np.array(constraints)
    
    def optimize(self):
        """
        Perform the optimization to find the material combination that minimizes cost
        while meeting all requirements.
        
        Returns:
            dict: Optimal material quantities and total cost.
                Format: {'materials': {material_name: quantity}, 'total_cost': float}
        """
        # Initial guess (equal distribution)
        x0 = np.array([self.requirements['total_quantity'] / len(self.material_names)] * len(self.material_names))
        
        # Bounds (each material quantity must be >= 0)
        bounds = [(0, None) for _ in range(len(self.material_names))]
        
        # Constraints
        constraints = [
            {'type': 'ineq', 'fun': self.strength_constraint},
            {'type': 'eq', 'fun': self.quantity_constraint},
            {'type': 'ineq', 'fun': self.availability_constraint}
        ]
        
        # Optimization
        result = minimize(
            self.objective_function,
            x0,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints,
            options={'disp': True}
        )
        
        if not result.success:
            raise ValueError("Optimization failed: " + result.message)
        
        # Prepare results
        optimized_quantities = {}
        for i, material in enumerate(self.material_names):
            optimized_quantities[material] = max(0, result.x[i])  # Ensure no negative quantities
            
        return {
            'materials': optimized_quantities,
            'total_cost': result.fun
        }

# Example usage
if __name__ == "__main__":
    # Define available materials
    materials = {
        'concrete_30MPa': {'cost': 150, 'strength': 30, 'quantity': 1000},
        'concrete_40MPa': {'cost': 200, 'strength': 40, 'quantity': 800},
        'steel_rebar': {'cost': 500, 'strength': 500, 'quantity': 200}
    }
    
    # Define project requirements
    requirements = {
        'min_strength': 35,  # MPa
        'total_quantity': 500  # cubic meters
    }
    
    try:
        optimizer = MaterialOptimizer(materials, requirements)
        result = optimizer.optimize()
        
        print("Optimal Material Usage:")
        for material, quantity in result['materials'].items():
            print(f"- {material}: {quantity:.2f} units")
        print(f"Total Cost: ${result['total_cost']:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
