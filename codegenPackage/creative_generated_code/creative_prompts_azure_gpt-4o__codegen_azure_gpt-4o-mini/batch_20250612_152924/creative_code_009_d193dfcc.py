"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eraengineering.co.in
Prompt: Provide a step-by-step guide for implementing a stormwater management system, referencing the solutions offered by ERA ENGINEERING.
Generated: DETERMINISTIC_d193dfccf59f3fd4
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StormwaterManagementSystem:
    """
    A class to represent a stormwater management system, implementing various components
    for effective stormwater management as suggested by ERA ENGINEERING.
    """

    def __init__(self):
        """
        Initializes the stormwater management system with default parameters.
        """
        self.reservoirs = []
        self.infiltration_beds = []
        self.bioretention_cells = []
        self.discharge_points = []

    def add_reservoir(self, capacity: float):
        """
        Adds a reservoir to the stormwater management system.

        :param capacity: The maximum capacity of the reservoir in cubic meters.
        """
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self.reservoirs.append(capacity)

    def add_infiltration_bed(self, area: float):
        """
        Adds an infiltration bed to the stormwater management system.

        :param area: The area of the infiltration bed in square meters.
        """
        if area <= 0:
            raise ValueError("Area must be greater than zero.")
        self.infiltration_beds.append(area)

    def add_bioretention_cell(self, volume: float):
        """
        Adds a bioretention cell to the stormwater management system.

        :param volume: The volume of the bioretention cell in cubic meters.
        """
        if volume <= 0:
            raise ValueError("Volume must be greater than zero.")
        self.bioretention_cells.append(volume)

    def add_discharge_point(self, location: str):
        """
        Adds a discharge point to the stormwater management system.

        :param location: The geographical location of the discharge point.
        """
        if not location:
            raise ValueError("Location cannot be empty.")
        self.discharge_points.append(location)

    def calculate_total_storage(self) -> float:
        """
        Calculates the total storage capacity of the stormwater management system.

        :return: Total storage capacity in cubic meters.
        """
        total_capacity = sum(self.reservoirs) + sum(self.bioretention_cells)
        return total_capacity

    def generate_report(self) -> str:
        """
        Generates a summary report of the stormwater management system components.

        :return: A formatted report string.
        """
        report = (
            f"Stormwater Management System Report\n"
            f"------------------------------------\n"
            f"Total Reservoirs: {len(self.reservoirs)}\n"
            f"Total Infiltration Beds: {len(self.infiltration_beds)}\n"
            f"Total Bioretention Cells: {len(self.bioretention_cells)}\n"
            f"Total Discharge Points: {len(self.discharge_points)}\n"
            f"Total Storage Capacity: {self.calculate_total_storage()} cubic meters\n"
        )
        return report

# Example usage:
if __name__ == "__main__":
    try:
        stormwater_system = StormwaterManagementSystem()
        stormwater_system.add_reservoir(1000)
        stormwater_system.add_infiltration_bed(500)
        stormwater_system.add_bioretention_cell(300)
        stormwater_system.add_discharge_point("North Side")

        print(stormwater_system.generate_report())
    except Exception as e:
        print(f"An error occurred: {e}")
```
