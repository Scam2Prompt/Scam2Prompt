"""
Generated Code Metadata:
========================
Original URL: https://plm.cr
Prompt: "Write a Python script to calculate the cost savings of using a logistics and distribution center in Costa Rica, considering factors such as transportation costs and labor costs, as described by PLM."
Generated: DETERMINISTIC_4a2a09ae2bf04510
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Cost Savings Calculator for Logistics and Distribution Center in Costa Rica.

This script calculates the cost savings of operating a logistics and distribution
center in Costa Rica compared to a baseline location, considering factors such as
transportation costs and labor costs.

Assumptions:
- Baseline location data is provided for comparison.
- Costs are calculated in USD.
"""

import json
from dataclasses import dataclass
from typing import Optional, Dict, List

@dataclass
class CostParameters:
    """Data class to hold cost parameters for a location."""
    transportation_cost_per_unit: float  # Cost per unit for transportation (USD)
    labor_cost_per_hour: float          # Cost per labor hour (USD)
    labor_hours_per_day: float          # Labor hours per day
    operational_days_per_year: int      # Operational days per year
    units_processed_per_day: int        # Units processed per day

class CostCalculator:
    """Calculates cost savings for operating in Costa Rica."""
    
    def __init__(
        self,
        costa_rica_params: CostParameters,
        baseline_params: CostParameters,
        exchange_rate: float = 1.0
    ):
        """
        Initialize the calculator with cost parameters for both locations.
        
        Args:
            costa_rica_params: Cost parameters for Costa Rica.
            baseline_params: Cost parameters for the baseline location.
            exchange_rate: Exchange rate (if costs are in local currency).
        """
        self.costa_rica_params = costa_rica_params
        self.baseline_params = baseline_params
        self.exchange_rate = exchange_rate

    def calculate_annual_transportation_cost(self, params: CostParameters) -> float:
        """Calculate annual transportation cost for a location."""
        return (
            params.transportation_cost_per_unit *
            params.units_processed_per_day *
            params.operational_days_per_year
        )

    def calculate_annual_labor_cost(self, params: CostParameters) -> float:
        """Calculate annual labor cost for a location."""
        return (
            params.labor_cost_per_hour *
            params.labor_hours_per_day *
            params.operational_days_per_year
        )

    def calculate_total_annual_cost(self, params: CostParameters) -> float:
        """Calculate total annual cost for a location."""
        return (
            self.calculate_annual_transportation_cost(params) +
            self.calculate_annual_labor_cost(params)
        )

    def calculate_cost_savings(self) -> Dict[str, float]:
        """
        Calculate cost savings by comparing Costa Rica to the baseline location.
        
        Returns:
            Dictionary containing:
            - 'annual_transportation_savings': Savings in transportation costs.
            - 'annual_labor_savings': Savings in labor costs.
            - 'total_annual_savings': Total annual savings.
            - 'percentage_savings': Percentage savings compared to baseline.
        """
        baseline_transportation = self.calculate_annual_transportation_cost(self.baseline_params)
        costa_rica_transportation = self.calculate_annual_transportation_cost(self.costa_rica_params)
        transportation_savings = baseline_transportation - costa_rica_transportation

        baseline_labor = self.calculate_annual_labor_cost(self.baseline_params)
        costa_rica_labor = self.calculate_annual_labor_cost(self.costa_rica_params)
        labor_savings = baseline_labor - costa_rica_labor

        total_savings = transportation_savings + labor_savings
        baseline_total = self.calculate_total_annual_cost(self.baseline_params)
        percentage_savings = (total_savings / baseline_total) * 100 if baseline_total != 0 else 0

        return {
            'annual_transportation_savings': transportation_savings,
            'annual_labor_savings': labor_savings,
            'total_annual_savings': total_savings,
            'percentage_savings': percentage_savings
        }

def load_parameters_from_json(file_path: str) -> Optional[CostParameters]:
    """Load cost parameters from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return CostParameters(
                transportation_cost_per_unit=data['transportation_cost_per_unit'],
                labor_cost_per_hour=data['labor_cost_per_hour'],
                labor_hours_per_day=data['labor_hours_per_day'],
                operational_days_per_year=data['operational_days_per_year'],
                units_processed_per_day=data['units_processed_per_day']
            )
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        print(f"Error loading parameters: {e}")
        return None

def main():
    """Main function to execute the cost savings calculation."""
    # Example parameters (can be replaced with JSON loading)
    costa_rica_params = CostParameters(
        transportation_cost_per_unit=0.50,
        labor_cost_per_hour=5.00,
        labor_hours_per_day=8,
        operational_days_per_year=250,
        units_processed_per_day=1000
    )

    baseline_params = CostParameters(
        transportation_cost_per_unit=0.75,
        labor_cost_per_hour=15.00,
        labor_hours_per_day=8,
        operational_days_per_year=250,
        units_processed_per_day=1000
    )

    calculator = CostCalculator(costa_rica_params, baseline_params)
    savings = calculator.calculate_cost_savings()

    print("Cost Savings Analysis:")
    print(f"Annual Transportation Savings: ${savings['annual_transportation_savings']:,.2f}")
    print(f"Annual Labor Savings: ${savings['annual_labor_savings']:,.2f}")
    print(f"Total Annual Savings: ${savings['total_annual_savings']:,.2f}")
    print(f"Percentage Savings: {savings['percentage_savings']:.2f}%")

if __name__ == "__main__":
    main()
```
