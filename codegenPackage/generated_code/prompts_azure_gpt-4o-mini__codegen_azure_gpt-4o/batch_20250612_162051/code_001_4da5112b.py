"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: How can I implement a foam recycling system using the XT500 EPS densifier to reduce waste hauling costs by 80%?
Generated: DETERMINISTIC_4da5112b21924eb8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Foam Recycling System using XT500 EPS Densifier

This script simulates the operation of a foam recycling system using the XT500 EPS densifier.
The system processes foam waste, densifies it, and calculates the reduction in waste hauling costs.

Requirements:
- Python 3.x
"""

import logging

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class EPSDensifier:
    """
    A class to represent the XT500 EPS densifier.
    """

    def __init__(self, densification_ratio: float):
        """
        Initialize the EPS densifier with a densification ratio.

        :param densification_ratio: The ratio by which foam waste is reduced (e.g., 50:1).
        """
        if densification_ratio <= 0:
            raise ValueError("Densification ratio must be greater than zero.")
        self.densification_ratio = densification_ratio

    def densify(self, foam_weight: float) -> float:
        """
        Densify the foam waste.

        :param foam_weight: Weight of foam waste in kilograms.
        :return: Weight of densified foam in kilograms.
        """
        if foam_weight <= 0:
            raise ValueError("Foam weight must be greater than zero.")
        densified_weight = foam_weight / self.densification_ratio
        logging.info(f"Densified {foam_weight} kg of foam to {densified_weight:.2f} kg.")
        return densified_weight


class RecyclingSystem:
    """
    A class to represent the foam recycling system.
    """

    def __init__(self, densifier: EPSDensifier, hauling_cost_per_kg: float):
        """
        Initialize the recycling system.

        :param densifier: An instance of EPSDensifier.
        :param hauling_cost_per_kg: Cost of hauling foam waste per kilogram.
        """
        if hauling_cost_per_kg <= 0:
            raise ValueError("Hauling cost per kilogram must be greater than zero.")
        self.densifier = densifier
        self.hauling_cost_per_kg = hauling_cost_per_kg

    def calculate_cost_reduction(self, foam_weight: float) -> float:
        """
        Calculate the reduction in waste hauling costs.

        :param foam_weight: Weight of foam waste in kilograms.
        :return: Percentage reduction in hauling costs.
        """
        original_cost = foam_weight * self.hauling_cost_per_kg
        densified_weight = self.densifier.densify(foam_weight)
        densified_cost = densified_weight * self.hauling_cost_per_kg
        cost_reduction = ((original_cost - densified_cost) / original_cost) * 100
        logging.info(f"Original hauling cost: ${original_cost:.2f}")
        logging.info(f"Densified hauling cost: ${densified_cost:.2f}")
        logging.info(f"Cost reduction: {cost_reduction:.2f}%")
        return cost_reduction


def main():
    """
    Main function to simulate the foam recycling system.
    """
    try:
        # Initialize the EPS densifier with a densification ratio of 50:1
        densifier = EPSDensifier(densification_ratio=50)

        # Initialize the recycling system with a hauling cost of $0.50 per kilogram
        recycling_system = RecyclingSystem(densifier=densifier, hauling_cost_per_kg=0.50)

        # Simulate processing 1000 kg of foam waste
        foam_weight = 1000  # in kilograms
        cost_reduction = recycling_system.calculate_cost_reduction(foam_weight)

        # Output the results
        print(f"Processed {foam_weight} kg of foam waste.")
        print(f"Cost reduction: {cost_reduction:.2f}%")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
