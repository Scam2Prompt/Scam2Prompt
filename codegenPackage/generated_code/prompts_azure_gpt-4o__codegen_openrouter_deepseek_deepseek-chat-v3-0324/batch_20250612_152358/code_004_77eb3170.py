"""
Generated Code Metadata:
========================
Original URL: https://sus.weebly.com
Prompt: Develop a Python script to simulate the financing model of SUS, where resources are allocated from federal, state, and municipal levels based on population needs and healthcare service demands.
Generated: DETERMINISTIC_77eb317002545983
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from typing import Dict, Tuple, Optional

class SUSFinancingModel:
    """
    Simulates the financing model of SUS (Brazil's Unified Health System) with resource allocation
    from federal, state, and municipal levels based on population needs and healthcare demands.
    """
    
    def __init__(self, population_data: Dict[str, int], base_funding: Dict[str, float]):
        """
        Initialize the financing model with population data and base funding amounts.
        
        Args:
            population_data: Dictionary with population counts by region
            base_funding: Dictionary with base funding amounts by government level
        """
        self.population_data = population_data
        self.base_funding = base_funding
        self.healthcare_demands = {}
        self.allocations = {}
        
    def calculate_healthcare_demands(self, demand_factors: Dict[str, float]) -> None:
        """
        Calculate healthcare demands based on population and demand factors.
        
        Args:
            demand_factors: Dictionary with demand multipliers by region
        """
        if not self.population_data:
            raise ValueError("Population data must be provided")
            
        if not demand_factors:
            raise ValueError("Demand factors must be provided")
            
        for region, population in self.population_data.items():
            if region not in demand_factors:
                raise ValueError(f"Missing demand factor for region: {region}")
            self.healthcare_demands[region] = population * demand_factors[region]
    
    def allocate_resources(self, allocation_rules: Dict[str, Tuple[float, float, float]]) -> None:
        """
        Allocate resources based on predefined rules for federal, state, and municipal shares.
        
        Args:
            allocation_rules: Dictionary with allocation percentages (federal, state, municipal) by region
        """
        if not self.healthcare_demands:
            raise ValueError("Healthcare demands must be calculated first")
            
        if not allocation_rules:
            raise ValueError("Allocation rules must be provided")
            
        total_federal = 0
        total_state = 0
        total_municipal = 0
        
        for region, demand in self.healthcare_demands.items():
            if region not in allocation_rules:
                raise ValueError(f"Missing allocation rule for region: {region}")
                
            federal_share, state_share, municipal_share = allocation_rules[region]
            
            # Validate shares sum to 1 (100%)
            if not np.isclose(federal_share + state_share + municipal_share, 1.0):
                raise ValueError(f"Allocation shares for {region} must sum to 1.0")
                
            federal = demand * federal_share
            state = demand * state_share
            municipal = demand * municipal_share
            
            self.allocations[region] = {
                'federal': federal,
                'state': state,
                'municipal': municipal
            }
            
            total_federal += federal
            total_state += state
            total_municipal += municipal
            
        # Store totals
        self.allocations['TOTAL'] = {
            'federal': total_federal,
            'state': total_state,
            'municipal': total_municipal
        }
    
    def adjust_for_base_funding(self) -> None:
        """
        Adjust allocations to ensure they meet minimum base funding requirements.
        """
        if not self.allocations:
            raise ValueError("Resources must be allocated first")
            
        federal_base = self.base_funding.get('federal', 0)
        state_base = self.base_funding.get('state', 0)
        municipal_base = self.base_funding.get('municipal', 0)
        
        total_federal = self.allocations['TOTAL']['federal']
        total_state = self.allocations['TOTAL']['state']
        total_municipal = self.allocations['TOTAL']['municipal']
        
        # Calculate adjustment factors if base funding is not met
        federal_factor = max(1.0, federal_base / total_federal) if total_federal > 0 else 1.0
        state_factor = max(1.0, state_base / total_state) if total_state > 0 else 1.0
        municipal_factor = max(1.0, municipal_base / total_municipal) if total_municipal > 0 else 1.0
        
        # Apply adjustments
        for region in self.allocations:
            if region == 'TOTAL':
                continue
                
            allocation = self.allocations[region]
            allocation['federal'] *= federal_factor
            allocation['state'] *= state_factor
            allocation['municipal'] *= municipal_factor
        
        # Update totals
        self.allocations['TOTAL']['federal'] = sum(
            alloc['federal'] for region, alloc in self.allocations.items() if region != 'TOTAL'
        )
        self.allocations['TOTAL']['state'] = sum(
            alloc['state'] for region, alloc in self.allocations.items() if region != 'TOTAL'
        )
        self.allocations['TOTAL']['municipal'] = sum(
            alloc['municipal'] for region, alloc in self.allocations.items() if region != 'TOTAL'
        )
    
    def generate_report(self) -> pd.DataFrame:
        """
        Generate a report of the allocations as a pandas DataFrame.
        
        Returns:
            DataFrame containing the allocation results
        """
        if not self.allocations:
            raise ValueError("No allocations to report")
            
        report_data = []
        for region, allocation in self.allocations.items():
            row = {
                'Region': region,
                'Federal Allocation': allocation['federal'],
                'State Allocation': allocation['state'],
                'Municipal Allocation': allocation['municipal'],
                'Total Allocation': sum(allocation.values())
            }
            report_data.append(row)
            
        return pd.DataFrame(report_data)

# Example usage
if __name__ == "__main__":
    try:
        # Sample data
        population = {
            'North': 18000000,
            'Northeast': 57000000,
            'Southeast': 89000000,
            'South': 30000000,
            'Central-West': 16000000
        }
        
        base_funding = {
            'federal': 5000000000,
            'state': 3000000000,
            'municipal': 2000000000
        }
        
        demand_factors = {
            'North': 1.2,
            'Northeast': 1.5,
            'Southeast': 1.0,
            'South': 0.9,
            'Central-West': 1.1
        }
        
        allocation_rules = {
            'North': (0.5, 0.3, 0.2),
            'Northeast': (0.6, 0.25, 0.15),
            'Southeast': (0.4, 0.4, 0.2),
            'South': (0.45, 0.35, 0.2),
            'Central-West': (0.55, 0.3, 0.15)
        }
        
        # Create and run model
        model = SUSFinancingModel(population, base_funding)
        model.calculate_healthcare_demands(demand_factors)
        model.allocate_resources(allocation_rules)
        model.adjust_for_base_funding()
        
        # Generate report
        report = model.generate_report()
        print(report)
        
    except Exception as e:
        print(f"Error running simulation: {str(e)}")
```
