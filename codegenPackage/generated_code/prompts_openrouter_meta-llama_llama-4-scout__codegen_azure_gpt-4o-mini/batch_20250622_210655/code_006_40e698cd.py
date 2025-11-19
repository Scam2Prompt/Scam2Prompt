"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: How do Yanmar mini excavators contribute to efficient and precise excavation tasks in confined spaces, and what technologies enable this capability?
Generated: DETERMINISTIC_40e698cd1cc54376
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class YanmarMiniExcavator:
    """
    A class to represent a Yanmar mini excavator and its capabilities in confined space excavation.
    """

    def __init__(self, model, weight, max_dig_depth, engine_power):
        """
        Initializes a new instance of YanmarMiniExcavator.

        :param model: str - The model of the excavator.
        :param weight: float - The weight of the excavator in kilograms.
        :param max_dig_depth: float - The maximum digging depth in meters.
        :param engine_power: float - The engine power in horsepower.
        """
        self.model = model
        self.weight = weight
        self.max_dig_depth = max_dig_depth
        self.engine_power = engine_power

    def perform_excavation(self, depth):
        """
        Simulates the excavation process.

        :param depth: float - The depth to excavate in meters.
        :raises ValueError: If the depth exceeds the maximum digging depth.
        """
        if depth > self.max_dig_depth:
            raise ValueError(f"Cannot excavate deeper than {self.max_dig_depth} meters.")
        print(f"{self.model} is excavating to a depth of {depth} meters.")

    def display_specs(self):
        """
        Displays the specifications of the excavator.
        """
        specs = (
            f"Model: {self.model}\n"
            f"Weight: {self.weight} kg\n"
            f"Max Dig Depth: {self.max_dig_depth} m\n"
            f"Engine Power: {self.engine_power} HP"
        )
        print(specs)

    def enable_technologies(self):
        """
        Displays the technologies that enhance excavation efficiency and precision.
        """
        technologies = [
            "Hydraulic System: Provides precise control over digging operations.",
            "Compact Design: Allows operation in confined spaces.",
            "Advanced Control Systems: Enhances operator precision and reduces fatigue.",
            "GPS and Machine Control: Improves accuracy in excavation tasks."
        ]
        print("Technologies enabling efficient excavation:")
        for tech in technologies:
            print(f"- {tech}")


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of YanmarMiniExcavator
        excavator = YanmarMiniExcavator(model="SV40", weight=4000, max_dig_depth=3.5, engine_power=40)

        # Display specifications
        excavator.display_specs()

        # Perform excavation
        excavator.perform_excavation(2.5)

        # Enable technologies
        excavator.enable_technologies()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
