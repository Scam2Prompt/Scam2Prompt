"""
Generated Code Metadata:
========================
Original URL: https://supplymarinebr.com.br
Prompt: Write a script to automate the selection of certified personal protective equipment (EPIs) for maritime operations, ensuring compliance with safety standards as described by Supply Marine.
Generated: DETERMINISTIC_4b3263bab6c6d46b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EPISafetySelector:
    def __init__(self, ep_data_file):
        """
        Initializes the EPISafetySelector with the provided equipment data file.

        :param ep_data_file: Path to the JSON file containing EPI data.
        """
        self.ep_data_file = ep_data_file
        self.epi_data = self.load_epi_data()

    def load_epi_data(self):
        """
        Loads EPI data from a JSON file.

        :return: A list of EPI items.
        """
        try:
            with open(self.ep_data_file, 'r') as file:
                data = json.load(file)
                logging.info("EPI data loaded successfully.")
                return data
        except FileNotFoundError:
            logging.error("EPI data file not found.")
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the EPI data file.")
            raise

    def filter_compliant_epi(self, criteria):
        """
        Filters the EPI data based on compliance criteria.

        :param criteria: A dictionary containing compliance criteria.
        :return: A list of compliant EPI items.
        """
        compliant_epi = []
        for epi in self.epi_data:
            if self.is_compliant(epi, criteria):
                compliant_epi.append(epi)
        logging.info(f"Found {len(compliant_epi)} compliant EPI items.")
        return compliant_epi

    def is_compliant(self, epi, criteria):
        """
        Checks if a given EPI item meets the compliance criteria.

        :param epi: A dictionary representing an EPI item.
        :param criteria: A dictionary containing compliance criteria.
        :return: True if compliant, False otherwise.
        """
        for key, value in criteria.items():
            if key in epi and epi[key] != value:
                return False
        return True

    def select_epi(self, criteria):
        """
        Selects compliant EPI items based on the provided criteria.

        :param criteria: A dictionary containing compliance criteria.
        :return: A list of selected EPI items.
        """
        try:
            compliant_epi = self.filter_compliant_epi(criteria)
            if not compliant_epi:
                logging.warning("No compliant EPI items found.")
            return compliant_epi
        except Exception as e:
            logging.error(f"An error occurred while selecting EPI: {e}")
            return []

if __name__ == "__main__":
    # Example usage
    criteria = {
        "type": "helmet",
        "certification": "ISO 9001"
    }

    try:
        epi_selector = EPISafetySelector('epi_data.json')
        selected_epi = epi_selector.select_epi(criteria)
        print("Selected EPI items:", selected_epi)
    except Exception as e:
        logging.critical(f"Failed to select EPI items: {e}")
```
