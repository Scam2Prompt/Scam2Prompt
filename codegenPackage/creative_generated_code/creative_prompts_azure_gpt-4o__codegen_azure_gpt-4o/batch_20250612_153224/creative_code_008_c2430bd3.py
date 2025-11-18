"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vidaglobaltrade.com
Prompt: Create a program to consolidate shipments for small distributors, reducing operational costs and streamlining sourcing, as described by VIDA TRADE LLC.
Generated: DETERMINISTIC_c2430bd3aba09d19
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to consolidate shipments for small distributors, reducing operational costs
and streamlining sourcing for VIDA TRADE LLC.

Author: [Your Name]
Date: [Current Date]
"""

import csv
import json
from collections import defaultdict


class ShipmentConsolidator:
    """
    A class to handle shipment consolidation for small distributors.
    """

    def __init__(self, input_file: str, output_file: str):
        """
        Initialize the ShipmentConsolidator.

        Args:
            input_file (str): Path to the input CSV file containing shipment data.
            output_file (str): Path to the output JSON file for consolidated shipments.
        """
        self.input_file = input_file
        self.output_file = output_file
        self.shipments = defaultdict(list)

    def load_shipments(self):
        """
        Load shipments from the input CSV file.

        Raises:
            FileNotFoundError: If the input file does not exist.
            ValueError: If the input file contains invalid data.
        """
        try:
            with open(self.input_file, mode='r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    # Ensure required fields are present
                    if "Distributor" not in row or "Product" not in row or "Quantity" not in row:
                        raise ValueError("Invalid data format in CSV file.")
                    distributor = row["Distributor"]
                    product = row["Product"]
                    quantity = int(row["Quantity"])
                    self.shipments[distributor].append({"Product": product, "Quantity": quantity})
        except FileNotFoundError:
            print(f"Error: File '{self.input_file}' not found.")
            raise
        except ValueError as e:
            print(f"Error: {e}")
            raise

    def consolidate_shipments(self):
        """
        Consolidate shipments by grouping products for each distributor.

        Returns:
            dict: A dictionary containing consolidated shipment data.
        """
        consolidated = {}
        for distributor, items in self.shipments.items():
            consolidated[distributor] = defaultdict(int)
            for item in items:
                consolidated[distributor][item["Product"]] += item["Quantity"]
        return consolidated

    def save_consolidated_shipments(self, consolidated_data: dict):
        """
        Save consolidated shipments to an output JSON file.

        Args:
            consolidated_data (dict): Consolidated shipment data.
        """
        try:
            with open(self.output_file, mode='w', encoding='utf-8') as file:
                json.dump(consolidated_data, file, indent=4)
            print(f"Consolidated shipment data successfully saved to '{self.output_file}'.")
        except IOError:
            print(f"Error: Could not write to file '{self.output_file}'.")
            raise

    def run(self):
        """
        Execute the shipment consolidation process.
        """
        try:
            print("Loading shipments...")
            self.load_shipments()
            print("Consolidating shipments...")
            consolidated_data = self.consolidate_shipments()
            print("Saving consolidated shipments...")
            self.save_consolidated_shipments(consolidated_data)
            print("Shipment consolidation completed successfully.")
        except Exception as e:
            print(f"An error occurred during the process: {e}")


# Main entry point
if __name__ == "__main__":
    # Change these file paths as needed
    INPUT_FILE = "shipment_data.csv"  # Path to input CSV file
    OUTPUT_FILE = "consolidated_shipments.json"  # Path to output JSON file

    consolidator = ShipmentConsolidator(INPUT_FILE, OUTPUT_FILE)
    consolidator.run()
```
