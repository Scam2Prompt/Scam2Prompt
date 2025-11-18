"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://forestx.se
Prompt: Suggest a workflow for integrating unique measurement products developed in collaboration with Dalgas, as highlighted by ForestX, into forestry management software.
Generated: DETERMINISTIC_e1389b2481887cb9
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import json
from datetime import datetime
from typing import List, Dict, Any

class MeasurementProduct:
    """
    A class to represent a unique measurement product in forestry management.
    """

    def __init__(self, product_id: str, name: str, metrics: Dict[str, Any]):
        """
        Initialize the measurement product with an ID, name, and associated metrics.

        Args:
            product_id (str): Unique identifier for the measurement product.
            name (str): Name of the measurement product.
            metrics (dict): Dictionary containing various metrics related to the product.
        """
        self.product_id = product_id
        self.name = name
        self.metrics = metrics
        self.created_at = datetime.now()

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the measurement product to a dictionary format for easy JSON serialization.

        Returns:
            dict: A dictionary representation of the measurement product.
        """
        return {
            "product_id": self.product_id,
            "name": self.name,
            "metrics": self.metrics,
            "created_at": self.created_at.isoformat()
        }

class ForestryManagementSystem:
    """
    A class to handle integration of measurement products into forestry management software.
    """

    def __init__(self):
        self.products = []

    def add_product(self, product: MeasurementProduct) -> None:
        """
        Adds a new measurement product to the system.

        Args:
            product (MeasurementProduct): The measurement product to add.
        """
        self.products.append(product)

    def export_products(self, file_path: str) -> None:
        """
        Export the list of measurement products to a JSON file.

        Args:
            file_path (str): File path where the JSON file will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump([product.to_dict() for product in self.products], file, indent=4)
            print(f"Products exported successfully to {file_path}")
        except IOError as e:
            print(f"Error writing to file {file_path}: {e}")

    def load_products(self, file_path: str) -> None:
        """
        Load measurement products from a JSON file into the system.

        Args:
            file_path (str): File path from where the JSON file will be read.
        """
        try:
            with open(file_path, 'r') as file:
                products_data = json.load(file)
                for product_data in products_data:
                    product = MeasurementProduct(
                        product_id=product_data['product_id'],
                        name=product_data['name'],
                        metrics=product_data['metrics']
                    )
                    self.add_product(product)
            print(f"Products loaded successfully from {file_path}")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file {file_path}: {e}")

# Example usage
if __name__ == "__main__":
    # Create an instance of the forestry management system
    fms = ForestryManagementSystem()

    # Define a sample measurement product
    sample_product = MeasurementProduct(
        product_id="MP001",
        name="Tree Height Measurement",
        metrics={
            "height": "20m",
            "diameter": "30cm",
            "gps_coordinates": "45.123456, -93.123456"
        }
    )

    # Add the sample product to the system
    fms.add_product(sample_product)

    # Export products to a JSON file
    fms.export_products("measurement_products.json")

    # Load products from a JSON file
    fms.load_products("measurement_products.json")
```
