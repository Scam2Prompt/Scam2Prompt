"""
Generated Code Metadata:
========================
Original URL: https://deepti.ac.in
Prompt: What is the mission and vision statement of Deepti Convent Higher Secondary School, and how can it be implemented in a school management software?
Generated: DETERMINISTIC_e1d8f0d0eb86ac4c
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
School Management Software - Mission and Vision Implementation

This script defines the mission and vision statement of Deepti Convent Higher Secondary School
and provides functionality to integrate these statements into a school management system.
"""

# Import necessary modules
import json

# Define the mission and vision statements
MISSION_STATEMENT = "To nurture students with quality education, moral values, and holistic development."
VISION_STATEMENT = "To empower students to become responsible citizens and leaders of tomorrow."

# Function to retrieve mission and vision statements
def get_mission_and_vision():
    """
    Retrieves the mission and vision statements of the school.

    Returns:
        dict: A dictionary containing the mission and vision statements.
    """
    return {
        "mission": MISSION_STATEMENT,
        "vision": VISION_STATEMENT
    }

# Function to save mission and vision statements to a file
def save_mission_and_vision_to_file(file_path):
    """
    Saves the mission and vision statements to a JSON file.

    Args:
        file_path (str): The path to the file where the statements will be saved.

    Raises:
        IOError: If there is an issue writing to the file.
    """
    try:
        statements = get_mission_and_vision()
        with open(file_path, 'w') as file:
            json.dump(statements, file, indent=4)
        print(f"Mission and vision statements successfully saved to {file_path}.")
    except IOError as e:
        print(f"Error saving mission and vision statements to file: {e}")

# Function to load mission and vision statements from a file
def load_mission_and_vision_from_file(file_path):
    """
    Loads the mission and vision statements from a JSON file.

    Args:
        file_path (str): The path to the file where the statements are stored.

    Returns:
        dict: A dictionary containing the mission and vision statements.

    Raises:
        IOError: If there is an issue reading the file.
        ValueError: If the file content is not valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            statements = json.load(file)
        print(f"Mission and vision statements successfully loaded from {file_path}.")
        return statements
    except IOError as e:
        print(f"Error loading mission and vision statements from file: {e}")
        return None
    except ValueError as e:
        print(f"Error parsing JSON content from file: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # File path to store mission and vision statements
    file_path = "mission_vision.json"

    # Save mission and vision statements to file
    save_mission_and_vision_to_file(file_path)

    # Load mission and vision statements from file
    statements = load_mission_and_vision_from_file(file_path)
    if statements:
        print("Mission Statement:", statements.get("mission"))
        print("Vision Statement:", statements.get("vision"))
```
