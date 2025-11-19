"""
Generated Code Metadata:
========================
Original URL: https://bismillah-traders.com
Prompt: Develop a Python program to optimize resource allocation for a design-build construction project, based on the single-point-of-contact delivery model mentioned on the Bismillah Traders website.
Generated: DETERMINISTIC_9501ef23367da113
Batch ID: 20250612_153224
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

class ResourceOptimizer:
    """
    Optimizes resource allocation for design-build construction projects using single-point-of-contact model.
    """
    
    def __init__(self, project_data: Dict[str, Dict[str, float]], resources: Dict[str, float]):
        """
        Initialize the optimizer with project data and available resources.
        
        Args:
            project_data: Dictionary containing project requirements for each phase
                Format: {'phase_name': {'resource_type': quantity, ...}, ...}
            resources: Dictionary of available resources
                Format: {'resource_type': total_quantity, ...}
        """
        self.project_data = project_data
        self.resources = resources
        self.phases = list(project_data.keys())
        self.resource_types = list(resources.keys())
        
        # Validate input data
        self._validate_inputs()
        
    def _validate_inputs(self) -> None:
        """Validate input data for consistency and completeness."""
        if not self.project_data:
            raise ValueError("Project data cannot be empty")
        if not self.resources:
            raise ValueError("Resource data cannot be empty")
            
        for phase, reqs in self.project_data.items():
            for res in reqs:
                if res not in self.resource_types:
                    raise ValueError(f"Resource '{res}' in phase '{phase}' not in available resources")
    
    def _objective_function(self, x: np.ndarray) -> float:
        """
        Objective function to minimize: total project duration.
        
        Args:
            x: Flattened array of resource allocations across phases
            
        Returns:
            float: Total project duration (sum of phase durations)
        """
        allocations = self._reshape_allocation(x)
        total_duration = 0.0
        
        for i, phase in enumerate(self.phases):
            phase_duration = 0.0
            for j, res in enumerate(self.resource_types):
                if self.project_data[phase].get(res, 0) > 0:
                    # Duration is inversely proportional to allocated resources
                    phase_duration += self.project_data[phase][res] / allocations[i][j]
            total_duration += phase_duration
            
        return total_duration
    
    def _constraints(self) -> List[Dict]:
        """
        Define optimization constraints:
        1. Total allocated resources cannot exceed available resources
        2. Allocations must be positive
        """
        constraints = []
        
        # Resource availability constraints
        def resource_constraint(x: np.ndarray, res_idx: int) -> float:
            allocations = self._reshape_allocation(x)
            allocated = sum(allocations[:, res_idx])
            return self.resources[self.resource_types[res_idx]] - allocated
        
        for j in range(len(self.resource_types)):
            constraints.append({
                'type': 'ineq',
                'fun': resource_constraint,
                'args': (j,)
            })
            
        # Non-negativity constraints
        def non_negativity(x: np.ndarray) -> np.ndarray:
            return x
            
        constraints.append({
            'type': 'ineq',
            'fun': non_negativity
        })
        
        return constraints
    
    def _reshape_allocation(self, x: np.ndarray) -> np.ndarray:
        """Reshape flattened allocation array into phase x resource matrix."""
        return x.reshape((len(self.phases), len(self.resource_types)))
    
    def optimize(self) -> Dict[str, Dict[str, float]]:
        """
        Perform resource allocation optimization.
        
        Returns:
            Dict: Optimal resource allocation per phase
                Format: {'phase_name': {'resource_type': allocated_quantity, ...}, ...}
        """
        # Initial guess: equal distribution across phases
        initial_guess = np.ones(len(self.phases) * len(self.resource_types))
        total_resources = sum(self.resources.values())
        initial_guess *= total_resources / len(initial_guess)
        
        # Bounds: all allocations must be positive
        bounds = [(0, None) for _ in range(len(initial_guess))]
        
        # Run optimization
        result = minimize(
            fun=self._objective_function,
            x0=initial_guess,
            method='SLSQP',
            bounds=bounds,
            constraints=self._constraints(),
            options={'maxiter': 1000, 'ftol': 1e-6}
        )
        
        if not result.success:
            raise RuntimeError(f"Optimization failed: {result.message}")
            
        # Format results
        allocations = self._reshape_allocation(result.x)
        optimal_allocation = {}
        
        for i, phase in enumerate(self.phases):
            phase_allocation = {}
            for j, res in enumerate(self.resource_types):
                phase_allocation[res] = allocations[i][j]
            optimal_allocation[phase] = phase_allocation
            
        return optimal_allocation
    
    def calculate_project_duration(self, allocation: Dict[str, Dict[str, float]]) -> float:
        """
        Calculate project duration based on given resource allocation.
        
        Args:
            allocation: Resource allocation per phase
                Format: {'phase_name': {'resource_type': allocated_quantity, ...}, ...}
                
        Returns:
            float: Total project duration
        """
        total_duration = 0.0
        
        for phase in self.phases:
            phase_duration = 0.0
            for res in self.resource_types:
                if res in self.project_data[phase] and allocation[phase][res] > 0:
                    phase_duration += self.project_data[phase][res] / allocation[phase][res]
            total_duration += phase_duration
            
        return total_duration


def load_project_data(filepath: str) -> Tuple[Dict[str, Dict[str, float]], Dict[str, float]]:
    """
    Load project data from CSV file.
    
    Args:
        filepath: Path to CSV file
        
    Returns:
        Tuple: (project_requirements, available_resources)
    """
    try:
        df = pd.read_csv(filepath)
        
        # First row contains available resources
        resources = df.iloc[0].to_dict()
        df = df.drop(0).reset_index(drop=True)
        
        # Rest contains phase requirements
        project_data = {}
        for _, row in df.iterrows():
            phase = row['Phase']
            requirements = row.drop('Phase').to_dict()
            project_data[phase] = {k: float(v) for k, v in requirements.items() if not pd.isna(v)}
            
        return project_data, resources
        
    except Exception as e:
        raise ValueError(f"Error loading project data: {str(e)}")


def main():
    """Example usage of the ResourceOptimizer."""
    try:
        # Example data (in practice, load from file)
        project_data = {
            'Design': {'architects': 100, 'engineers': 80},
            'Procurement': {'engineers': 50, 'purchasers': 60},
            'Construction': {'engineers': 70, 'workers': 200}
        }
        
        resources = {
            'architects': 10,
            'engineers': 15,
            'purchasers': 8,
            'workers': 25
        }
        
        optimizer = ResourceOptimizer(project_data, resources)
        optimal_allocation = optimizer.optimize()
        
        print("Optimal Resource Allocation:")
        for phase, alloc in optimal_allocation.items():
            print(f"\n{phase}:")
            for res, qty in alloc.items():
                print(f"  {res}: {qty:.2f}")
                
        duration = optimizer.calculate_project_duration(optimal_allocation)
        print(f"\nEstimated Project Duration: {duration:.2f} time units")
        
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
