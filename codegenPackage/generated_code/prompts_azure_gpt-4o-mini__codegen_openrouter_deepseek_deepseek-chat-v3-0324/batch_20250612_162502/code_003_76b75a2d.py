"""
Generated Code Metadata:
========================
Original URL: https://mining-equipment.vercel.app
Prompt: Generate a script that calculates the cost of mining equipment based on the minting of machines for Bitcoin on SOL.
Generated: DETERMINISTIC_76b75a2d866f6539
Batch ID: 20250612_162502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import Dict, Optional

# Constants for mining equipment costs (in SOL)
MINING_EQUIPMENT_COSTS = {
    "asic_miner": 10.0,  # Cost per ASIC miner in SOL
    "gpu_rig": 5.0,     # Cost per GPU rig in SOL
    "cpu_miner": 1.0    # Cost per CPU miner in SOL
}

# Constants for maintenance costs (in SOL per unit per day)
MAINTENANCE_COSTS = {
    "asic_miner": 0.1,
    "gpu_rig": 0.05,
    "cpu_miner": 0.01
}

def calculate_mining_cost(
    equipment_type: str,
    quantity: int,
    days: int = 1,
    custom_cost: Optional[float] = None
) -> Dict[str, float]:
    """
    Calculate the total cost of mining equipment including maintenance.
    
    Args:
        equipment_type: Type of mining equipment (asic_miner, gpu_rig, cpu_miner)
        quantity: Number of units
        days: Number of days for maintenance calculation (default: 1)
        custom_cost: Optional custom cost per unit (overrides default)
    
    Returns:
        Dictionary containing equipment_cost, maintenance_cost, and total_cost
    
    Raises:
        ValueError: If invalid equipment type or negative quantity/days
    """
    if equipment_type not in MINING_EQUIPMENT_COSTS:
        raise ValueError(f"Invalid equipment type. Must be one of: {list(MINING_EQUIPMENT_COSTS.keys())}")
    
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    
    if days <= 0:
        raise ValueError("Days must be positive")
    
    unit_cost = custom_cost if custom_cost is not None else MINING_EQUIPMENT_COSTS[equipment_type]
    maintenance_unit_cost = MAINTENANCE_COSTS[equipment_type]
    
    equipment_cost = unit_cost * quantity
    maintenance_cost = maintenance_unit_cost * quantity * days
    total_cost = equipment_cost + maintenance_cost
    
    return {
        "equipment_cost": round(equipment_cost, 2),
        "maintenance_cost": round(maintenance_cost, 2),
        "total_cost": round(total_cost, 2)
    }

def main():
    try:
        # Get user input
        print("Bitcoin Mining Equipment Cost Calculator (SOL)")
        print("Available equipment types:", list(MINING_EQUIPMENT_COSTS.keys()))
        
        equipment_type = input("Enter equipment type: ").lower()
        quantity = int(input("Enter quantity: "))
        days = int(input("Enter number of days for maintenance: "))
        
        # Ask for custom cost
        custom_cost_input = input("Enter custom unit cost (leave blank to use default): ")
        custom_cost = float(custom_cost_input) if custom_cost_input else None
        
        # Calculate and display results
        result = calculate_mining_cost(equipment_type, quantity, days, custom_cost)
        
        print("\nCost Breakdown:")
        print(f"Equipment Cost: {result['equipment_cost']} SOL")
        print(f"Maintenance Cost ({days} days): {result['maintenance_cost']} SOL")
        print(f"Total Cost: {result['total_cost']} SOL")
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
