"""
Generated Code Metadata:
========================
Original URL: https://trindadetelecom.com.br
Prompt: Write a Python script to compare internet plans with different speeds and prices, such as 333 MEGA for R$ 99,90, 555 MEGA for R$ 109,90, and 888 MEGA for R$ 129,90, and determine which one is the best value.
Generated: DETERMINISTIC_0108b372b3241eaf
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from dataclasses import dataclass
from typing import List

@dataclass
class InternetPlan:
    """Class representing an internet plan with speed and price."""
    name: str
    speed_mbps: float
    price: float

def calculate_value(speed: float, price: float) -> float:
    """Calculate the value ratio (speed per unit price)."""
    if price <= 0:
        raise ValueError("Price must be greater than zero.")
    return speed / price

def compare_plans(plans: List[InternetPlan]) -> InternetPlan:
    """
    Compare internet plans and return the one with best value (highest speed/price ratio).
    
    Args:
        plans: List of InternetPlan objects to compare
        
    Returns:
        InternetPlan: The plan with the best value
        
    Raises:
        ValueError: If plans list is empty
    """
    if not plans:
        raise ValueError("No plans provided for comparison.")
    
    best_plan = None
    best_value = -1
    
    for plan in plans:
        try:
            current_value = calculate_value(plan.speed_mbps, plan.price)
            if current_value > best_value:
                best_value = current_value
                best_plan = plan
        except ValueError as e:
            print(f"Error processing plan {plan.name}: {e}", file=sys.stderr)
    
    return best_plan

def main():
    """Main function to demonstrate plan comparison."""
    # Example plans data
    plans = [
        InternetPlan("333 MEGA", 333, 99.90),
        InternetPlan("555 MEGA", 555, 109.90),
        InternetPlan("888 MEGA", 888, 129.90)
    ]
    
    try:
        best_plan = compare_plans(plans)
        if best_plan:
            print(f"Best value plan: {best_plan.name}")
            print(f"Speed: {best_plan.speed_mbps} Mbps")
            print(f"Price: R$ {best_plan.price:.2f}")
            print(f"Value ratio: {calculate_value(best_plan.speed_mbps, best_plan.price):.2f} Mbps/R$")
        else:
            print("No valid plans found for comparison.")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
