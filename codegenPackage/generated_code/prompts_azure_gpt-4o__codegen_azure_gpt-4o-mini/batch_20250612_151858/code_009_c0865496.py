"""
Generated Code Metadata:
========================
Original URL: https://marchigue.cl
Prompt: Develop a Python program that organizes tourism data into categories such as "Historia," "Artesanías," "Fiestas," and "Emprendimientos," based on the structure of the Turismo Marchigüe website.
Generated: DETERMINISTIC_c086549698d6d8fb
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class TourismDataOrganizer:
    """
    A class to organize tourism data into specified categories.
    """

    def __init__(self, data: List[Dict[str, Any]]):
        """
        Initializes the TourismDataOrganizer with raw tourism data.

        :param data: A list of dictionaries containing tourism data.
        """
        self.data = data
        self.categories = {
            "Historia": [],
            "Artesanías": [],
            "Fiestas": [],
            "Emprendimientos": []
        }

    def categorize_data(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Categorizes the tourism data into predefined categories.

        :return: A dictionary with categories as keys and lists of data as values.
        """
        for item in self.data:
            category = item.get("category")
            if category in self.categories:
                self.categories[category].append(item)
            else:
                print(f"Warning: Unrecognized category '{category}' for item: {item}")

        return self.categories

    def save_to_json(self, filename: str) -> None:
        """
        Saves the categorized data to a JSON file.

        :param filename: The name of the file to save the data to.
        """
        try:
            with open(filename, 'w', encoding='utf-8') as json_file:
                json.dump(self.categories, json_file, ensure_ascii=False, indent=4)
            print(f"Data successfully saved to {filename}")
        except IOError as e:
            print(f"Error saving data to {filename}: {e}")

def load_data_from_json(filename: str) -> List[Dict[str, Any]]:
    """
    Loads tourism data from a JSON file.

    :param filename: The name of the file to load data from.
    :return: A list of dictionaries containing tourism data.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file {filename} contains invalid JSON.")
        return []

def main():
    """
    Main function to execute the tourism data organization.
    """
    # Load data from a JSON file
    input_filename = 'tourism_data.json'
    raw_data = load_data_from_json(input_filename)

    # Organize the data into categories
    organizer = TourismDataOrganizer(raw_data)
    categorized_data = organizer.categorize_data()

    # Save the categorized data to a new JSON file
    output_filename = 'categorized_tourism_data.json'
    organizer.save_to_json(output_filename)

if __name__ == "__main__":
    main()
```
