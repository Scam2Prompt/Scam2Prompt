"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: "Develop a comparison tool in Python for evaluating different shading solutions like roller shutters and Venetian blinds, considering factors such as UV protection and energy efficiency."
Generated: DETERMINISTIC_b7d8318dbff45234
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import Dict, List, Tuple, Optional

class ShadingSolution:
    """Class representing a shading solution with its properties."""
    
    def __init__(self, name: str, uv_protection: float, energy_efficiency: float, 
                 cost: float, maintenance: float, light_control: float):
        """
        Initialize a shading solution with its properties.
        
        Args:
            name: Name of the shading solution
            uv_protection: UV protection rating (0-1)
            energy_efficiency: Energy efficiency rating (0-1)
            cost: Cost rating (1-10, 1 being cheapest)
            maintenance: Maintenance rating (1-10, 1 being lowest maintenance)
            light_control: Light control rating (0-1)
        """
        self.name = name
        self.uv_protection = uv_protection
        self.energy_efficiency = energy_efficiency
        self.cost = cost
        self.maintenance = maintenance
        self.light_control = light_control
        
    def to_dict(self) -> Dict:
        """Convert the shading solution properties to a dictionary."""
        return {
            'Name': self.name,
            'UV Protection': self.uv_protection,
            'Energy Efficiency': self.energy_efficiency,
            'Cost': self.cost,
            'Maintenance': self.maintenance,
            'Light Control': self.light_control
        }

class ShadingComparisonTool:
    """Tool for comparing different shading solutions."""
    
    def __init__(self):
        """Initialize the comparison tool with an empty list of solutions."""
        self.solutions = []
        
    def add_solution(self, solution: ShadingSolution) -> None:
        """Add a shading solution to the comparison tool.
        
        Args:
            solution: ShadingSolution object to add
        """
        self.solutions.append(solution)
        
    def compare_all(self, weights: Optional[Dict[str, float]] = None) -> pd.DataFrame:
        """
        Compare all shading solutions based on weighted criteria.
        
        Args:
            weights: Dictionary of weights for each criterion. If None, uses equal weights.
                    Expected keys: 'uv_protection', 'energy_efficiency', 'cost',
                    'maintenance', 'light_control'
                    
        Returns:
            DataFrame with comparison results and total scores
        """
        if not self.solutions:
            raise ValueError("No shading solutions added for comparison.")
            
        default_weights = {
            'uv_protection': 0.2,
            'energy_efficiency': 0.2,
            'cost': 0.2,
            'maintenance': 0.2,
            'light_control': 0.2
        }
        
        weights = weights or default_weights
        
        # Validate weights
        if not all(0 <= weight <= 1 for weight in weights.values()):
            raise ValueError("All weights must be between 0 and 1.")
            
        if not abs(sum(weights.values()) - 1.0) < 0.0001:
            raise ValueError("Weights must sum to 1.")
            
        # Prepare data
        data = [sol.to_dict() for sol in self.solutions]
        df = pd.DataFrame(data)
        
        # Normalize cost and maintenance (lower is better)
        df['Cost_Normalized'] = 1 - (df['Cost'] - df['Cost'].min()) / (df['Cost'].max() - df['Cost'].min())
        df['Maintenance_Normalized'] = 1 - (df['Maintenance'] - df['Maintenance'].min()) / (df['Maintenance'].max() - df['Maintenance'].min())
        
        # Calculate weighted score
        df['Score'] = (
            df['UV Protection'] * weights['uv_protection'] +
            df['Energy Efficiency'] * weights['energy_efficiency'] +
            df['Cost_Normalized'] * weights['cost'] +
            df['Maintenance_Normalized'] * weights['maintenance'] +
            df['Light Control'] * weights['light_control']
        )
        
        # Sort by score
        df = df.sort_values('Score', ascending=False)
        
        return df
    
    def compare_pair(self, solution1: str, solution2: str) -> Tuple[Dict, Dict]:
        """
        Compare two shading solutions by name.
        
        Args:
            solution1: Name of first solution to compare
            solution2: Name of second solution to compare
            
        Returns:
            Tuple of dictionaries with the properties of each solution
        """
        sol1 = next((sol for sol in self.solutions if sol.name == solution1), None)
        sol2 = next((sol for sol in self.solutions if sol.name == solution2), None)
        
        if not sol1 or not sol2:
            raise ValueError("One or both solutions not found.")
            
        return sol1.to_dict(), sol2.to_dict()

def example_usage():
    """Example usage of the ShadingComparisonTool."""
    tool = ShadingComparisonTool()
    
    # Add some example shading solutions
    tool.add_solution(ShadingSolution(
        "Roller Shutters",
        uv_protection=0.9,
        energy_efficiency=0.8,
        cost=6,
        maintenance=3,
        light_control=0.7
    ))
    
    tool.add_solution(ShadingSolution(
        "Venetian Blinds",
        uv_protection=0.7,
        energy_efficiency=0.6,
        cost=4,
        maintenance=5,
        light_control=0.9
    ))
    
    tool.add_solution(ShadingSolution(
        "Solar Shades",
        uv_protection=0.95,
        energy_efficiency=0.9,
        cost=8,
        maintenance=4,
        light_control=0.6
    ))
    
    # Compare all with default weights
    print("Comparison with equal weights:")
    print(tool.compare_all())
    
    # Compare with custom weights (prioritize UV protection and energy efficiency)
    custom_weights = {
        'uv_protection': 0.3,
        'energy_efficiency': 0.3,
        'cost': 0.1,
        'maintenance': 0.1,
        'light_control': 0.2
    }
    print("\nComparison with custom weights:")
    print(tool.compare_all(custom_weights))
    
    # Compare two specific solutions
    print("\nPair comparison:")
    sol1, sol2 = tool.compare_pair("Roller Shutters", "Venetian Blinds")
    print("Roller Shutters:", sol1)
    print("Venetian Blinds:", sol2)

if __name__ == "__main__":
    example_usage()
```
