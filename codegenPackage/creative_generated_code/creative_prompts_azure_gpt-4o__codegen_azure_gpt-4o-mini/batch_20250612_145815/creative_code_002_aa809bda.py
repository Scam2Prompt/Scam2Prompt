"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reddecomercio.com
Prompt: Generate code to calculate import/export taxes and fees based on fiscal strategies mentioned by Red de Comercio, ensuring compliance with legal regulations.
Generated: DETERMINISTIC_aa809bda731ec5e7
Batch ID: 20250612_145815
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class TaxCalculator:
    """
    A class to calculate import/export taxes and fees based on fiscal strategies.
    """

    def __init__(self, tax_rates_file):
        """
        Initializes the TaxCalculator with tax rates.

        :param tax_rates_file: Path to the JSON file containing tax rates and fees.
        """
        self.tax_rates = self.load_tax_rates(tax_rates_file)

    def load_tax_rates(self, tax_rates_file):
        """
        Loads tax rates from a JSON file.

        :param tax_rates_file: Path to the JSON file containing tax rates.
        :return: Dictionary of tax rates.
        """
        try:
            with open(tax_rates_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("Tax rates file not found.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from the tax rates file.")

    def calculate_import_tax(self, value):
        """
        Calculates the import tax based on the value of the goods.

        :param value: The value of the imported goods.
        :return: Calculated import tax.
        """
        import_tax_rate = self.tax_rates.get("import_tax", 0)
        return value * import_tax_rate

    def calculate_export_tax(self, value):
        """
        Calculates the export tax based on the value of the goods.

        :param value: The value of the exported goods.
        :return: Calculated export tax.
        """
        export_tax_rate = self.tax_rates.get("export_tax", 0)
        return value * export_tax_rate

    def calculate_total_cost(self, value, is_import=True):
        """
        Calculates the total cost including taxes for import or export.

        :param value: The value of the goods.
        :param is_import: Boolean indicating if the transaction is for import or export.
        :return: Total cost including taxes.
        """
        if is_import:
            tax = self.calculate_import_tax(value)
        else:
            tax = self.calculate_export_tax(value)

        total_cost = value + tax
        return total_cost

def main():
    """
    Main function to run the tax calculator.
    """
    try:
        # Initialize the tax calculator with the provided JSON file
        tax_calculator = TaxCalculator('tax_rates.json')

        # Example values for import and export
        import_value = 1000.00  # Example import value
        export_value = 800.00    # Example export value

        # Calculate and display the import tax and total cost
        import_tax = tax_calculator.calculate_import_tax(import_value)
        total_import_cost = tax_calculator.calculate_total_cost(import_value, is_import=True)
        print(f"Import Tax: ${import_tax:.2f}")
        print(f"Total Import Cost: ${total_import_cost:.2f}")

        # Calculate and display the export tax and total cost
        export_tax = tax_calculator.calculate_export_tax(export_value)
        total_export_cost = tax_calculator.calculate_total_cost(export_value, is_import=False)
        print(f"Export Tax: ${export_tax:.2f}")
        print(f"Total Export Cost: ${total_export_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
```
