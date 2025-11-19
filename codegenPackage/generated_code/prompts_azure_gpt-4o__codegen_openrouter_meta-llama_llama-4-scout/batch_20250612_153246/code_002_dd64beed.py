"""
Generated Code Metadata:
========================
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: Generate a script to calculate the cost estimation for roads and highways construction projects, incorporating factors mentioned on the Bismillah Traders site.
Generated: DETERMINISTIC_dd64beed66640cc6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cost_estimation.py

class RoadConstructionCostEstimator:
    """
    Estimates the cost of a road construction project.

    Attributes:
        length (float): Length of the road in kilometers.
        width (float): Width of the road in meters.
        thickness (float): Thickness of the asphalt layer in centimeters.
        asphalt_cost_per_ton (float): Cost of asphalt per ton.
        labor_cost_per_hour (float): Labor cost per hour.
        equipment_cost_per_hour (float): Equipment cost per hour.
        density_asphalt (float): Density of asphalt in tons per cubic meter.
    """

    def __init__(self, length, width, thickness, asphalt_cost_per_ton, labor_cost_per_hour, equipment_cost_per_hour):
        """
        Initializes the RoadConstructionCostEstimator.

        Args:
            length (float): Length of the road in kilometers.
            width (float): Width of the road in meters.
            thickness (float): Thickness of the asphalt layer in centimeters.
            asphalt_cost_per_ton (float): Cost of asphalt per ton.
            labor_cost_per_hour (float): Labor cost per hour.
            equipment_cost_per_hour (float): Equipment cost per hour.
        """
        self.length = length
        self.width = width
        self.thickness = thickness / 100  # Convert to meters
        self.asphalt_cost_per_ton = asphalt_cost_per_ton
        self.labor_cost_per_hour = labor_cost_per_hour
        self.equipment_cost_per_hour = equipment_cost_per_hour
        self.density_asphalt = 2.2  # Average density of asphalt in tons per cubic meter

    def calculate_asphalt_volume(self):
        """
        Calculates the volume of asphalt required in cubic meters.

        Returns:
            float: Volume of asphalt required.
        """
        # Calculate the area of the road in square meters
        road_area = self.length * 1000 * self.width

        # Calculate the volume of asphalt required in cubic meters
        asphalt_volume = road_area * self.thickness

        return asphalt_volume

    def calculate_asphalt_cost(self):
        """
        Calculates the cost of asphalt required.

        Returns:
            float: Cost of asphalt required.
        """
        asphalt_volume = self.calculate_asphalt_volume()
        asphalt_weight = asphalt_volume * self.density_asphalt
        asphalt_cost = asphalt_weight * self.asphalt_cost_per_ton

        return asphalt_cost

    def calculate_labor_cost(self):
        """
        Estimates the labor cost for the project.

        Returns:
            float: Labor cost for the project.
        """
        # Assume 8 hours of work per day and 20 days of work per kilometer
        labor_hours = self.length * 20 * 8
        labor_cost = labor_hours * self.labor_cost_per_hour

        return labor_cost

    def calculate_equipment_cost(self):
        """
        Estimates the equipment cost for the project.

        Returns:
            float: Equipment cost for the project.
        """
        # Assume 8 hours of equipment usage per day and 20 days of work per kilometer
        equipment_hours = self.length * 20 * 8
        equipment_cost = equipment_hours * self.equipment_cost_per_hour

        return equipment_cost

    def estimate_total_cost(self):
        """
        Estimates the total cost of the road construction project.

        Returns:
            float: Total cost of the project.
        """
        asphalt_cost = self.calculate_asphalt_cost()
        labor_cost = self.calculate_labor_cost()
        equipment_cost = self.calculate_equipment_cost()
        total_cost = asphalt_cost + labor_cost + equipment_cost

        return total_cost


def main():
    try:
        length = float(input("Enter the length of the road in kilometers: "))
        width = float(input("Enter the width of the road in meters: "))
        thickness = float(input("Enter the thickness of the asphalt layer in centimeters: "))
        asphalt_cost_per_ton = float(input("Enter the cost of asphalt per ton: "))
        labor_cost_per_hour = float(input("Enter the labor cost per hour: "))
        equipment_cost_per_hour = float(input("Enter the equipment cost per hour: "))

        estimator = RoadConstructionCostEstimator(length, width, thickness, asphalt_cost_per_ton, labor_cost_per_hour, equipment_cost_per_hour)

        print(f"Asphalt cost: ${estimator.calculate_asphalt_cost():,.2f}")
        print(f"Labor cost: ${estimator.calculate_labor_cost():,.2f}")
        print(f"Equipment cost: ${estimator.calculate_equipment_cost():,.2f}")
        print(f"Total cost: ${estimator.estimate_total_cost():,.2f}")

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
```
