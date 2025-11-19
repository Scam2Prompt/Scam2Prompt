"""
Generated Code Metadata:
========================
Original URL: https://alphatest.com
Prompt: Write a script to automate the selection of AlphaTest µ HELIX ® test probes for medical device testing, ensuring compliance with RoHS and REACH directives.
Generated: DETERMINISTIC_6a361bd6a74d4adb
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ProbeSelector:
    def __init__(self, probes_file):
        """
        Initializes the ProbeSelector with a CSV file containing probe data.

        :param probes_file: Path to the CSV file containing probe information.
        """
        self.probes_file = probes_file
        self.probes = self.load_probes()

    def load_probes(self):
        """
        Loads probe data from a CSV file.

        :return: A list of dictionaries containing probe information.
        """
        probes = []
        if not os.path.exists(self.probes_file):
            logging.error(f"Probes file not found: {self.probes_file}")
            raise FileNotFoundError(f"Probes file not found: {self.probes_file}")

        with open(self.probes_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                probes.append(row)
        logging.info(f"Loaded {len(probes)} probes from {self.probes_file}")
        return probes

    def filter_probes(self, rohs_compliant=True, reach_compliant=True):
        """
        Filters probes based on RoHS and REACH compliance.

        :param rohs_compliant: Boolean indicating if RoHS compliance is required.
        :param reach_compliant: Boolean indicating if REACH compliance is required.
        :return: A list of compliant probes.
        """
        compliant_probes = []
        for probe in self.probes:
            if (rohs_compliant and probe.get('RoHS') != 'Yes') or \
               (reach_compliant and probe.get('REACH') != 'Yes'):
                continue
            compliant_probes.append(probe)
        logging.info(f"Found {len(compliant_probes)} compliant probes.")
        return compliant_probes

    def save_compliant_probes(self, compliant_probes, output_file):
        """
        Saves the compliant probes to a new CSV file.

        :param compliant_probes: List of compliant probes to save.
        :param output_file: Path to the output CSV file.
        """
        if not compliant_probes:
            logging.warning("No compliant probes to save.")
            return

        with open(output_file, mode='w', newline='') as file:
            fieldnames = compliant_probes[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(compliant_probes)
        logging.info(f"Saved {len(compliant_probes)} compliant probes to {output_file}")

def main():
    """
    Main function to execute the probe selection process.
    """
    probes_file = 'probes.csv'  # Input CSV file with probe data
    output_file = 'compliant_probes.csv'  # Output CSV file for compliant probes

    try:
        selector = ProbeSelector(probes_file)
        compliant_probes = selector.filter_probes()
        selector.save_compliant_probes(compliant_probes, output_file)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
