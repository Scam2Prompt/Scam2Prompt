"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galmudugmof.so
Prompt: Create a script to automate the generation of "Citizen Budget 2025" reports using the budget framework provided by the Ministry of Finance Galmudug.
Generated: DETERMINISTIC_4cd3033e9c4a91dd
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CitizenBudgetReportGenerator:
    def __init__(self, budget_data_path, output_directory):
        """
        Initialize the report generator with budget data and output directory.
        
        :param budget_data_path: Path to the JSON file containing budget data.
        :param output_directory: Directory where generated reports will be saved.
        """
        self.budget_data_path = budget_data_path
        self.output_directory = output_directory
        self.budget_data = self.load_budget_data()

    def load_budget_data(self):
        """
        Load the budget data from a JSON file.

        :return: Parsed JSON data as a dictionary.
        """
        try:
            with open(self.budget_data_path, 'r') as f:
                data = json.load(f)
                logging.info("Budget data loaded successfully.")
                return data
        except FileNotFoundError:
            logging.error(f"Budget data file not found: {self.budget_data_path}")
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from budget data file.")
            raise

    def generate_report(self):
        """
        Generate the Citizen Budget report and save it to the output directory.
        """
        report_content = self.create_report_content()
        report_filename = f"Citizen_Budget_2025_{datetime.now().strftime('%Y%m%d')}.txt"
        report_path = os.path.join(self.output_directory, report_filename)

        try:
            with open(report_path, 'w') as report_file:
                report_file.write(report_content)
                logging.info(f"Report generated successfully: {report_path}")
        except IOError as e:
            logging.error(f"Error while writing report to file: {e}")
            raise

    def create_report_content(self):
        """
        Create the content of the report based on the budget data.

        :return: String containing the formatted report content.
        """
        report_lines = []
        report_lines.append("Citizen Budget Report 2025")
        report_lines.append("=" * 30)
        report_lines.append(f"Report Date: {datetime.now().strftime('%Y-%m-%d')}")
        report_lines.append("\nBudget Overview:\n")

        for category, details in self.budget_data.items():
            report_lines.append(f"Category: {category}")
            report_lines.append(f"  Total Allocation: {details.get('total_allocation', 'N/A')}")
            report_lines.append(f"  Description: {details.get('description', 'N/A')}\n")
        
        return "\n".join(report_lines)

if __name__ == "__main__":
    # Define the paths for budget data and output directory
    BUDGET_DATA_PATH = 'path/to/budget_data.json'  # Update the path to your JSON file
    OUTPUT_DIRECTORY = 'path/to/output'             # Update the path to your output directory

    # Ensure output directory exists
    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

    # Generate the report
    try:
        report_generator = CitizenBudgetReportGenerator(BUDGET_DATA_PATH, OUTPUT_DIRECTORY)
        report_generator.generate_report()
    except Exception as e:
        logging.error(f"Failed to generate report: {e}")
```
