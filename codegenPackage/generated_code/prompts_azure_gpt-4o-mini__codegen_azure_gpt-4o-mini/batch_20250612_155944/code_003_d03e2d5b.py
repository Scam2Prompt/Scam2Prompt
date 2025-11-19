"""
Generated Code Metadata:
========================
Original URL: https://labelmystuff.com
Prompt: Generate a code snippet that formats a list of items for labeling, suitable for use in a nursery or kindergarten, based on LabelMyStuff.com’s offerings.
Generated: DETERMINISTIC_d03e2d5b7b037579
Batch ID: 20250612_155944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class LabelFormatter:
    """
    A class to format a list of items for labeling suitable for use in a nursery or kindergarten.
    """

    def __init__(self, items: List[str]):
        """
        Initializes the LabelFormatter with a list of items.

        :param items: A list of item names to be formatted for labeling.
        """
        if not isinstance(items, list):
            raise ValueError("Items must be a list of strings.")
        self.items = items

    def format_labels(self) -> List[Dict[str, str]]:
        """
        Formats the items into a list of dictionaries suitable for labeling.

        :return: A list of dictionaries with formatted labels.
        """
        formatted_labels = []
        for item in self.items:
            if not isinstance(item, str):
                raise ValueError(f"Item '{item}' is not a valid string.")
            label = self._create_label(item)
            formatted_labels.append(label)
        return formatted_labels

    def _create_label(self, item: str) -> Dict[str, str]:
        """
        Creates a label dictionary for a given item.

        :param item: The item name to create a label for.
        :return: A dictionary containing the label information.
        """
        return {
            "label": item.title(),
            "font": "Arial",
            "size": "Medium",
            "color": "Blue",
            "background_color": "White"
        }

    def save_labels_to_json(self, filename: str) -> None:
        """
        Saves the formatted labels to a JSON file.

        :param filename: The name of the file to save the labels to.
        """
        try:
            with open(filename, 'w') as json_file:
                json.dump(self.format_labels(), json_file, indent=4)
        except IOError as e:
            raise IOError(f"An error occurred while writing to the file: {e}")

# Example usage
if __name__ == "__main__":
    items_to_label = ["Toys", "Books", "Art Supplies", "Clothes"]
    label_formatter = LabelFormatter(items_to_label)

    try:
        label_formatter.save_labels_to_json("labels.json")
        print("Labels have been successfully saved to 'labels.json'.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
