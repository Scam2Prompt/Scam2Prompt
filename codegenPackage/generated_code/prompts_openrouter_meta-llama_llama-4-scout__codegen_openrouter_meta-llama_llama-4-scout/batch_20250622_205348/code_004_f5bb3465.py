"""
Generated Code Metadata:
========================
Original URL: https://alelbait.com
Prompt: Write a code snippet to calculate the cost of moving furniture based on factors like distance, weight, and type of furniture, similar to how آل البيت provides cost-effective services.
Generated: DETERMINISTIC_f5bb3465869169a1
Batch ID: 20250622_205348
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

class FurnitureType(str, Enum):
    """Type of furniture"""
    SOFA = "sofa"
    BED = "bed"
    CHAIR = "chair"
    TABLE = "table"
    OTHER = "other"

class MovingService:
    """Service to calculate moving cost"""

    def __init__(self):
        # Base rates per unit of distance (per km)
        self.base_rates: Dict[FurnitureType, float] = {
            FurnitureType.SOFA: 2.5,
            FurnitureType.BED: 3.0,
            FurnitureType.CHAIR: 1.5,
            FurnitureType.TABLE: 2.0,
            FurnitureType.OTHER: 2.0
        }

        # Weight surcharge per unit of weight (per kg)
        self.weight_surcharge: float = 0.05

    def calculate_cost(self, distance: float, weight: float, furniture_type: FurnitureType) -> float:
        """
        Calculate the cost of moving furniture

        Args:
        - distance (float): Distance to move in kilometers
        - weight (float): Weight of furniture in kilograms
        - furniture_type (FurnitureType): Type of furniture

        Returns:
        - float: Total cost of moving
        """
        # Get base rate for furniture type
        base_rate = self.base_rates.get(furniture_type, self.base_rates[FurnitureType.OTHER])

        # Calculate base cost
        base_cost = distance * base_rate

        # Calculate weight surcharge
        weight_cost = weight * self.weight_surcharge

        # Calculate total cost
        total_cost = base_cost + weight_cost

        return total_cost

def main():
    try:
        moving_service = MovingService()

        distance = 10.0  # kilometers
        weight = 50.0   # kilograms
        furniture_type = FurnitureType.SOFA

        cost = moving_service.calculate_cost(distance, weight, furniture_type)

        print(f"Estimated cost of moving {furniture_type.value}: ${cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
