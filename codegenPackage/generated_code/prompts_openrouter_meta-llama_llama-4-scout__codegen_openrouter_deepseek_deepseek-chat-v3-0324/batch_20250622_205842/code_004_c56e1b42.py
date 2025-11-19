"""
Generated Code Metadata:
========================
Original URL: https://neumayaa.com.ar
Prompt: "What is the importance of TKPH in selecting tires for industrial equipment, and how to calculate it?"
Generated: DETERMINISTIC_c56e1b42464e22a6
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This module provides functionality to calculate TKPH (Ton Kilometer Per Hour)
for industrial equipment tires, which is crucial for selecting appropriate tires
based on operational conditions.
"""

class TireTKPHCalculator:
    """
    A class to calculate TKPH (Ton Kilometer Per Hour) for industrial tires.
    TKPH is a critical parameter for selecting tires that can withstand
    specific operational conditions without overheating.
    """

    def __init__(self, load_per_tire_kg, speed_kmh, operating_hours_per_day):
        """
        Initialize the calculator with operational parameters.

        Args:
            load_per_tire_kg (float): Load carried by each tire in kilograms
            speed_kmh (float): Average operating speed in km/h
            operating_hours_per_day (float): Daily operating hours
        """
        self.load_per_tire_kg = load_per_tire_kg
        self.speed_kmh = speed_kmh
        self.operating_hours_per_day = operating_hours_per_day

    def calculate_tkph(self):
        """
        Calculate TKPH value based on the formula:
        TKPH = (Load per tire in tons) × (Average speed in km/h) × (Operating hours per day)

        Returns:
            float: Calculated TKPH value

        Raises:
            ValueError: If any input parameter is negative
        """
        if any(val < 0 for val in [self.load_per_tire_kg, self.speed_kmh, self.operating_hours_per_day]):
            raise ValueError("All input parameters must be positive values")

        load_in_tons = self.load_per_tire_kg / 1000
        return load_in_tons * self.speed_kmh * self.operating_hours_per_day

    def is_tire_suitable(self, tire_max_tkph):
        """
        Check if a tire is suitable based on its maximum TKPH rating.

        Args:
            tire_max_tkph (float): Manufacturer's maximum TKPH rating for the tire

        Returns:
            bool: True if calculated TKPH is within tire's rating, False otherwise

        Raises:
            ValueError: If tire_max_tkph is negative
        """
        if tire_max_tkph < 0:
            raise ValueError("Tire maximum TKPH must be a positive value")

        calculated_tkph = self.calculate_tkph()
        return calculated_tkph <= tire_max_tkph


# Example usage
if __name__ == "__main__":
    try:
        # Example parameters
        calculator = TireTKPHCalculator(
            load_per_tire_kg=45000,  # 45 tons per tire
            speed_kmh=25,            # 25 km/h average speed
            operating_hours_per_day=12  # 12 hours operation
        )

        tkph_value = calculator.calculate_tkph()
        print(f"Calculated TKPH: {tkph_value:.2f}")

        tire_rating = 15000  # Example tire rating
        if calculator.is_tire_suitable(tire_rating):
            print("Tire is suitable for these operating conditions")
        else:
            print("Tire is NOT suitable - TKPH exceeds rating")
    except ValueError as e:
        print(f"Error: {e}")
```
