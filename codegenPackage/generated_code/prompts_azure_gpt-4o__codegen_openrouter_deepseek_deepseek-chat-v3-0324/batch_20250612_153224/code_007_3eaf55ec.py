"""
Generated Code Metadata:
========================
Original URL: https://unisonplus.vn
Prompt: Develop a tool to assist in infrastructure project feasibility studies, including cost estimation and risk analysis, inspired by Unison Plus's consulting services.
Generated: DETERMINISTIC_3eaf55ece330d678
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
Infrastructure Project Feasibility Tool
This tool assists in conducting feasibility studies for infrastructure projects,
including cost estimation and risk analysis.
"""

import json
import math
import random
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Union

class FeasibilityStudy:
    """
    Main class for conducting infrastructure project feasibility studies.
    Handles cost estimation, risk analysis, and report generation.
    """
    
    def __init__(self, project_name: str, project_duration: int, currency: str = "USD"):
        """
        Initialize the feasibility study with basic project information.
        
        Args:
            project_name: Name of the infrastructure project
            project_duration: Duration in months
            currency: Currency for cost calculations (default: USD)
        """
        self.project_name = project_name
        self.project_duration = project_duration
        self.currency = currency
        self.cost_components = {}
        self.risk_factors = {}
        self.assumptions = []
        
    def add_cost_component(self, name: str, cost: float, category: str, 
                          uncertainty: float = 0.1) -> None:
        """
        Add a cost component to the project.
        
        Args:
            name: Name of the cost component
            cost: Estimated base cost
            category: Category (e.g., 'Materials', 'Labor')
            uncertainty: Percentage uncertainty (0-1) for Monte Carlo simulation
        """
        if uncertainty < 0 or uncertainty > 1:
            raise ValueError("Uncertainty must be between 0 and 1")
            
        self.cost_components[name] = {
            'base_cost': cost,
            'category': category,
            'uncertainty': uncertainty
        }
    
    def add_risk_factor(self, name: str, probability: float, impact: float, 
                       mitigation: str = "") -> None:
        """
        Add a risk factor to the project.
        
        Args:
            name: Name of the risk factor
            probability: Probability of occurrence (0-1)
            impact: Financial impact if risk occurs (in same currency as project)
            mitigation: Optional mitigation strategy
        """
        if probability < 0 or probability > 1:
            raise ValueError("Probability must be between 0 and 1")
            
        self.risk_factors[name] = {
            'probability': probability,
            'impact': impact,
            'mitigation': mitigation
        }
    
    def add_assumption(self, assumption: str) -> None:
        """Add an assumption to the feasibility study."""
        self.assumptions.append(assumption)
    
    def estimate_total_cost(self, simulations: int = 1000) -> Dict[str, Union[float, Dict]]:
        """
        Estimate total project cost using Monte Carlo simulation.
        
        Args:
            simulations: Number of simulations to run (default: 1000)
            
        Returns:
            Dictionary containing cost statistics and breakdown
        """
        if not self.cost_components:
            raise ValueError("No cost components have been added")
            
        total_costs = []
        category_breakdown = {category: [] for category in set(
            comp['category'] for comp in self.cost_components.values()
        )}
        
        for _ in range(simulations):
            sim_total = 0
            sim_categories = {category: 0 for category in category_breakdown.keys()}
            
            for name, component in self.cost_components.items():
                # Apply uncertainty using triangular distribution
                min_cost = component['base_cost'] * (1 - component['uncertainty'])
                max_cost = component['base_cost'] * (1 + component['uncertainty'])
                likely_cost = component['base_cost']
                
                # Triangular distribution calculation
                rand = random.random()
                if rand < ((likely_cost - min_cost) / (max_cost - min_cost)):
                    sim_cost = min_cost + math.sqrt(rand * (max_cost - min_cost) * (likely_cost - min_cost))
                else:
                    sim_cost = max_cost - math.sqrt((1 - rand) * (max_cost - min_cost) * (max_cost - likely_cost))
                
                sim_total += sim_cost
                sim_categories[component['category']] += sim_cost
            
            total_costs.append(sim_total)
            for category, cost in sim_categories.items():
                category_breakdown[category].append(cost)
        
        # Calculate statistics
        total_costs_sorted = sorted(total_costs)
        n = len(total_costs_sorted)
        
        def percentile(p):
            return total_costs_sorted[int(n * p / 100)]
        
        return {
            'mean': sum(total_costs) / n,
            'median': total_costs_sorted[n // 2],
            'p10': percentile(10),
            'p90': percentile(90),
            'min': min(total_costs),
            'max': max(total_costs),
            'category_breakdown': {
                category: {
                    'mean': sum(costs) / n,
                    'percentage': sum(costs) / sum(total_costs) * 100
                }
                for category, costs in category_breakdown.items()
            }
        }
    
    def analyze_risks(self) -> Dict[str, Union[float, Dict]]:
        """
        Analyze project risks and calculate expected monetary impact.
        
        Returns:
            Dictionary containing risk statistics and prioritized risks
        """
        if not self.risk_factors:
            raise ValueError("No risk factors have been added")
            
        total_expected_impact = 0
        prioritized_risks = []
        
        for name, risk in self.risk_factors.items():
            expected_impact = risk['probability'] * risk['impact']
            total_expected_impact += expected_impact
            prioritized_risks.append({
                'name': name,
                'expected_impact': expected_impact,
                'probability': risk['probability'],
                'impact': risk['impact'],
                'mitigation': risk['mitigation']
            })
        
        # Sort risks by expected impact (descending)
        prioritized_risks.sort(key=lambda x: x['expected_impact'], reverse=True)
        
        return {
            'total_expected_impact': total_expected_impact,
            'prioritized_risks': prioritized_risks
        }
    
    def generate_report(self, file_path: Optional[str] = None) -> str:
        """
        Generate a comprehensive feasibility report.
        
        Args:
            file_path: Optional path to save report as JSON file
            
        Returns:
            JSON string containing the full report
        """
        cost_analysis = self.estimate_total_cost()
        risk_analysis = self.analyze_risks()
        
        report = {
            'metadata': {
                'project_name': self.project_name,
                'project_duration': self.project_duration,
                'currency': self.currency,
                'report_date': datetime.now().isoformat()
            },
            'cost_analysis': cost_analysis,
            'risk_analysis': risk_analysis,
            'assumptions': self.assumptions,
            'summary': {
                'total_cost_estimate': cost_analysis['mean'],
                'total_risk_impact': risk_analysis['total_expected_impact'],
                'contingency_recommendation': cost_analysis['p90'] - cost_analysis['mean']
            }
        }
        
        report_json = json.dumps(report, indent=2)
        
        if file_path:
            with open(file_path, 'w') as f:
                f.write(report_json)
                
        return report_json

# Example usage
if __name__ == "__main__":
    # Create a feasibility study for a bridge construction project
    study = FeasibilityStudy(
        project_name="Harbor Bridge Reconstruction",
        project_duration=24,
        currency="USD"
    )
    
    # Add cost components
    study.add_cost_component("Steel", 2500000, "Materials", 0.15)
    study.add_cost_component("Concrete", 1800000, "Materials", 0.12)
    study.add_cost_component("Labor", 3200000, "Labor", 0.2)
    study.add_cost_component("Equipment", 950000, "Equipment", 0.18)
    study.add_cost_component("Permits", 150000, "Administrative", 0.05)
    
    # Add risk factors
    study.add_risk_factor("Material price increase", 0.4, 500000, 
                         "Lock in prices with suppliers")
    study.add_risk_factor("Labor strike", 0.15, 750000, 
                         "Negotiate labor agreements early")
    study.add_risk_factor("Weather delays", 0.3, 300000, 
                         "Build in weather contingency days")
    study.add_risk_factor("Design changes", 0.25, 400000, 
                         "Finalize design before construction")
    
    # Add assumptions
    study.add_assumption("No major regulatory changes during project")
    study.add_assumption("Inflation rate remains below 3% annually")
    
    # Generate and print report
    report = study.generate_report("harbor_bridge_feasibility.json")
    print(report)
```
