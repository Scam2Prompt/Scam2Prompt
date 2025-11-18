"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.espglobal.co
Prompt: Design a training module in Python that incorporates ESP Global's education and coaching resources to teach agents how to use digital tools for property sales.
Generated: DETERMINISTIC_15889ec57989576a
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Training Module for ESP Global Sales Agents on Digital Tools for Property Sales
Author: [Your Name]
Date: [Today's Date]
Description: This Python module provides training functionality using ESP Global's educational resources and coaching system.
"""

import os
import json
import logging

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("training_module.log"), logging.StreamHandler()]
)

class ESPTrainingModule:
    """
    A class that represents the ESP Global training module for agents.
    """

    def __init__(self, resources_file):
        """
        Initializes the training module with resources.

        :param resources_file: Path to the JSON file containing training resources.
        """
        self.resources = {}
        self.resources_file = resources_file
        self.load_resources()

    def load_resources(self):
        """
        Loads educational resources from a JSON file.

        :raises FileNotFoundError: If the resources file does not exist.
        :raises JSONDecodeError: If the resources file contains invalid JSON.
        """
        try:
            if not os.path.exists(self.resources_file):
                raise FileNotFoundError(f"Resources file '{self.resources_file}' not found.")
            
            with open(self.resources_file, 'r') as file:
                self.resources = json.load(file)
                logging.info("Training resources successfully loaded.")
        except FileNotFoundError as e:
            logging.error(e)
            raise
        except json.JSONDecodeError as e:
            logging.error("Invalid JSON format in resources file.")
            raise

    def display_resources(self):
        """
        Displays the list of training resources to the user.
        """
        if not self.resources:
            logging.warning("No resources available to display.")
            print("No resources found. Please check the resources file.")
            return

        print("Training Resources:")
        for category, tools in self.resources.items():
            print(f"Category: {category}")
            for tool in tools:
                print(f"  - {tool}")

    def start_training(self):
        """
        Starts the training process by guiding users through the available resources.
        """
        print("Welcome to the ESP Global Training Module!")
        self.display_resources()

        print("\nPlease select a category to begin training:")
        categories = list(self.resources.keys())
        for idx, category in enumerate(categories, start=1):
            print(f"{idx}. {category}")

        try:
            user_choice = int(input("\nEnter the number corresponding to your choice: "))
            if user_choice < 1 or user_choice > len(categories):
                raise ValueError("Invalid choice. Please select a valid category number.")
            
            selected_category = categories[user_choice - 1]
            print(f"\nYou have selected: {selected_category}")
            print("Training resources available in this category:")
            for tool in self.resources[selected_category]:
                print(f"  - {tool}")

            print("\nBegin training with these tools and follow the instructions provided.")
        except ValueError as e:
            logging.error(e)
            print("Error: Invalid input. Please try again.")

    def add_resource(self, category, tool_name):
        """
        Adds a new resource to the training module.

        :param category: The category of the resource.
        :param tool_name: The name of the tool to add.
        """
        if category not in self.resources:
            self.resources[category] = []
        
        self.resources[category].append(tool_name)
        logging.info(f"Added new resource: '{tool_name}' under category '{category}'.")
        self.save_resources()

    def save_resources(self):
        """
        Saves updated resources back to the JSON file.

        :raises IOError: If there is an error saving the file.
        """
        try:
            with open(self.resources_file, 'w') as file:
                json.dump(self.resources, file, indent=4)
                logging.info("Resources successfully saved.")
        except IOError as e:
            logging.error("Error saving resources file.")
            raise

if __name__ == "__main__":
    # Path to the resources file (update as needed)
    resources_path = "training_resources.json"

    try:
        # Initialize the training module
        training_module = ESPTrainingModule(resources_path)

        # Start the training process
        training_module.start_training()

        # Example of adding a new resource (can be removed/commented in production)
        # training_module.add_resource("Digital Marketing Tools", "Social Media Ads Manager")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print("An error occurred while running the training module. Please check the logs for details.")
```
