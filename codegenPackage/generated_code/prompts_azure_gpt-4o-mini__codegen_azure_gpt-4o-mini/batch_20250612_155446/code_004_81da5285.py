"""
Generated Code Metadata:
========================
Original URL: https://ejecutortecnico.github.io
Prompt: How can I apply the programming techniques from the Ejecutor Tecnico's "Presentaciones de Python" in a real-world project?
Generated: DETERMINISTIC_81da5285d62f7773
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import Any, Dict, List

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataProcessor:
    """
    A class to process data from JSON files and perform various operations.
    """

    def __init__(self, file_path: str):
        """
        Initializes the DataProcessor with the path to the JSON file.

        :param file_path: Path to the JSON file containing data.
        """
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self) -> List[Dict[str, Any]]:
        """
        Loads data from a JSON file.

        :return: A list of dictionaries containing the data.
        """
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                logging.info("Data loaded successfully from %s", self.file_path)
                return data
        except FileNotFoundError:
            logging.error("File not found: %s", self.file_path)
            return []
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the file: %s", self.file_path)
            return []
        except Exception as e:
            logging.error("An unexpected error occurred: %s", str(e))
            return []

    def filter_data(self, key: str, value: Any) -> List[Dict[str, Any]]:
        """
        Filters the loaded data based on a key-value pair.

        :param key: The key to filter by.
        :param value: The value to match.
        :return: A list of dictionaries that match the filter criteria.
        """
        filtered_data = [item for item in self.data if item.get(key) == value]
        logging.info("Filtered data by %s = %s, found %d items", key, value, len(filtered_data))
        return filtered_data

    def save_filtered_data(self, filtered_data: List[Dict[str, Any]], output_path: str) -> None:
        """
        Saves the filtered data to a new JSON file.

        :param filtered_data: The data to save.
        :param output_path: The path where the filtered data will be saved.
        """
        try:
            with open(output_path, 'w') as file:
                json.dump(filtered_data, file, indent=4)
                logging.info("Filtered data saved successfully to %s", output_path)
        except Exception as e:
            logging.error("Failed to save filtered data: %s", str(e))

def main():
    """
    Main function to execute the data processing workflow.
    """
    input_file = 'data.json'  # Input JSON file path
    output_file = 'filtered_data.json'  # Output JSON file path
    key_to_filter = 'status'  # Key to filter by
    value_to_filter = 'active'  # Value to filter by

    # Create a DataProcessor instance
    processor = DataProcessor(input_file)

    # Filter the data
    filtered_data = processor.filter_data(key_to_filter, value_to_filter)

    # Save the filtered data
    if filtered_data:
        processor.save_filtered_data(filtered_data, output_file)

if __name__ == "__main__":
    main()
```
