"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isoplas.com
Prompt: Generate a Python script that utilizes Isoplas Corporation's packaging solutions, specifically for creating a microwavable container design.
Generated: DETERMINISTIC_aae4e5b06dc60a6b
Batch ID: 20250612_160127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
microwave_container_design.py

This script is designed to create a microwavable container design using
Isoplas Corporation's packaging solutions. The script defines a class
to handle container properties and methods to ensure that the design
meets safety and functionality standards.
"""

class MicrowaveContainer:
    def __init__(self, material: str, volume: float, diameter: float, height: float):
        """
        Initializes a new MicrowaveContainer instance.

        Parameters:
        material (str): The material of the container.
        volume (float): The volume of the container in liters.
        diameter (float): The diameter of the container in centimeters.
        height (float): The height of the container in centimeters.
        """
        self.material = material
        self.volume = volume
        self.diameter = diameter
        self.height = height

        # Validate the inputs
        self.validate_container()

    def validate_container(self):
        """Validates the properties of the container."""
        if self.volume <= 0:
            raise ValueError("Volume must be greater than zero.")
        if self.diameter <= 0:
            raise ValueError("Diameter must be greater than zero.")
        if self.height <= 0:
            raise ValueError("Height must be greater than zero.")
        if self.material not in ["polypropylene", "polyethylene", "glass"]:
            raise ValueError("Material must be one of the following: polypropylene, polyethylene, or glass.")

    def calculate_surface_area(self) -> float:
        """
        Calculates the surface area of the container.

        Returns:
        float: The surface area in square centimeters.
        """
        import math
        return math.pi * self.diameter * (self.height + self.diameter)

    def can_withstand_heat(self, temperature: float) -> bool:
        """
        Checks if the container can withstand the given temperature.

        Parameters:
        temperature (float): The temperature in degrees Celsius.

        Returns:
        bool: True if the container can withstand the temperature, False otherwise.
        """
        # Example heat resistance limits
        heat_resistance = {
            "polypropylene": 120,
            "polyethylene": 80,
            "glass": 300
        }

        if self.material in heat_resistance:
            return temperature <= heat_resistance[self.material]
        else:
            raise ValueError("Unknown material for heat resistance check.")

    def design_summary(self) -> str:
        """
        Returns a summary of the container design.

        Returns:
        str: A summary string.
        """
        return (
            f"Container Design Summary:\n"
            f"Material: {self.material}\n"
            f"Volume: {self.volume}L\n"
            f"Diameter: {self.diameter}cm\n"
            f"Height: {self.height}cm\n"
            f"Surface Area: {self.calculate_surface_area():.2f} cm²"
        )


# Example Usage
if __name__ == "__main__":
    try:
        # Create a microwavable container instance
        container = MicrowaveContainer(material="polypropylene", volume=2.0, diameter=20.0, height=10.0)
        
        # Display container summary
        print(container.design_summary())
        
        # Check if it can withstand a specific temperature
        temperature_check = 100  # degrees Celsius
        if container.can_withstand_heat(temperature_check):
            print(f"The container can withstand {temperature_check}°C.")
        else:
            print(f"The container cannot withstand {temperature_check}°C.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
