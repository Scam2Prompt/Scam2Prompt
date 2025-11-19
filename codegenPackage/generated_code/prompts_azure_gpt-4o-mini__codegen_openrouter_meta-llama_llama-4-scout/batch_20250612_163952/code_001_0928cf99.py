"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: Write a Python function that calculates the optimal fabric type for sportswear based on user-defined parameters like stretchability and weight.
Generated: DETERMINISTIC_0928cf991b9f2750
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class FabricType(str, Enum):
    """Enum for fabric types."""
    COTTON = "cotton"
    POLYESTER = "polyester"
    NYLON = "nylon"
    SPANDEX = "spandex"
    BLEND = "blend"

class SportswearRequirements:
    """Class to hold sportswear requirements."""
    def __init__(self, stretchability: float, weight: float):
        """
        Initialize sportswear requirements.

        Args:
        - stretchability (float): The required stretchability (0-100).
        - weight (float): The required weight (0-1000 grams).
        """
        if not (0 <= stretchability <= 100):
            raise ValueError("Stretchability must be between 0 and 100")
        if not (0 <= weight <= 1000):
            raise ValueError("Weight must be between 0 and 1000 grams")

        self.stretchability = stretchability
        self.weight = weight

def calculate_optimal_fabric(requirements: SportswearRequirements) -> FabricType:
    """
    Calculate the optimal fabric type based on user-defined parameters.

    Args:
    - requirements (SportswearRequirements): The sportswear requirements.

    Returns:
    - FabricType: The optimal fabric type.
    """
    # Define fabric properties
    fabric_properties: Dict[FabricType, Dict[str, float]] = {
        FabricType.COTTON: {"stretchability": 10, "weight": 200},
        FabricType.POLYESTER: {"stretchability": 20, "weight": 300},
        FabricType.NYLON: {"stretchability": 30, "weight": 400},
        FabricType.SPANDEX: {"stretchability": 80, "weight": 100},
        FabricType.BLEND: {"stretchability": 50, "weight": 250},
    }

    # Initialize optimal fabric and its score
    optimal_fabric = FabricType.COTTON
    optimal_score = float("-inf")

    # Iterate over fabrics and calculate scores
    for fabric, properties in fabric_properties.items():
        # Calculate score based on requirements
        score = (properties["stretchability"] / requirements.stretchability) * 0.6 + \
                (requirements.weight / properties["weight"]) * 0.4

        # Update optimal fabric if score is better
        if score > optimal_score:
            optimal_score = score
            optimal_fabric = fabric

    return optimal_fabric

def main():
    try:
        # Get user input
        stretchability = float(input("Enter required stretchability (0-100): "))
        weight = float(input("Enter required weight (0-1000 grams): "))

        # Create sportswear requirements
        requirements = SportswearRequirements(stretchability, weight)

        # Calculate optimal fabric
        optimal_fabric = calculate_optimal_fabric(requirements)

        # Print result
        print(f"The optimal fabric type is: {optimal_fabric.value}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
