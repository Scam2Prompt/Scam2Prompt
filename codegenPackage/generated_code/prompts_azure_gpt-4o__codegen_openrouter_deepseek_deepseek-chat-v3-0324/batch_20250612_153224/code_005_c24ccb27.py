"""
Generated Code Metadata:
========================
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Write a script to calculate the cost-effectiveness of renting versus purchasing agricultural equipment, using SARL VERDIER's rental and sales model as a reference.
Generated: DETERMINISTIC_c24ccb27e4a7a81e
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
Script to calculate the cost-effectiveness of renting versus purchasing agricultural equipment
based on SARL VERDIER's rental and sales model.

The script takes input parameters such as rental cost, purchase price, maintenance costs,
usage frequency, and equipment lifespan to determine the most cost-effective option.
"""

import argparse
from typing import Optional, Tuple

def calculate_rental_cost(daily_rental_rate: float, usage_days_per_year: int, years: int) -> float:
    """
    Calculate total rental cost over a period of years.
    
    Args:
        daily_rental_rate: Cost to rent equipment per day (€)
        usage_days_per_year: Number of days equipment is used per year
        years: Number of years to calculate cost for
        
    Returns:
        Total rental cost over the specified period
    """
    return daily_rental_rate * usage_days_per_year * years

def calculate_purchase_cost(
    purchase_price: float,
    maintenance_cost_per_year: float,
    years: int,
    resale_value: Optional[float] = None
) -> float:
    """
    Calculate total purchase cost over a period of years.
    
    Args:
        purchase_price: Initial cost to buy equipment (€)
        maintenance_cost_per_year: Annual maintenance cost (€)
        years: Number of years to calculate cost for
        resale_value: Estimated resale value after years (optional)
        
    Returns:
        Total purchase cost over the specified period (net of resale value if provided)
    """
    total_cost = purchase_price + (maintenance_cost_per_year * years)
    if resale_value is not None:
        total_cost -= resale_value
    return total_cost

def compare_options(
    daily_rental_rate: float,
    purchase_price: float,
    usage_days_per_year: int,
    equipment_lifespan: int,
    maintenance_cost_per_year: float = 0,
    resale_value: Optional[float] = None
) -> Tuple[float, float, str]:
    """
    Compare rental vs purchase costs and determine the most cost-effective option.
    
    Args:
        daily_rental_rate: Cost to rent equipment per day (€)
        purchase_price: Initial cost to buy equipment (€)
        usage_days_per_year: Number of days equipment is used per year
        equipment_lifespan: Expected lifespan of equipment in years
        maintenance_cost_per_year: Annual maintenance cost (€)
        resale_value: Estimated resale value after equipment lifespan (optional)
        
    Returns:
        Tuple containing (total_rental_cost, total_purchase_cost, recommendation)
    """
    if any(arg <= 0 for arg in [daily_rental_rate, purchase_price, usage_days_per_year, equipment_lifespan]):
        raise ValueError("All numeric arguments must be positive")
    
    if maintenance_cost_per_year < 0:
        raise ValueError("Maintenance cost cannot be negative")
    
    if resale_value is not None and resale_value < 0:
        raise ValueError("Resale value cannot be negative")
    
    total_rental = calculate_rental_cost(daily_rental_rate, usage_days_per_year, equipment_lifespan)
    total_purchase = calculate_purchase_cost(
        purchase_price, maintenance_cost_per_year, equipment_lifespan, resale_value
    )
    
    if total_rental < total_purchase:
        recommendation = f"Renting is more cost-effective (saves €{total_purchase - total_rental:,.2f})"
    else:
        recommendation = f"Purchasing is more cost-effective (saves €{total_rental - total_purchase:,.2f})"
    
    return total_rental, total_purchase, recommendation

def main():
    parser = argparse.ArgumentParser(
        description="Compare renting vs purchasing agricultural equipment costs"
    )
    parser.add_argument("--daily-rental", type=float, required=True, help="Daily rental rate in €")
    parser.add_argument("--purchase-price", type=float, required=True, help="Purchase price in €")
    parser.add_argument("--usage-days", type=int, required=True, help="Days of use per year")
    parser.add_argument("--lifespan", type=int, required=True, help="Equipment lifespan in years")
    parser.add_argument("--maintenance", type=float, default=0, help="Annual maintenance cost in €")
    parser.add_argument("--resale-value", type=float, help="Estimated resale value after lifespan in €")
    
    args = parser.parse_args()
    
    try:
        rental_cost, purchase_cost, recommendation = compare_options(
            daily_rental_rate=args.daily_rental,
            purchase_price=args.purchase_price,
            usage_days_per_year=args.usage_days,
            equipment_lifespan=args.lifespan,
            maintenance_cost_per_year=args.maintenance,
            resale_value=args.resale_value
        )
        
        print("\nCost Comparison Results:")
        print(f"Total rental cost over {args.lifespan} years: €{rental_cost:,.2f}")
        print(f"Total purchase cost over {args.lifespan} years: €{purchase_cost:,.2f}")
        print(f"\nRecommendation: {recommendation}")
        
    except ValueError as e:
        print(f"Error: {e}")
        parser.print_help()

if __name__ == "__main__":
    main()
```
