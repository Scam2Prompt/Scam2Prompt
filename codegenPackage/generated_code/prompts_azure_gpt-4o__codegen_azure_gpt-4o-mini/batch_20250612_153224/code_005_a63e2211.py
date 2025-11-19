"""
Generated Code Metadata:
========================
Original URL: https://createxpro.com
Prompt: Write code to simulate the application of sublimation on various materials like glass, ceramic, and polyester, as outlined by CreatexPro.
Generated: DETERMINISTIC_a63e22117e71a4c9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict

class Material:
    """Class representing a material that can undergo sublimation."""
    
    def __init__(self, name: str, sublimation_temp: float):
        """
        Initialize a Material instance.

        :param name: Name of the material.
        :param sublimation_temp: Temperature at which sublimation occurs (in Celsius).
        """
        self.name = name
        self.sublimation_temp = sublimation_temp

    def apply_sublimation(self, temperature: float) -> str:
        """
        Simulate the application of sublimation on the material.

        :param temperature: The temperature at which sublimation is attempted.
        :return: Result of the sublimation process.
        """
        if temperature < 0:
            raise ValueError("Temperature cannot be below absolute zero.")
        
        if temperature >= self.sublimation_temp:
            return f"Sublimation applied successfully on {self.name} at {temperature}°C."
        else:
            return f"Sublimation failed on {self.name}. Required temperature: {self.sublimation_temp}°C, provided: {temperature}°C."


class SublimationSimulator:
    """Class to simulate sublimation on various materials."""
    
    def __init__(self, materials: List[Material]):
        """
        Initialize the SublimationSimulator with a list of materials.

        :param materials: List of Material instances.
        """
        self.materials = materials

    def simulate(self, temperature: float) -> Dict[str, str]:
        """
        Simulate sublimation on all materials at a given temperature.

        :param temperature: The temperature to apply for sublimation.
        :return: Dictionary with material names as keys and sublimation results as values.
        """
        results = {}
        for material in self.materials:
            try:
                result = material.apply_sublimation(temperature)
                results[material.name] = result
            except ValueError as e:
                results[material.name] = str(e)
        return results


def main():
    """Main function to run the sublimation simulation."""
    # Define materials with their sublimation temperatures
    materials = [
        Material("Glass", 600.0),
        Material("Ceramic", 800.0),
        Material("Polyester", 200.0)
    ]

    # Create a simulator instance
    simulator = SublimationSimulator(materials)

    # Simulate sublimation at a random temperature between 150°C and 850°C
    temperature = random.uniform(150.0, 850.0)
    print(f"Simulating sublimation at {temperature:.2f}°C...\n")

    # Run the simulation and print results
    results = simulator.simulate(temperature)
    for material, result in results.items():
        print(result)


if __name__ == "__main__":
    main()
```
