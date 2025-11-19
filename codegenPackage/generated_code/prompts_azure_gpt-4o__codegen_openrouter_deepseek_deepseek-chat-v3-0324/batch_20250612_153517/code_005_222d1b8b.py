"""
Generated Code Metadata:
========================
Original URL: https://fesit.cl
Prompt: Generate a Python script to model the effects of decentralization in tax collection, reflecting FESIT's advocacy for decentralized systems.
Generated: DETERMINISTIC_222d1b8b43fd619a
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Tax Decentralization Model - FESIT Advocacy

This script models the effects of decentralization in tax collection,
comparing centralized vs decentralized systems across various metrics.
"""

import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List, Dict, Tuple
import random
from enum import Enum, auto


class TaxSystemType(Enum):
    CENTRALIZED = auto()
    DECENTRALIZED = auto()


@dataclass
class Region:
    name: str
    population: int
    economic_activity: float  # Scale from 0-1
    tax_compliance: float  # Scale from 0-1
    local_government_efficiency: float  # Scale from 0-1


@dataclass
class TaxCollectionResult:
    total_revenue: float
    collection_cost: float
    compliance_rate: float
    citizen_satisfaction: float
    economic_growth: float


class TaxSystemModel:
    def __init__(self, regions: List[Region], system_type: TaxSystemType):
        self.regions = regions
        self.system_type = system_type
        self.results: Dict[str, TaxCollectionResult] = {}

    def _calculate_centralized_tax(self, region: Region) -> TaxCollectionResult:
        # Centralized system assumptions
        base_revenue = region.population * region.economic_activity * 1000
        efficiency_loss = 0.3  # Central bureaucracy inefficiency
        compliance_factor = 0.7 * region.tax_compliance  # Lower local knowledge
        
        revenue = base_revenue * compliance_factor * (1 - efficiency_loss)
        cost = base_revenue * 0.15  # Higher collection costs
        satisfaction = 0.5 * region.tax_compliance  # Lower satisfaction
        
        return TaxCollectionResult(
            total_revenue=revenue,
            collection_cost=cost,
            compliance_rate=compliance_factor,
            citizen_satisfaction=satisfaction,
            economic_growth=region.economic_activity * 0.8  # Centralized growth factor
        )

    def _calculate_decentralized_tax(self, region: Region) -> TaxCollectionResult:
        # Decentralized system assumptions
        base_revenue = region.population * region.economic_activity * 1000
        efficiency_gain = 0.1 * region.local_government_efficiency
        compliance_factor = 0.9 * region.tax_compliance  # Better local knowledge
        
        revenue = base_revenue * compliance_factor * (1 + efficiency_gain)
        cost = base_revenue * 0.08  # Lower collection costs
        satisfaction = 0.8 * region.tax_compliance  # Higher satisfaction
        
        return TaxCollectionResult(
            total_revenue=revenue,
            collection_cost=cost,
            compliance_rate=compliance_factor,
            citizen_satisfaction=satisfaction,
            economic_growth=region.economic_activity * 1.2  # Decentralized growth factor
        )

    def run_simulation(self, years: int = 5) -> None:
        for year in range(1, years + 1):
            year_key = f"Year {year}"
            self.results[year_key] = TaxCollectionResult(0, 0, 0, 0, 0)
            
            for region in self.regions:
                if self.system_type == TaxSystemType.CENTRALIZED:
                    result = self._calculate_centralized_tax(region)
                else:
                    result = self._calculate_decentralized_tax(region)
                
                # Aggregate results
                self.results[year_key].total_revenue += result.total_revenue
                self.results[year_key].collection_cost += result.collection_cost
                self.results[year_key].compliance_rate = (
                    self.results[year_key].compliance_rate + result.compliance_rate
                ) / 2
                self.results[year_key].citizen_satisfaction = (
                    self.results[year_key].citizen_satisfaction + result.citizen_satisfaction
                ) / 2
                self.results[year_key].economic_growth = (
                    self.results[year_key].economic_growth + result.economic_growth
                ) / 2

    def get_results(self) -> Dict[str, TaxCollectionResult]:
        return self.results


def generate_sample_regions(num_regions: int = 5) -> List[Region]:
    regions = []
    for i in range(1, num_regions + 1):
        regions.append(
            Region(
                name=f"Region {i}",
                population=random.randint(100000, 500000),
                economic_activity=random.uniform(0.4, 0.9),
                tax_compliance=random.uniform(0.5, 0.95),
                local_government_efficiency=random.uniform(0.6, 0.95)
            )
        )
    return regions


def plot_comparison(centralized_results: Dict[str, TaxCollectionResult],
                    decentralized_results: Dict[str, TaxCollectionResult]) -> None:
    years = list(centralized_results.keys())
    
    # Prepare data
    metrics = [
        ('Total Revenue (billions)', lambda r: r.total_revenue / 1e9),
        ('Collection Cost (millions)', lambda r: r.collection_cost / 1e6),
        ('Compliance Rate', lambda r: r.compliance_rate),
        ('Citizen Satisfaction', lambda r: r.citizen_satisfaction),
        ('Economic Growth Factor', lambda r: r.economic_growth)
    ]
    
    fig, axes = plt.subplots(len(metrics), 1, figsize=(10, 15))
    fig.suptitle('Centralized vs Decentralized Tax Collection Comparison')
    
    for i, (title, metric_func) in enumerate(metrics):
        centralized_values = [metric_func(centralized_results[year]) for year in years]
        decentralized_values = [metric_func(decentralized_results[year]) for year in years]
        
        axes[i].plot(years, centralized_values, label='Centralized', marker='o')
        axes[i].plot(years, decentralized_values, label='Decentralized', marker='s')
        axes[i].set_title(title)
        axes[i].legend()
        axes[i].grid(True)
    
    plt.tight_layout()
    plt.show()


def main():
    # Generate sample regions
    regions = generate_sample_regions()
    
    # Run simulations
    centralized_model = TaxSystemModel(regions, TaxSystemType.CENTRALIZED)
    decentralized_model = TaxSystemModel(regions, TaxSystemType.DECENTRALIZED)
    
    centralized_model.run_simulation()
    decentralized_model.run_simulation()
    
    # Get and compare results
    centralized_results = centralized_model.get_results()
    decentralized_results = decentralized_model.get_results()
    
    # Display comparison
    plot_comparison(centralized_results, decentralized_results)


if __name__ == "__main__":
    main()
```
