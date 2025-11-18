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
class Grill:
    def __init__(self, levels, material, dimensions):
        """
        Initialize the Grill object.

        :param levels: Number of grilling levels (tapa de dos niveles).
        :param material: Material properties of the grill (e.g., steel, cast iron).
        :param dimensions: Dimensions of the grill (width, depth, height).
        """
        self.levels = levels
        self.material = material
        self.dimensions = dimensions
        self.temperature = 0  # Initial temperature in degrees Celsius

    def preheat(self, target_temp):
        """
        Preheat the grill to the target temperature.

        :param target_temp: Desired temperature to preheat to in degrees Celsius.
        :raises ValueError: If the target temperature is below 0 or too high.
        """
        if target_temp < 0:
            raise ValueError("Target temperature must be above 0 degrees Celsius.")
        elif target_temp > 300:
            raise ValueError("Target temperature is too high for safe grilling.")

        self.temperature = target_temp
        print(f"Grill preheated to {self.temperature}°C.")

    def grill_meat(self, cook_time):
        """
        Simulate grilling meat for a certain amount of time.

        :param cook_time: Time in minutes to grill the meat.
        :raises ValueError: If the cook time is negative.
        """
        if cook_time < 0:
            raise ValueError("Cook time cannot be negative.")

        print(f"Grilling meat at {self.temperature}°C for {cook_time} minutes...")
        # Simulate the grilling process
        self._simulate_grill_process(cook_time)

    def _simulate_grill_process(self, cook_time):
        """
        Private method to simulate the grilling process.

        :param cook_time: Time in minutes to grill the meat.
        """
        # Simplified simulation of the grilling process
        for minute in range(cook_time):
            print(f"Minute {minute + 1}: Meat is cooking...")
        
        print(f"Finished grilling for {cook_time} minutes at {self.temperature}°C.")

    def clean_grill(self):
        """
        Simulate cleaning the grill.
        """
        print("Cleaning the grill...")
        self.temperature = 0  # Reset temperature after cleaning
        print("Grill cleaned and cooled.")

# Example of usage
if __name__ == "__main__":
    try:
        # Define grill properties from Meat Master
        grill_levels = 2
        grill_material = "Stainless Steel"
        grill_dimensions = (100, 60, 20)  # Width, Depth, Height in cm

        # Create a grill instance
        my_grill = Grill(grill_levels, grill_material, grill_dimensions)

        # Preheat the grill
        my_grill.preheat(target_temp=250)

        # Grill meat for 20 minutes
        my_grill.grill_meat(cook_time=20)

        # Clean the grill after use
        my_grill.clean_grill()

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
