"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: Write a Python script to calculate the environmental impact of a construction project, factoring in metrics like hours worked and resources used, inspired by INARO S.A.S.'s focus on project optimization.
Generated: DETERMINISTIC_45328cf5a54939f9
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ConstructionProject:
    """
    A class to represent a construction project and calculate its environmental impact.
    """

    def __init__(self, hours_worked, resources_used):
        """
        Initializes the ConstructionProject with hours worked and resources used.

        :param hours_worked: Total hours worked on the project
        :param resources_used: Dictionary of resources used with their quantities
        """
        self.hours_worked = hours_worked
        self.resources_used = resources_used

    def calculate_carbon_footprint(self):
        """
        Calculate the carbon footprint based on hours worked and resources used.

        :return: Total carbon footprint in metric tons
        """
        try:
            # Constants for carbon footprint per hour and per resource unit
            carbon_per_hour = 0.1  # Example: 0.1 metric tons of CO2 per hour worked
            carbon_per_resource = {
                'concrete': 0.05,  # Example: 0.05 metric tons of CO2 per unit of concrete
                'steel': 0.07,     # Example: 0.07 metric tons of CO2 per unit of steel
                'wood': 0.03       # Example: 0.03 metric tons of CO2 per unit of wood
            }

            # Calculate total carbon footprint from hours worked
            total_footprint = self.hours_worked * carbon_per_hour

            # Calculate total carbon footprint from resources used
            for resource, quantity in self.resources_used.items():
                if resource in carbon_per_resource:
                    total_footprint += carbon_per_resource[resource] * quantity
                else:
                    logging.warning(f"Resource '{resource}' not recognized. Skipping.")

            return total_footprint

        except Exception as e:
            logging.error(f"Error calculating carbon footprint: {e}")
            return None

def main():
    """
    Main function to execute the environmental impact calculation.
    """
    # Example input data
    hours_worked = 1200  # Total hours worked on the project
    resources_used = {
        'concrete': 500,  # 500 units of concrete
        'steel': 300,     # 300 units of steel
        'wood': 200       # 200 units of wood
    }

    # Create a ConstructionProject instance
    project = ConstructionProject(hours_worked, resources_used)

    # Calculate the carbon footprint
    carbon_footprint = project.calculate_carbon_footprint()

    if carbon_footprint is not None:
        logging.info(f"Total carbon footprint for the project: {carbon_footprint:.2f} metric tons")

if __name__ == "__main__":
    main()
```
