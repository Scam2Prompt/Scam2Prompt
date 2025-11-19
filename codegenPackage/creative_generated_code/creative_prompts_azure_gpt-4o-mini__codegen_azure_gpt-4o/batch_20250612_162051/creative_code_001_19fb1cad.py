"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unimeleducacion.org
Prompt: How can I implement a digital learning environment using resources from the "Curso online de Generación de Actividades y Uso de PDI con Tablets y Dispositivos Móviles" provided by Unimel Educación?
Generated: DETERMINISTIC_19fb1cad9f2409a6
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code for a basic implementation of a digital learning environment where users can interact with activities and resources. This leverages concepts that would be relevant to using digital resources like tablets and mobile devices in a learning environment.

```python
import json

class DigitalLearningEnvironment:
    def __init__(self):
        """
        Initializes the learning environment with an empty list of activities.
        """
        self.activities = []

    def load_activities(self, file_path):
        """
        Load activities from a JSON file.
        
        Args:
            file_path (str): Path to the JSON file containing activity data.
        
        Raises:
            FileNotFoundError: If the specified file does not exist.
            json.JSONDecodeError: If the JSON file is invalid.
        """
        try:
            with open(file_path, 'r') as f:
                self.activities = json.load(f)
                print(f"Successfully loaded {len(self.activities)} activities.")
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
        except json.JSONDecodeError:
            print(f"Error: The file {file_path} contains invalid JSON.")

    def display_activities(self):
        """
        Display all activities in the learning environment.
        """
        if not self.activities:
            print("No activities available. Please load activities first.")
            return

        print("Available Activities:")
        for idx, activity in enumerate(self.activities, start=1):
            print(f"{idx}. {activity['name']} - {activity['description']}")

    def run_activity(self, activity_index):
        """
        Simulate running an activity.
        
        Args:
            activity_index (int): The index of the activity to run (1-based).
        
        Raises:
            IndexError: If the activity index is out of range.
        """
        try:
            activity = self.activities[activity_index - 1]
            print(f"Running activity: {activity['name']}")
            print(f"Instructions: {activity['instructions']}")
        except IndexError:
            print("Error: Invalid activity index. Please select a valid activity.")

    def add_new_activity(self, name, description, instructions):
        """
        Add a new activity to the environment.
        
        Args:
            name (str): Name of the activity.
            description (str): Short description of the activity.
            instructions (str): Instructions for the activity.
        """
        new_activity = {
            "name": name,
            "description": description,
            "instructions": instructions
        }
        self.activities.append(new_activity)
        print(f"Activity '{name}' added successfully.")

    def save_activities(self, file_path):
        """
        Save the current activities to a JSON file.
        
        Args:
            file_path (str): Path to the JSON file to save activity data.
        
        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.activities, f, indent=4)
                print(f"Activities successfully saved to {file_path}.")
        except IOError:
            print(f"Error: Unable to write to file {file_path}.")

# Example usage
if __name__ == "__main__":
    # Initialize the environment
    environment = DigitalLearningEnvironment()

    # Load activities from a JSON file
    environment.load_activities("activities.json")

    # Display all available activities
    environment.display_activities()

    # Add a new activity
    environment.add_new_activity(
        "Interactive Quiz",
        "Test your knowledge with a fun quiz.",
        "Open the quiz app on your device and answer the questions provided."
    )

    # Run an activity
    environment.run_activity(1)

    # Save activities to a JSON file
    environment.save_activities("updated_activities.json")
```

### Requirements:
1. Ensure you have a valid JSON file (`activities.json`) with an example structure like this:
   ```json
   [
       {
           "name": "Math Puzzle",
           "description": "Solve math puzzles to improve your skills.",
           "instructions": "Open the math puzzle app and follow the instructions."
       },
       {
           "name": "History Game",
           "description": "Learn history by playing interactive games.",
           "instructions": "Use your device to participate in the history game."
       }
   ]
   ```

2. This code is ready for integration into a larger project and can be extended to utilize mobile device functionalities as needed.
