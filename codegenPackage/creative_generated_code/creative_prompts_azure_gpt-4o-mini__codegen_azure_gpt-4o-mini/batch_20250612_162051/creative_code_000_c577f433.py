"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lexuscertifications.com
Prompt: Write a Python script to implement an Environmental Management System (ISO 14001) based on the guidelines provided by Lexus Certifications.
Generated: DETERMINISTIC_c577f433e1a938e4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EnvironmentalManagementSystem:
    def __init__(self, data_file='ems_data.json'):
        """
        Initializes the Environmental Management System with the given data file.

        Args:
            data_file (str): Path to the JSON file storing EMS data. Defaults to 'ems_data.json'.
        """
        self.data_file = data_file
        self.ems_data = self.load_data()

    def load_data(self):
        """
        Loads EMS data from a JSON file.

        Returns:
            dict: The EMS data loaded from the file.
        """
        if not os.path.exists(self.data_file):
            logging.warning("Data file does not exist, initializing empty EMS data.")
            return {}
        
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            logging.error(f"Error loading data file: {e}")
            return {}

    def save_data(self):
        """
        Saves the current EMS data to a JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.ems_data, file, indent=4)
            logging.info("EMS data saved successfully.")
        except IOError as e:
            logging.error(f"Error saving data file: {e}")

    def add_policy(self, policy):
        """
        Adds a new environmental policy to the EMS data.

        Args:
            policy (str): The environmental policy to be added.
        """
        if 'policies' not in self.ems_data:
            self.ems_data['policies'] = []
        self.ems_data['policies'].append(policy)
        logging.info(f"Policy added: {policy}")
        self.save_data()

    def list_policies(self):
        """
        Lists all environmental policies in the EMS data.
        
        Returns:
            list: List of environmental policies.
        """
        return self.ems_data.get('policies', [])

    def set_objectives(self, objectives):
        """
        Sets the environmental objectives for the EMS.

        Args:
            objectives (list): A list of environmental objectives to be set.
        """
        self.ems_data['objectives'] = objectives
        logging.info("Environmental objectives set.")
        self.save_data()

    def get_objectives(self):
        """
        Gets the environmental objectives from the EMS data.
        
        Returns:
            list: List of environmental objectives.
        """
        return self.ems_data.get('objectives', [])

def main():
    """
    Main function to demonstrate the functionality of the Environmental Management System.
    """
    ems = EnvironmentalManagementSystem()

    try:
        # Adding policies
        ems.add_policy("Reduce waste generation by 20% by 2025.")
        ems.add_policy("Implement recycling programs across all departments.")

        # Listing policies
        policies = ems.list_policies()
        logging.info(f"Current Environmental Policies: {policies}")

        # Setting objectives
        ems.set_objectives(["Achieve ISO 14001 certification by 2024", "Reduce carbon footprint by 30% by 2030"])

        # Getting objectives
        objectives = ems.get_objectives()
        logging.info(f"Current Environmental Objectives: {objectives}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
