"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprintnan.app
Prompt: Write code to simulate the structural integrity of fabricated letters (e.g., metal, plaswood, acrylic) under different environmental conditions, using the material specifications from ThePrintNan.
Generated: DETERMINISTIC_6704d8e0e49a99ed
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Initialize logging for debugging and error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Material:
    """
    Class representing material specifications for fabricated letters.
    """
    def __init__(self, name, tensile_strength, thermal_resistance, coefficient_of_expansion):
        """
        Initialize material properties.
        
        :param name: Name of the material (e.g., metal, plaswood, acrylic).
        :param tensile_strength: Tensile strength of the material in MPa.
        :param thermal_resistance: Thermal resistance in °C.
        :param coefficient_of_expansion: Linear coefficient of thermal expansion (1/°C).
        """
        self.name = name
        self.tensile_strength = tensile_strength
        self.thermal_resistance = thermal_resistance
        self.coefficient_of_expansion = coefficient_of_expansion

    def __str__(self):
        return f"Material: {self.name}, Tensile Strength: {self.tensile_strength} MPa, " \
               f"Thermal Resistance: {self.thermal_resistance} °C, " \
               f"Coefficient of Expansion: {self.coefficient_of_expansion} 1/°C"


class Environment:
    """
    Class representing environmental conditions.
    """
    def __init__(self, temperature, load):
        """
        Initialize environmental properties.
        
        :param temperature: Temperature in °C.
        :param load: Applied mechanical load in MPa.
        """
        self.temperature = temperature
        self.load = load


def simulate_integrity(material, environment):
    """
    Simulates the structural integrity of a fabricated letter under given environmental conditions.
    
    :param material: Material object containing specifications of the material.
    :param environment: Environment object containing environmental conditions.
    :return: Result of the simulation as a string.
    """
    try:
        # Check if the material can withstand the applied load
        if environment.load > material.tensile_strength:
            return f"Structural failure: {material.name} cannot withstand the applied load of {environment.load} MPa."

        # Check if the material can withstand the environmental temperature
        if environment.temperature > material.thermal_resistance:
            return f"Structural failure: {material.name} cannot withstand the temperature of {environment.temperature} °C."

        # Calculate expansion due to temperature
        expansion = material.coefficient_of_expansion * environment.temperature
        logging.info(f"Expansion calculated for {material.name}: {expansion}")

        return f"{material.name} remains structurally intact under the given conditions."
    except Exception as e:
        logging.error(f"Error in simulating integrity: {e}")
        return "An error occurred during the simulation."


if __name__ == "__main__":
    # Example material specifications (from ThePrintNan data)
    metal = Material(name="Metal", tensile_strength=250, thermal_resistance=400, coefficient_of_expansion=0.000012)
    plaswood = Material(name="Plaswood", tensile_strength=50, thermal_resistance=120, coefficient_of_expansion=0.000075)
    acrylic = Material(name="Acrylic", tensile_strength=70, thermal_resistance=80, coefficient_of_expansion=0.000095)

    # Example environmental conditions
    environment1 = Environment(temperature=50, load=30)
    environment2 = Environment(temperature=500, load=200)

    # Simulating integrity
    logging.info(simulate_integrity(metal, environment1))
    logging.info(simulate_integrity(plaswood, environment1))
    logging.info(simulate_integrity(acrylic, environment2))
```
