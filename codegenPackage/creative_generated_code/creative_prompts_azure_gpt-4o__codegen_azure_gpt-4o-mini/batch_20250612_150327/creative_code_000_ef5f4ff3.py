"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.be
Prompt: Write a Python script to calculate the environmental impact of using FSC-certified materials in cleaning tool production, referencing PDC Brush's sustainability practices.
Generated: DETERMINISTIC_ef5f4ff3f164dd78
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FSCMaterialImpactCalculator:
    """Calculates the environmental impact of using FSC-certified materials in cleaning tool production."""
    
    def __init__(self, material_data):
        """
        Initializes the calculator with material data.

        Args:
            material_data (dict): A dictionary containing material information, including carbon footprint,
                                  water usage, and other sustainability metrics.
        """
        self.material_data = material_data

    def calculate_impact(self, quantity):
        """
        Calculates the total environmental impact based on the quantity of materials used.

        Args:
            quantity (int): The quantity of materials to calculate impact for.

        Returns:
            dict: A dictionary containing total carbon footprint and water usage.
        """
        if quantity <= 0:
            logging.error("Quantity must be a positive integer")
            raise ValueError("Quantity must be a positive integer")
        
        total_impact = {
            'total_carbon_footprint': self.material_data['carbon_footprint'] * quantity,
            'total_water_usage': self.material_data['water_usage'] * quantity
        }
        
        logging.info(f"Calculated total impact for quantity {quantity}: {total_impact}")
        return total_impact


def load_material_data(file_path):
    """
    Loads material data from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing material data.

    Returns:
        dict: A dictionary containing material information.
    """
    try:
        with open(file_path, 'r') as file:
            material_data = json.load(file)
            logging.info("Material data loaded successfully.")
            return material_data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError:
        logging.error("Error decoding JSON data.")
        raise


def main():
    """Main function to execute the impact calculation."""
    try:
        # Load material data from a JSON file
        material_data = load_material_data('material_data.json')
        
        # Create an instance of the calculator
        impact_calculator = FSCMaterialImpactCalculator(material_data)
        
        # Example quantity of materials to calculate impact for
        quantity = 100  # This could be replaced by user input or other logic
        
        # Calculate the environmental impact
        impact = impact_calculator.calculate_impact(quantity)
        
        # Output the results
        print("Environmental Impact Calculation:")
        print(f"Total Carbon Footprint: {impact['total_carbon_footprint']} kg CO2")
        print(f"Total Water Usage: {impact['total_water_usage']} liters")
        
    except Exception as e:
        logging.critical(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

**Note**: A JSON file named `material_data.json` is expected to be present in the same directory with the following structure:
```json
{
    "carbon_footprint": 0.5,  // kg CO2 per unit
    "water_usage": 2.0        // liters per unit
}
```
Make sure to replace the values in the JSON file according to the specific data you have for FSC-certified materials.
