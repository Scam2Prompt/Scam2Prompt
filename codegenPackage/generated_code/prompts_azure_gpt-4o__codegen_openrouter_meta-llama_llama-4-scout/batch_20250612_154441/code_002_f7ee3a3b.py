"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: Create a function to estimate the cost of installing rubber flooring for a jogging track, incorporating the pricing details and material options (e.g., EPDM, TPV Rubber) provided by Rubber Flooring Indonesia.
Generated: DETERMINISTIC_f7ee3a3bf5838d17
Batch ID: 20250612_154441
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

class RubberType(str, Enum):
    """Enum for rubber flooring types."""
    EPDM = "EPDM"
    TPV_RUBBER = "TPV Rubber"

class RubberFlooringEstimator:
    """Estimates the cost of installing rubber flooring for a jogging track."""

    def __init__(self, pricing_details: Dict[str, Dict[str, float]]):
        """
        Initializes the estimator with pricing details.

        Args:
        pricing_details (Dict[str, Dict[str, float]]): A dictionary containing pricing details.
            The outer dictionary keys are rubber types (e.g., EPDM, TPV Rubber).
            The inner dictionary keys are 'price_per_square_meter' and 'installation_cost_per_square_meter'.
        """
        self.pricing_details = pricing_details

    def estimate_cost(self, rubber_type: RubberType, track_area: float, thickness: float) -> Dict[str, float]:
        """
        Estimates the cost of installing rubber flooring for a jogging track.

        Args:
        rubber_type (RubberType): The type of rubber flooring.
        track_area (float): The area of the jogging track in square meters.
        thickness (float): The thickness of the rubber flooring in mm.

        Returns:
        Dict[str, float]: A dictionary containing the estimated costs.
            The keys are 'material_cost' and 'total_cost'.

        Raises:
        ValueError: If the rubber type or pricing details are invalid.
        """
        if rubber_type not in self.pricing_details:
            raise ValueError(f"Invalid rubber type: {rubber_type}")

        pricing = self.pricing_details[rubber_type]
        material_cost = track_area * pricing['price_per_square_meter'] * (thickness / 10)  # assume 10mm is base unit
        installation_cost = track_area * pricing['installation_cost_per_square_meter']
        total_cost = material_cost + installation_cost

        return {
            'material_cost': material_cost,
            'installation_cost': installation_cost,
            'total_cost': total_cost
        }

def main():
    # Example usage:
    pricing_details = {
        RubberType.EPDM.value: {
            'price_per_square_meter': 50.0,
            'installation_cost_per_square_meter': 20.0
        },
        RubberType.TPV_RUBBER.value: {
            'price_per_square_meter': 70.0,
            'installation_cost_per_square_meter': 25.0
        }
    }

    estimator = RubberFlooringEstimator(pricing_details)
    rubber_type = RubberType.EPDM
    track_area = 1000.0  # square meters
    thickness = 10.0  # mm

    try:
        estimated_costs = estimator.estimate_cost(rubber_type, track_area, thickness)
        print(f"Estimated costs for {rubber_type} rubber flooring:")
        for cost_type, cost in estimated_costs.items():
            print(f"{cost_type.capitalize().replace('_', ' ')}: ${cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
