"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unitramabrazz.blogspot.com
Prompt: Generate code to simulate the durability of materials like Plastionda and acrylic sheets under varying environmental conditions, based on the descriptions from the unitramabrazz website.
Generated: DETERMINISTIC_2c584edad832235d
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Material:
    """
    Represents a material with specific properties to simulate its durability under varying environmental conditions.
    """
    def __init__(self, name, base_durability, environmental_resistance):
        """
        Initialize the material with a name, base durability, and resistance to environmental factors.

        :param name: Name of the material (e.g., "Plastionda", "Acrylic Sheet").
        :param base_durability: Initial durability of the material (higher is better).
        :param environmental_resistance: Resistance to environmental factors (0.0 to 1.0), where 1.0 is fully resistant.
        """
        self.name = name
        self.base_durability = base_durability
        self.environmental_resistance = environmental_resistance

    def simulate_environmental_impact(self, temperature, humidity, uv_index):
        """
        Simulates the effect of environmental conditions on the material's durability.

        :param temperature: Ambient temperature in degrees Celsius.
        :param humidity: Humidity level in percentage (0 to 100).
        :param uv_index: UV radiation index (0 to 11+).
        :return: Adjusted durability after considering environmental impact.
        """
        # Calculate the impact factors
        temp_impact = max(0, (temperature - 25) * 0.02)  # Durability decreases above 25°C
        humidity_impact = max(0, (humidity - 50) * 0.01)  # Durability decreases above 50% humidity
        uv_impact = uv_index * 0.1  # UV index directly affects durability

        # Total impact modifier
        total_impact = temp_impact + humidity_impact + uv_impact

        # Adjust durability considering environmental resistance
        adjusted_durability = self.base_durability * (1 - total_impact * (1 - self.environmental_resistance))

        # Ensure durability doesn't drop below zero
        return max(0, adjusted_durability)

def simulate_materials(materials, conditions, num_iterations=100):
    """
    Simulates the durability of materials under varying environmental conditions.

    :param materials: List of Material objects to simulate.
    :param conditions: Dictionary with ranges for 'temperature', 'humidity', and 'uv_index'.
    :param num_iterations: Number of simulation iterations for durability testing.
    :return: Dictionary of results where each material is mapped to a list of durability values.
    """
    results = {material.name: [] for material in materials}

    for _ in range(num_iterations):
        # Randomly generate environmental conditions within the given ranges
        temperature = random.uniform(*conditions['temperature'])
        humidity = random.uniform(*conditions['humidity'])
        uv_index = random.uniform(*conditions['uv_index'])

        for material in materials:
            # Calculate the adjusted durability for the current conditions
            durability = material.simulate_environmental_impact(temperature, humidity, uv_index)
            results[material.name].append(durability)

    return results

def main():
    """
    Main function to set up materials, environmental conditions, and run the simulation.
    """
    # Define materials with their properties
    materials = [
        Material(name="Plastionda", base_durability=100, environmental_resistance=0.8),
        Material(name="Acrylic Sheet", base_durability=120, environmental_resistance=0.9)
    ]

    # Define environmental condition ranges
    conditions = {
        "temperature": (20, 40),  # Temperature range in °C
        "humidity": (30, 80),     # Humidity range in %
        "uv_index": (0, 11)       # UV index range
    }

    # Run the simulation
    num_iterations = 100
    results = simulate_materials(materials, conditions, num_iterations)

    # Display the results
    for material_name, durability_values in results.items():
        avg_durability = sum(durability_values) / len(durability_values)
        print(f"Material: {material_name}")
        print(f"  Average Durability: {avg_durability:.2f}")
        print(f"  Minimum Durability: {min(durability_values):.2f}")
        print(f"  Maximum Durability: {max(durability_values):.2f}")
        print()

if __name__ == "__main__":
    # Entry point of the simulation program
    main()
```
