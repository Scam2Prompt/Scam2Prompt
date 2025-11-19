"""
Generated Code Metadata:
========================
Original URL: https://etiquettetout.com
Prompt: Write a Python code to generate labels for identifying children's clothing and personal items for a summer camp.
Generated: DETERMINISTIC_4c4c385799a66374
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import string
import json
from typing import List, Dict

class LabelGenerator:
    """
    A class to generate labels for children's clothing and personal items for a summer camp.
    """

    def __init__(self, camp_name: str):
        """
        Initializes the LabelGenerator with the camp name.

        :param camp_name: The name of the summer camp.
        """
        self.camp_name = camp_name

    def generate_unique_id(self, length: int = 6) -> str:
        """
        Generates a unique identifier for the label.

        :param length: The length of the unique identifier.
        :return: A string representing the unique identifier.
        """
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    def create_label(self, item_name: str, child_name: str) -> Dict[str, str]:
        """
        Creates a label for a given item and child's name.

        :param item_name: The name of the item (e.g., T-shirt, water bottle).
        :param child_name: The name of the child.
        :return: A dictionary representing the label.
        """
        unique_id = self.generate_unique_id()
        label = {
            "camp_name": self.camp_name,
            "child_name": child_name,
            "item_name": item_name,
            "unique_id": unique_id
        }
        return label

    def generate_labels(self, items: List[str], child_name: str) -> List[Dict[str, str]]:
        """
        Generates labels for a list of items for a specific child.

        :param items: A list of item names.
        :param child_name: The name of the child.
        :return: A list of labels.
        """
        labels = []
        for item in items:
            try:
                label = self.create_label(item, child_name)
                labels.append(label)
            except Exception as e:
                print(f"Error generating label for {item}: {e}")
        return labels

    def save_labels_to_file(self, labels: List[Dict[str, str]], filename: str) -> None:
        """
        Saves the generated labels to a JSON file.

        :param labels: A list of labels to save.
        :param filename: The name of the file to save the labels to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(labels, file, indent=4)
            print(f"Labels successfully saved to {filename}.")
        except IOError as e:
            print(f"Error saving labels to file: {e}")

# Example usage
if __name__ == "__main__":
    camp_name = "Sunny Days Camp"
    child_name = "Alice"
    items = ["T-shirt", "Shorts", "Water Bottle", "Hat"]

    label_generator = LabelGenerator(camp_name)
    labels = label_generator.generate_labels(items, child_name)
    label_generator.save_labels_to_file(labels, "camp_labels.json")
```
