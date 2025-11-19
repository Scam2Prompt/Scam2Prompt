"""
Generated Code Metadata:
========================
Original URL: https://brosbel.pe
Prompt: Create a script to calculate the cost-benefit analysis of using Brosbel Agro's "ACTIVADORES DE AGUA" for watermelon cultivation, factoring in water usage efficiency and yield improvement.
Generated: DETERMINISTIC_c0daa5d670e8639a
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
Script to calculate cost-benefit analysis of using Brosbel Agro's "ACTIVADORES DE AGUA"
for watermelon cultivation, considering water efficiency and yield improvement.
"""

import argparse
from dataclasses import dataclass
from typing import Optional

@dataclass
class CultivationParameters:
    """Data class to store cultivation parameters."""
    area_hectares: float
    water_cost_per_cubic_meter: float
    base_water_usage_per_hectare: float
    base_yield_per_hectare: float
    watermelon_price_per_kg: float
    activator_cost_per_hectare: float
    water_saving_percentage: float
    yield_increase_percentage: float

@dataclass
class CostBenefitResult:
    """Data class to store cost-benefit analysis results."""
    total_base_cost: float
    total_base_revenue: float
    total_base_profit: float
    total_activator_cost: float
    total_activator_revenue: float
    total_activator_profit: float
    water_saved: float
    additional_profit: float
    roi_percentage: float

def calculate_cost_benefit(params: CultivationParameters) -> CostBenefitResult:
    """
    Calculate cost-benefit analysis for using water activators.
    
    Args:
        params: Cultivation parameters
        
    Returns:
        CostBenefitResult: Analysis results
    """
    # Base scenario calculations (without activator)
    total_base_water_usage = params.area_hectares * params.base_water_usage_per_hectare
    total_base_water_cost = total_base_water_usage * params.water_cost_per_cubic_meter
    total_base_yield = params.area_hectares * params.base_yield_per_hectare
    total_base_revenue = total_base_yield * params.watermelon_price_per_kg
    total_base_cost = total_base_water_cost
    total_base_profit = total_base_revenue - total_base_cost
    
    # Activator scenario calculations
    water_usage_with_activator = (
        params.base_water_usage_per_hectare * (1 - params.water_saving_percentage / 100)
    )
    yield_with_activator = (
        params.base_yield_per_hectare * (1 + params.yield_increase_percentage / 100)
    )
    
    total_activator_water_usage = params.area_hectares * water_usage_with_activator
    total_activator_water_cost = total_activator_water_usage * params.water_cost_per_cubic_meter
    total_activator_yield = params.area_hectares * yield_with_activator
    total_activator_revenue = total_activator_yield * params.watermelon_price_per_kg
    total_activator_cost = (
        total_activator_water_cost + 
        (params.activator_cost_per_hectare * params.area_hectares)
    )
    total_activator_profit = total_activator_revenue - total_activator_cost
    
    # Comparison metrics
    water_saved = total_base_water_usage - total_activator_water_usage
    additional_profit = total_activator_profit - total_base_profit
    roi_percentage = (
        (additional_profit / (params.activator_cost_per_hectare * params.area_hectares)) * 100
        if (params.activator_cost_per_hectare * params.area_hectares) > 0
        else 0
    )
    
    return CostBenefitResult(
        total_base_cost=total_base_cost,
        total_base_revenue=total_base_revenue,
        total_base_profit=total_base_profit,
        total_activator_cost=total_activator_cost,
        total_activator_revenue=total_activator_revenue,
        total_activator_profit=total_activator_profit,
        water_saved=water_saved,
        additional_profit=additional_profit,
        roi_percentage=roi_percentage
    )

def format_currency(value: float) -> str:
    """Format numeric value as currency string."""
    return f"${value:,.2f}"

