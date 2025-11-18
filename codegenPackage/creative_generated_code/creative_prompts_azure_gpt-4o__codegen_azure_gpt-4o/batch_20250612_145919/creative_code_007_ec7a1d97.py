"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswaphd.de
Prompt: Write code to aggregate vehicle data (geometric, electronic, and communication-related) from multiple manufacturers to inform the design of a universal battery swapping system for heavy-duty vehicles, as described in UniSwapHD.
Generated: DETERMINISTIC_ec7a1d977a1be80c
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import csv
import os
from typing import List, Dict

# Define a class to handle vehicle data aggregation
class VehicleDataAggregator:
    def __init__(self, input_files: List[str], output_file: str):
        """
        Initialize the aggregator.
        
        :param input_files: List of file paths containing vehicle data from manufacturers.
        :param output_file: File path to save the aggregated data.
        """
        self.input_files = input_files
        self.output_file = output_file
    
    def load_data(self) -> List[Dict]:
        """
        Load vehicle data from multiple files.

        :return: Combined list of vehicle data dictionaries.
        """
        aggregated_data = []

        for file_path in self.input_files:
            try:
                extension = os.path.splitext(file_path)[1].lower()
                if extension == ".json":
                    # Parse JSON files
                    with open(file_path, 'r') as json_file:
                        data = json.load(json_file)
                        aggregated_data.extend(data if isinstance(data, list) else [data])
                elif extension == ".csv":
                    # Parse CSV files
                    with open(file_path, 'r') as csv_file:
                        reader = csv.DictReader(csv_file)
                        aggregated_data.extend(list(reader))
                else:
                    # Skip unsupported file types
                    print(f"Unsupported file type: {file_path}")
            except Exception as e:
                print(f"Error loading file {file_path}: {e}")

        return aggregated_data

    def aggregate_data(self, raw_data: List[Dict]) -> Dict:
        """
        Aggregate vehicle data into a structured format suitable for analysis.
        
        :param raw_data: List of dictionaries containing raw vehicle data.
        :return: Dictionary containing aggregated data.
        """
        aggregated_result = {
            "geometric": [],
            "electronic": [],
            "communication": []
        }

        for vehicle in raw_data:
            try:
                # Categorize data based on key prefixes
                for key, value in vehicle.items():
                    if key.startswith("geo_"):
                        aggregated_result["geometric"].append({key: value})
                    elif key.startswith("elec_"):
                        aggregated_result["electronic"].append({key: value})
                    elif key.startswith("comm_"):
                        aggregated_result["communication"].append({key: value})
            except Exception as e:
                print(f"Error processing vehicle data: {e}")

        return aggregated_result

    def save_aggregated_data(self, aggregated_data: Dict):
        """
        Save aggregated vehicle data into a JSON file.

        :param aggregated_data: The aggregated vehicle data dictionary.
        """
        try:
            with open(self.output_file, 'w') as output:
                json.dump(aggregated_data, output, indent=4)
            print(f"Aggregated data saved to {self.output_file}")
        except Exception as e:
            print(f"Error saving aggregated data: {e}")

    def process(self):
        """
        Full pipeline for loading, aggregating, and saving vehicle data.
        """
        print("Loading data from manufacturers...")
        raw_data = self.load_data()

        print("Aggregating data...")
        aggregated_data = self.aggregate_data(raw_data)

        print("Saving aggregated data...")
        self.save_aggregated_data(aggregated_data)


if __name__ == "__main__":
    # List of input files containing vehicle data from manufacturers
    input_files = [
        "manufacturer1.json",
        "manufacturer2.csv",
        "manufacturer3.json"
    ]

    # Output file to save the aggregated data
    output_file = "aggregated_vehicle_data.json"

    # Initialize and execute the data aggregation pipeline
    aggregator = VehicleDataAggregator(input_files, output_file)
    aggregator.process()
```
