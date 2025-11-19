"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: Explain how to design a fire suppression system that complies with modern safety codes, using guidelines from Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_718f43536aee05c4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fire_suppression_system.py

class FireSuppressionSystem:
    """
    Designs a fire suppression system that complies with modern safety codes.

    Attributes:
        occupancy_type (str): Type of occupancy (e.g., office, residential, industrial)
        building_area (float): Area of the building in square feet
        hazard_level (str): Level of hazard (e.g., low, moderate, high)
    """

    def __init__(self, occupancy_type, building_area, hazard_level):
        """
        Initializes a FireSuppressionSystem object.

        Args:
            occupancy_type (str): Type of occupancy
            building_area (float): Area of the building in square feet
            hazard_level (str): Level of hazard

        Raises:
            ValueError: If occupancy type, building area, or hazard level is invalid
        """
        valid_occupancy_types = ["office", "residential", "industrial"]
        valid_hazard_levels = ["low", "moderate", "high"]

        if occupancy_type not in valid_occupancy_types:
            raise ValueError("Invalid occupancy type")
        if building_area <= 0:
            raise ValueError("Building area must be greater than zero")
        if hazard_level not in valid_hazard_levels:
            raise ValueError("Invalid hazard level")

        self.occupancy_type = occupancy_type
        self.building_area = building_area
        self.hazard_level = hazard_level

    def calculate_design_density(self):
        """
        Calculates the design density for the fire suppression system.

        Returns:
            float: Design density in gallons per minute per square foot
        """
        # Guidelines from Independence Fire Sprinkler Company
        design_densities = {
            "office": 0.1,
            "residential": 0.05,
            "industrial": 0.2
        }

        # Adjust design density based on hazard level
        if self.hazard_level == "high":
            return design_densities[self.occupancy_type] * 1.5
        elif self.hazard_level == "moderate":
            return design_densities[self.occupancy_type] * 1.0
        else:
            return design_densities[self.occupancy_type]

    def calculate_required_water_supply(self):
        """
        Calculates the required water supply for the fire suppression system.

        Returns:
            float: Required water supply in gallons per minute
        """
        design_density = self.calculate_design_density()
        return design_density * self.building_area

    def design_system(self):
        """
        Designs the fire suppression system.

        Returns:
            dict: System design parameters
        """
        system_design = {
            "occupancy_type": self.occupancy_type,
            "building_area": self.building_area,
            "hazard_level": self.hazard_level,
            "design_density": self.calculate_design_density(),
            "required_water_supply": self.calculate_required_water_supply()
        }

        # Additional system design parameters (e.g., pipe size, sprinkler type)
        # These would typically be determined based on the specific requirements of the system
        system_design["pipe_size"] = self.calculate_pipe_size()
        system_design["sprinkler_type"] = self.determine_sprinkler_type()

        return system_design

    def calculate_pipe_size(self):
        """
        Calculates the required pipe size for the fire suppression system.

        Returns:
            str: Required pipe size (e.g., 1", 2", 3")
        """
        # This is a simplified example and actual pipe size calculation would depend on various factors
        required_water_supply = self.calculate_required_water_supply()
        if required_water_supply < 100:
            return "1\""
        elif required_water_supply < 500:
            return "2\""
        else:
            return "3\""

    def determine_sprinkler_type(self):
        """
        Determines the required sprinkler type for the fire suppression system.

        Returns:
            str: Required sprinkler type (e.g., standard response, quick response)
        """
        # This is a simplified example and actual sprinkler type determination would depend on various factors
        if self.hazard_level == "high":
            return "quick response"
        else:
            return "standard response"


def main():
    try:
        occupancy_type = "office"
        building_area = 10000
        hazard_level = "moderate"

        system = FireSuppressionSystem(occupancy_type, building_area, hazard_level)
        system_design = system.design_system()

        print("System Design Parameters:")
        for parameter, value in system_design.items():
            print(f"{parameter.capitalize().replace('_', ' ')}: {value}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
