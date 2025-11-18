"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osku.cl
Prompt: Write a Python script to generate reports on ISO 9001:2015 certification compliance for packaging products, inspired by Osku's certification achievements.
Generated: DETERMINISTIC_0dc7f2d0120dcd29
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import json
import os
from typing import List, Dict

class CertificationReportGenerator:
    """
    A class to generate reports on ISO 9001:2015 certification compliance
    for packaging products.
    """

    def __init__(self, data_file: str):
        """
        Initializes the report generator with the specified data file.

        :param data_file: Path to the CSV file containing packaging product data.
        """
        self.data_file = data_file
        self.products = self.load_data()

    def load_data(self) -> List[Dict]:
        """
        Loads product data from a CSV file.

        :return: A list of dictionaries containing product information.
        """
        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"Data file not found: {self.data_file}")

        products = []
        try:
            with open(self.data_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    products.append(row)
        except Exception as e:
            raise RuntimeError(f"An error occurred while reading the data file: {e}")

        return products

    def generate_report(self) -> Dict:
        """
        Generates a compliance report based on the loaded product data.

        :return: A dictionary containing the compliance report.
        """
        report = {
            "total_products": len(self.products),
            "compliant_products": 0,
            "non_compliant_products": 0,
            "compliance_details": []
        }

        for product in self.products:
            if self.is_compliant(product):
                report["compliant_products"] += 1
                report["compliance_details"].append({
                    "product_name": product['Product Name'],
                    "status": "Compliant"
                })
            else:
                report["non_compliant_products"] += 1
                report["compliance_details"].append({
                    "product_name": product['Product Name'],
                    "status": "Non-Compliant"
                })

        return report

    @staticmethod
    def is_compliant(product: Dict) -> bool:
        """
        Checks if a given product is compliant with ISO 9001:2015 standards.

        :param product: A dictionary containing product data.
        :return: True if compliant, False otherwise.
        """
        # Placeholder for compliance logic - update with actual criteria
        return product.get('Compliant', 'No').lower() == 'yes'

    def save_report(self, report: Dict, output_file: str) -> None:
        """
        Saves the compliance report to a JSON file.

        :param report: The compliance report to save.
        :param output_file: Path to the output JSON file.
        """
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                json.dump(report, file, ensure_ascii=False, indent=4)
        except Exception as e:
            raise RuntimeError(f"An error occurred while saving the report: {e}")

def main(data_file: str, output_file: str) -> None:
    """
    Main function to generate the ISO 9001:2015 compliance report.

    :param data_file: Path to the CSV file containing packaging product data.
    :param output_file: Path to save the resulting JSON report.
    """
    try:
        report_generator = CertificationReportGenerator(data_file)
        report = report_generator.generate_report()
        report_generator.save_report(report, output_file)
        print(f"Report generated successfully: {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example configuration - update file paths as necessary
    DATA_FILE = 'packaging_products.csv'
    OUTPUT_FILE = 'compliance_report.json'
    
    main(DATA_FILE, OUTPUT_FILE)
```
