"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laotaigroup.com
Prompt: Generate a script using Python to automate the procurement process for heavy and light industrial equipment, as described in the services offered by Lao Tai Trading - Investment Group.
Generated: DETERMINISTIC_14d54be0b3104573
Batch ID: 20250612_153224
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
import csv
import os
from datetime import datetime

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("procurement_log.txt"),
        logging.StreamHandler()
    ]
)

class ProcurementAutomation:
    """
    A class to automate the procurement process for heavy and light industrial equipment.
    """

    def __init__(self, inventory_file, request_file, output_file):
        """
        Initialize the procurement automation system.

        :param inventory_file: Path to the inventory CSV file.
        :param request_file: Path to the request JSON file.
        :param output_file: Path to save the procurement summary.
        """
        self.inventory_file = inventory_file
        self.request_file = request_file
        self.output_file = output_file
        self.inventory_data = {}  # Stores inventory as a dictionary

    def load_inventory(self):
        """
        Load inventory data from a CSV file.
        """
        try:
            with open(self.inventory_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    item_id = row['ItemID']
                    self.inventory_data[item_id] = {
                        'Name': row['Name'],
                        'Category': row['Category'],
                        'Quantity': int(row['Quantity']),
                        'UnitPrice': float(row['UnitPrice'])
                    }
            logging.info("Inventory data loaded successfully.")
        except FileNotFoundError:
            logging.error(f"Inventory file '{self.inventory_file}' not found.")
            raise
        except Exception as e:
            logging.error(f"Error loading inventory file: {e}")
            raise

    def process_requests(self):
        """
        Process procurement requests from a JSON file.
        """
        try:
            with open(self.request_file, 'r') as file:
                requests = json.load(file)

            procurement_summary = []
            total_cost = 0

            for req in requests['ProcurementRequests']:
                item_id = req['ItemID']
                requested_quantity = req['Quantity']

                if item_id in self.inventory_data:
                    item = self.inventory_data[item_id]
                    if item['Quantity'] >= requested_quantity:
                        # Process the request
                        item['Quantity'] -= requested_quantity
                        cost = requested_quantity * item['UnitPrice']
                        total_cost += cost

                        procurement_summary.append({
                            'ItemID': item_id,
                            'Name': item['Name'],
                            'Category': item['Category'],
                            'Quantity': requested_quantity,
                            'Cost': cost
                        })
                        logging.info(f"Processed request for ItemID '{item_id}' - {requested_quantity} units.")
                    else:
                        logging.warning(f"Insufficient stock for ItemID '{item_id}'. Requested: {requested_quantity}, Available: {item['Quantity']}")
                else:
                    logging.warning(f"ItemID '{item_id}' not found in inventory.")

            # Save procurement summary to a file
            self.save_procurement_summary(procurement_summary, total_cost)
        except FileNotFoundError:
            logging.error(f"Request file '{self.request_file}' not found.")
            raise
        except json.JSONDecodeError:
            logging.error("Failed to decode the request JSON file.")
            raise
        except Exception as e:
            logging.error(f"Error processing requests: {e}")
            raise

    def save_procurement_summary(self, summary, total_cost):
        """
        Save the procurement summary to a CSV file.

        :param summary: List of dictionaries containing procurement details.
        :param total_cost: Total cost of procurement.
        """
        try:
            with open(self.output_file, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['ItemID', 'Name', 'Category', 'Quantity', 'Cost'])
                writer.writeheader()
                writer.writerows(summary)

                # Append total cost at the end
                file.write(f"Total Cost: {total_cost}\n")

            logging.info(f"Procurement summary saved to '{self.output_file}'.")
        except Exception as e:
            logging.error(f"Error saving procurement summary: {e}")
            raise

def main():
    """
    Main function to run the procurement automation script.
    """
    try:
        inventory_file = 'inventory.csv'   # Path to inventory file
        request_file = 'requests.json'    # Path to procurement request file
        output_file = 'procurement_summary.csv'  # Path to output file

        logging.info("Starting the procurement automation process.")
        procurement = ProcurementAutomation(inventory_file, request_file, output_file)
        procurement.load_inventory()
        procurement.process_requests()
        logging.info("Procurement automation process completed successfully.")
    except Exception as e:
        logging.error(f"Procurement automation process failed: {e}")

if __name__ == '__main__':
    main()
```
