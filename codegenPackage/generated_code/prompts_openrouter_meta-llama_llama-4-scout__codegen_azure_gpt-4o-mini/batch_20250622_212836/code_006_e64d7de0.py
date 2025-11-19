"""
Generated Code Metadata:
========================
Original URL: https://geosatelites.com
Prompt: Suggest a software solution for managing and processing data from various surveying equipment, including STEC and SOKKIA devices, for a geospatial project in Nicaragua.
Generated: DETERMINISTIC_e64d7de049a0b0b9
Batch ID: 20250622_212836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict, Any

class SurveyDataManager:
    """
    A class to manage and process data from various surveying equipment.
    Supports STEC and SOKKIA devices.
    """

    def __init__(self, data_directory: str):
        """
        Initializes the SurveyDataManager with a specified data directory.

        :param data_directory: Path to the directory containing survey data files.
        """
        self.data_directory = data_directory
        self.survey_data = []

    def load_data(self) -> None:
        """
        Loads survey data from JSON files in the specified directory.
        """
        try:
            for filename in os.listdir(self.data_directory):
                if filename.endswith('.json'):
                    file_path = os.path.join(self.data_directory, filename)
                    with open(file_path, 'r') as file:
                        data = json.load(file)
                        self.survey_data.append(data)
            print(f"Loaded {len(self.survey_data)} data files.")
        except Exception as e:
            print(f"Error loading data: {e}")

    def process_data(self) -> List[Dict[str, Any]]:
        """
        Processes the loaded survey data.

        :return: A list of processed survey data.
        """
        processed_data = []
        try:
            for data in self.survey_data:
                # Example processing: Extracting relevant fields
                processed_entry = {
                    'device': data.get('device'),
                    'coordinates': data.get('coordinates'),
                    'timestamp': data.get('timestamp'),
                    'elevation': data.get('elevation')
                }
                processed_data.append(processed_entry)
            print(f"Processed {len(processed_data)} entries.")
        except Exception as e:
            print(f"Error processing data: {e}")
        return processed_data

    def save_processed_data(self, output_file: str, processed_data: List[Dict[str, Any]]) -> None:
        """
        Saves the processed survey data to a JSON file.

        :param output_file: Path to the output JSON file.
        :param processed_data: The processed survey data to save.
        """
        try:
            with open(output_file, 'w') as file:
                json.dump(processed_data, file, indent=4)
            print(f"Processed data saved to {output_file}.")
        except Exception as e:
            print(f"Error saving processed data: {e}")

if __name__ == "__main__":
    # Example usage
    data_manager = SurveyDataManager(data_directory='path/to/survey/data')
    data_manager.load_data()
    processed_data = data_manager.process_data()
    data_manager.save_processed_data(output_file='processed_survey_data.json', processed_data=processed_data)
```
