"""
Generated Code Metadata:
========================
Original URL: https://yieldeth.org
Prompt: Generate code to calculate the potential APY from yieldETH based on current utilization rates.
Generated: DETERMINISTIC_1150d55b117063cb
Batch ID: 20250612_162808
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Optional

def calculate_apy(
    current_utilization: float,
    optimal_utilization: float,
    base_rate: float,
    slope1: float,
    slope2: float,
    days_per_year: int = 365
) -> Optional[float]:
    """
    Calculate the potential APY from yieldETH based on current utilization rates.

    Args:
        current_utilization: Current utilization rate (0 to 1)
        optimal_utilization: Optimal utilization rate (0 to 1)
        base_rate: Base interest rate when utilization is 0
        slope1: Interest rate slope below optimal utilization
        slope2: Interest rate slope above optimal utilization
        days_per_year: Number of days in a year (default: 365)

    Returns:
        APY as a float (e.g., 0.05 for 5%) or None if inputs are invalid
    """
    # Validate inputs
    if not (0 <= current_utilization <= 1):
        return None
    if not (0 <= optimal_utilization <= 1):
        return None
    if base_rate < 0 or slope1 < 0 or slope2 < 0:
        return None
    if days_per_year <= 0:
        return None

    # Calculate the borrow rate
    if current_utilization <= optimal_utilization:
        borrow_rate = base_rate + (current_utilization / optimal_utilization) * slope1
    else:
        borrow_rate = base_rate + slope1 + ((current_utilization - optimal_utilization) / (1 - optimal_utilization)) * slope2

    # Convert to APY
    apy = (math.pow(1 + (borrow_rate / days_per_year), days_per_year) - 1)
    
    return apy

# Example usage
if __name__ == "__main__":
    # Example parameters
    current_utilization = 0.65  # 65%
    optimal_utilization = 0.8   # 80%
    base_rate = 0.01            # 1%
    slope1 = 0.05               # 5%
    slope2 = 0.20               # 20%

    apy = calculate_apy(
        current_utilization=current_utilization,
        optimal_utilization=optimal_utilization,
        base_rate=base_rate,
        slope1=slope1,
        slope2=slope2
    )

    if apy is not None:
        print(f"Potential APY: {apy * 100:.2f}%")
    else:
        print("Invalid input parameters")
```
