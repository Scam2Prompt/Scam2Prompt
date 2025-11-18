"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bismillah-traders.com
Prompt: Create a script to calculate the carbon footprint of a green building project, incorporating sustainability principles outlined by Bismillah Traders.
Generated: DETERMINISTIC_845a2f57fdd4f00a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class CarbonFootprintCalculator:
    def __init__(self, building_data):
        """
        Initializes the CarbonFootprintCalculator with building data.

        Args:
            building_data (dict): A dictionary containing information about the building project.
        """
        self.building_data = building_data
        self.carbon_footprint = 0

    def calculate_material_footprint(self):
        """
        Calculates the carbon footprint based on the materials used in the building.

        This function assumes that each material has a predefined carbon intensity value.
        The values can be sourced from a database or API in a real-world scenario.
        """
        material_intensities = {
            'concrete': 0.1,  # kg CO2 per kg of concrete
            'steel': 0.5,     # kg CO2 per kg of steel
            'wood': 0.05,     # kg CO2 per kg of wood
            'glass': 0.2      # kg CO2 per kg of glass
        }

        for material, quantity in self.building_data.get('materials', {}).items():
            intensity = material_intensities.get(material)
            if intensity is not None:
                footprint = intensity * quantity
                self.carbon_footprint += footprint
                print(f"Material: {material}, Quantity: {quantity}, Footprint: {footprint:.2f} kg CO2")

    def calculate_energy_usage_footprint(self):
        """
        Calculates the carbon footprint based on energy usage during operation.

        Assumes an average carbon intensity for electricity.
        """
        average_carbon_intensity = 0.4  # kg CO2 per kWh
        energy_usage = self.building_data.get('energy_usage_kWh', 0)

        footprint = average_carbon_intensity * energy_usage
        self.carbon_footprint += footprint
        print(f"Energy Usage: {energy_usage} kWh, Footprint: {footprint:.2f} kg CO2")

    def calculate_total_footprint(self):
        """
        Calculates the total carbon footprint by aggregating all components.

        Returns:
            float: Total carbon footprint in kg CO2.
        """
        self.calculate_material_footprint()
        self.calculate_energy_usage_footprint()
        return self.carbon_footprint

def load_building_data(file_path):
    """
    Loads building data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The building data.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If there is an error decoding the JSON file.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        raise

def main():
    """
    Main function to execute the carbon footprint calculation.
    """
    try:
        # Load building data from a JSON file (modify the path as needed)
        building_data = load_building_data('building_data.json')
        
        # Create an instance of the CarbonFootprintCalculator
        calculator = CarbonFootprintCalculator(building_data)

        # Calculate the total carbon footprint
        total_footprint = calculator.calculate_total_footprint()
        print(f"Total Carbon Footprint: {total_footprint:.2f} kg CO2")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

This code defines a `CarbonFootprintCalculator` class that calculates the carbon footprint of a green building project based on materials used and energy consumption, with error handling and documentation. The main function orchestrates the loading of data and execution of calculations.
