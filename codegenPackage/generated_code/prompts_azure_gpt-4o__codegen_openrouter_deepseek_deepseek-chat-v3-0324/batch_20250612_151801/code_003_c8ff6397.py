"""
Generated Code Metadata:
========================
Original URL: https://kubitz.com.br
Prompt: Write a script to calculate the cost-benefit ratio of implementing modular conveyor belts, such as Kubitz Esteiras, with varying lengths and configurations.
Generated: DETERMINISTIC_c8ff63978ff75a2f
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the cost-benefit ratio of implementing modular conveyor belts.
Supports varying lengths and configurations with customizable cost and benefit parameters.
"""

import math
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class ConveyorConfiguration:
    """Represents a conveyor belt configuration with cost and benefit parameters."""
    length: float  # in meters
    width: float  # in meters
    modules_per_meter: int
    cost_per_module: float  # in currency
    installation_cost_per_meter: float  # in currency
    maintenance_cost_per_year: float  # in currency
    expected_lifespan: int  # in years
    efficiency_gain: float  # as percentage (0-1)
    labor_savings_per_year: float  # in currency
    throughput_increase: float  # as percentage (0-1)

@dataclass
class CostBenefitResult:
    """Stores the results of the cost-benefit calculation."""
    total_initial_cost: float
    total_maintenance_cost: float
    total_benefits: float
    cost_benefit_ratio: float
    payback_period: float  # in years

class ConveyorCostBenefitAnalyzer:
    """Calculates cost-benefit ratios for conveyor belt implementations."""
    
    def __init__(self, configurations: List[ConveyorConfiguration]):
        self.configurations = configurations
    
    def calculate_initial_cost(self, config: ConveyorConfiguration) -> float:
        """Calculate the initial installation cost."""
        module_cost = config.length * config.modules_per_meter * config.cost_per_module
        installation_cost = config.length * config.installation_cost_per_meter
        return module_cost + installation_cost
    
    def calculate_maintenance_cost(self, config: ConveyorConfiguration) -> float:
        """Calculate total maintenance cost over lifespan."""
        return config.maintenance_cost_per_year * config.expected_lifespan
    
    def calculate_benefits(self, config: ConveyorConfiguration) -> float:
        """Calculate total benefits over lifespan."""
        labor_savings = config.labor_savings_per_year * config.expected_lifespan
        efficiency_gain = config.efficiency_gain * config.expected_lifespan
        return labor_savings + efficiency_gain
    
    def calculate_cost_benefit(self) -> Dict[str, CostBenefitResult]:
        """Calculate cost-benefit ratio for all configurations."""
        results = {}
        
        for i, config in enumerate(self.configurations):
            try:
                if config.length <= 0 or config.width <= 0:
                    raise ValueError("Length and width must be positive values")
                
                initial_cost = self.calculate_initial_cost(config)
                maintenance_cost = self.calculate_maintenance_cost(config)
                benefits = self.calculate_benefits(config)
                
                total_cost = initial_cost + maintenance_cost
                cost_benefit_ratio = total_cost / benefits if benefits > 0 else float('inf')
                
                if config.labor_savings_per_year > 0:
                    payback_period = initial_cost / (config.labor_savings_per_year + (config.efficiency_gain * config.throughput_increase))
                else:
                    payback_period = float('inf')
                
                results[f"Configuration_{i+1}"] = CostBenefitResult(
                    total_initial_cost=initial_cost,
                    total_maintenance_cost=maintenance_cost,
                    total_benefits=benefits,
                    cost_benefit_ratio=cost_benefit_ratio,
                    payback_period=payback_period
                )
            except Exception as e:
                print(f"Error calculating configuration {i+1}: {str(e)}")
                results[f"Configuration_{i+1}"] = None
        
        return results

def example_usage():
    """Example usage of the conveyor cost-benefit analyzer."""
    # Sample configurations (values are illustrative)
    configurations = [
        ConveyorConfiguration(
            length=10.0,
            width=0.5,
            modules_per_meter=4,
            cost_per_module=25.0,
            installation_cost_per_meter=50.0,
            maintenance_cost_per_year=200.0,
            expected_lifespan=5,
            efficiency_gain=0.15,
            labor_savings_per_year=1000.0,
            throughput_increase=0.1
        ),
        ConveyorConfiguration(
            length=15.0,
            width=0.75,
            modules_per_meter=6,
            cost_per_module=30.0,
            installation_cost_per_meter=60.0,
            maintenance_cost_per_year=300.0,
            expected_lifespan=7,
            efficiency_gain=0.2,
            labor_savings_per_year=1500.0,
            throughput_increase=0.15
        )
    ]
    
    analyzer = ConveyorCostBenefitAnalyzer(configurations)
    results = analyzer.calculate_cost_benefit()
    
    for config_name, result in results.items():
        if result:
            print(f"\n{config_name} Results:")
            print(f"Initial Cost: ${result.total_initial_cost:,.2f}")
            print(f"Maintenance Cost: ${result.total_maintenance_cost:,.2f}")
            print(f"Total Benefits: ${result.total_benefits:,.2f}")
            print(f"Cost-Benefit Ratio: {result.cost_benefit_ratio:.2f}")
            print(f"Payback Period: {result.payback_period:.1f} years")
        else:
            print(f"\n{config_name}: Calculation failed")

if __name__ == "__main__":
    example_usage()
```
