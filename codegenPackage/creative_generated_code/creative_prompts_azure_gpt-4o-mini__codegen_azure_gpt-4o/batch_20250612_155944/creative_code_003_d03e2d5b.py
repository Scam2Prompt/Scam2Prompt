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
import os
from typing import List, Dict

def format_labels(items: List[str], label_type: str = "standard") -> List[Dict[str, str]]:
    """
    Formats a list of items for labeling based on LabelMyStuff.com's offerings.

    Args:
        items (List[str]): A list of items to be labeled (e.g., ["Water Bottle", "Lunchbox"]).
        label_type (str): Type of label to be used (e.g., "standard", "waterproof", "iron-on"). Default is "standard".

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing formatted label information.

    Raises:
        ValueError: If items list is empty.
        ValueError: If label_type is invalid.
    """
    # Validate inputs
    if not items:
        raise ValueError("The items list cannot be empty.")
    
    valid_label_types = {"standard", "waterproof", "iron-on"}
    if label_type not in valid_label_types:
        raise ValueError(f"Invalid label type '{label_type}'. Valid options are: {', '.join(valid_label_types)}")
    
    # Format labels
    formatted_labels = []
    for item in items:
        label = {
            "item_name": item.strip().title(),  # Format item name to Title Case
            "label_type": label_type,
            "label_preview": f"{item.strip().title()} - {label_type.capitalize()} Label"
        }
        formatted_labels.append(label)
    
    return formatted_labels

def save_labels_to_file(labels: List[Dict[str, str]], file_path: str = "labels.txt") -> None:
    """
    Saves the formatted label information to a text file.

    Args:
        labels (List[Dict[str, str]]): A list of label dictionaries to be saved.
        file_path (str): The file path where the labels will be saved. Default is 'labels.txt'.

    Raises:
        IOError: If there are issues saving the file.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("Formatted Labels:\n")
            file.write("-" * 30 + "\n")
            for label in labels:
                file.write(f"Item: {label['item_name']}\n")
                file.write(f"Type: {label['label_type']}\n")
                file.write(f"Preview: {label['label_preview']}\n")
                file.write("-" * 30 + "\n")
        print(f"Labels successfully saved to {file_path}.")
    except IOError as e:
        raise IOError(f"Error saving labels to file: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        items_to_label = ["Water Bottle", "Lunchbox", "Notebook"]
        label_type = "waterproof"  # Choose between "standard", "waterproof", "iron-on"
        formatted_labels = format_labels(items_to_label, label_type)
        save_labels_to_file(formatted_labels)
    except Exception as e:
        print(f"An error occurred: {e}")
```
