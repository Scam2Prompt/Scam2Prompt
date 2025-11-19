"""
Generated Code Metadata:
========================
Original URL: https://sautikenya.com
Prompt: Provide code to model the environmental benefits of clean energy adoption in rural Kenya, as described in Sauti Kenya's briquette-making initiative.
Generated: DETERMINISTIC_a6e351401b48eed3
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Environmental Impact Model for Clean Energy Adoption in Rural Kenya
This script models the environmental benefits of Sauti Kenya's briquette-making initiative.
It calculates reductions in deforestation, CO2 emissions, and household energy costs.
"""

import math
from dataclasses import dataclass
from typing import List, Dict, Tuple
import matplotlib.pyplot as plt
import numpy as np

@dataclass
class Household:
    """Represents a household participating in the briquette program"""
    id: int
    members: int
    traditional_fuel_consumption: float  # kg per day
    briquette_adoption_rate: float  # 0-1 percentage
    briquette_efficiency: float  # compared to traditional fuel
    
    @property
    def effective_fuel_reduction(self) -> float:
        """Calculate actual fuel reduction considering adoption rate and efficiency"""
        return self.traditional_fuel_consumption * self.briquette_adoption_rate * (1 - self.briquette_efficiency)

@dataclass
class EnvironmentalImpact:
    """Stores calculated environmental impact metrics"""
    co2_reduction_kg: float
    trees_saved: float
    cost_savings_usd: float
    health_benefits: float  # arbitrary scale

class BriquetteProgram:
    """Models the environmental impact of a briquette-making initiative"""
    
    # Constants (values based on research studies)
    CO2_PER_KG_FUEL = 2.5  # kg CO2 per kg of traditional fuel
    TREES_PER_KG_FUEL = 0.005  # trees saved per kg fuel not burned
    COST_PER_KG_FUEL = 0.15  # USD per kg traditional fuel
    COST_PER_KG_BRIQUETTE = 0.10  # USD per kg briquette
    HEALTH_BENEFIT_FACTOR = 0.8  # arbitrary scaling factor
    
    def __init__(self, households: List[Household], duration_days: int = 365):
        self.households = households
        self.duration_days = duration_days
        
    def calculate_impact(self) -> EnvironmentalImpact:
        """Calculate aggregate environmental impact across all households"""
        total_co2 = 0.0
        total_trees = 0.0
        total_cost_savings = 0.0
        total_health = 0.0
        
        for household in self.households:
            daily_reduction = household.effective_fuel_reduction
            total_reduction = daily_reduction * self.duration_days
            
            # CO2 emissions reduction
            total_co2 += total_reduction * self.CO2_PER_KG_FUEL
            
            # Trees saved from deforestation
            total_trees += total_reduction * self.TREES_PER_KG_FUEL
            
            # Cost savings calculation
            traditional_cost = household.traditional_fuel_consumption * self.COST_PER_KG_FUEL * self.duration_days
            briquette_cost = (household.traditional_fuel_consumption * household.briquette_adoption_rate * 
                             self.briquette_efficiency * self.COST_PER_KG_BRIQUETTE * self.duration_days)
            remaining_traditional_cost = (household.traditional_fuel_consumption * 
                                         (1 - household.briquette_adoption_rate) * 
                                         self.COST_PER_KG_FUEL * self.duration_days)
            total_cost_savings += traditional_cost - (briquette_cost + remaining_traditional_cost)
            
            # Health benefits (simplified proxy)
            total_health += daily_reduction * self.HEALTH_BENEFIT_FACTOR * household.members
        
        return EnvironmentalImpact(
            co2_reduction_kg=total_co2,
            trees_saved=total_trees,
            cost_savings_usd=total_cost_savings,
            health_benefits=total_health
        )
    
    def generate_report(self, impact: EnvironmentalImpact) -> Dict[str, str]:
        """Generate a human-readable report of the environmental impact"""
        return {
            "CO2 Reduction": f"{impact.co2_reduction_kg:,.2f} kg CO2 emissions avoided",
            "Trees Saved": f"{impact.trees_saved:,.1f} trees preserved from deforestation",
            "Cost Savings": f"${impact.cost_savings_usd:,.2f} saved by households",
            "Health Impact": f"Significant indoor air quality improvement for {len(self.households)} families"
        }
    
    def plot_impact(self, impact: EnvironmentalImpact):
        """Visualize the environmental impact metrics"""
        metrics = ['CO2 Reduction (kg)', 'Trees Saved', 'Cost Savings (USD)']
        values = [impact.co2_reduction_kg, impact.trees_saved, impact.cost_savings_usd]
        
        plt.figure(figsize=(10, 6))
        bars = plt.bar(metrics, values, color=['#2ecc71', '#27ae60', '#16a085'])
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:,.0f}',
                    ha='center', va='bottom')
        
        plt.title('Environmental Impact of Briquette Adoption')
        plt.ylabel('Annual Impact')
        plt.tight_layout()
        plt.show()

def sample_households(num_households: int = 100) -> List[Household]:
    """Generate sample household data with realistic distributions"""
    rng = np.random.default_rng()
    
    households = []
    for i in range(num_households):
        members = int(rng.normal(5, 1.5))
        members = max(1, members)  # Ensure at least 1 member
        
        fuel_use = rng.normal(8, 2)
        fuel_use = max(3, min(fuel_use, 15))  # Realistic bounds
        
        adoption = rng.beta(2, 5)  # Most households have low-medium adoption
        efficiency = rng.normal(0.6, 0.1)  # Briquettes are ~60% as efficient
        
        households.append(Household(
            id=i,
            members=members,
            traditional_fuel_consumption=fuel_use,
            briquette_adoption_rate=adoption,
            briquette_efficiency=efficiency
        ))
    
    return households

def main():
    """Run the environmental impact analysis"""
    try:
        # Generate sample data for 200 households
        households = sample_households(200)
        
        # Initialize and run the program model
        program = BriquetteProgram(households)
        impact = program.calculate_impact()
        
        # Generate and print report
        report = program.generate_report(impact)
        for metric, result in report.items():
            print(f"{metric}: {result}")
        
        # Visualize results
        program.plot_impact(impact)
        
    except Exception as e:
        print(f"Error in analysis: {str(e)}")
        raise

if __name__ == "__main__":
    main()
```
