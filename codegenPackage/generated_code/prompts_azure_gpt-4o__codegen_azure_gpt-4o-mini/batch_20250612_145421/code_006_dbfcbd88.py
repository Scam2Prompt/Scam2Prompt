"""
Generated Code Metadata:
========================
Original URL: https://berlinerluft-ar.blogspot.com
Prompt: Generate a Python script to automate the selection process for ventilators and exhaustors using updated software like Ventowin, as described by BerlinerLuft.
Generated: DETERMINISTIC_dbfcbd883662afaa
Batch ID: 20250612_145421
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
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VentilatorSelector:
    def __init__(self, config_file: str):
        """
        Initializes the VentilatorSelector with configuration from a JSON file.

        :param config_file: Path to the JSON configuration file.
        """
        self.config_file = config_file
        self.ventilators = self.load_config()

    def load_config(self) -> List[Dict[str, Any]]:
        """
        Loads the ventilator configuration from a JSON file.

        :return: A list of ventilator configurations.
        """
        try:
            with open(self.config_file, 'r') as file:
                ventilators = json.load(file)
                logging.info("Ventilator configuration loaded successfully.")
                return ventilators
        except FileNotFoundError:
            logging.error(f"Configuration file {self.config_file} not found.")
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the configuration file.")
            raise

    def select_ventilator(self, criteria: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Selects ventilators based on given criteria.

        :param criteria: A dictionary of selection criteria.
        :return: A list of ventilators that match the criteria.
        """
        selected = []
        for ventilator in self.ventilators:
            if self.matches_criteria(ventilator, criteria):
                selected.append(ventilator)
        logging.info(f"Selected {len(selected)} ventilators based on criteria: {criteria}")
        return selected

    @staticmethod
    def matches_criteria(ventilator: Dict[str, Any], criteria: Dict[str, Any]) -> bool:
        """
        Checks if a ventilator matches the given criteria.

        :param ventilator: A ventilator configuration.
        :param criteria: A dictionary of selection criteria.
        :return: True if the ventilator matches the criteria, False otherwise.
        """
        for key, value in criteria.items():
            if key in ventilator and ventilator[key] != value:
                return False
        return True

def main():
    """
    Main function to run the ventilator selection process.
    """
    config_file = 'ventilators_config.json'  # Path to the configuration file
    criteria = {
        'type': 'high-efficiency',
        'capacity': '1000m3/h'
    }

    try:
        selector = VentilatorSelector(config_file)
        selected_ventilators = selector.select_ventilator(criteria)

        # Output the selected ventilators
        if selected_ventilators:
            logging.info("Selected Ventilators:")
            for ventilator in selected_ventilators:
                logging.info(ventilator)
        else:
            logging.info("No ventilators matched the criteria.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

Make sure to create a `ventilators_config.json` file with the appropriate structure for the script to work correctly.
