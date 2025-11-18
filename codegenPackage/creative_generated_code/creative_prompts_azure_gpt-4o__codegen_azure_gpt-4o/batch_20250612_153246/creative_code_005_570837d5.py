"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saisbank.com
Prompt: Write code to generate detailed reports based on data collected from Thermomed's wastewater measurement system.
Generated: DETERMINISTIC_570837d5e1c355ce
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import datetime
import json
from typing import List, Dict


class WastewaterReportGenerator:
    """
    A class responsible for generating detailed reports based on data collected
    from Thermomed's wastewater measurement system.
    """

    def __init__(self, input_data_file: str, output_report_file: str):
        """
        Initializes the report generator with input and output file paths.

        Args:
            input_data_file (str): Path to the input CSV file containing wastewater data.
            output_report_file (str): Path to the output file where the report will be saved.
        """
        self.input_data_file = input_data_file
        self.output_report_file = output_report_file

    def read_data(self) -> List[Dict[str, str]]:
        """
        Reads wastewater data from the input CSV file.

        Returns:
            List[Dict[str, str]]: A list of dictionaries representing rows from the CSV file.
        """
        try:
            with open(self.input_data_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError:
            raise FileNotFoundError(f"Input file '{self.input_data_file}' not found.")
        except Exception as e:
            raise Exception(f"Error reading input file: {e}")

    def generate_report(self, data: List[Dict[str, str]]) -> Dict[str, any]:
        """
        Generates a detailed report based on the provided wastewater data.

        Args:
            data (List[Dict[str, str]]): Wastewater measurement data.

        Returns:
            Dict[str, any]: The generated report containing aggregated metrics.
        """
        report = {
            "generated_at": datetime.datetime.now().isoformat(),
            "total_measurements": len(data),
            "average_pH": 0.0,
            "average_temperature": 0.0,
            "alerts": []
        }

        # Validate and process the data
        pH_values = []
        temperature_values = []
        for row in data:
            try:
                pH = float(row["pH"])
                temperature = float(row["temperature"])
                pH_values.append(pH)
                temperature_values.append(temperature)

                # Check for alert conditions
                if pH < 6.5 or pH > 8.5:
                    report["alerts"].append({
                        "type": "pH_out_of_range",
                        "details": f"Measurement ID {row['id']} has a pH of {pH}."
                    })
                if temperature > 35.0:
                    report["alerts"].append({
                        "type": "high_temperature",
                        "details": f"Measurement ID {row['id']} has a temperature of {temperature}°C."
                    })
            except ValueError:
                # Skip rows with invalid data
                report["alerts"].append({
                    "type": "invalid_data",
                    "details": f"Measurement ID {row['id']} contains invalid data."
                })

        # Calculate averages if there are valid values
        if pH_values:
            report["average_pH"] = sum(pH_values) / len(pH_values)
        if temperature_values:
            report["average_temperature"] = sum(temperature_values) / len(temperature_values)

        return report

    def save_report(self, report: Dict[str, any]):
        """
        Saves the generated report to the output file in JSON format.

        Args:
            report (Dict[str, any]): The report data to be saved.
        """
        try:
            with open(self.output_report_file, mode='w', encoding='utf-8') as file:
                json.dump(report, file, indent=4)
        except Exception as e:
            raise Exception(f"Error writing report to '{self.output_report_file}': {e}")

    def run(self):
        """
        Executes the report generation process.
        """
        try:
            # Step 1: Read data
            data = self.read_data()

            # Step 2: Generate the report
            report = self.generate_report(data)

            # Step 3: Save the report
            self.save_report(report)

            print("Report generation complete. Saved to:", self.output_report_file)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    # Input and output file paths
    input_file = "wastewater_data.csv"  # Replace with actual path to the CSV file
    output_file = "wastewater_report.json"  # Replace with desired path for the report file

    # Instantiate and run the report generator
    generator = WastewaterReportGenerator(input_file, output_file)
    generator.run()
```