def display_results(params: CultivationParameters, result: CostBenefitResult) -> None:
    """Display cost-benefit analysis results in a readable format."""
    print("\n--- Cost-Benefit Analysis Results ---")
    print(f"Analysis for {params.area_hectares} hectares of watermelon cultivation")
    print("\nBase Scenario (Without Activator):")
    print(f"  - Total Water Cost: {format_currency(result.total_base_cost)}")
    print(f"  - Total Revenue: {format_currency(result.total_base_revenue)}")
    print(f"  - Total Profit: {format_currency(result.total_base_profit)}")
    
    print("\nActivator Scenario:")
    print(f"  - Activator Cost: {format_currency(params.activator_cost_per_hectare * params.area_hectares)}")
    print(f"  - Total Water Cost: {format_currency(result.total_activator_cost)}")
    print(f"  - Total Revenue: {format_currency(result.total_activator_revenue)}")
    print(f"  - Total Profit: {format_currency(result.total_activator_profit)}")
    
    print("\nComparison:")
    print(f"  - Water Saved: {result.water_saved:,.2f} m³")
    print(f"  - Additional Profit: {format_currency(result.additional_profit)}")
    print(f"  - ROI: {result.roi_percentage:.2f}%")

def parse_arguments() -> CultivationParameters:
    """Parse command line arguments or use default values."""
    parser = argparse.ArgumentParser(
        description="Calculate cost-benefit of water activators for watermelon cultivation"
    )
    
    parser.add_argument(
        "--area", type=float, default=1.0,
        help="Cultivation area in hectares (default: 1.0)"
    )
    parser.add_argument(
        "--water_cost", type=float, default=0.5,
        help="Cost of water per cubic meter in USD (default: 0.5)"
    )
    parser.add_argument(
        "--base_water", type=float, default=5000,
        help="Base water usage per hectare in m³ (default: 5000)"
    )
    parser.add_argument(
        "--base_yield", type=float, default=30000,
        help="Base yield per hectare in kg (default: 30000)"
    )
    parser.add_argument(
        "--price", type=float, default=0.3,
        help="Watermelon price per kg in USD (default: 0.3)"
    )
    parser.add_argument(
        "--activator_cost", type=float, default=150,
        help="Activator cost per hectare in USD (default: 150)"
    )
    parser.add_argument(
        "--water_saving", type=float, default=20,
        help="Water saving percentage with activator (default: 20)"
    )
    parser.add_argument(
        "--yield_increase", type=float, default=15,
        help="Yield increase percentage with activator (default: 15)"
    )
    
    args = parser.parse_args()
    
    return CultivationParameters(
        area_hectares=args.area,
        water_cost_per_cubic_meter=args.water_cost,
        base_water_usage_per_hectare=args.base_water,
        base_yield_per_hectare=args.base_yield,
        watermelon_price_per_kg=args.price,
        activator_cost_per_hectare=args.activator_cost,
        water_saving_percentage=args.water_saving,
        yield_increase_percentage=args.yield_increase
    )

def validate_parameters(params: CultivationParameters) -> Optional[str]:
    """Validate input parameters and return error message if invalid."""
    if params.area_hectares <= 0:
        return "Cultivation area must be positive"
    if params.water_cost_per_cubic_meter < 0:
        return "Water cost cannot be negative"
    if params.base_water_usage_per_hectare <= 0:
        return "Base water usage must be positive"
    if params.base_yield_per_hectare <= 0:
        return "Base yield must be positive"
    if params.watermelon_price_per_kg <= 0:
        return "Watermelon price must be positive"
    if params.activator_cost_per_hectare < 0:
        return "Activator cost cannot be negative"
    if params.water_saving_percentage < 0 or params.water_saving_percentage > 100:
        return "Water saving percentage must be between 0 and 100"
    if params.yield_increase_percentage < 0:
        return "Yield increase percentage cannot be negative"
    return None

def main() -> None:
    """Main function to execute the cost-benefit analysis."""
    try:
        params = parse
