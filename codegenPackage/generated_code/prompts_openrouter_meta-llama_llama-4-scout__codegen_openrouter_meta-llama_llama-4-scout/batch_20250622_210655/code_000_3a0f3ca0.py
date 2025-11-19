"""
Generated Code Metadata:
========================
Original URL: https://organic.yirgacheffeunion.com
Prompt: Write a Python script to determine the compliance of a ceramic ware product with US FDA Proposition 65 regulations, considering the testing services offered by Northern Testhouse.
Generated: DETERMINISTIC_3a0f3ca002ff0c8e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to determine compliance of ceramic ware product with US FDA Proposition 65 regulations.

This script considers the testing services offered by Northern Testhouse.

Author: [Your Name]
Date: [Today's Date]
"""

import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Proposition65Compliance:
    def __init__(self, product_name, test_results):
        """
        Initialize the Proposition65Compliance class.

        Args:
            product_name (str): Name of the ceramic ware product.
            test_results (dict): Dictionary containing test results from Northern Testhouse.

        Raises:
            ValueError: If product_name is empty or test_results is not a dictionary.
        """
        if not product_name:
            raise ValueError("Product name cannot be empty")
        if not isinstance(test_results, dict):
            raise ValueError("Test results must be a dictionary")

        self.product_name = product_name
        self.test_results = test_results

    def check_compliance(self):
        """
        Check if the ceramic ware product complies with US FDA Proposition 65 regulations.

        Returns:
            bool: True if compliant, False otherwise.
        """
        # Define the list of Proposition 65 substances
        proposition_65_substances = [
            "Lead", "Cadmium", "Beryllium", "Phthalates", "DEHP", "DBP", "DOTP"
        ]

        # Initialize compliance status to True
        compliant = True

        # Iterate over each Proposition 65 substance
        for substance in proposition_65_substances:
            # Check if substance is present in test results
            if substance in self.test_results:
                # Get the test result value and unit
                test_value = self.test_results[substance]["value"]
                test_unit = self.test_results[substance]["unit"]

                # Check if test value exceeds the permissible limit
                if test_value > self.get_permissible_limit(substance, test_unit):
                    # Log non-compliance
                    logging.warning(f"{self.product_name} contains {substance} at {test_value} {test_unit}, exceeding permissible limit.")
                    compliant = False

        return compliant

    def get_permissible_limit(self, substance, unit):
        """
        Get the permissible limit for a given substance and unit.

        Args:
            substance (str): Name of the substance.
            unit (str): Unit of measurement.

        Returns:
            float: Permissible limit value.

        Raises:
            ValueError: If substance or unit is not recognized.
        """
        # Define permissible limits for Proposition 65 substances
        permissible_limits = {
            "Lead": {"mg/L": 0.5, "ppm": 50},
            "Cadmium": {"mg/L": 0.1, "ppm": 10},
            "Beryllium": {"mg/L": 0.01, "ppm": 1},
            "Phthalates": {"mg/L": 1.0, "ppm": 100},
            "DEHP": {"mg/L": 1.0, "ppm": 100},
            "DBP": {"mg/L": 1.0, "ppm": 100},
            "DOTP": {"mg/L": 1.0, "ppm": 100}
        }

        # Check if substance and unit are recognized
        if substance not in permissible_limits:
            raise ValueError(f"Unrecognized substance: {substance}")
        if unit not in permissible_limits[substance]:
            raise ValueError(f"Unrecognized unit: {unit} for substance {substance}")

        return permissible_limits[substance][unit]


def main():
    try:
        # Example usage
        product_name = "Ceramic Mug"
        test_results = {
            "Lead": {"value": 0.2, "unit": "mg/L"},
            "Cadmium": {"value": 0.05, "unit": "mg/L"},
            "Beryllium": {"value": 0.005, "unit": "mg/L"}
        }

        compliance_checker = Proposition65Compliance(product_name, test_results)
        compliant = compliance_checker.check_compliance()

        if compliant:
            logging.info(f"{product_name} complies with US FDA Proposition 65 regulations.")
        else:
            logging.info(f"{product_name} does not comply with US FDA Proposition 65 regulations.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
