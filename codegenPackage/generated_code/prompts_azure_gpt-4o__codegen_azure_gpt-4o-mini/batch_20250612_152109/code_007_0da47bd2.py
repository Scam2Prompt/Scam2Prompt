"""
Generated Code Metadata:
========================
Original URL: https://meatmaster.pe
Prompt: Write code to simulate the grilling process on a Parrilla with tapa de dos niveles, incorporating the material properties and dimensions provided by Meat Master.
Generated: DETERMINISTIC_0da47bd2df5ed8c1
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Parrilla:
    """
    A class to simulate the grilling process on a Parrilla with a two-level lid.
    """

    def __init__(self, material, dimensions):
        """
        Initializes the Parrilla with the given material properties and dimensions.

        :param material: A dictionary containing material properties (e.g., thermal conductivity, heat capacity).
        :param dimensions: A dictionary containing dimensions (e.g., width, height, depth).
        """
        self.material = material
        self.dimensions = dimensions
        self.temperature = 20  # Initial temperature in Celsius
        self.grill_time = 0  # Time in minutes

    def heat_up(self, target_temp, time):
        """
        Simulates heating the Parrilla to a target temperature over a specified time.

        :param target_temp: The desired temperature to reach in Celsius.
        :param time: The time in minutes to reach the target temperature.
        """
        if target_temp <= self.temperature:
            raise ValueError("Target temperature must be higher than current temperature.")
        if time <= 0:
            raise ValueError("Time must be a positive value.")

        # Simulate the heating process
        self.temperature = target_temp
        self.grill_time += time
        print(f"Heating up to {target_temp}°C over {time} minutes.")

    def grill(self, food_item, cook_time):
        """
        Simulates grilling a food item for a specified cook time.

        :param food_item: The name of the food item being grilled.
        :param cook_time: The time in minutes to grill the food item.
        """
        if self.temperature < 100:
            raise RuntimeError("Temperature too low to grill. Please heat the Parrilla first.")
        if cook_time <= 0:
            raise ValueError("Cook time must be a positive value.")

        # Simulate the grilling process
        self.grill_time += cook_time
        print(f"Grilling {food_item} for {cook_time} minutes at {self.temperature}°C.")

    def get_status(self):
        """
        Returns the current status of the Parrilla including temperature and total grill time.

        :return: A string representing the current status of the Parrilla.
        """
        return f"Current temperature: {self.temperature}°C, Total grill time: {self.grill_time} minutes."


# Example usage
if __name__ == "__main__":
    # Define material properties and dimensions
    material_properties = {
        'thermal_conductivity': 50,  # W/m·K
        'heat_capacity': 900  # J/kg·K
    }
    dimensions = {
        'width': 1.0,  # meters
        'height': 0.5,  # meters
        'depth': 0.5  # meters
    }

    # Create a Parrilla instance
    parrilla = Parrilla(material_properties, dimensions)

    try:
        # Heat up the Parrilla
        parrilla.heat_up(target_temp=200, time=15)

        # Grill a food item
        parrilla.grill(food_item="Steak", cook_time=10)

        # Get the current status
        print(parrilla.get_status())
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
```
