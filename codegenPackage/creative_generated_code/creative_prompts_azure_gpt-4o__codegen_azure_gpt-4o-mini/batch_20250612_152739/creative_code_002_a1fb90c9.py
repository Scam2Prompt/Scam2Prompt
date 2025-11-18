"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synerex-bo.com
Prompt: Recommend libraries or tools compatible with the Synerex platform for handling data stored in directory structures like "lxy" or "Op."
Generated: DETERMINISTIC_a1fb90c956abff97
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from typing import List, Dict

class DirectoryDataHandler:
    """
    A class to handle data stored in directory structures compatible with the Synerex platform.
    """

    def __init__(self, base_directory: str):
        """
        Initializes the DirectoryDataHandler with a base directory.

        :param base_directory: The base directory where data is stored.
        """
        self.base_directory = base_directory
        self.validate_directory()

    def validate_directory(self):
        """ Validates that the base directory exists. """
        if not os.path.isdir(self.base_directory):
            raise ValueError(f"Directory '{self.base_directory}' does not exist.")

    def list_directories(self) -> List[str]:
        """
        Lists all directories in the base directory.

        :return: A list of directory names.
        """
        try:
            return [d for d in os.listdir(self.base_directory) if os.path.isdir(os.path.join(self.base_directory, d))]
        except Exception as e:
            raise RuntimeError(f"Failed to list directories: {str(e)}")

    def read_json_from_directory(self, directory_name: str) -> Dict:
        """
        Reads a JSON file from the specified directory.

        :param directory_name: The name of the directory to read from.
        :return: A dictionary containing the JSON data.
        """
        directory_path = os.path.join(self.base_directory, directory_name)
        json_file_path = os.path.join(directory_path, 'data.json')

        if not os.path.isfile(json_file_path):
            raise FileNotFoundError(f"JSON file 'data.json' not found in '{directory_path}'.")

        try:
            with open(json_file_path, 'r') as json_file:
                return json.load(json_file)
        except json.JSONDecodeError:
            raise ValueError(f"Failed to decode JSON from file '{json_file_path}'.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while reading JSON: {str(e)}")

    def save_json_to_directory(self, directory_name: str, data: Dict) -> None:
        """
        Saves a JSON file to the specified directory.

        :param directory_name: The name of the directory to save to.
        :param data: The dictionary data to save as JSON.
        """
        directory_path = os.path.join(self.base_directory, directory_name)
        os.makedirs(directory_path, exist_ok=True)
        json_file_path = os.path.join(directory_path, 'data.json')

        try:
            with open(json_file_path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        except Exception as e:
            raise RuntimeError(f"Failed to save JSON to '{json_file_path}': {str(e)}")


if __name__ == "__main__":
    # Example usage
    try:
        handler = DirectoryDataHandler("path/to/base/directory")
        directories = handler.list_directories()
        print("Directories:", directories)

        # Read JSON data from a specific directory
        data = handler.read_json_from_directory("example_directory")
        print("Data from JSON:", data)

        # Save new JSON data
        new_data = {"key": "value"}
        handler.save_json_to_directory("example_directory", new_data)
        print("New data saved successfully.")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
