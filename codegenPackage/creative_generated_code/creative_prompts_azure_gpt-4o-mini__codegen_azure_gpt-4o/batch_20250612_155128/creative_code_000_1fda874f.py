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

Below is a clean, production-ready Python implementation of an ICT-based solution for farm management aligned with Good Agricultural Practices:

```python
import json
import datetime

# Constants for Good Agricultural Practices (GAP)
GAP_RULES = {
    "soil_management": "Maintain soil quality through proper crop rotation and organic matter.",
    "water_management": "Optimize water usage with irrigation systems and avoid water wastage.",
    "crop_health": "Use integrated pest management (IPM) and minimize chemical pesticides.",
    "record_keeping": "Maintain detailed records of farm activities for traceability.",
    "worker_safety": "Ensure safety and proper training for all farm workers."
}

class FarmManagementSystem:
    """
    A class to manage farm activities and ensure adherence to Good Agricultural Practices (GAP).
    """

    def __init__(self):
        """
        Initializes the farm management system.
        """
        self.activities = []  # List to store farm activities
        self.inventory = {}   # Dictionary to track inventory of resources
    
    def add_activity(self, activity_name, description, date=None):
        """
        Add a new farm activity to the system.
        
        Parameters:
            activity_name (str): Name of the activity.
            description (str): Description of the activity.
            date (str): Optional date of the activity (YYYY-MM-DD).
        """
        try:
            if not date:
                date = datetime.datetime.now().strftime('%Y-%m-%d')
            activity = {
                "name": activity_name,
                "description": description,
                "date": date
            }
            self.activities.append(activity)
            print(f"Activity '{activity_name}' added successfully.")
        except Exception as e:
            print(f"Error adding activity: {str(e)}")
    
    def view_activities(self):
        """
        View all recorded farm activities.
        """
        if not self.activities:
            print("No activities recorded yet.")
            return
        print("Farm Activities:")
        for activity in self.activities:
            print(f"- {activity['date']}: {activity['name']} - {activity['description']}")
    
    def update_inventory(self, item, quantity):
        """
        Update the inventory with a new item or modify quantity of an existing item.
        
        Parameters:
            item (str): Name of the inventory item.
            quantity (int): Quantity of the item to add or subtract.
        """
        try:
            if item in self.inventory:
                self.inventory[item] += quantity
            else:
                self.inventory[item] = quantity
            if self.inventory[item] < 0:
                raise ValueError("Quantity cannot be negative.")
            print(f"Inventory updated: {item} - {self.inventory[item]}")
        except Exception as e:
            print(f"Error updating inventory: {str(e)}")
    
    def view_inventory(self):
        """
        View the current inventory of resources.
        """
        if not self.inventory:
            print("No inventory items recorded yet.")
            return
        print("Farm Inventory:")
        for item, quantity in self.inventory.items():
            print(f"- {item}: {quantity}")
    
    def save_data_to_file(self, filename="farm_data.json"):
        """
        Save farm activities and inventory data to a JSON file.
        
        Parameters:
            filename (str): Name of the file to save data to. Default is 'farm_data.json'.
        """
        try:
            farm_data = {
                "activities": self.activities,
                "inventory": self.inventory
            }
            with open(filename, 'w') as file:
                json.dump(farm_data, file, indent=4)
            print(f"Farm data saved to '{filename}'.")
        except Exception as e:
            print(f"Error saving data: {str(e)}")
    
    def load_data_from_file(self, filename="farm_data.json"):
        """
        Load farm activities and inventory data from a JSON file.
        
        Parameters:
            filename (str): Name of the file to load data from. Default is 'farm_data.json'.
        """
        try:
            with open(filename, 'r') as file:
                farm_data = json.load(file)
                self.activities = farm_data.get("activities", [])
                self.inventory = farm_data.get("inventory", {})
            print(f"Farm data loaded from '{filename}'.")
        except FileNotFoundError:
            print(f"No data file found with name '{filename}'.")
        except Exception as e:
            print(f"Error loading data: {str(e)}")
    
    def display_gap_rules(self):
        """
        Display Good Agricultural Practices (GAP) rules.
        """
        print("Good Agricultural Practices (GAP) Rules:")
        for rule, description in GAP_RULES.items():
            print(f"- {rule}: {description}")

# Example Usage
if __name__ == "__main__":
    farm_system = FarmManagementSystem()
    
    # Display GAP rules
    farm_system.display_gap_rules()
    
    # Add activities
    farm_system.add_activity("Planting", "Planted tomatoes in field #1.")
    farm_system.add_activity("Irrigation", "Installed drip irrigation system.")

    # View activities
    farm_system.view_activities()
    
    # Update inventory
    farm_system.update_inventory("Fertilizer", 100)
    farm_system.update_inventory("Seeds", 50)
    
    # View inventory
    farm_system.view_inventory()
    
    # Save data to file
    farm_system.save_data_to_file()
    
    # Load data from file
    farm_system.load_data_from_file()
```

This Python script adheres to best practices, includes comprehensive error handling, and is designed to manage farm activities and inventory, while emphasizing adherence to Good Agricultural Practices.
