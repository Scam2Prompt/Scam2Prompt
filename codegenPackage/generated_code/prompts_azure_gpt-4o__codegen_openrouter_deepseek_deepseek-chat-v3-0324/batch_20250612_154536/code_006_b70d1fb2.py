"""
Generated Code Metadata:
========================
Original URL: https://metamask.raymasterbatch.com
Prompt: Develop a program to optimize pigment dispersion for automotive applications, using concepts from Ray Colors' nano masterbatch solutions.
Generated: DETERMINISTIC_b70d1fb239896919
Batch ID: 20250612_154536
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
from typing import List, Tuple, Dict, Optional
import matplotlib.pyplot as plt
from enum import Enum

class PigmentType(Enum):
    """Enumeration of pigment types for automotive applications."""
    ORGANIC = 1
    INORGANIC = 2
    METALLIC = 3
    PEARLESCENT = 4

class DispersionOptimizer:
    """
    A class to optimize pigment dispersion for automotive applications
    using concepts from nano masterbatch solutions.
    """
    
    def __init__(self, pigment_type: PigmentType, target_color: np.ndarray, 
                 constraints: Dict[str, Tuple[float, float]]):
        """
        Initialize the dispersion optimizer.
        
        Args:
            pigment_type: Type of pigment (from PigmentType enum)
            target_color: Target color as RGB values (0-1 range)
            constraints: Dictionary of constraints with min/max values
                        (e.g., {'viscosity': (0.5, 1.5), 'particle_size': (0.01, 0.1)})
        """
        self.pigment_type = pigment_type
        self.target_color = target_color
        self.constraints = constraints
        
        # Default parameters based on pigment type
        self._set_default_parameters()
        
    def _set_default_parameters(self):
        """Set default parameters based on pigment type."""
        self.params = {
            'concentration': 0.05,
            'mixing_time': 120,
            'temperature': 25,
            'shear_rate': 1000
        }
        
        if self.pigment_type == PigmentType.ORGANIC:
            self.params.update({
                'particle_size': 0.05,
                'dispersant_ratio': 0.1
            })
        elif self.pigment_type == PigmentType.INORGANIC:
            self.params.update({
                'particle_size': 0.1,
                'dispersant_ratio': 0.15
            })
        elif self.pigment_type == PigmentType.METALLIC:
            self.params.update({
                'particle_size': 0.2,
                'dispersant_ratio': 0.2
            })
        elif self.pigment_type == PigmentType.PEARLESCENT:
            self.params.update({
                'particle_size': 0.15,
                'dispersant_ratio': 0.25
            })
    
    def _color_model(self, x: np.ndarray) -> np.ndarray:
        """
        Simplified color model that predicts resulting color based on parameters.
        
        Args:
            x: Array of parameters [concentration, particle_size, dispersant_ratio]
            
        Returns:
            Predicted RGB color (0-1 range)
        """
        concentration, particle_size, dispersant_ratio = x
        
        # Base color effect based on pigment type
        if self.pigment_type == PigmentType.ORGANIC:
            base_effect = np.array([0.8, 0.2, 0.1])
        elif self.pigment_type == PigmentType.INORGANIC:
            base_effect = np.array([0.1, 0.7, 0.2])
        elif self.pigment_type == PigmentType.METALLIC:
            base_effect = np.array([0.3, 0.3, 0.9])
        elif self.pigment_type == PigmentType.PEARLESCENT:
            base_effect = np.array([0.5, 0.5, 0.5])
        
        # Simplified model accounting for parameters
        r = base_effect[0] * concentration * (1 - particle_size) * (1 + dispersant_ratio)
        g = base_effect[1] * concentration * (1 - particle_size) * (1 + dispersant_ratio)
        b = base_effect[2] * concentration * (1 - particle_size) * (1 + dispersant_ratio)
        
        return np.clip(np.array([r, g, b]), 0, 1)
    
    def _objective_function(self, x: np.ndarray) -> float:
        """
        Objective function to minimize - difference between target and predicted color.
        
        Args:
            x: Array of parameters [concentration, particle_size, dispersant_ratio]
            
        Returns:
            Color difference metric (Euclidean distance)
        """
        predicted_color = self._color_model(x)
        return np.linalg.norm(predicted_color - self.target_color)
    
    def _constraint_functions(self) -> List[dict]:
        """Generate constraint functions for the optimization problem."""
        constraints = []
        
        # Concentration constraint
        if 'concentration' in self.constraints:
            min_c, max_c = self.constraints['concentration']
            constraints.append({
                'type': 'ineq',
                'fun': lambda x: x[0] - min_c
            })
            constraints.append({
                'type': 'ineq',
                'fun': lambda x: max_c - x[0]
            })
        
        # Particle size constraint
        if 'particle_size' in self.constraints:
            min_p, max_p = self.constraints['particle_size']
            constraints.append({
                'type': 'ineq',
                'fun': lambda x: x[1] - min_p
            })
            constraints.append({
                'type': 'ineq',
                'fun': lambda x: max_p - x[1]
            })
        
        # Dispersant ratio constraint
        if 'dispersant_ratio' in self.constraints:
            min_d, max_d = self.constraints['dispersant_ratio']
            constraints.append({
                'type': 'ineq',
                'fun': lambda x: x[2] - min_d
            })
            constraints.append({
                'type': 'ineq',
                'fun': lambda x: max_d - x[2]
            })
            
        return constraints
    
    def optimize(self, max_iterations: int = 100) -> Dict[str, float]:
        """
        Optimize pigment dispersion parameters.
        
        Args:
            max_iterations: Maximum number of iterations for optimization
            
        Returns:
            Dictionary of optimized parameters
        """
        # Initial guess
        x0 = np.array([
            self.params['concentration'],
            self.params['particle_size'],
            self.params['dispersant_ratio']
        ])
        
        # Constraints
        constraints = self._constraint_functions()
        
        # Bounds (0-1 for all parameters)
        bounds = [(0.001, 1), (0.001, 1), (0.001, 1)]
        
        # Optimization
        result = minimize(
            self._objective_function,
            x0,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints,
            options={'maxiter': max_iterations}
        )
        
        if not result.success:
            raise RuntimeError(f"Optimization failed: {result.message}")
        
        # Return optimized parameters
        optimized_params = {
            'concentration': result.x[0],
            'particle_size': result.x[1],
            'dispersant_ratio': result.x[2],
            'color_difference': result.fun,
            'iterations': result.nit
        }
        
        return optimized_params
    
    def visualize_optimization(self, optimized_params: Dict[str, float]):
        """
        Visualize the optimization results.
        
        Args:
            optimized_params: Dictionary of optimized parameters
        """
        fig, ax = plt.subplots(1, 2, figsize=(12, 5))
        
        # Color comparison
        original_color = self._color_model(np.array([
            self.params['concentration'],
            self.params['particle_size'],
            self.params['dispersant_ratio']
        ]))
        
        optimized_color = self._color_model(np.array([
            optimized_params['concentration'],
            optimized_params['particle_size'],
            optimized_params['dispersant_ratio']
        ]))
        
        colors = [original_color, optimized_color, self.target_color]
        labels = ['Original', 'Optimized', 'Target']
        
        for i, (color, label) in enumerate(zip(colors, labels)):
            ax[0].bar(i, 1, color=color, label=label)
            ax[0].text(i, 0.5, f"{color.round(2)}", ha='center', va='center')
        
        ax[0].set_xticks(range(3))
        ax[0].set_xticklabels(labels)
        ax[0].set_title('Color Comparison')
        ax[0].legend()
        
        # Parameter comparison
        params = ['concentration', 'particle_size', 'dispersant_ratio']
        original_values = [self.params[p] for p in params]
        optimized_values = [optimized_params[p] for p in params]
        
        x = np.arange(len(params))
        width = 0.35
        
        ax[1].bar(x - width/2, original_values, width, label='Original')
        ax[1].bar(x + width/2, optimized_values, width, label
