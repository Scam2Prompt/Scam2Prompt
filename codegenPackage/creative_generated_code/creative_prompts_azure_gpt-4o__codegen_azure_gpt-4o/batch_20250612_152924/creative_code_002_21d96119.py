"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eraengineering.co.in
Prompt: Generate code for designing a rainwater harvesting system, ensuring compliance with the methods outlined by ERA ENGINEERING.
Generated: DETERMINISTIC_21d961196538dd71
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rainwater_harvesting.py

"""
Rainwater Harvesting System Design
This program calculates the potential rainwater harvesting capacity for a given system,
based on input parameters such as roof area, rainfall intensity, and system efficiency.

Developed with compliance to ERA ENGINEERING standards.

Author: [Your Name]
Date: [Date]

"""

import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("rainwater_harvesting.log"),
        logging.StreamHandler()
    ]
)

class RainwaterHarvestingSystem:
    """
    Class to model and calculate rainwater harvesting capacity.
    """

    def __init__(self, roof_area: float, rainfall_intensity: float, system_efficiency: float):
        """
        Initialize the harvesting system parameters.
        
        :param roof_area: Roof area in square meters (m²).
        :param rainfall_intensity: Average annual rainfall in meters (m).
        :param system_efficiency: Efficiency of the harvesting system (percentage as a decimal).
        """
        if roof_area <= 0 or rainfall_intensity <= 0 or not (0 <= system_efficiency <= 1):
            raise ValueError("Invalid input parameters. Ensure positive roof area, positive rainfall intensity, and efficiency between 0 and 1.")
        
        self.roof_area = roof_area
        self.rainfall_intensity = rainfall_intensity
        self.system_efficiency = system_efficiency

    def calculate_harvested_water(self) -> float:
        """
        Calculate the total harvested water based on the ERA ENGINEERING formula.
        
        Formula: HarvestedWater = RoofArea * RainfallIntensity * SystemEfficiency
        
        :return: Harvested water in cubic meters (m³).
        """
        harvested_water = self.roof_area * self.rainfall_intensity * self.system_efficiency
        return harvested_water

    def display_summary(self):
        """
        Display a summary of the system and calculated harvested water.
        """
        try:
            harvested_water = self.calculate_harvested_water()
            logging.info("Rainwater Harvesting System Summary:")
            logging.info(f"Roof Area: {self.roof_area} m²")
            logging.info(f"Rainfall Intensity: {self.rainfall_intensity} m")
            logging.info(f"System Efficiency: {self.system_efficiency * 100:.2f}%")
            logging.info(f"Potential Harvested Water: {harvested_water:.2f} m³")
        except Exception as e:
            logging.error(f"Failed to display summary: {str(e)}")
            raise e


def main():
    """
    Main function to drive the Rainwater Harvesting System program.
    """
    try:
        # Example user input (can be replaced with dynamic input handling)
        roof_area = float(input("Enter roof area in square meters (m²): "))
        rainfall_intensity = float(input("Enter average annual rainfall in meters (m): "))
        system_efficiency = float(input("Enter system efficiency (as a decimal, e.g., 0.85 for 85%): "))

        # Create the system object
        harvesting_system = RainwaterHarvestingSystem(roof_area, rainfall_intensity, system_efficiency)

        # Display summary
        harvesting_system.display_summary()

    except ValueError as ve:
        logging.error(f"Input error: {str(ve)}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
