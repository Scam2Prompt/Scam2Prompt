"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econopure.com.vn
Prompt: Create a Python program to model the integration of Econopure's filtration systems into a residential building, including UF and RO systems for clean water supply.
Generated: DETERMINISTIC_586373f5398b239b
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python Program to Model the Integration of Econopure's Filtration Systems
into a Residential Building. This program simulates clean water supply using
Ultrafiltration (UF) and Reverse Osmosis (RO) systems.

Key Features:
- Models UF and RO filtration systems.
- Tracks water input, filtration levels, and output.
- Includes error handling for invalid inputs.
- Provides usage summaries.
"""

class FiltrationSystem:
    """
    Base class representing a generic filtration system.
    """
    def __init__(self, name, max_capacity):
        """
        Initialize the filtration system.

        :param name: Name of the filtration system (UF or RO).
        :param max_capacity: Maximum processing capacity in liters per day.
        """
        self.name = name
        self.max_capacity = max_capacity
        self.water_processed = 0

    def process_water(self, input_water):
        """
        Process water through the filtration system.

        :param input_water: Amount of water (in liters) to process.
        :return: Amount of clean water (in liters) produced.
        """
        if input_water < 0:
            raise ValueError("Input water must be a non-negative value.")
        if input_water > self.max_capacity:
            raise ValueError(f"Input water exceeds system's maximum capacity of {self.max_capacity} liters.")
        
        self.water_processed += input_water
        # Assume 95% efficiency for UF and 99% for RO
        efficiency = 0.95 if self.name == "UF" else 0.99
        return input_water * efficiency

    def usage_summary(self):
        """
        Provide a summary of the system's usage.

        :return: A string summarizing the total water processed.
        """
        return f"{self.name} System has processed {self.water_processed:.2f} liters of water."

class ResidentialBuilding:
    """
    Class representing a residential building with integrated filtration systems.
    """
    def __init__(self, uf_capacity, ro_capacity):
        """
        Initialize the residential building's filtration systems.

        :param uf_capacity: Maximum capacity of the UF system (liters per day).
        :param ro_capacity: Maximum capacity of the RO system (liters per day).
        """
        self.uf_system = FiltrationSystem("UF", uf_capacity)
        self.ro_system = FiltrationSystem("RO", ro_capacity)

    def supply_clean_water(self, uf_input, ro_input):
        """
        Simulate supplying clean water using UF and RO systems.

        :param uf_input: Amount of water input to the UF system (in liters).
        :param ro_input: Amount of water input to the RO system (in liters).
        :return: A tuple of clean water produced by UF and RO systems.
        """
        try:
            uf_clean_water = self.uf_system.process_water(uf_input)
            ro_clean_water = self.ro_system.process_water(ro_input)
            return uf_clean_water, ro_clean_water
        except ValueError as e:
            print(f"Error: {e}")
            return None, None

    def building_summary(self):
        """
        Provide a summary of the building's water filtration systems usage.

        :return: A string summarizing the usage of UF and RO systems.
        """
        return f"{self.uf_system.usage_summary()}\n{self.ro_system.usage_summary()}"

# Example usage
if __name__ == "__main__":
    # Initialize residential building with UF and RO system capacities
    building = ResidentialBuilding(uf_capacity=500, ro_capacity=300)

    # Simulate water input
    uf_input = 450  # Example input in liters for UF
    ro_input = 250  # Example input in liters for RO

    uf_clean, ro_clean = building.supply_clean_water(uf_input, ro_input)

    if uf_clean is not None and ro_clean is not None:
        print(f"Clean water produced: \nUF System: {uf_clean:.2f} liters\nRO System: {ro_clean:.2f} liters")

    # Display usage summary
    print("\nFiltration Systems Usage Summary:")
    print(building.building_summary())
```
