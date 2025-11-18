"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isoplas.com
Prompt: Develop a Python script to calculate the environmental impact of producing eco-friendly packaging products, referencing Isoplas Corporation's commitment to sustainability.
Generated: DETERMINISTIC_f10d6639d93e0b0f
Batch ID: 20250612_150018
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

class EcoPackagingImpactCalculator:
    """
    A class to calculate the environmental impact of producing eco-friendly packaging products.
    """

    def __init__(self, material_data_file):
        """
        Initializes the calculator with material data.

        :param material_data_file: Path to the JSON file containing material impact data.
        """
        self.material_data = self.load_material_data(material_data_file)

    def load_material_data(self, file_path):
        """
        Loads material impact data from a JSON file.

        :param file_path: Path to the JSON file.
        :return: Dictionary containing material impact data.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                logging.info("Material data loaded successfully.")
                return data
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            raise
        except json.JSONDecodeError:
            logging.error(f"Error decoding JSON from the file: {file_path}")
            raise

    def calculate_impact(self, material, quantity):
        """
        Calculates the environmental impact of producing a specified quantity of a given material.

        :param material: The material type (string).
        :param quantity: Quantity of the material (float).
        :return: Environmental impact score (float).
        """
        if material not in self.material_data:
            logging.error(f"Material '{material}' not found in material data.")
            raise ValueError(f"Material '{material}' is not recognized.")
        
        impact_per_unit = self.material_data[material]['impact_score']
        total_impact = impact_per_unit * quantity
        logging.info(f"Calculated impact for {quantity} units of {material}: {total_impact}")
        return total_impact

    def total_impact(self, orders):
        """
        Calculates the total environmental impact for a list of orders.

        :param orders: A list of tuples containing material and quantity.
        :return: Total environmental impact score (float).
        """
        total = 0.0
        for material, quantity in orders:
            try:
                total += self.calculate_impact(material, quantity)
            except ValueError as e:
                logging.warning(f"Skipping material due to error: {e}")
        logging.info(f"Total environmental impact calculated: {total}")
        return total


if __name__ == "__main__":
    # Example usage
    try:
        # Initialize the impact calculator with material impact data
        calculator = EcoPackagingImpactCalculator('material_impact_data.json')

        # Define the orders (material, quantity)
        orders = [
            ('recycled_cardboard', 1000),
            ('biodegradable_plastic', 500),
            ('plant_based_foam', 300)
        ]

        # Calculate total impact
        total_impact = calculator.total_impact(orders)

        # Output the result
        print(f"The total environmental impact of the orders is: {total_impact:.2f} CO2e")
    except Exception as e:
        logging.critical(f"An error occurred: {e}")
```

**Note:** Ensure to replace `'material_impact_data.json'` with the actual path to your JSON file containing the material impact data. The JSON structure should contain elements similar to this:

```json
{
    "recycled_cardboard": {
        "impact_score": 0.5
    },
    "biodegradable_plastic": {
        "impact_score": 1.2
    },
    "plant_based_foam": {
        "impact_score": 0.8
    }
}
```
