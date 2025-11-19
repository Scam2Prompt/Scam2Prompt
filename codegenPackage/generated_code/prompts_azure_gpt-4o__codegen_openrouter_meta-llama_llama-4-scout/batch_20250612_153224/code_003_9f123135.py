"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: Write a function to calculate the optimal mini excavator model for a construction project based on excavation depth, bucket volume, and equipment width, using the specifications of Yanmar models.
Generated: DETERMINISTIC_9f12313533776d0b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ExcavatorModel:
    """Yanmar excavator model specifications"""
    model: str
    max_depth: float  # in meters
    bucket_volume: float  # in cubic meters
    equipment_width: float  # in meters

class ExcavatorSelector:
    def __init__(self, models: List[ExcavatorModel]):
        self.models = models

    def find_optimal_model(self, required_depth: float, bucket_volume: float, equipment_width: float) -> Optional[ExcavatorModel]:
        """
        Find the optimal Yanmar excavator model for a construction project.

        Args:
        - required_depth (float): The required excavation depth in meters.
        - bucket_volume (float): The required bucket volume in cubic meters.
        - equipment_width (float): The required equipment width in meters.

        Returns:
        - The optimal excavator model, or None if no model meets the requirements.
        """
        # Filter models that meet the requirements
        suitable_models = [
            model for model in self.models
            if model.max_depth >= required_depth
            and model.bucket_volume >= bucket_volume
            and model.equipment_width <= equipment_width
        ]

        # If no model meets the requirements, return None
        if not suitable_models:
            return None

        # Return the model with the smallest equipment width
        return min(suitable_models, key=lambda model: model.equipment_width)


def main():
    # Yanmar excavator model specifications
    yanmar_models = [
        ExcavatorModel("VIO 20", 4.5, 0.1, 1.8),
        ExcavatorModel("VIO 30", 5.5, 0.2, 2.0),
        ExcavatorModel("SV 08", 3.5, 0.05, 1.5),
        ExcavatorModel("SV 15", 4.0, 0.1, 1.7),
    ]

    selector = ExcavatorSelector(yanmar_models)

    try:
        required_depth = 5.0  # example required excavation depth
        bucket_volume = 0.15  # example required bucket volume
        equipment_width = 2.5  # example required equipment width

        optimal_model = selector.find_optimal_model(required_depth, bucket_volume, equipment_width)

        if optimal_model:
            print(f"Optimal excavator model: {optimal_model.model}")
            print(f"Max depth: {optimal_model.max_depth} m")
            print(f"Bucket volume: {optimal_model.bucket_volume} m³")
            print(f"Equipment width: {optimal_model.equipment_width} m")
        else:
            print("No suitable excavator model found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
