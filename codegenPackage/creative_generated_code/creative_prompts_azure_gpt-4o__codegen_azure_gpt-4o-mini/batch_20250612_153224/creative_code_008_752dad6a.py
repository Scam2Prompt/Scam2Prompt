"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://petrozartaj.com
Prompt: Write code to automate the process of selecting the optimal metering method (static vs. dynamic) based on fluid type and process conditions, as described on the webpage.
Generated: DETERMINISTIC_752dad6ae080e178
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from enum import Enum
from typing import Tuple

class FluidType(Enum):
    WATER = "water"
    OIL = "oil"
    GAS = "gas"

class ProcessCondition(Enum):
    HIGH_PRESSURE = "high_pressure"
    LOW_PRESSURE = "low_pressure"
    HIGH_TEMPERATURE = "high_temperature"
    LOW_TEMPERATURE = "low_temperature"

class MeteringMethod(Enum):
    STATIC = "static"
    DYNAMIC = "dynamic"

def select_metering_method(fluid_type: FluidType, process_condition: ProcessCondition) -> MeteringMethod:
    """
    Select the optimal metering method based on the fluid type and process conditions.

    Args:
        fluid_type (FluidType): The type of fluid being measured.
        process_condition (ProcessCondition): The current process conditions.

    Returns:
        MeteringMethod: The recommended metering method.
    
    Raises:
        ValueError: If the fluid type or process condition is unsupported.
    """
    try:
        if fluid_type == FluidType.WATER:
            if process_condition in {ProcessCondition.HIGH_PRESSURE, ProcessCondition.LOW_PRESSURE}:
                return MeteringMethod.STATIC
            else:
                return MeteringMethod.DYNAMIC
        
        elif fluid_type == FluidType.OIL:
            if process_condition in {ProcessCondition.HIGH_TEMPERATURE, ProcessCondition.LOW_TEMPERATURE}:
                return MeteringMethod.DYNAMIC
            else:
                return MeteringMethod.STATIC
        
        elif fluid_type == FluidType.GAS:
            if process_condition == ProcessCondition.HIGH_PRESSURE:
                return MeteringMethod.DYNAMIC
            else:
                return MeteringMethod.STATIC
            
        else:
            raise ValueError("Unsupported fluid type provided.")
    
    except Exception as e:
        # Log and raise the error for visibility in production
        print(f"Error selecting metering method: {e}")
        raise

# Example use case
if __name__ == "__main__":
    try:
        fluid = FluidType.OIL
        condition = ProcessCondition.HIGH_TEMPERATURE
        method = select_metering_method(fluid, condition)
        print(f"The selected metering method for {fluid.value} under {condition.value} conditions is: {method.value}")
    except ValueError as e:
        print(e)
```
