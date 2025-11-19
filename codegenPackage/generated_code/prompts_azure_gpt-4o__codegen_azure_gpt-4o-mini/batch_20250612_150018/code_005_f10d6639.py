"""
Generated Code Metadata:
========================
Original URL: https://isoplas.com
Prompt: Develop a Python script to calculate the environmental impact of producing eco-friendly packaging products, referencing Isoplas Corporation's commitment to sustainability.
Generated: DETERMINISTIC_f10d6639d93e0b0f
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EcoPackagingCalculator:
    """
    A class to calculate the environmental impact of producing eco-friendly packaging products.
    """

    def __init__(self, material_data_file):
        """
        Initializes the EcoPackagingCalculator with material data.

        :param material_data_file: Path to the JSON file containing material data.
        """
        self.material_data = self.load_material_data(material_data_file)

    def load_material_data(self, file_path):
        """
        Loads material data from a JSON file.

        :param file_path: Path to the JSON file.
        :return: Dictionary containing material data.
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
            logging.error("Error decoding JSON from the file.")
            raise

    def calculate_impact(self, material_type, quantity):
        """
        Calculates the environmental impact based on material type and quantity.

        :param material_type: Type of material (e.g., 'biodegradable', 'recyclable').
        :param quantity: Quantity of material in kilograms.
        :return: Environmental impact score.
        """
        if material_type not in self.material_data:
            logging.error(f"Material type '{material_type}' not found in material data.")
            raise ValueError(f"Material type '{material_type}' is not valid.")

        impact_factor = self.material_data[material_type]['impact_factor']
        impact_score = impact_factor * quantity
        logging.info(f"Calculated impact for {quantity}kg of {material_type}: {impact_score}")
        return impact_score

    def total_impact(self, orders):
        """
        Calculates the total environmental impact for a list of orders.

        :param orders: List of tuples containing (material_type, quantity).
        :return: Total environmental impact score.
        """
        total_score = 0
        for material_type, quantity in orders:
            try:
                total_score += self.calculate_impact(material_type, quantity)
            except ValueError as e:
                logging.warning(e)
        logging.info(f"Total environmental impact score: {total_score}")
        return total_score

if __name__ == "__main__":
    # Example usage
    try:
        calculator = EcoPackagingCalculator('material_data.json')
        orders = [
            ('biodegradable', 100),  # 100 kg of biodegradable material
            ('recyclable', 50),      # 50 kg of recyclable material
        ]
        total_impact_score = calculator.total_impact(orders)
        print(f"Total Environmental Impact Score: {total_impact_score}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

**Note:** Ensure that you have a `material_data.json` file structured appropriately with material types and their corresponding impact factors for the script to run successfully.
