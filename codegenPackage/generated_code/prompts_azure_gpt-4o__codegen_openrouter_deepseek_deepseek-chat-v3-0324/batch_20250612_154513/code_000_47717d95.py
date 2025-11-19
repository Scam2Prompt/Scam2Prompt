"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Write a Python script to calculate the environmental impact of cement production using emission levels data, referencing the sustainability strategies discussed by Tanzania Portland Cement Public Limited Company (TPCPLC).
Generated: DETERMINISTIC_47717d95ed24a5fc
Batch ID: 20250612_154513
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

class CementEmissionCalculator:
    """
    A class to calculate the environmental impact of cement production based on emission levels.
    References sustainability strategies from Tanzania Portland Cement Public Limited Company (TPCPLC).
    """
    
    def __init__(self, emission_factors: Dict[str, float], production_data: Dict[str, float]):
        """
        Initialize the calculator with emission factors and production data.
        
        Args:
            emission_factors: Dictionary mapping emission types to their factors (kg CO2 per ton of cement).
            production_data: Dictionary containing production metrics (e.g., annual production in tons).
        """
        self.emission_factors = emission_factors
        self.production_data = production_data
        self.validate_inputs()
    
    def validate_inputs(self) -> None:
        """Validate that emission factors and production data are provided correctly."""
        if not isinstance(self.emission_factors, dict) or not self.emission_factors:
            raise ValueError("Emission factors must be a non-empty dictionary.")
        if not isinstance(self.production_data, dict) or not self.production_data:
            raise ValueError("Production data must be a non-empty dictionary.")
        if "annual_production_tons" not in self.production_data:
            raise ValueError("Production data must include 'annual_production_tons'.")
    
    def calculate_total_emissions(self) -> Dict[str, float]:
        """
        Calculate total emissions for each emission type based on production data.
        
        Returns:
            Dictionary mapping emission types to total emissions (kg CO2).
        """
        total_emissions = {}
        annual_production = self.production_data["annual_production_tons"]
        
        for emission_type, factor in self.emission_factors.items():
            total_emissions[emission_type] = annual_production * factor
        
        return total_emissions
    
    def calculate_emission_reduction(self, reduction_strategies: Dict[str, float]) -> Dict[str, float]:
        """
        Calculate potential emission reductions based on sustainability strategies.
        
        Args:
            reduction_strategies: Dictionary mapping strategies to their reduction percentages (0-1).
        
        Returns:
            Dictionary mapping emission types to reduced emissions (kg CO2).
        """
        if not isinstance(reduction_strategies, dict):
            raise ValueError("Reduction strategies must be a dictionary.")
        
        total_emissions = self.calculate_total_emissions()
        reduced_emissions = {}
        
        for emission_type, current_emission in total_emissions.items():
            reduction_percentage = reduction_strategies.get(emission_type, 0.0)
            if not 0 <= reduction_percentage <= 1:
                raise ValueError(f"Reduction percentage for {emission_type} must be between 0 and 1.")
            reduced_emissions[emission_type] = current_emission * (1 - reduction_percentage)
        
        return reduced_emissions
    
    def generate_report(self, reduced_emissions: Optional[Dict[str, float]] = None) -> pd.DataFrame:
        """
        Generate a report comparing original and reduced emissions.
        
        Args:
            reduced_emissions: Optional dictionary of reduced emissions (from calculate_emission_reduction).
        
        Returns:
            Pandas DataFrame containing the emission report.
        """
        total_emissions = self.calculate_total_emissions()
        data = {
            "Emission Type": list(total_emissions.keys()),
            "Total Emissions (kg CO2)": list(total_emissions.values()),
        }
        
        if reduced_emissions:
            data["Reduced Emissions (kg CO2)"] = [reduced_emissions.get(et, 0.0) for et in total_emissions.keys()]
            data["Reduction (%)"] = [
                ((total_emissions[et] - reduced_emissions.get(et, 0.0)) / total_emissions[et]) * 100 
                for et in total_emissions.keys()
            ]
        
        report_df = pd.DataFrame(data)
        return report_df

# Example usage
if __name__ == "__main__":
    # Sample data based on TPCPLC sustainability strategies
    emission_factors = {
        "clinker_production": 0.83,  # kg CO2 per ton of cement
        "electricity_consumption": 0.12,
        "transportation": 0.05,
    }
    
    production_data = {
        "annual_production_tons": 1_000_000,  # 1 million tons annually
    }
    
    reduction_strategies = {
        "clinker_production": 0.15,  # 15% reduction
        "electricity_consumption": 0.10,  # 10% reduction
    }
    
    try:
        calculator = CementEmissionCalculator(emission_factors, production_data)
        reduced_emissions = calculator.calculate_emission_reduction(reduction_strategies)
        report = calculator.generate_report(reduced_emissions)
        
        print("Cement Production Emission Report:")
        print(report)
        
    except ValueError as e:
        print(f"Error: {e}")
```
