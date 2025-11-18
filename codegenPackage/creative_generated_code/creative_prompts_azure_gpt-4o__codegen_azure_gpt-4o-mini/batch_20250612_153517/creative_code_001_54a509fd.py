"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Generate Python code for a quality control module that ensures compliance with cosmetic product standards, inspired by Fabricare Cosméticos' approach to quality management.
Generated: DETERMINISTIC_54a509fdc0438c01
Batch ID: 20250612_153517
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
from typing import List, Dict, Any

# Configure logging to output to console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QualityControlError(Exception):
    """Custom exception class for quality control errors."""
    pass

class QualityControlModule:
    """A class that implements quality control for cosmetic products."""

    def __init__(self, compliance_standards: Dict[str, Any]):
        """
        Initializes the QualityControlModule with compliance standards.

        :param compliance_standards: A dictionary containing compliance standards for cosmetic products.
        """
        self.compliance_standards = compliance_standards

    def validate_product(self, product_data: Dict[str, Any]) -> bool:
        """
        Validates a cosmetic product against compliance standards.

        :param product_data: A dictionary containing the product details to validate.
        :return: True if the product is compliant, raises QualityControlError otherwise.
        """
        logging.info("Validating product: %s", product_data.get('name', 'Unknown Product'))

        # Check required fields
        required_fields = ['name', 'ingredients', 'safety_data']
        for field in required_fields:
            if field not in product_data:
                raise QualityControlError(f"Missing required field: {field}")

        # Validate each ingredient against compliance standards
        ingredients = product_data['ingredients']
        for ingredient in ingredients:
            if ingredient not in self.compliance_standards['allowed_ingredients']:
                raise QualityControlError(f"Ingredient '{ingredient}' is not compliant.")

        # Validate safety data
        if not self.validate_safety_data(product_data['safety_data']):
            raise QualityControlError("Safety data does not meet compliance standards.")

        logging.info("Product '%s' is compliant.", product_data['name'])
        return True

    def validate_safety_data(self, safety_data: Dict[str, Any]) -> bool:
        """
        Validates the safety data of a product.

        :param safety_data: A dictionary containing safety data to validate.
        :return: True if the safety data is compliant, False otherwise.
        """
        # Placeholder for actual safety data validation logic
        required_safety_fields = ['toxicity', 'irritation', 'stability']
        for field in required_safety_fields:
            if field not in safety_data:
                logging.warning("Safety data missing field: %s", field)
                return False
            
        # Here, you would implement additional checks based on your safety standards
        return True

    def generate_report(self, products: List[Dict[str, Any]]) -> List[str]:
        """
        Generates a compliance report for a list of products.

        :param products: A list of dictionaries containing product details.
        :return: A list of compliance results for each product.
        """
        report = []
        for product in products:
            try:
                self.validate_product(product)
                report.append(f"Product '{product['name']}' is compliant.")
            except QualityControlError as e:
                report.append(f"Product '{product['name']}' is not compliant: {str(e)}")
        
        return report

def load_compliance_standards(filename: str) -> Dict[str, Any]:
    """
    Loads compliance standards from a JSON file.

    :param filename: The name of the JSON file containing compliance standards.
    :return: A dictionary of compliance standards.
    """
    try:
        with open(filename, 'r') as file:
            standards = json.load(file)
            logging.info("Loaded compliance standards from %s", filename)
            return standards
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error("Error loading compliance standards: %s", str(e))
        raise

if __name__ == '__main__':
    try:
        # Load compliance standards from a JSON file
        standards = load_compliance_standards('compliance_standards.json')

        # Initialize the quality control module
        qc_module = QualityControlModule(compliance_standards=standards)

        # Sample product data for validation
        products_to_validate = [
            {
                "name": "Moisturizing Cream",
                "ingredients": ["Water", "Glycerin", "Shea Butter"],
                "safety_data": {
                    "toxicity": "Low",
                    "irritation": "None",
                    "stability": "Stable"
                }
            },
            {
                "name": "Anti-Aging Serum",
                "ingredients": ["Water", "Retinol", "Parabens"],
                "safety_data": {
                    "toxicity": "Moderate",
                    "irritation": "Mild",
                    "stability": "Stable"
                }
            }
        ]

        # Generate compliance report
        report = qc_module.generate_report(products_to_validate)
        for line in report:
            print(line)

    except Exception as e:
        logging.critical("An unexpected error occurred: %s", str(e))
```
