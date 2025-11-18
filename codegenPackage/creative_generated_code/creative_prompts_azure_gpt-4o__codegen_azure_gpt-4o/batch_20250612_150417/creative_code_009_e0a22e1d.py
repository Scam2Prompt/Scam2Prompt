"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pumpx.me
Prompt: Provide code to generate a report summarizing operational data from PumpX's PanelX equipment, formatted for presentation to stakeholders in the construction industry.
Generated: DETERMINISTIC_e0a22e1d283f0bac
Batch ID: 20250612_150417
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
from datetime import datetime
from typing import List, Dict


class PumpXReportGenerator:
    """
    A class to generate and summarize operational data reports from PumpX's PanelX equipment.
    """

    def __init__(self, input_file: str, output_file: str):
        """
        Initialize the report generator with input and output file paths.

        :param input_file: Path to the CSV file containing raw operational data.
        :param output_file: Path to save the generated summary report as a JSON file.
        """
        self.input_file = input_file
        self.output_file = output_file

    def read_data(self) -> List[Dict[str, str]]:
        """
        Reads operational data from a CSV file.

        :return: A list of dictionaries, where each dictionary represents a row of data.
        """
        try:
            with open(self.input_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except Exception as e:
            raise RuntimeError(f"Error reading data from {self.input_file}: {e}")

    def summarize_data(self, data: List[Dict[str, str]]) -> Dict[str, Dict[str, float]]:
        """
        Summarizes operational data, calculating metrics such as total runtime and average efficiency.

        :param data: A list of dictionaries representing the raw data rows.
        :return: A dictionary containing the summarized metrics.
        """
        summary = {}
        total_runtime = 0
        total_efficiency = 0
        entry_count = 0

        for row in data:
            try:
                equipment_id = row['EquipmentID']
                runtime = float(row['RuntimeHours'])
                efficiency = float(row['Efficiency'])

                if equipment_id not in summary:
                    summary[equipment_id] = {
                        "TotalRuntime": 0.0,
                        "AverageEfficiency": 0.0,
                        "EntryCount": 0
                    }

                # Update metrics for this equipment ID
                summary[equipment_id]["TotalRuntime"] += runtime
                summary[equipment_id]["EntryCount"] += 1
                total_runtime += runtime
                total_efficiency += efficiency
                entry_count += 1

            except (KeyError, ValueError) as e:
                print(f"Skipping invalid row: {row} ({e})")

        # Calculate average efficiency for each equipment
        for equipment_id, metrics in summary.items():
            if metrics["EntryCount"] > 0:
                metrics["AverageEfficiency"] = total_efficiency / metrics["EntryCount"]

        # Add global summary metrics
        summary['Global'] = {
            "TotalRuntime": total_runtime,
            "AverageEfficiency": total_efficiency / entry_count if entry_count > 0 else 0.0
        }

        return summary

    def write_summary(self, summary: Dict[str, Dict[str, float]]):
        """
        Writes the summarized data to a JSON file.

        :param summary: The summarized data dictionary.
        """
        try:
            with open(self.output_file, mode='w', encoding='utf-8') as file:
                json.dump(summary, file, indent=4)
        except Exception as e:
            raise RuntimeError(f"Error writing summary to {self.output_file}: {e}")

    def generate_report(self):
        """
        Main method to generate the operational data report.
        """
        print("Reading data...")
        data = self.read_data()

        print("Summarizing data...")
        summary = self.summarize_data(data)

        print("Writing summary to file...")
        self.write_summary(summary)

        print(f"Report successfully generated: {self.output_file}")


if __name__ == "__main__":
    # Example usage: Adjust file paths as necessary
    INPUT_FILE = "pumpx_operational_data.csv"
    OUTPUT_FILE = f"pumpx_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    try:
        report_generator = PumpXReportGenerator(INPUT_FILE, OUTPUT_FILE)
        report_generator.generate_report()
    except RuntimeError as e:
        print(f"Failed to generate report: {e}")
```
