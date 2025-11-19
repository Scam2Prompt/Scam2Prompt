"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: Create a script for performing geotechnical expertise and detailed instrument-based inspections of construction sites, as outlined by the Научно-образовательный центр «Геотехника».
Generated: DETERMINISTIC_7cd98937b8c2752a
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GeotechnicalInspection:
    def __init__(self, site_name, inspector_name):
        """
        Initialize the GeotechnicalInspection class.

        :param site_name: Name of the construction site
        :param inspector_name: Name of the inspector performing the inspection
        """
        self.site_name = site_name
        self.inspector_name = inspector_name
        self.inspection_data = []

    def add_inspection_record(self, instrument, measurement, notes):
        """
        Add a record of an inspection measurement.

        :param instrument: Name of the instrument used
        :param measurement: Measurement value
        :param notes: Additional notes regarding the measurement
        """
        record = {
            'instrument': instrument,
            'measurement': measurement,
            'notes': notes,
            'timestamp': datetime.now().isoformat()
        }
        self.inspection_data.append(record)
        logging.info(f"Added inspection record: {record}")

    def save_inspection_report(self, file_path):
        """
        Save the inspection report to a JSON file.

        :param file_path: Path to the file where the report will be saved
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump({
                    'site_name': self.site_name,
                    'inspector_name': self.inspector_name,
                    'inspection_data': self.inspection_data
                }, json_file, indent=4)
            logging.info(f"Inspection report saved to {file_path}")
        except IOError as e:
            logging.error(f"Failed to save inspection report: {e}")

    def load_inspection_report(self, file_path):
        """
        Load an inspection report from a JSON file.

        :param file_path: Path to the file from which the report will be loaded
        """
        try:
            with open(file_path, 'r') as json_file:
                report = json.load(json_file)
                self.site_name = report['site_name']
                self.inspector_name = report['inspector_name']
                self.inspection_data = report['inspection_data']
            logging.info(f"Inspection report loaded from {file_path}")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to load inspection report: {e}")

def main():
    # Example usage of the GeotechnicalInspection class
    site_name = "Construction Site A"
    inspector_name = "John Doe"
    
    inspection = GeotechnicalInspection(site_name, inspector_name)
    
    # Adding inspection records
    inspection.add_inspection_record("Piezometer", 12.5, "Normal water level")
    inspection.add_inspection_record("Inclinometer", 0.2, "Slight inclination detected")
    
    # Saving the inspection report
    report_file_path = os.path.join(os.getcwd(), f"{site_name.replace(' ', '_')}_inspection_report.json")
    inspection.save_inspection_report(report_file_path)

    # Loading the inspection report
    inspection.load_inspection_report(report_file_path)

if __name__ == "__main__":
    main()
```
