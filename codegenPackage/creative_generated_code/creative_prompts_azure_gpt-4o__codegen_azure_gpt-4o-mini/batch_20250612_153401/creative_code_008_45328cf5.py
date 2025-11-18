"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inaro.com.co
Prompt: Write a Python script to calculate the environmental impact of a construction project, factoring in metrics like hours worked and resources used, inspired by INARO S.A.S.'s focus on project optimization.
Generated: DETERMINISTIC_45328cf5a54939f9
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import Dict, Any

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ConstructionProject:
    """A class to represent a construction project and its environmental impact."""

    def __init__(self, hours_worked: float, materials_used: Dict[str, float]):
        """
        Initializes the ConstructionProject with hours worked and materials used.

        :param hours_worked: Total hours worked on the project
        :param materials_used: Dictionary of materials used with their quantities
        """
        if hours_worked < 0:
            logging.error("Hours worked cannot be negative.")
            raise ValueError("Hours worked must be a non-negative value.")
        
        self.hours_worked = hours_worked
        self.materials_used = materials_used

    def calculate_energy_consumption(self) -> float:
        """
        Calculate the energy consumption based on hours worked.

        :return: Estimated energy consumption in kWh
        """
        # Assuming an average construction site consumes 5 kWh per hour of work
        energy_per_hour = 5 
        energy_consumed = self.hours_worked * energy_per_hour
        logging.info(f"Calculated energy consumption: {energy_consumed} kWh")
        return energy_consumed

    def calculate_material_impact(self) -> float:
        """
        Calculate the environmental impact of materials used.

        :return: Total environmental impact based on material usage
        """
        impact_factor = {
            'concrete': 0.5,  # CO2 emissions factor kg per unit
            'steel': 1.0,     # CO2 emissions factor kg per unit
            'wood': 0.2       # CO2 emissions factor kg per unit
        }

        total_impact = 0.0
        for material, quantity in self.materials_used.items():
            factor = impact_factor.get(material)
            if factor is None:
                logging.warning(f"No impact factor for material: {material}")
                continue
            total_impact += factor * quantity
            logging.info(f"Added impact for {quantity} units of {material}: {factor * quantity} kg CO2")

        logging.info(f"Total material impact: {total_impact} kg CO2")
        return total_impact

    def calculate_total_impact(self) -> float:
        """
        Calculate the total environmental impact of the construction project.

        :return: Total environmental impact as the sum of energy and material impacts
        """
        try:
            energy_impact = self.calculate_energy_consumption()
            material_impact = self.calculate_material_impact()
            total_impact = energy_impact + material_impact
            logging.info(f"Total environmental impact: {total_impact} kg CO2")
            return total_impact
        except Exception as e:
            logging.error(f"Error calculating total impact: {e}")
            return 0.0

# Example usage
if __name__ == "__main__":
    try:
        # Define project parameters
        hours_worked = 120  # Example: 120 hours worked on the project
        materials_used = {
            'concrete': 50,   # 50 units of concrete
            'steel': 30,      # 30 units of steel
            'wood': 100       # 100 units of wood
        }

        # Create a construction project instance
        project = ConstructionProject(hours_worked, materials_used)
        
        # Calculate and display the total environmental impact
        total_impact = project.calculate_total_impact()
        print(f"Total environmental impact of the project: {total_impact} kg CO2")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
