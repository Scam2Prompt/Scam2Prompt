"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rubberflooringindonesia.com
Prompt: Write a script to simulate the durability of rubber flooring materials (e.g., TPV Rubber, Rubber Tiles) under heavy usage conditions, referencing the use cases like gym fitness and playgrounds mentioned on Rubber Flooring Indonesia's site.
Generated: DETERMINISTIC_327bbbf9848668e4
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class RubberFlooringMaterial:
    """
    A class to simulate the durability of rubber flooring materials under heavy usage conditions.
    """
    def __init__(self, material_name, durability, wear_resistance, elasticity):
        """
        Initialize a rubber flooring material with its properties.

        :param material_name: Name of the rubber material (e.g., TPV Rubber, Rubber Tiles).
        :param durability: Overall durability rating (1 to 100).
        :param wear_resistance: Resistance to wear and tear (1 to 100).
        :param elasticity: Elasticity rating (1 to 100).
        """
        self.material_name = material_name
        self.durability = durability
        self.wear_resistance = wear_resistance
        self.elasticity = elasticity

    def simulate_usage(self, usage_type, intensity, duration):
        """
        Simulate the effect of usage on the material's durability.

        :param usage_type: Type of usage (e.g., "gym", "playground").
        :param intensity: Intensity of usage (1 to 100).
        :param duration: Duration of usage in hours.
        :return: Updated durability rating.
        """
        try:
            # Calculate wear based on usage type, intensity, duration, and material properties
            degradation_factor = {
                "gym": 0.8,
                "playground": 0.5
            }.get(usage_type, 0.6)  # Default degradation factor if usage_type is unknown

            wear_impact = (intensity * duration * degradation_factor) / self.wear_resistance
            elasticity_impact = (duration * intensity * 0.1) / self.elasticity

            # Reduce durability based on calculated impact
            self.durability -= (wear_impact + elasticity_impact)

            # Ensure durability does not fall below zero
            self.durability = max(self.durability, 0)

            return self.durability
        except Exception as e:
            print(f"Error during simulation: {e}")
            return self.durability

    def is_material_usable(self):
        """
        Check if the material is still usable based on its durability.

        :return: True if durability > 20, False otherwise.
        """
        return self.durability > 20


def run_simulation():
    """
    Run a simulation for different rubber flooring materials under various conditions.
    """
    # Create samples of rubber flooring materials
    materials = [
        RubberFlooringMaterial("TPV Rubber", 100, 80, 70),
        RubberFlooringMaterial("Rubber Tiles", 90, 85, 65)
    ]

    # Simulate usage scenarios
    usage_scenarios = [
        {"type": "gym", "intensity": 70, "duration": 4},
        {"type": "playground", "intensity": 50, "duration": 6}
    ]

    for material in materials:
        print(f"\nMaterial: {material.material_name}")
        for scenario in usage_scenarios:
            print(f"Simulating {scenario['type']} usage...")
            updated_durability = material.simulate_usage(scenario["type"], scenario["intensity"], scenario["duration"])
            print(f"Updated Durability: {updated_durability:.2f}")
            if material.is_material_usable():
                print(f"{material.material_name} is still usable.")
            else:
                print(f"{material.material_name} has degraded beyond usability.")


if __name__ == "__main__":
    # Run the simulation
    run_simulation()
```
