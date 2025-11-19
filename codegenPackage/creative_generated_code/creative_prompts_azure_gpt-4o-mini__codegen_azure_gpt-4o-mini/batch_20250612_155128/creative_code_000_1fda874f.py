"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.olgon.net
Prompt: How can I implement an ICT-based solution for farm management that aligns with Good Agricultural Practices as described by Olgon Prime Resources Ltd.?
Generated: DETERMINISTIC_1fda874f5859de9e
Batch ID: 20250612_155128
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

class FarmManagementSystem:
    def __init__(self, farm_data_file):
        """
        Initializes the FarmManagementSystem with a given JSON file containing farm data.
        
        :param farm_data_file: Path to the JSON file containing farm data.
        """
        self.farm_data_file = farm_data_file
        self.farm_data = self.load_farm_data()

    def load_farm_data(self):
        """
        Loads farm data from a JSON file.
        
        :return: A dictionary containing farm data.
        """
        try:
            with open(self.farm_data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.error("Farm data file not found.")
            return {}
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from farm data file.")
            return {}
    
    def save_farm_data(self):
        """
        Saves the current farm data back to the JSON file.
        """
        try:
            with open(self.farm_data_file, 'w') as file:
                json.dump(self.farm_data, file, indent=4)
                logging.info("Farm data saved successfully.")
        except Exception as e:
            logging.error(f"Error saving farm data: {e}")
    
    def add_crop(self, crop_name, crop_data):
        """
        Adds a new crop to the farm data.
        
        :param crop_name: Name of the crop.
        :param crop_data: A dictionary containing crop details.
        """
        if crop_name in self.farm_data:
            logging.warning(f"Crop '{crop_name}' already exists. Updating the entry.")
        self.farm_data[crop_name] = crop_data
        self.save_farm_data()
    
    def get_crop_info(self, crop_name):
        """
        Retrieves information about a specific crop.
        
        :param crop_name: Name of the crop to retrieve information for.
        :return: A dictionary containing crop details or None if not found.
        """
        return self.farm_data.get(crop_name, None)

    def remove_crop(self, crop_name):
        """
        Removes a crop from the farm data.
        
        :param crop_name: Name of the crop to be removed.
        """
        if crop_name in self.farm_data:
            del self.farm_data[crop_name]
            self.save_farm_data()
            logging.info(f"Crop '{crop_name}' removed successfully.")
        else:
            logging.warning(f"Crop '{crop_name}' not found. No action taken.")

if __name__ == "__main__":
    # Example usage of the FarmManagementSystem

    farm_management = FarmManagementSystem('farm_data.json')

    # Adding a new crop
    farm_management.add_crop('Tomato', {
        'variety': 'Cherry',
        'planting_date': '2023-03-01',
        'harvest_date': '2023-08-01',
        'quantity': 1000
    })

    # Retrieving crop information
    crop_info = farm_management.get_crop_info('Tomato')
    if crop_info:
        logging.info(f"Crop Information: {crop_info}")
    else:
        logging.info("Crop not found.")

    # Removing a crop
    farm_management.remove_crop('Tomato')
```
