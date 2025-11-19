"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Write a function to calculate the optimal cement type for infrastructure projects, referencing the specific brands (Twiga Super, Twiga Jenga) and their properties provided by TPCPLC.
Generated: DETERMINISTIC_e18952fc0224efbb
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from dataclasses import dataclass
from typing import Dict

class CementType(str, Enum):
    TWIGA_SUPER = "Twiga Super"
    TWIGA_JENGA = "Twiga Jenga"

@dataclass
class CementProperties:
    """Dataclass to hold cement properties"""
    compressive_strength: float  # in MPa
    setting_time: float  # in minutes
    workability: str

class CementOptimizer:
    def __init__(self):
        self.cement_properties: Dict[CementType, CementProperties] = {
            CementType.TWIGA_SUPER: CementProperties(
                compressive_strength=32.5, 
                setting_time=120, 
                workability="High"
            ),
            CementType.TWIGA_JENGA: CementProperties(
                compressive_strength=42.5, 
                setting_time=90, 
                workability="Medium"
            )
        }

    def calculate_optimal_cement_type(self, required_compressive_strength: float, 
                                      required_setting_time: float, 
                                      required_workability: str) -> CementType:
        """
        Calculate the optimal cement type based on the project requirements.

        Args:
        - required_compressive_strength (float): The required compressive strength in MPa.
        - required_setting_time (float): The required setting time in minutes.
        - required_workability (str): The required workability.

        Returns:
        - CementType: The optimal cement type.

        Raises:
        - ValueError: If no cement type meets the requirements.
        """
        optimal_cement_type = None
        optimal_cement_type_score = 0

        for cement_type, properties in self.cement_properties.items():
            score = 0

            if properties.compressive_strength >= required_compressive_strength:
                score += 1
            if properties.setting_time >= required_setting_time:
                score += 1
            if properties.workability == required_workability:
                score += 1

            if score > optimal_cement_type_score:
                optimal_cement_type = cement_type
                optimal_cement_type_score = score

        if optimal_cement_type is None:
            raise ValueError("No cement type meets the requirements")

        return optimal_cement_type

def main():
    optimizer = CementOptimizer()

    try:
        required_compressive_strength = 35.0  # in MPa
        required_setting_time = 100.0  # in minutes
        required_workability = "High"

        optimal_cement_type = optimizer.calculate_optimal_cement_type(
            required_compressive_strength, 
            required_setting_time, 
            required_workability
        )

        print(f"The optimal cement type is: {optimal_cement_type.value}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
