"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labelmystuff.com
Prompt: Generate a code snippet that formats a list of items for labeling, suitable for use in a nursery or kindergarten, based on LabelMyStuff.com’s offerings.
Generated: DETERMINISTIC_d03e2d5b7b037579
Batch ID: 20250612_155944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class LabelFormatter:
    """
    A class to format lists of items for labeling in a nursery or kindergarten.
    """

    def __init__(self, items: List[str]):
        """
        Initializes the LabelFormatter with a list of items.

        :param items: A list of item names to be formatted for labeling.
        """
        if not items:
            raise ValueError("The item list cannot be empty.")
        self.items = items

    def format_labels(self) -> List[Dict[str, str]]:
        """
        Formats the items for labeling.

        :return: A list of dictionaries containing formatted label details.
        """
        formatted_labels = []
        
        for item in self.items:
            label = self.create_label(item)
            formatted_labels.append(label)

        return formatted_labels

    @staticmethod
    def create_label(item: str) -> Dict[str, str]:
        """
        Creates a formatted label for a single item.

        :param item: The name of the item to be labeled.
        :return: A dictionary containing the label format.
        """
        if not isinstance(item, str) or not item.strip():
            raise ValueError(f"Invalid item name: {item}")

        # Format the label in a specific style
        label = {
            'item': item.strip(),
            'formatted_label': f"Label: {item.title()}",
            'color': 'bright',  # Example attribute, can be customized
            'size': 'medium'    # Example attribute, can be customized
        }
        
        return label

if __name__ == "__main__":
    # Example usage
    try:
        items_to_label = ["Toys", "Books", "Art Supplies", "Blocks"]
        formatter = LabelFormatter(items_to_label)
        labels = formatter.format_labels()
        
        for label in labels:
            print(label)

    except ValueError as e:
        print(f"Error: {e}")
```
