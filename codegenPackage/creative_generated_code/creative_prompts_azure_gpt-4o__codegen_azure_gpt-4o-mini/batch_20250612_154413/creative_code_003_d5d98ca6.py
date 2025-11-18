"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eagle-tex.cn
Prompt: Write a program in Python to parse and organize fabric data from Shaoxing Eagles Textile Co., Ltd., grouping items like "French Terry," "Hacci," and "Two Face Waffle Cloth" into categories.
Generated: DETERMINISTIC_d5d98ca629857ee7
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from collections import defaultdict
from typing import Dict, List, Any

class FabricParser:
    """
    A class to parse and organize fabric data from a textile company.
    """

    def __init__(self, input_file: str):
        """
        Initializes the FabricParser with the path to the input CSV file.
        
        :param input_file: Path to the CSV file containing fabric data.
        """
        self.input_file = input_file
        self.fabric_data = defaultdict(list)

    def parse_fabric_data(self) -> None:
        """
        Parses the CSV file and organizes fabric items into categories.
        """
        try:
            with open(self.input_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    category = self.categorize_fabric(row['Fabric Type'])
                    self.fabric_data[category].append(row)
        except FileNotFoundError:
            print(f"Error: The file {self.input_file} was not found.")
        except Exception as e:
            print(f"An error occurred while parsing the file: {e}")

    def categorize_fabric(self, fabric_type: str) -> str:
        """
        Determines the category of the fabric based on its type.
        
        :param fabric_type: The type of fabric to categorize.
        :return: Category as a string.
        """
        fabric_type = fabric_type.lower()
        if 'terry' in fabric_type:
            return 'French Terry'
        elif 'hacci' in fabric_type:
            return 'Hacci'
        elif 'waffle' in fabric_type:
            return 'Two Face Waffle Cloth'
        else:
            return 'Other'

    def get_fabric_summary(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Returns a summary of the organized fabric data.
        
        :return: A dictionary with fabric categories as keys and a list of items as values.
        """
        return dict(self.fabric_data)

# Example usage:
if __name__ == "__main__":
    parser = FabricParser('fabric_data.csv')  # Replace with the actual CSV file path
    parser.parse_fabric_data()
    summary = parser.get_fabric_summary()

    for category, items in summary.items():
        print(f"{category}: {len(items)} items")
        for item in items:
            print(f"  - {item}")
```

Make sure to replace `'fabric_data.csv'` with the actual path to your CSV file containing the fabric data for parsing.
