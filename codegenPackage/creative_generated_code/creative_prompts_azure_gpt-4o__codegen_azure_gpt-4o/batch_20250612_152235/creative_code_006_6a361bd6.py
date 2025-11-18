"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphatest.com
Prompt: Write a script to automate the selection of AlphaTest µ HELIX ® test probes for medical device testing, ensuring compliance with RoHS and REACH directives.
Generated: DETERMINISTIC_6a361bd6a74d4adb
Batch ID: 20250612_152235
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

# Define a class to handle the selection of AlphaTest µ HELIX probes
class TestProbeSelector:
    def __init__(self, catalog_file, compliance_file):
        """
        Initializes the selector with the necessary files.
        
        :param catalog_file: Path to the CSV file containing the test probe catalog
        :param compliance_file: Path to the JSON file containing compliance information
        """
        self.catalog_file = catalog_file
        self.compliance_file = compliance_file

    def load_catalog(self):
        """
        Loads the test probe catalog from the CSV file.

        :return: List of dictionaries representing the test probes
        """
        try:
            with open(self.catalog_file, mode='r') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except FileNotFoundError:
            raise FileNotFoundError(f"Catalog file '{self.catalog_file}' not found.")
        except Exception as e:
            raise Exception(f"Error loading catalog file: {str(e)}")

    def load_compliance_data(self):
        """
        Loads compliance data from the JSON file.

        :return: Dictionary containing compliance information
        """
        try:
            with open(self.compliance_file, mode='r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Compliance file '{self.compliance_file}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Compliance file '{self.compliance_file}' contains invalid JSON.")
        except Exception as e:
            raise Exception(f"Error loading compliance file: {str(e)}")

    def filter_probes(self, catalog, compliance_data):
        """
        Filters the probes based on compliance data (RoHS and REACH directives).

        :param catalog: List of test probes from the catalog
        :param compliance_data: Compliance information
        :return: List of compliant test probes
        """
        compliant_probes = []
        rohs_compliant = compliance_data.get("RoHS", [])
        reach_compliant = compliance_data.get("REACH", [])

        for probe in catalog:
            if probe['Model'] in rohs_compliant and probe['Model'] in reach_compliant:
                compliant_probes.append(probe)
        
        return compliant_probes

    def save_filtered_probes(self, probes, output_file):
        """
        Saves the filtered probes to an output CSV file.

        :param probes: List of filtered test probes
        :param output_file: Path to the output CSV file
        """
        try:
            with open(output_file, mode='w', newline='') as file:
                if probes:
                    writer = csv.DictWriter(file, fieldnames=probes[0].keys())
                    writer.writeheader()
                    writer.writerows(probes)
                else:
                    file.write("No compliant probes found.")
        except Exception as e:
            raise Exception(f"Error saving filtered probes: {str(e)}")

    def run(self, output_file):
        """
        Executes the selection process from catalog loading to filtering and saving results.

        :param output_file: Path to the output CSV file
        """
        try:
            catalog = self.load_catalog()
            compliance_data = self.load_compliance_data()
            filtered_probes = self.filter_probes(catalog, compliance_data)
            self.save_filtered_probes(filtered_probes, output_file)
            print(f"Filtered probes saved to '{output_file}'.")
        except Exception as e:
            print(f"Error: {str(e)}")

# Main entry point of the script
if __name__ == "__main__":
    # Input files (replace with actual file paths)
    catalog_file = "probe_catalog.csv"
    compliance_file = "compliance_data.json"
    output_file = "filtered_probes.csv"

    # Ensure input files exist
    if not os.path.exists(catalog_file):
        print(f"Error: Catalog file '{catalog_file}' does not exist.")
    elif not os.path.exists(compliance_file):
        print(f"Error: Compliance file '{compliance_file}' does not exist.")
    else:
        # Execute the selection process
        selector = TestProbeSelector(catalog_file, compliance_file)
        selector.run(output_file)
```
