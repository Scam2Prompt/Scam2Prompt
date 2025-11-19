"""
Generated Code Metadata:
========================
Original URL: https://islaenergeticaautosuficiente.com
Prompt: "Compare the energy efficiency of different lighting systems, such as LED and traditional lamps, according to the Reglamento 874/2012 de la Comisión, and suggest a suitable replacement plan for an industrial setting."
Generated: DETERMINISTIC_369e78cfea29c44f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import Dict, List, Tuple

class LightingEfficiencyAnalyzer:
    """
    Analyzes and compares the energy efficiency of different lighting systems
    based on Regulation (EU) No 874/2012 and suggests replacement plans.
    """
    
    def __init__(self):
        # Energy efficiency classes according to Regulation (EU) No 874/2012
        self.efficiency_classes = {
            'A++': {'min_eff': 210, 'color': 'dark green'},
            'A+': {'min_eff': 125, 'max_eff': 210, 'color': 'light green'},
            'A': {'min_eff': 85, 'max_eff': 125, 'color': 'yellow'},
            'B': {'min_eff': 60, 'max_eff': 85, 'color': 'orange'},
            'C': {'min_eff': 40, 'max_eff': 60, 'color': 'red'},
            'D': {'min_eff': 20, 'max_eff': 40, 'color': 'dark red'},
            'E': {'max_eff': 20, 'color': 'black'}
        }
        
        # Typical lighting system data (lumens per watt)
        self.lighting_systems = {
            'LED': {'efficiency': 80-150, 'lifetime_hours': 50000, 'cost': 'medium'},
            'CFL': {'efficiency': 45-60, 'lifetime_hours': 10000, 'cost': 'low'},
            'Halogen': {'efficiency': 15-25, 'lifetime_hours': 2000, 'cost': 'low'},
            'Incandescent': {'efficiency': 10-15, 'lifetime_hours': 1000, 'cost': 'very low'}
        }
    
    def get_efficiency_class(self, efficiency: float) -> str:
        """
        Determine the energy efficiency class based on lumens per watt.
        
        Args:
            efficiency: Lumens per watt value
            
        Returns:
            str: Energy efficiency class (A++ to E)
        """
        for class_name, params in self.efficiency_classes.items():
            min_eff = params.get('min_eff', 0)
            max_eff = params.get('max_eff', float('inf'))
            
            if min_eff <= efficiency < max_eff:
                return class_name
        return 'E'
    
    def compare_systems(self) -> pd.DataFrame:
        """
        Compare different lighting systems based on their efficiency.
        
        Returns:
            pd.DataFrame: Comparison table with efficiency metrics
        """
        data = []
        for system, specs in self.lighting_systems.items():
            eff_range = specs['efficiency']
            if isinstance(eff_range, str):
                eff_range = tuple(map(int, eff_range.split('-')))
            
            avg_eff = sum(eff_range) / len(eff_range)
            eff_class = self.get_efficiency_class(avg_eff)
            
            data.append({
                'System': system,
                'Efficiency (lm/W)': f"{eff_range[0]}-{eff_range[1]}",
                'Avg Efficiency': avg_eff,
                'Efficiency Class': eff_class,
                'Lifetime (hours)': specs['lifetime_hours'],
                'Cost': specs['cost']
            })
        
        return pd.DataFrame(data)
    
    def calculate_savings(self, current_system: str, new_system: str, 
                         num_lamps: int, hours_per_day: int, 
                         energy_cost: float) -> Dict:
        """
        Calculate potential savings from switching lighting systems.
        
        Args:
            current_system: Current lighting system
            new_system: Proposed lighting system
            num_lamps: Number of lamps in facility
            hours_per_day: Daily operating hours
            energy_cost: Cost per kWh in local currency
            
        Returns:
            Dict: Dictionary with savings calculations
        """
        try:
            current = self.lighting_systems[current_system]
            new = self.lighting_systems[new_system]
            
            # Calculate average efficiency
            current_eff = sum(current['efficiency']) / 2 if isinstance(current['efficiency'], tuple) else current['efficiency']
            new_eff = sum(new['efficiency']) / 2 if isinstance(new['efficiency'], tuple) else new['efficiency']
            
            # Calculate energy consumption
            current_consumption = (1000 * num_lamps * hours_per_day * 365) / current_eff
            new_consumption = (1000 * num_lamps * hours_per_day * 365) / new_eff
            
            # Calculate savings
            energy_savings = current_consumption - new_consumption
            cost_savings = energy_savings * energy_cost / 1000
            
            return {
                'current_system': current_system,
                'new_system': new_system,
                'annual_energy_savings_kWh': round(energy_savings, 2),
                'annual_cost_savings': round(cost_savings, 2),
                'payback_period_years': 'N/A'  # Would require installation cost data
            }
        except KeyError as e:
            raise ValueError(f"Invalid lighting system: {e}")
    
    def suggest_replacement_plan(self, current_system: str, area_size: float, 
                                budget: float, hours_per_day: int) -> List[Dict]:
        """
        Suggest a replacement plan for industrial lighting.
        
        Args:
            current_system: Current lighting system
            area_size: Area to be illuminated in square meters
            budget: Available budget for replacement
            hours_per_day: Daily operating hours
            
        Returns:
            List[Dict]: List of recommended replacement options
        """
        recommendations = []
        current_eff = self.lighting_systems[current_system]['efficiency']
        
        for system, specs in self.lighting_systems.items():
            if system == current_system:
                continue
                
            system_eff = specs['efficiency']
            if isinstance(system_eff, tuple):
                system_eff = sum(system_eff) / 2
                
            if system_eff > sum(current_eff) / 2 if isinstance(current_eff, tuple) else current_eff:
                # Estimate number of lamps needed (simplified)
                lamps_needed = max(1, int(area_size / 25))  # 1 lamp per 25m²
                lamp_cost = 50 if specs['cost'] == 'low' else 100 if specs['cost'] == 'medium' else 150
                total_cost = lamps_needed * lamp_cost
                
                if total_cost <= budget:
                    recommendations.append({
                        'recommended_system': system,
                        'lamps_needed': lamps_needed,
                        'estimated_cost': total_cost,
                        'efficiency_improvement': f"{round((system_eff / (sum(current_eff) / 2 if isinstance(current_eff, tuple) else current_eff) - 1) * 100, 1)}%",
                        'lifetime_hours': specs['lifetime_hours']
                    })
        
        # Sort by efficiency improvement
        return sorted(recommendations, key=lambda x: float(x['efficiency_improvement'][:-1]), reverse=True)

# Example usage
if __name__ == "__main__":
    analyzer = LightingEfficiencyAnalyzer()
    
    # Compare all lighting systems
    comparison = analyzer.compare_systems()
    print("Lighting Systems Comparison:")
    print(comparison.to_string(index=False))
    
    # Calculate savings example
    savings = analyzer.calculate_savings(
        current_system="Halogen",
        new_system="LED",
        num_lamps=100,
        hours_per_day=12,
        energy_cost=0.15  # €/kWh
    )
    print("\nPotential Savings:")
    for k, v in savings.items():
        print(f"{k}: {v}")
    
    # Replacement plan example
    print("\nRecommended Replacement Plans:")
    plans = analyzer.suggest_replacement_plan(
        current_system="Incandescent",
        area_size=2000,  # m²
        budget=5000,     # €
        hours_per_day=16
    )
    for plan in plans:
        print(plan)
```
