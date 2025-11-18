"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marchigue.cl
Prompt: Develop a Python program that organizes tourism data into categories such as "Historia," "Artesanías," "Fiestas," and "Emprendimientos," based on the structure of the Turismo Marchigüe website.
Generated: DETERMINISTIC_c086549698d6d8fb
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

# Define a class to organize tourism data
class TourismOrganizer:
    def __init__(self):
        """Initialize the TourismOrganizer with an empty data structure."""
        self.data = {
            "Historia": [],
            "Artesanías": [],
            "Fiestas": [],
            "Emprendimientos": []
        }

    def add_entry(self, category: str, entry: Dict[str, Any]) -> None:
        """
        Add a tourism entry to the specified category.

        Args:
            category (str): The category to which the entry belongs.
            entry (Dict[str, Any]): The tourism entry containing relevant information.

        Raises:
            ValueError: If the category is not recognized.
        """
        if category not in self.data:
            raise ValueError(f"Category '{category}' is not recognized. Use one of {list(self.data.keys())}.")

        self.data[category].append(entry)

    def load_data(self, json_file: str) -> None:
        """
        Load tourism data from a JSON file.

        Args:
            json_file (str): The path to the JSON file containing tourism data.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(json_file, 'r') as file:
                loaded_data = json.load(file)

            for category, entries in loaded_data.items():
                if category in self.data:
                    self.data[category].extend(entries)
                else:
                    raise ValueError(f"Category '{category}' in file is not recognized.")
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{json_file}' was not found.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"The file '{json_file}' contains invalid JSON.")

    def save_data(self, json_file: str) -> None:
        """
        Save the organized tourism data to a JSON file.

        Args:
            json_file (str): The path to save the organized tourism data.

        Raises:
            IOError: If the file cannot be written to.
        """
        try:
            with open(json_file, 'w') as file:
                json.dump(self.data, file, indent=4)
        except IOError:
            raise IOError(f"Could not write to the file '{json_file}'.")

    def get_data(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Get the organized tourism data.

        Returns:
            Dict[str, List[Dict[str, Any]]]: The organized tourism data.
        """
        return self.data

# Example usage of the TourismOrganizer
if __name__ == "__main__":
    organizer = TourismOrganizer()
    
    # Load existing tourism data from a JSON file
    try:
        organizer.load_data("tourism_data.json")
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"Error loading data: {e}")

    # Example of adding an entry
    try:
        new_entry = {
            "name": "Fiesta de la Vendimia",
            "description": "Celebration of grape harvest.",
            "date": "March"
        }
        organizer.add_entry("Fiestas", new_entry)
    except ValueError as e:
        print(f"Error adding entry: {e}")

    # Save the organized data back to a new JSON file
    try:
        organizer.save_data("organized_tourism_data.json")
    except IOError as e:
        print(f"Error saving data: {e}")

    # Retrieve and print organized data
    organized_data = organizer.get_data()
    print(json.dumps(organized_data, indent=4, ensure_ascii=False))
```
