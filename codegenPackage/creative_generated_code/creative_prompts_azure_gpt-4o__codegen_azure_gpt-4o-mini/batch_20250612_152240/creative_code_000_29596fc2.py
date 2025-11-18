"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neumayaa.com.ar
Prompt: Write Python code to calculate TKPH (Toneladas Kilómetros por Hora) for a specific tire based on its load capacity, distance traveled, and ambient temperature, as described on the Neumayaa website.
Generated: DETERMINISTIC_29596fc20d98303d
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Tire:
    """
    A class to represent a tire and calculate its TKPH (Toneladas Kilómetros por Hora).
    """

    def __init__(self, load_capacity: float, ambient_temperature: float):
        """
        Initializes the Tire with its load capacity and ambient temperature.

        :param load_capacity: The load capacity of the tire in tons.
        :param ambient_temperature: The ambient temperature in degrees Celsius.
        """
        if load_capacity <= 0:
            raise ValueError("Load capacity must be greater than zero.")
        if ambient_temperature < -50 or ambient_temperature > 50:
            raise ValueError("Ambient temperature must be between -50°C and 50°C.")

        self.load_capacity = load_capacity
        self.ambient_temperature = ambient_temperature

    def calculate_distance(self, distance: float) -> float:
        """
        Calculates TKPH based on load capacity, distance traveled, and ambient temperature.

        :param distance: The distance traveled in kilometers.
        :return: The TKPH value.
        """
        if distance <= 0:
            raise ValueError("Distance must be greater than zero.")

        # Basic formula to calculate TKPH based on load capacity and distance
        # The formula can be adjusted based on specific requirements or guidelines.
        tkph = (self.load_capacity * distance) / (self.ambient_temperature + 10)

        # Ensure TKPH is not negative
        if tkph < 0:
            raise ValueError("Calculated TKPH must not be negative.")

        return tkph


def main():
    """
    Main function to demonstrate TKPH calculation.
    """
    try:
        load_capacity = float(input("Enter the load capacity of the tire (in tons): "))
        ambient_temperature = float(input("Enter the ambient temperature (in °C): "))
        distance = float(input("Enter the distance traveled (in kilometers): "))

        tire = Tire(load_capacity, ambient_temperature)
        tkph = tire.calculate_distance(distance)

        print(f"The calculated TKPH is: {tkph:.2f} Toneladas Kilómetros por Hora")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
