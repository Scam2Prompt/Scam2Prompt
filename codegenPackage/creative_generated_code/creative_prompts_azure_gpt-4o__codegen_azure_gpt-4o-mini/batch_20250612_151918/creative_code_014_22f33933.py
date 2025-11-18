"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Write a Python script to calculate the environmental impact savings of switching to CMQLF's solid cosmetics compared to traditional liquid products.
Generated: DETERMINISTIC_22f3393397d73c31
Batch ID: 20250612_151918
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

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EnvironmentalImpactCalculator:
    def __init__(self, liquid_product_data, solid_product_data):
        """
        Initialize the EnvironmentalImpactCalculator with the data for liquid and solid products.

        Args:
            liquid_product_data (dict): A dictionary containing environmental impact metrics for liquid products.
            solid_product_data (dict): A dictionary containing environmental impact metrics for solid products.
        """
        self.liquid_product_data = liquid_product_data
        self.solid_product_data = solid_product_data

    def calculate_savings(self):
        """
        Calculate the environmental impact savings from switching to solid cosmetics.

        Returns:
            dict: A dictionary with the savings in various metrics.
        """
        try:
            savings = {
                'plastic_saved': self.liquid_product_data['plastic_usage'] - self.solid_product_data['plastic_usage'],
                'water_saved': self.liquid_product_data['water_usage'] - self.solid_product_data['water_usage'],
                'carbon_saved': self.liquid_product_data['carbon_emissions'] - self.solid_product_data['carbon_emissions']
            }
            return savings
        except KeyError as e:
            logging.error(f"Missing data in product metrics: {e}")
            raise ValueError("Invalid product data provided. Please check the input data.")

def load_product_data(file_path):
    """
    Load product data from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing product data.
        
    Returns:
        dict: The loaded product data.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        logging.error("File not found. Please check the file path.")
        raise
    except json.JSONDecodeError:
        logging.error("Error decoding JSON file. Please check the file format.")
        raise

def main():
    """
    Main function to execute the environmental impact savings calculation.
    """
    try:
        # Load product data from JSON files
        liquid_product_data = load_product_data('liquid_product_data.json')
        solid_product_data = load_product_data('solid_product_data.json')

        # Initialize the calculator and calculate savings
        calculator = EnvironmentalImpactCalculator(liquid_product_data, solid_product_data)
        savings = calculator.calculate_savings()

        # Output the results
        logging.info("Environmental Impact Savings:")
        for metric, value in savings.items():
            logging.info(f"{metric}: {value:.2f}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that you have the appropriate JSON files (`liquid_product_data.json` and `solid_product_data.json`) with relevant data structured as follows:

```json
{
    "plastic_usage": 100.0,
    "water_usage": 50.0,
    "carbon_emissions": 30.0
}
``` 

Adjust the values as necessary to reflect the actual environmental impact metrics for the products being compared.
