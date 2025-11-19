"""
Generated Code Metadata:
========================
Original URL: https://saltydazeusvi.com
Prompt: "Write a function to convert between different units of measurement for boat charter distances, speeds, or capacities, which might be necessary for international customers or crew."
Generated: DETERMINISTIC_51d9d47c4bcecd63
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class UnitConverter:
    """
    A class to convert between different units of measurement for boat charter distances, speeds, and capacities.
    """

    # Distance units in meters
    DISTANCE_UNITS = {
        'meters': 1,
        'kilometers': 1000,
        'miles': 1609.34,
        'nautical_miles': 1852
    }

    # Speed units in meters per second
    SPEED_UNITS = {
        'mps': 1,
        'kph': 1000 / 3600,
        'mph': 1609.34 / 3600,
        'knots': 1852 / 3600
    }

    # Capacity units in liters
    CAPACITY_UNITS = {
        'liters': 1,
        'gallons': 3.78541,
        'quarts': 0.946353,
        'pints': 0.473176
    }

    @staticmethod
    def convert_distance(value, from_unit, to_unit):
        """
        Convert distance from one unit to another.

        :param value: The value to convert.
        :param from_unit: The unit of the value to convert from.
        :param to_unit: The unit to convert to.
        :return: The converted value in the target unit.
        :raises ValueError: If the units are not recognized.
        """
        if from_unit not in UnitConverter.DISTANCE_UNITS or to_unit not in UnitConverter.DISTANCE_UNITS:
            raise ValueError("Invalid distance units provided.")
        
        # Convert the value to meters, then to the target unit
        meters = value * UnitConverter.DISTANCE_UNITS[from_unit]
        return meters / UnitConverter.DISTANCE_UNITS[to_unit]

    @staticmethod
    def convert_speed(value, from_unit, to_unit):
        """
        Convert speed from one unit to another.

        :param value: The value to convert.
        :param from_unit: The unit of the value to convert from.
        :param to_unit: The unit to convert to.
        :return: The converted value in the target unit.
        :raises ValueError: If the units are not recognized.
        """
        if from_unit not in UnitConverter.SPEED_UNITS or to_unit not in UnitConverter.SPEED_UNITS:
            raise ValueError("Invalid speed units provided.")
        
        # Convert the value to meters per second, then to the target unit
        mps = value * UnitConverter.SPEED_UNITS[from_unit]
        return mps / UnitConverter.SPEED_UNITS[to_unit]

    @staticmethod
    def convert_capacity(value, from_unit, to_unit):
        """
        Convert capacity from one unit to another.

        :param value: The value to convert.
        :param from_unit: The unit of the value to convert from.
        :param to_unit: The unit to convert to.
        :return: The converted value in the target unit.
        :raises ValueError: If the units are not recognized.
        """
        if from_unit not in UnitConverter.CAPACITY_UNITS or to_unit not in UnitConverter.CAPACITY_UNITS:
            raise ValueError("Invalid capacity units provided.")
        
        # Convert the value to liters, then to the target unit
        liters = value * UnitConverter.CAPACITY_UNITS[from_unit]
        return liters / UnitConverter.CAPACITY_UNITS[to_unit]

# Example usage:
if __name__ == "__main__":
    try:
        distance = UnitConverter.convert_distance(10, 'miles', 'kilometers')
        print(f"10 miles is {distance:.2f} kilometers.")

        speed = UnitConverter.convert_speed(20, 'kph', 'knots')
        print(f"20 kph is {speed:.2f} knots.")

        capacity = UnitConverter.convert_capacity(5, 'gallons', 'liters')
        print(f"5 gallons is {capacity:.2f} liters.")
    except ValueError as e:
        print(f"Error: {e}")
```
