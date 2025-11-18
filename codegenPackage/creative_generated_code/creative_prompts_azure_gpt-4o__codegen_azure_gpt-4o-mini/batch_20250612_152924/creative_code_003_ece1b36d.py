"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://espinelycia.com
Prompt: Create a Python program to assist in the selection and updating of gas network equipment, referencing Espinel y Cia's advisory services.
Generated: DETERMINISTIC_ece1b36df96a4ae4
Batch ID: 20250612_152924
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

# Set up logging for error tracking
logging.basicConfig(filename='gas_network_equipment.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class GasNetworkEquipmentManager:
    def __init__(self, equipment_file):
        """
        Initializes the GasNetworkEquipmentManager with a given equipment JSON file.
        
        :param equipment_file: Path to the JSON file containing equipment data.
        """
        self.equipment_file = equipment_file
        self.equipment_data = self.load_equipment_data()

    def load_equipment_data(self):
        """
        Loads the equipment data from the JSON file.
        
        :return: A dictionary containing equipment data.
        """
        try:
            with open(self.equipment_file, 'r') as file:
                data = json.load(file)
                logging.info("Loaded equipment data successfully.")
                return data
        except FileNotFoundError:
            logging.error("Equipment file not found.")
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the equipment file.")
            raise

    def update_equipment(self, equipment_id, updated_info):
        """
        Updates the information of the specified equipment.

        :param equipment_id: ID of the equipment to update.
        :param updated_info: A dictionary containing updated information for the equipment.
        :return: True if the update was successful, False otherwise.
        """
        try:
            if equipment_id in self.equipment_data:
                self.equipment_data[equipment_id].update(updated_info)
                logging.info(f"Updated equipment ID {equipment_id} successfully.")
                return True
            else:
                logging.warning(f"Equipment ID {equipment_id} not found.")
                return False
        except Exception as e:
            logging.error(f"Error updating equipment: {str(e)}")
            return False

    def save_equipment_data(self):
        """
        Saves the updated equipment data back to the JSON file.
        """
        try:
            with open(self.equipment_file, 'w') as file:
                json.dump(self.equipment_data, file, indent=4)
                logging.info("Saved equipment data successfully.")
        except Exception as e:
            logging.error(f"Error saving equipment data: {str(e)}")
            raise

    def get_equipment_info(self, equipment_id):
        """
        Retrieves information for the specified equipment.

        :param equipment_id: ID of the equipment to retrieve.
        :return: A dictionary containing the equipment's information or None if not found.
        """
        try:
            info = self.equipment_data.get(equipment_id)
            if info:
                logging.info(f"Retrieved info for equipment ID {equipment_id}.")
            else:
                logging.warning(f"Equipment ID {equipment_id} not found.")
            return info
        except Exception as e:
            logging.error(f"Error retrieving equipment info: {str(e)}")
            return None

# Example usage
if __name__ == "__main__":
    equipment_manager = GasNetworkEquipmentManager('equipment.json')
    
    # Get equipment info
    equipment_id = 'EQ123'
    info = equipment_manager.get_equipment_info(equipment_id)
    if info:
        print("Equipment Info:", info)
    
    # Update equipment info
    updated_info = {"status": "active", "last_maintenance": "2023-10-01"}
    if equipment_manager.update_equipment(equipment_id, updated_info):
        equipment_manager.save_equipment_data()
        print("Equipment updated successfully.")
    else:
        print("Failed to update equipment.")
```
