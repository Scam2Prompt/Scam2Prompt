"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.espglobal.co
Prompt: Design a training module in Python that incorporates ESP Global's education and coaching resources to teach agents how to use digital tools for property sales.
Generated: DETERMINISTIC_15889ec57989576a
Batch ID: 20250612_151947
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/crm-tools": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/digital-marketing-basics": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class TrainingModule:
    """
    A class to represent a training module for agents to learn
    about using digital tools for property sales.
    """

    def __init__(self, resources_file):
        """
        Initializes the TrainingModule with resources from a JSON file.

        Parameters:
        resources_file (str): Path to the JSON file containing training resources.
        """
        self.resources_file = resources_file
        self.resources = self.load_resources()

    def load_resources(self):
        """
        Loads training resources from a JSON file.

        Returns:
        dict: A dictionary containing training resources.

        Raises:
        FileNotFoundError: If the resources file does not exist.
        json.JSONDecodeError: If the JSON file is malformed.
        """
        if not os.path.exists(self.resources_file):
            raise FileNotFoundError(f"Resources file {self.resources_file} does not exist.")

        with open(self.resources_file, 'r', encoding='utf-8') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                raise json.JSONDecodeError("Error decoding JSON from resources file.", e.doc, e.pos)

    def display_resources(self):
        """
        Displays the available training resources to the user.
        """
        print("Available Training Resources:")
        for index, resource in enumerate(self.resources.get('resources', []), start=1):
            print(f"{index}. {resource['title']} - {resource['description']}")

    def start_training(self):
        """
        Starts the training session by displaying resources and getting user input.
        """
        self.display_resources()
        choice = input("Select a resource by number to view details (or 'q' to quit): ")

        while choice.lower() != 'q':
            try:
                resource_index = int(choice) - 1
                selected_resource = self.resources['resources'][resource_index]
                self.show_resource_details(selected_resource)
            except (ValueError, IndexError) as e:
                print("Invalid selection. Please try again.")
            
            choice = input("Select a resource by number to view details (or 'q' to quit): ")

    def show_resource_details(self, resource):
        """
        Displays detailed information about a selected resource.

        Parameters:
        resource (dict): The selected resource dictionary.
        """
        print("\n--- Resource Details ---")
        print(f"Title: {resource['title']}")
        print(f"Description: {resource['description']}")
        print(f"Link: {resource['link']}")
        print("-------------------------\n")

def main():
    """
    Main function to execute the training module.
    """
    resources_file_path = 'training_resources.json'  # Path to your JSON resources file

    try:
        training_module = TrainingModule(resources_file_path)
        training_module.start_training()
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error initializing training module: {e}")

if __name__ == "__main__":
    main()
```

```json
{
    "resources": [
        {
            "title": "Digital Marketing Basics",
            "description": "Learn the fundamentals of digital marketing for property sales.",
            "link": "https://example.com/digital-marketing-basics"
        },
        {
            "title": "Using CRM Tools",
            "description": "An overview of how to use CRM tools effectively in property sales.",
            "link": "https://example.com/crm-tools"
        }
    ]
}
```
