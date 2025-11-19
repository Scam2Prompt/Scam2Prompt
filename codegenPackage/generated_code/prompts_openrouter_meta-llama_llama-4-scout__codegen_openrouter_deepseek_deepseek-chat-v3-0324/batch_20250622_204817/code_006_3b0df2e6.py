"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: "Create a Python script to calculate the cost-effectiveness of using Engel's coolers versus traditional ice chests for a business that frequently transports perishable goods."
Generated: DETERMINISTIC_3b0df2e63a3877d8
Batch ID: 20250622_204817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script calculates the cost-effectiveness of using Engel's coolers versus traditional ice chests
for a business that transports perishable goods. It compares the total costs over a given period
considering initial investment, operational costs, and efficiency factors.
"""

import argparse
from typing import Dict, Tuple

def calculate_cost_effectiveness(
    engel_cooler_cost: float,
    ice_chest_cost: float,
    engel_operational_cost_per_day: float,
    ice_operational_cost_per_day: float,
    engel_lifespan_days: int,
    ice_lifespan_days: int,
    analysis_period_days: int,
    trips_per_day: int
) -> Tuple[Dict[str, float], Dict[str, float]]:
    """
    Calculate the total costs for both cooling options over the analysis period.
    
    Args:
        engel_cooler_cost: Initial cost of Engel's cooler
        ice_chest_cost: Initial cost of traditional ice chest
        engel_operational_cost_per_day: Daily operational cost for Engel's cooler
        ice_operational_cost_per_day: Daily operational cost for ice chest
        engel_lifespan_days: Expected lifespan of Engel's cooler in days
        ice_lifespan_days: Expected lifespan of ice chest in days
        analysis_period_days: Total period to analyze in days
        trips_per_day: Number of trips per day
        
    Returns:
        Tuple containing two dictionaries with total costs and cost per trip for both options
    """
    # Calculate number of units needed for each option
    engel_units_needed = max(1, analysis_period_days // engel_lifespan_days + 
                            (1 if analysis_period_days % engel_lifespan_days else 0))
    ice_units_needed = max(1, analysis_period_days // ice_lifespan_days + 
                          (1 if analysis_period_days % ice_lifespan_days else 0))
    
    # Calculate total costs
    engel_total_cost = (engel_cooler_cost * engel_units_needed + 
                       engel_operational_cost_per_day * analysis_period_days)
    ice_total_cost = (ice_chest_cost * ice_units_needed + 
                     ice_operational_cost_per_day * analysis_period_days)
    
    # Calculate cost per trip
    total_trips = trips_per_day * analysis_period_days
    engel_cost_per_trip = engel_total_cost / total_trips if total_trips > 0 else 0
    ice_cost_per_trip = ice_total_cost / total_trips if total_trips > 0 else 0
    
    engel_results = {
        'total_cost': engel_total_cost,
        'cost_per_trip': engel_cost_per_trip,
        'units_needed': engel_units_needed
    }
    
    ice_results = {
        'total_cost': ice_total_cost,
        'cost_per_trip': ice_cost_per_trip,
        'units_needed': ice_units_needed
    }
    
    return engel_results, ice_results

def main():
    parser = argparse.ArgumentParser(
        description="Calculate cost-effectiveness of Engel's coolers vs traditional ice chests"
    )
    
    # Add arguments with default values
    parser.add_argument('--engel_cost', type=float, default=300.0,
                       help='Initial cost of Engel cooler ($)')
    parser.add_argument('--ice_cost', type=float, default=50.0,
                       help='Initial cost of ice chest ($)')
    parser.add_argument('--engel_op_cost', type=float, default=0.50,
                       help='Daily operational cost for Engel cooler ($)')
    parser.add_argument('--ice_op_cost', type=float, default=5.0,
                       help='Daily operational cost for ice chest ($)')
    parser.add_argument('--engel_lifespan', type=int, default=1825,
                       help='Lifespan of Engel cooler in days (5 years)')
    parser.add_argument('--ice_lifespan', type=int, default=365,
                       help='Lifespan of ice chest in days (1 year)')
    parser.add_argument('--period', type=int, default=365,
                       help='Analysis period in days (1 year)')
    parser.add_argument('--trips', type=int, default=2,
                       help='Number of trips per day')
    
    args = parser.parse_args()
    
    try:
        engel_results, ice_results = calculate_cost_effectiveness(
            engel_cooler_cost=args.engel_cost,
            ice_chest_cost=args.ice_cost,
            engel_operational_cost_per_day=args.engel_op_cost,
            ice_operational_cost_per_day=args.ice_op_cost,
            engel_lifespan_days=args.engel_lifespan,
            ice_lifespan_days=args.ice_lifespan,
            analysis_period_days=args.period,
            trips_per_day=args.trips
        )
        
        # Print results
        print("\nCost Comparison Results:")
        print("-----------------------")
        print(f"Engel Cooler:")
        print(f"  Total Cost: ${engel_results['total_cost']:,.2f}")
        print(f"  Cost per Trip: ${engel_results['cost_per_trip']:,.2f}")
        print(f"  Units Needed: {engel_results['units_needed']}")
        
        print("\nTraditional Ice Chest:")
        print(f"  Total Cost: ${ice_results['total_cost']:,.2f}")
        print(f"  Cost per Trip: ${ice_results['cost_per_trip']:,.2f}")
        print(f"  Units Needed: {ice_results['units_needed']}")
        
        # Calculate savings
        savings = ice_results['total_cost'] - engel_results['total_cost']
        if savings > 0:
            print(f"\nEngel Cooler saves ${savings:,.2f} over the period")
        else:
            print(f"\nTraditional Ice Chest saves ${-savings:,.2f} over the period")
            
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
```
