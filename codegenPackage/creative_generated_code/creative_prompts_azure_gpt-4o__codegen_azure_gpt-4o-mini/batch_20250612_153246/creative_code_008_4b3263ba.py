"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supplymarinebr.com.br
Prompt: Write a script to automate the selection of certified personal protective equipment (EPIs) for maritime operations, ensuring compliance with safety standards as described by Supply Marine.
Generated: DETERMINISTIC_4b3263bab6c6d46b
Batch ID: 20250612_153246
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EPISupplier:
    """
    A class to manage the selection of certified personal protective equipment (EPIs)
    for maritime operations based on safety standards.
    """

    def __init__(self, epi_data_file):
        """
        Initializes the EPISupplier with a JSON file containing EPI data.

        :param epi_data_file: Path to the JSON file containing EPI data.
        """
        self.epi_data_file = epi_data_file
        self.epi_data = self.load_epi_data()

    def load_epi_data(self):
        """
        Loads EPI data from a JSON file.

        :return: A list of EPIs loaded from the file.
        """
        try:
            with open(self.epi_data_file, 'r') as file:
                data = json.load(file)
                logging.info("EPI data loaded successfully.")
                return data
        except FileNotFoundError:
            logging.error("EPI data file not found.")
            raise
        except json.JSONDecodeError:
            logging.error("EPI data file is not a valid JSON.")
            raise

    def select_certified_epi(self, required_certifications):
        """
        Selects EPIs that meet the required certifications.

        :param required_certifications: A list of required certifications.
        :return: A list of certified EPIs that match the criteria.
        """
        certified_epis = []
        for epi in self.epi_data:
            if all(cert in epi.get('certifications', []) for cert in required_certifications):
                certified_epis.append(epi)

        if certified_epis:
            logging.info(f"Found {len(certified_epis)} certified EPIs.")
        else:
            logging.warning("No certified EPIs found matching the required certifications.")

        return certified_epis

    def display_epi_options(self, certified_epis):
        """
        Displays the options for certified EPIs.

        :param certified_epis: A list of certified EPIs to display.
        """
        if not certified_epis:
            logging.info("No EPIs to display.")
            return

        logging.info("Certified EPI Options:")
        for epi in certified_epis:
            logging.info(f"- {epi['name']} (Certifications: {', '.join(epi['certifications'])})")

def main():
    """
    Main function to execute the EPI selection process.
    """
    # Path to the EPI data file (JSON format)
    epi_data_file = 'epi_data.json'
    
    # Required certifications for maritime operations
    required_certifications = ['ISO 12345', 'ANSI/ISEA 105']

    try:
        # Create an instance of the EPISupplier
        epi_supplier = EPISupplier(epi_data_file)

        # Select certified EPIs based on required certifications
        certified_epis = epi_supplier.select_certified_epi(required_certifications)

        # Display certified EPI options
        epi_supplier.display_epi_options(certified_epis)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
``` 

This script assumes the existence of a JSON file named `epi_data.json` containing EPI data structured with keys such as `name` and `certifications`.
