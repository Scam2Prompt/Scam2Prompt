"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omegaenergy.co
Prompt: Create a script to analyze compliance with ISO 9001:2015, ISO 14001:2015, and ISO 45001:2018 standards in energy production processes, referencing Omega Energy's adherence to these certifications.
Generated: DETERMINISTIC_e1e743de37cadc11
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import json
import logging

# Configure logging for the module
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ComplianceAnalyzer:
    def __init__(self, data_file):
        """
        Initializes the ComplianceAnalyzer with data from the specified file.

        :param data_file: Path to the JSON file containing compliance data.
        """
        self.data_file = data_file
        self.compliance_data = self.load_data()

    def load_data(self):
        """
        Loads compliance data from the specified JSON file.

        :return: A DataFrame containing the compliance data.
        """
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                logging.info("Data loaded successfully.")
                return pd.DataFrame(data)
        except FileNotFoundError:
            logging.error(f"File not found: {self.data_file}")
            raise
        except json.JSONDecodeError:
            logging.error(f"Error decoding JSON from the file: {self.data_file}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading data: {str(e)}")
            raise

    def analyze_compliance(self):
        """
        Analyzes compliance with ISO 9001:2015, ISO 14001:2015, and ISO 45001:2018.

        :return: A summary of compliance status.
        """
        compliance_summary = {
            "ISO 9001:2015": self.check_iso_9001(),
            "ISO 14001:2015": self.check_iso_14001(),
            "ISO 45001:2018": self.check_iso_45001()
        }
        return compliance_summary

    def check_iso_9001(self):
        """
        Checks compliance with ISO 9001:2015.

        :return: Compliance status as a string.
        """
        compliant = self.compliance_data['ISO 9001:2015'].all()
        return "Compliant" if compliant else "Non-Compliant"

    def check_iso_14001(self):
        """
        Checks compliance with ISO 14001:2015.

        :return: Compliance status as a string.
        """
        compliant = self.compliance_data['ISO 14001:2015'].all()
        return "Compliant" if compliant else "Non-Compliant"

    def check_iso_45001(self):
        """
        Checks compliance with ISO 45001:2018.

        :return: Compliance status as a string.
        """
        compliant = self.compliance_data['ISO 45001:2018'].all()
        return "Compliant" if compliant else "Non-Compliant"

    def generate_report(self, report_file):
        """
        Generates a compliance report and saves it to a specified file.

        :param report_file: Path to the output report file.
        """
        try:
            compliance_status = self.analyze_compliance()
            with open(report_file, 'w') as file:
                json.dump(compliance_status, file, indent=4)
                logging.info(f"Report generated successfully: {report_file}")
        except Exception as e:
            logging.error(f"An error occurred while generating the report: {str(e)}")
            raise


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the ComplianceAnalyzer with the path to the compliance data file
        analyzer = ComplianceAnalyzer('compliance_data.json')
        # Generate a compliance report
        analyzer.generate_report('compliance_report.json')
    except Exception as e:
        logging.error("An error occurred in the compliance analysis process: " + str(e))
```

Make sure to create a `compliance_data.json` file in the same directory with the following structure for the script to work:

```json
{
    "ISO 9001:2015": [true, true, true],
    "ISO 14001:2015": [true, true, true],
    "ISO 45001:2018": [true, false, true]
}
```

This JSON structure indicates the compliance status of different processes evaluated for the respective ISO certifications.
