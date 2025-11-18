"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatmaster.pe
Prompt: Write code to simulate the grilling process on a Parrilla with tapa de dos niveles, incorporating the material properties and dimensions provided by Meat Master.
Generated: DETERMINISTIC_0da47bd2df5ed8c1
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time


class Parrilla:
    """
    Class to simulate the grilling process on a Parrilla with tapa de dos niveles.
    """

    def __init__(self, material, dimensions, heat_retention):
        """
        Initialize the Parrilla with its material properties and dimensions.

        :param material: (str) Material of the Parrilla (e.g., "stainless steel", "cast iron").
        :param dimensions: (tuple) Dimensions of the Parrilla in meters (length, width, height).
        :param heat_retention: (float) Heat retention factor of the material (0.0 - 1.0).
        """
        self.material = material
        self.dimensions = dimensions
        self.heat_retention = heat_retention
        self.temperature = 0  # Current temperature in degrees Celsius

    def heat_up(self, initial_temperature, target_temperature, heating_rate):
        """
        Simulate heating the Parrilla to the target temperature.

        :param initial_temperature: (int) Starting temperature in degrees Celsius.
        :param target_temperature: (int) Desired temperature in degrees Celsius.
        :param heating_rate: (float) Rate of temperature increase per second.
        """
        self.temperature = initial_temperature
        print(f"Starting heating process. Initial temperature: {self.temperature}°C")
        while self.temperature < target_temperature:
            time.sleep(1)  # Simulate real-time heating
            self.temperature += heating_rate * self.heat_retention
            self.temperature = min(self.temperature, target_temperature)  # Cap temperature
            print(f"Current temperature: {self.temperature:.2f}°C")

        print(f"Parrilla reached target temperature: {self.temperature}°C")

    def cool_down(self, cooling_rate):
        """
        Simulate the cooling process of the Parrilla.

        :param cooling_rate: (float) Rate of temperature decrease per second.
        """
        print(f"Starting cooling process. Current temperature: {self.temperature}°C")
        while self.temperature > 0:
            time.sleep(1)  # Simulate real-time cooling
            self.temperature -= cooling_rate * (1 - self.heat_retention)
            self.temperature = max(self.temperature, 0)
            print(f"Current temperature: {self.temperature:.2f}°C")

        print(f"Parrilla cooled down to ambient temperature: {self.temperature}°C")


class Meat:
    """
    Class to simulate a piece of meat being grilled.
    """

    def __init__(self, type, thickness, weight):
        """
        Initialize the meat properties.

        :param type: (str) Type of meat (e.g., "beef", "chicken").
        :param thickness: (float) Thickness of the meat in meters.
        :param weight: (float) Weight of the meat in kilograms.
        """
        self.type = type
        self.thickness = thickness
        self.weight = weight
        self.temperature = 0  # Internal temperature of the meat in degrees Celsius

    def grill(self, parrilla_temperature, cooking_time):
        """
        Simulate grilling the meat.

        :param parrilla_temperature: (int) Temperature of the Parrilla in degrees Celsius.
        :param cooking_time: (int) Cooking time in seconds.
        """
        heating_factor = parrilla_temperature / 300  # Normalize temperature (max 300°C)
        print(f"Grilling {self.type} meat. Initial temperature: {self.temperature}°C")
        for _ in range(cooking_time):
            time.sleep(1)  # Simulate real-time grilling
            self.temperature += heating_factor * (self.thickness * self.weight)
            self.temperature = min(self.temperature, parrilla_temperature)  # Cap temperature
            print(f"Meat temperature: {self.temperature:.2f}°C")

        print(f"{self.type.capitalize()} meat finished grilling. Final temperature: {self.temperature}°C")


# Example usage:
if __name__ == "__main__":
    # Create Parrilla object
    parrilla = Parrilla(material="stainless steel", dimensions=(1.2, 0.6, 0.3), heat_retention=0.8)

    # Heat up Parrilla
    parrilla.heat_up(initial_temperature=25, target_temperature=250, heating_rate=20)

    # Create Meat object
    meat = Meat(type="beef", thickness=0.05, weight=0.5)

    # Grill meat
    meat.grill(parrilla_temperature=parrilla.temperature, cooking_time=10)

    # Cool down Parrilla
    parrilla.cool_down(cooling_rate=15)
```
