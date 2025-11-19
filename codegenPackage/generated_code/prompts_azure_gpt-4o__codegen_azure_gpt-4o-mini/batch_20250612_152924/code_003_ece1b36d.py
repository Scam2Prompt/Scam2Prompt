"""
Generated Code Metadata:
========================
Original URL: https://espinelycia.com
Prompt: Create a Python program to assist in the selection and updating of gas network equipment, referencing Espinel y Cia's advisory services.
Generated: DETERMINISTIC_ece1b36df96a4ae4
Batch ID: 20250612_152924
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

class GasNetworkEquipment:
    """
    A class to represent gas network equipment and manage its selection and updates.
    """

    def __init__(self, equipment_data_file):
        """
        Initializes the GasNetworkEquipment with data from a JSON file.

        :param equipment_data_file: Path to the JSON file containing equipment data.
        """
        self.equipment_data_file = equipment_data_file
        self.equipment_data = self.load_equipment_data()

    def load_equipment_data(self):
        """
        Loads equipment data from a JSON file.

        :return: A dictionary containing equipment data.
        """
        try:
            with open(self.equipment_data_file, 'r') as file:
                data = json.load(file)
                logging.info("Equipment data loaded successfully.")
                return data
        except FileNotFoundError:
            logging.error("The equipment data file was not found.")
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the equipment data file.")
            raise

    def select_equipment(self, criteria):
        """
        Selects equipment based on given criteria.

        :param criteria: A dictionary containing selection criteria.
        :return: A list of equipment that matches the criteria.
        """
        selected_equipment = []
        for equipment in self.equipment_data.get('equipment', []):
            if all(equipment.get(key) == value for key, value in criteria.items()):
                selected_equipment.append(equipment)
        logging.info(f"Selected {len(selected_equipment)} equipment(s) based on criteria: {criteria}.")
        return selected_equipment

    def update_equipment(self, equipment_id, updates):
        """
        Updates the equipment details based on the provided updates.

        :param equipment_id: The ID of the equipment to update.
        :param updates: A dictionary containing the updates to apply.
        :return: A boolean indicating success or failure of the update.
        """
        for equipment in self.equipment_data.get('equipment', []):
            if equipment['id'] == equipment_id:
                equipment.update(updates)
                logging.info(f"Equipment with ID {equipment_id} updated successfully.")
                return True
        logging.warning(f"Equipment with ID {equipment_id} not found for update.")
        return False

    def save_equipment_data(self):
        """
        Saves the current equipment data back to the JSON file.
        """
        try:
            with open(self.equipment_data_file, 'w') as file:
                json.dump(self.equipment_data, file, indent=4)
                logging.info("Equipment data saved successfully.")
        except IOError:
            logging.error("Error saving equipment data to the file.")
            raise

def main():
    """
    Main function to demonstrate the GasNetworkEquipment class functionality.
    """
    equipment_file = 'equipment_data.json'  # Path to the equipment data file
    gas_network = GasNetworkEquipment(equipment_file)

    # Example criteria for selecting equipment
    selection_criteria = {
        'type': 'valve',
        'status': 'active'
    }
    
    # Select equipment based on criteria
    selected = gas_network.select_equipment(selection_criteria)
    print("Selected Equipment:", selected)

    # Example update for a specific equipment
    equipment_id_to_update = 1
    updates = {
        'status': 'inactive'
    }
    
    if gas_network.update_equipment(equipment_id_to_update, updates):
        gas_network.save_equipment_data()

if __name__ == "__main__":
    main()
```
