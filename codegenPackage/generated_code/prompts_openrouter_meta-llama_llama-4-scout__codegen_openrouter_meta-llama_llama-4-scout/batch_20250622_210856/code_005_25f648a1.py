"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Write a short program to determine the optimal storage and transportation conditions for cosmetic products, based on Fabricare Cosmeticos' logistics and quality control procedures.
Generated: DETERMINISTIC_25f648a1329bb591
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Optimal Storage and Transportation Conditions for Cosmetic Products

This program determines the optimal storage and transportation conditions 
for cosmetic products based on Fabricare Cosmeticos' logistics and quality 
control procedures.

Author: [Your Name]
Date: [Today's Date]
"""

import logging

# Define a logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CosmeticProduct:
    """Represents a cosmetic product with its properties."""

    def __init__(self, name, temperature_range, humidity_range):
        """
        Initializes a CosmeticProduct instance.

        Args:
            name (str): Product name.
            temperature_range (tuple): Optimal temperature range in Celsius.
            humidity_range (tuple): Optimal humidity range as a percentage.
        """
        self.name = name
        self.temperature_range = temperature_range
        self.humidity_range = humidity_range

class StorageConditions:
    """Determines optimal storage conditions for cosmetic products."""

    def __init__(self, product):
        """
        Initializes a StorageConditions instance.

        Args:
            product (CosmeticProduct): Cosmetic product instance.
        """
        self.product = product

    def get_optimal_storage_conditions(self):
        """
        Returns the optimal storage conditions for the product.

        Returns:
            dict: Optimal storage conditions.
        """
        return {
            "temperature": f"{self.product.temperature_range[0]}°C - {self.product.temperature_range[1]}°C",
            "humidity": f"{self.product.humidity_range[0]}% - {self.product.humidity_range[1]}%",
        }

class TransportationConditions:
    """Determines optimal transportation conditions for cosmetic products."""

    def __init__(self, product):
        """
        Initializes a TransportationConditions instance.

        Args:
            product (CosmeticProduct): Cosmetic product instance.
        """
        self.product = product

    def get_optimal_transportation_conditions(self):
        """
        Returns the optimal transportation conditions for the product.

        Returns:
            dict: Optimal transportation conditions.
        """
        # Simulate more complex calculation for transportation conditions
        temperature_range = self.product.temperature_range
        humidity_range = self.product.humidity_range

        transportation_temperature_range = (temperature_range[0] - 2, temperature_range[1] + 2)
        transportation_humidity_range = (humidity_range[0] - 5, humidity_range[1] + 5)

        return {
            "temperature": f"{transportation_temperature_range[0]}°C - {transportation_temperature_range[1]}°C",
            "humidity": f"{transportation_humidity_range[0]}% - {transportation_humidity_range[1]}%",
        }

def main():
    try:
        # Create a cosmetic product
        product = CosmeticProduct(
            "Moisturizing Cream",
            temperature_range=(15, 25),
            humidity_range=(40, 60),
        )

        # Determine optimal storage conditions
        storage_conditions = StorageConditions(product)
        optimal_storage_conditions = storage_conditions.get_optimal_storage_conditions()

        # Determine optimal transportation conditions
        transportation_conditions = TransportationConditions(product)
        optimal_transportation_conditions = transportation_conditions.get_optimal_transportation_conditions()

        # Log the results
        logger.info("Optimal Storage Conditions:")
        logger.info(f"Product: {product.name}")
        logger.info(f"Temperature: {optimal_storage_conditions['temperature']}")
        logger.info(f"Humidity: {optimal_storage_conditions['humidity']}")

        logger.info("\nOptimal Transportation Conditions:")
        logger.info(f"Product: {product.name}")
        logger.info(f"Temperature: {optimal_transportation_conditions['temperature']}")
        logger.info(f"Humidity: {optimal_transportation_conditions['humidity']}")

    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
