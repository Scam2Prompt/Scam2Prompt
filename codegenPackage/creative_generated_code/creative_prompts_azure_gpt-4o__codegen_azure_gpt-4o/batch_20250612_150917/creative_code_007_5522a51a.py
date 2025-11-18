"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.specialmetal.ir
Prompt: Write code to generate a report summarizing the inventory of superalloys available at Special Metal Iran, including their chemical composition and industrial applications.
Generated: DETERMINISTIC_5522a51ac7f67541
Batch ID: 20250612_150917
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
from typing import List, Dict, Any


class InventoryReport:
    def __init__(self, inventory_file: str):
        """
        Initialize the InventoryReport class with the inventory file path.
        :param inventory_file: Path to the CSV file containing inventory data
        """
        self.inventory_file = inventory_file

    def load_inventory_data(self) -> List[Dict[str, Any]]:
        """
        Load inventory data from a CSV file.
        :return: List of dictionaries representing the inventory data
        """
        inventory_data = []
        try:
            with open(self.inventory_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    inventory_data.append(row)
        except FileNotFoundError:
            raise FileNotFoundError(f"Inventory file '{self.inventory_file}' not found.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the inventory file: {e}")
        return inventory_data

    def generate_summary(self, inventory_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Generate a summary report of the inventory.
        :param inventory_data: List of dictionaries representing the inventory data
        :return: Dictionary summarizing the inventory
        """
        summary = {
            "total_items": len(inventory_data),
            "alloys": {}
        }

        for item in inventory_data:
            try:
                alloy_name = item.get("Alloy")
                chemical_composition = item.get("Chemical Composition")
                industrial_application = item.get("Industrial Application")

                if not alloy_name:
                    continue

                if alloy_name not in summary["alloys"]:
                    summary["alloys"][alloy_name] = {
                        "chemical_composition": chemical_composition,
                        "industrial_applications": set()
                    }

                if industrial_application:
                    summary["alloys"][alloy_name]["industrial_applications"].add(
                        industrial_application)

            except KeyError as e:
                raise KeyError(f"Missing required field in inventory data: {e}")
            except Exception as e:
                raise Exception(f"An error occurred while processing item: {e}")

        # Convert sets to lists for JSON serialization
        for alloy in summary["alloys"]:
            summary["alloys"][alloy]["industrial_applications"] = list(
                summary["alloys"][alloy]["industrial_applications"])

        return summary

    def save_report(self, summary: Dict[str, Any], output_file: str) -> None:
        """
        Save the summary report to a JSON file.
        :param summary: Dictionary containing the inventory summary
        :param output_file: Path to the output JSON file
        """
        try:
            with open(output_file, mode='w', encoding='utf-8') as file:
                json.dump(summary, file, indent=4)
        except Exception as e:
            raise Exception(f"An error occurred while saving the report: {e}")


# Main execution block
if __name__ == "__main__":
    # Path to the input inventory CSV file
    inventory_csv_path = "inventory.csv"
    # Path to the output summary report JSON file
    output_json_path = "inventory_summary.json"

    try:
        # Initialize the InventoryReport
        report_generator = InventoryReport(inventory_csv_path)

        # Load inventory data from CSV
        inventory_data = report_generator.load_inventory_data()

        # Generate inventory summary
        summary_report = report_generator.generate_summary(inventory_data)

        # Save summary report to JSON
        report_generator.save_report(summary_report, output_json_path)

        print(f"Inventory summary report generated successfully: {output_json_path}")
    except Exception as e:
        print(f"Error: {e}")
```
