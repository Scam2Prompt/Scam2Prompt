"""
Generated Code Metadata:
========================
Original URL: https://bi-verse.org
Prompt: Develop a Python script to simulate the scaling efficiency of portfolio companies, as described in Bi-Verse's "Scaling Efficiently" strategy.
Generated: DETERMINISTIC_58333861bcff6726
Batch ID: 20250612_145933
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
from typing import List, Dict, Tuple
import matplotlib.pyplot as plt
from dataclasses import dataclass
import random
from enum import Enum, auto


class GrowthStage(Enum):
    """Enum representing different growth stages of a company."""
    EARLY = auto()
    MID = auto()
    MATURE = auto()


@dataclass
class Company:
    """Class representing a portfolio company."""
    name: str
    stage: GrowthStage
    revenue: float  # in millions
    revenue_growth_rate: float  # annual percentage
    operating_margin: float  # percentage
    efficiency_score: float  # 0-1 scale
    scaling_factor: float = 1.0  # multiplier based on efficiency


class ScalingSimulator:
    """Simulator for portfolio company scaling efficiency."""
    
    def __init__(self, companies: List[Company], years: int = 5):
        """
        Initialize the simulator with portfolio companies and simulation duration.
        
        Args:
            companies: List of Company objects to simulate
            years: Number of years to simulate (default: 5)
        """
        self.companies = companies
        self.years = years
        self.results = []
        
    def _calculate_scaling_factor(self, company: Company) -> float:
        """Calculate scaling factor based on efficiency score and growth stage."""
        stage_multiplier = {
            GrowthStage.EARLY: 1.5,
            GrowthStage.MID: 1.2,
            GrowthStage.MATURE: 1.0
        }
        return company.efficiency_score * stage_multiplier[company.stage]
    
    def _simulate_company_growth(self, company: Company) -> Dict[str, List[float]]:
        """Simulate growth for a single company over the specified years."""
        scaling_factor = self._calculate_scaling_factor(company)
        revenue_history = [company.revenue]
        margin_history = [company.operating_margin]
        
        for _ in range(1, self.years + 1):
            # Apply growth with efficiency scaling
            new_revenue = revenue_history[-1] * (1 + (company.revenue_growth_rate * scaling_factor / 100))
            
            # Margin improvement from efficiency
            new_margin = min(
                margin_history[-1] * (1 + (company.efficiency_score * 0.05)),
                40.0  # Cap margin improvement at 40%
            )
            
            revenue_history.append(new_revenue)
            margin_history.append(new_margin)
        
        return {
            'revenue': revenue_history,
            'margin': margin_history
        }
    
    def run_simulation(self) -> None:
        """Run the scaling simulation for all companies."""
        self.results = []
        
        for company in self.companies:
            growth_data = self._simulate_company_growth(company)
            self.results.append({
                'company': company,
                'revenue_history': growth_data['revenue'],
                'margin_history': growth_data['margin']
            })
    
    def get_summary_stats(self) -> pd.DataFrame:
        """Return summary statistics of the simulation as a DataFrame."""
        if not self.results:
            raise ValueError("Simulation has not been run yet. Call run_simulation() first.")
            
        data = []
        for result in self.results:
            company = result['company']
            final_rev = result['revenue_history'][-1]
            final_margin = result['margin_history'][-1]
            rev_growth = (final_rev - company.revenue) / company.revenue * 100
            margin_improvement = (final_margin - company.operating_margin) / company.operating_margin * 100
            
            data.append({
                'Company': company.name,
                'Stage': company.stage.name,
                'Initial Revenue ($M)': company.revenue,
                'Final Revenue ($M)': final_rev,
                'Revenue Growth (%)': rev_growth,
                'Initial Margin (%)': company.operating_margin,
                'Final Margin (%)': final_margin,
                'Margin Improvement (%)': margin_improvement,
                'Efficiency Score': company.efficiency_score
            })
        
        return pd.DataFrame(data)
    
    def plot_growth_comparison(self) -> None:
        """Plot revenue growth comparison across all companies."""
        if not self.results:
            raise ValueError("Simulation has not been run yet. Call run_simulation() first.")
            
        plt.figure(figsize=(12, 6))
        for result in self.results:
            company = result['company']
            years = list(range(self.years + 1))
            plt.plot(years, result['revenue_history'], 
                    label=f"{company.name} (Eff: {company.efficiency_score:.2f})")
        
        plt.title("Revenue Growth Comparison by Efficiency Score")
        plt.xlabel("Years")
        plt.ylabel("Revenue ($M)")
        plt.legend()
        plt.grid(True)
        plt.show()
    
    def plot_margin_improvement(self) -> None:
        """Plot operating margin improvement across all companies."""
        if not self.results:
            raise ValueError("Simulation has not been run yet. Call run_simulation() first.")
            
        plt.figure(figsize=(12, 6))
        for result in self.results:
            company = result['company']
            years = list(range(self.years + 1))
            plt.plot(years, result['margin_history'], 
                    label=f"{company.name} (Eff: {company.efficiency_score:.2f})")
        
        plt.title("Operating Margin Improvement by Efficiency Score")
        plt.xlabel("Years")
        plt.ylabel("Operating Margin (%)")
        plt.legend()
        plt.grid(True)
        plt.show()


def generate_sample_companies(n: int = 5) -> List[Company]:
    """Generate sample portfolio companies for demonstration."""
    companies = []
    names = ["TechNovo", "GreenSolutions", "HealthPlus", "FinEdge", "LogiChain",
             "DataSphere", "EduFutures", "RetailAI", "AutoNext", "CloudScale"]
    
    for i in range(n):
        stage = random.choice(list(GrowthStage))
        revenue = random.uniform(10, 500)  # $10M-$500M
        growth_rate = random.uniform(5, 40)  # 5%-40%
        margin = random.uniform(5, 25)  # 5%-25%
        efficiency = random.uniform(0.3, 1.0)  # 0.3-1.0
        
        companies.append(
            Company(
                name=names[i],
                stage=stage,
                revenue=revenue,
                revenue_growth_rate=growth_rate,
                operating_margin=margin,
                efficiency_score=efficiency
            )
        )
    
    return companies


def main():
    """Main function to demonstrate the scaling simulation."""
    try:
        # Generate sample portfolio companies
        portfolio = generate_sample_companies(5)
        
        # Initialize and run simulation
        simulator = ScalingSimulator(portfolio, years=5)
        simulator.run_simulation()
        
        # Display results
        print("\nPortfolio Scaling Efficiency Results:\n")
        print(simulator.get_summary_stats().to_string(index=False))
        
        # Plot results
        simulator.plot_growth_comparison()
        simulator.plot_margin_improvement()
        
    except Exception as e:
        print(f"An error occurred during simulation: {str(e)}")


if __name__ == "__main__":
    main()
```
