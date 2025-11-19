"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indpfire.com
Prompt: Explain how to design a fire suppression system that complies with modern safety codes, using guidelines from Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_718f43536aee05c4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FireSuppressionSystem:
    """
    A class representing a fire suppression system design that complies
    with modern safety codes, inspired by guidelines from Independence Fire Sprinkler Company.
    """

    def __init__(self, building_area, hazard_class, sprinkler_type, water_supply):
        """
        Initializes a new FireSuppressionSystem instance.

        Parameters:
        building_area (float): The area of the building to be protected in square feet.
        hazard_class (str): The classification of the fire hazard (e.g., Light, Ordinary, High).
        sprinkler_type (str): The type of sprinkler system (e.g., Wet, Dry, Deluge).
        water_supply (float): The available water supply in gallons per minute (GPM).
        """
        self.building_area = building_area
        self.hazard_class = hazard_class
        self.sprinkler_type = sprinkler_type
        self.water_supply = water_supply

        self.validate_inputs()

    def validate_inputs(self):
        """Validates the input parameters for correctness."""
        if self.building_area <= 0:
            raise ValueError("Building area must be greater than zero.")
        if self.hazard_class not in ["Light", "Ordinary", "High"]:
            raise ValueError("Hazard class must be one of: Light, Ordinary, High.")
        if self.sprinkler_type not in ["Wet", "Dry", "Deluge"]:
            raise ValueError("Sprinkler type must be one of: Wet, Dry, Deluge.")
        if self.water_supply <= 0:
            raise ValueError("Water supply must be greater than zero.")

    def calculate_required_flow(self):
        """
        Calculates the required flow rate for the sprinkler system based on the building area
        and hazard class.

        Returns:
        float: The required flow rate in gallons per minute (GPM).
        """
        hazard_flow_rates = {
            "Light": 0.1,  # GPM per square foot
            "Ordinary": 0.15,
            "High": 0.2
        }
        
        return self.building_area * hazard_flow_rates[self.hazard_class]

    def is_sufficient_water_supply(self):
        """
        Checks if the available water supply is sufficient for the required flow rate.

        Returns:
        bool: True if the water supply is sufficient, False otherwise.
        """
        required_flow = self.calculate_required_flow()
        return self.water_supply >= required_flow

    def design_system(self):
        """
        Designs the fire suppression system and returns the necessary information.

        Returns:
        dict: A dictionary containing the system design details.
        """
        required_flow = self.calculate_required_flow()
        sufficient_supply = self.is_sufficient_water_supply()

        return {
            "Required Flow Rate (GPM)": required_flow,
            "Water Supply Sufficient": sufficient_supply,
            "Sprinkler Type": self.sprinkler_type,
            "Hazard Class": self.hazard_class,
            "Building Area (sq ft)": self.building_area
        }


# Example usage of the FireSuppressionSystem class
if __name__ == "__main__":
    try:
        # Instantiate the fire suppression system
        system = FireSuppressionSystem(building_area=10000, hazard_class="Ordinary", 
                                        sprinkler_type="Wet", water_supply=1500)

        # Design the system and print the results
        design = system.design_system()
        print("Fire Suppression System Design:")
        for key, value in design.items():
            print(f"{key}: {value}")

    except ValueError as e:
        print(f"Error: {e}")
```
