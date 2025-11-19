"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: Write a program in Python to parse and organize fabric data from Shaoxing Eagles Textile Co., Ltd., grouping items like "French Terry," "Hacci," and "Two Face Waffle Cloth" into categories.
Generated: DETERMINISTIC_d5d98ca629857ee7
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from collections import defaultdict

class FabricDataParser:
    """
    A class to parse and organize fabric data from Shaoxing Eagles Textile Co., Ltd.
    """

    def __init__(self, fabric_data):
        """
        Initializes the FabricDataParser with raw fabric data.

        :param fabric_data: A list of dictionaries containing fabric information.
        """
        self.fabric_data = fabric_data
        self.organized_data = defaultdict(list)

    def parse_data(self):
        """
        Parses the fabric data and organizes it into categories.
        """
        try:
            for fabric in self.fabric_data:
                category = self.get_category(fabric)
                self.organized_data[category].append(fabric)
        except Exception as e:
            print(f"Error while parsing data: {e}")

    def get_category(self, fabric):
        """
        Determines the category of a fabric item based on its type.

        :param fabric: A dictionary containing fabric information.
        :return: A string representing the category of the fabric.
        """
        fabric_type = fabric.get('type', '').lower()
        if 'french terry' in fabric_type:
            return 'French Terry'
        elif 'hacci' in fabric_type:
            return 'Hacci'
        elif 'waffle' in fabric_type:
            return 'Waffle Cloth'
        else:
            return 'Other'

    def get_organized_data(self):
        """
        Returns the organized fabric data.

        :return: A dictionary with fabric categories as keys and lists of fabrics as values.
        """
        return dict(self.organized_data)

def main():
    # Sample fabric data from Shaoxing Eagles Textile Co., Ltd.
    sample_fabric_data = [
        {"type": "French Terry Cotton", "color": "Blue", "width": "150cm"},
        {"type": "Hacci Knit", "color": "Red", "width": "140cm"},
        {"type": "Two Face Waffle Cloth", "color": "Green", "width": "160cm"},
        {"type": "Polyester Fabric", "color": "Black", "width": "150cm"},
        {"type": "French Terry Spandex", "color": "Gray", "width": "150cm"},
    ]

    # Create an instance of FabricDataParser
    parser = FabricDataParser(sample_fabric_data)

    # Parse the fabric data
    parser.parse_data()

    # Get and print the organized fabric data
    organized_data = parser.get_organized_data()
    print(json.dumps(organized_data, indent=4))

if __name__ == "__main__":
    main()
```
