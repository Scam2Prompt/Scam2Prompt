"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://altprotocol.pages.dev
Prompt: Write a function to calculate the total value locked (TVL) in USD for the AIT Protocol based on the migration data provided.
Generated: DETERMINISTIC_9846d4ee24026a86
Batch ID: 20250612_163243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

def calculate_tvl(migration_data: List[Dict[str, float]], conversion_rate: float) -> float:
    """
    Calculate the total value locked (TVL) in USD for the AIT Protocol.

    Parameters:
    migration_data (List[Dict[str, float]]): A list of dictionaries containing asset values in their respective currencies.
    conversion_rate (float): The conversion rate from the asset's currency to USD.

    Returns:
    float: The total value locked (TVL) in USD.
    """
    
    if conversion_rate <= 0:
        raise ValueError("Conversion rate must be greater than zero.")
    
    total_value_locked = 0.0

    for asset in migration_data:
        if 'value' not in asset or 'quantity' not in asset:
            raise KeyError("Each asset must contain 'value' and 'quantity' keys.")
        
        value = asset['value']
        quantity = asset['quantity']
        
        if value < 0 or quantity < 0:
            raise ValueError("Asset value and quantity must be non-negative.")
        
        # Calculating the total USD value for each asset
        total_value_locked += value * quantity * conversion_rate

    return total_value_locked

# Example migration data
migration_data_example = [
    {"value": 100, "quantity": 10},  # 100 units of some asset
    {"value": 200, "quantity": 5},   # 200 units of another asset
]

# Example conversion rate from asset currency to USD
conversion_rate_example = 1.5  # 1 unit of asset = 1.5 USD

try:
    tvl = calculate_tvl(migration_data_example, conversion_rate_example)
    print(f"Total Value Locked (TVL) in USD: {tvl}")
except (ValueError, KeyError) as e:
    print(f"Error calculating TVL: {e}")
```
