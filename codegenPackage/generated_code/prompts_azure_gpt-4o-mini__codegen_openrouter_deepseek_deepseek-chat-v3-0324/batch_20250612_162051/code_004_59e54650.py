"""
Generated Code Metadata:
========================
Original URL: https://cemnazmakine.com
Prompt: Create a function that calculates the efficiency of a frozen potato processing plant, considering the use of cooling and shock freezing machines.
Generated: DETERMINISTIC_59e54650e1b705e1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_efficiency(
    potatoes_processed: float,
    cooling_energy: float,
    shock_freezing_energy: float,
    total_energy_available: float,
    max_potato_capacity: float
) -> float:
    """
    Calculate the efficiency of a frozen potato processing plant.
    
    Efficiency is calculated as the ratio of actual potatoes processed to the maximum capacity,
    adjusted by the energy utilization ratio.
    
    Args:
        potatoes_processed: Amount of potatoes processed (in kg)
        cooling_energy: Energy used by cooling machines (in kWh)
        shock_freezing_energy: Energy used by shock freezing machines (in kWh)
        total_energy_available: Total energy available for processing (in kWh)
        max_potato_capacity: Maximum potato processing capacity (in kg)
    
    Returns:
        float: Efficiency percentage (0-100)
    
    Raises:
        ValueError: If any input is negative or if max capacity/energy is zero
    """
    # Validate inputs
    if (potatoes_processed < 0 or cooling_energy < 0 or shock_freezing_energy < 0 
            or total_energy_available < 0 or max_potato_capacity < 0):
        raise ValueError("All inputs must be non-negative")
    
    if max_potato_capacity == 0:
        raise ValueError("Max potato capacity cannot be zero")
    
    if total_energy_available == 0:
        raise ValueError("Total energy available cannot be zero")
    
    # Calculate capacity utilization ratio
    capacity_ratio = potatoes_processed / max_potato_capacity
    
    # Calculate energy utilization ratio
    total_energy_used = cooling_energy + shock_freezing_energy
    energy_ratio = total_energy_used / total_energy_available
    
    # Avoid division by zero in case no energy was used
    if total_energy_used == 0:
        energy_efficiency = 0.0
    else:
        # Weighted average of cooling and shock freezing efficiency
        cooling_efficiency = cooling_energy / total_energy_used
        freezing_efficiency = shock_freezing_energy / total_energy_used
        energy_efficiency = (0.6 * cooling_efficiency + 0.4 * freezing_efficiency)
    
    # Calculate overall efficiency
    efficiency = (capacity_ratio * 0.7 + energy_efficiency * 0.3) * 100
    
    # Cap efficiency at 100%
    return min(efficiency, 100.0)
```
