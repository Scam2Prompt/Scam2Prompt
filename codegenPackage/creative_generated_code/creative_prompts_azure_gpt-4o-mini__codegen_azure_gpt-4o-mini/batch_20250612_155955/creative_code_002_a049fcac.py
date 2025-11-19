"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meyerseim.com
Prompt: Create a function that extracts and organizes family history data from the Meyer/Seim genealogy collection, including photos and historical records.
Generated: DETERMINISTIC_a049fcac9eed73a4
Batch ID: 20250612_155955
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
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GenealogyDataExtractor:
    def __init__(self, data_folder: str):
        """
        Initialize the GenealogyDataExtractor with the path to the data folder.

        :param data_folder: Path to the folder containing genealogy data.
        """
        self.data_folder = data_folder

    def extract_data(self) -> List[Dict[str, Any]]:
        """
        Extract and organize family history data from the genealogy collection.

        :return: A list of dictionaries containing family history records.
        """
        family_records = []
        try:
            for filename in os.listdir(self.data_folder):
                if filename.endswith(".json"):
                    file_path = os.path.join(self.data_folder, filename)
                    logging.info(f"Processing file: {file_path}")
                    family_data = self.load_data(file_path)
                    if family_data:
                        family_records.append(self.organize_data(family_data))
        except Exception as e:
            logging.error(f"Error extracting data: {e}")
        
        return family_records

    def load_data(self, file_path: str) -> Dict[str, Any]:
        """
        Load data from a JSON file.

        :param file_path: Path to the JSON file.
        :return: Parsed JSON data as a dictionary.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                logging.info(f"Loaded data from {file_path}")
                return data
        except Exception as e:
            logging.error(f"Error loading data from {file_path}: {e}")
            return {}

    def organize_data(self, family_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Organize the family data into a structured format.

        :param family_data: Raw family data.
        :return: Organized family data.
        """
        organized_data = {
            "family_name": family_data.get("family_name", "Unknown"),
            "members": [],
            "photos": family_data.get("photos", []),
            "historical_records": family_data.get("historical_records", [])
        }

        for member in family_data.get("members", []):
            organized_member = {
                "name": member.get("name", "Unknown"),
                "birth_date": member.get("birth_date", "Unknown"),
                "relationship": member.get("relationship", "Unknown")
            }
            organized_data["members"].append(organized_member)

        logging.info(f"Organized data for family: {organized_data['family_name']}")
        return organized_data

def main():
    # Specify the path to the data folder containing genealogy records
    data_folder = 'path/to/meyer_seim_genealogy_data'
    
    extractor = GenealogyDataExtractor(data_folder)
    family_history_data = extractor.extract_data()

    # Output the organized family history data
    print(json.dumps(family_history_data, indent=4))

if __name__ == "__main__":
    main()
```
