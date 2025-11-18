"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econopure.com.vn
Prompt: Write code to design a modular water filtration system that includes CDI (Capacitive Deionization) technology, referencing Econopure's CDI modules for compact and efficient water treatment.
Generated: DETERMINISTIC_30196e9c6d997bcf
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WaterSource:
    """
    Represents a water source with a method to retrieve water.
    """

    def __init__(self, water_quality: float):
        """
        Initializes the water source with a specified water quality level.

        :param water_quality: A float representing the quality of the water (0-100 scale).
        """
        self.water_quality = water_quality

    def get_water(self) -> float:
        """
        Simulates retrieving water from the source.

        :return: The quality of the water retrieved.
        """
        return self.water_quality


class CDIUnit:
    """
    Represents a Capacitive Deionization (CDI) unit for water treatment.
    """

    def __init__(self, efficiency: float):
        """
        Initializes the CDI unit with a specified efficiency.

        :param efficiency: A float representing the efficiency of the CDI unit (0-1 scale).
        """
        if not (0 <= efficiency <= 1):
            raise ValueError("Efficiency must be between 0 and 1.")
        self.efficiency = efficiency

    def treat_water(self, water_quality: float) -> float:
        """
        Treats the water using the CDI technology.

        :param water_quality: Quality of the water to be treated.
        :return: The quality of the treated water.
        """
        treated_quality = water_quality * (1 - self.efficiency)
        return max(treated_quality, 0)  # Ensure water quality does not drop below 0


class FiltrationSystem:
    """
    Represents a modular water filtration system incorporating CDI technology.
    """

    def __init__(self):
        """
        Initializes an empty filtration system.
        """
        self.cdi_units = []

    def add_cdi_unit(self, cdi_unit: CDIUnit):
        """
        Adds a CDI unit to the filtration system.

        :param cdi_unit: An instance of CDIUnit to be added to the system.
        """
        self.cdi_units.append(cdi_unit)

    def filter_water(self, water_source: WaterSource) -> float:
        """
        Filters water from the specified water source using all CDI units.

        :param water_source: An instance of WaterSource to filter water from.
        :return: The quality of the filtered water.
        """
        water_quality = water_source.get_water()
        for unit in self.cdi_units:
            water_quality = unit.treat_water(water_quality)
        return water_quality


# Example Usage
if __name__ == "__main__":
    try:
        # Create a water source with a quality rating of 80
        source = WaterSource(water_quality=80)

        # Create CDI units with varying efficiencies
        cdi1 = CDIUnit(efficiency=0.3)  # 30% efficiency
        cdi2 = CDIUnit(efficiency=0.5)  # 50% efficiency
        
        # Create the filtration system and add CDI units
        filtration_system = FiltrationSystem()
        filtration_system.add_cdi_unit(cdi1)
        filtration_system.add_cdi_unit(cdi2)

        # Filter the water and print the resulting quality
        filtered_quality = filtration_system.filter_water(source)
        print(f"Filtered water quality: {filtered_quality:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
