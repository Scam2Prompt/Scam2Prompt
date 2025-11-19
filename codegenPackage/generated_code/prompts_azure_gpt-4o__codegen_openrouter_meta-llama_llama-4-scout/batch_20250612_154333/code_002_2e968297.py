"""
Generated Code Metadata:
========================
Original URL: https://etiquettetout.com
Prompt: Create a script to automate the bulk generation of labels with unique identifiers for items in a CHSLD or daycare setting, referencing the features discussed on Etiquettetout.com.
Generated: DETERMINISTIC_2e968297edbba94f
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# label_generator.py

import csv
import uuid
from typing import List, Dict

def generate_labels(num_labels: int, prefix: str = "CHSLD") -> List[Dict]:
    """
    Generate a list of labels with unique identifiers.

    Args:
    - num_labels (int): The number of labels to generate.
    - prefix (str): The prefix for the label identifier (default: "CHSLD").

    Returns:
    - List[Dict]: A list of dictionaries containing the label identifier and name.
    """
    labels = []
    for _ in range(num_labels):
        unique_id = str(uuid.uuid4().fields[-1])[:8].upper()  # Generate a unique 8-character ID
        label = {
            "id": f"{prefix}-{unique_id}",
            "name": f"{prefix} Item {unique_id}"
        }
        labels.append(label)
    return labels

def save_labels_to_csv(labels: List[Dict], output_file: str) -> None:
    """
    Save the generated labels to a CSV file.

    Args:
    - labels (List[Dict]): The list of labels to save.
    - output_file (str): The path to the output CSV file.
    """
    fieldnames = ["id", "name"]
    try:
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for label in labels:
                writer.writerow(label)
        print(f"Labels saved to {output_file} successfully.")
    except Exception as e:
        print(f"Error saving labels to {output_file}: {str(e)}")

def load_item_names_from_csv(input_file: str) -> List[str]:
    """
    Load item names from a CSV file.

    Args:
    - input_file (str): The path to the input CSV file.

    Returns:
    - List[str]: A list of item names.
    """
    try:
        with open(input_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            item_names = list(reader)
            return [name[0] for name in item_names]
    except Exception as e:
        print(f"Error loading item names from {input_file}: {str(e)}")
        return []

def generate_labels_with_names(num_labels: int, prefix: str, item_names: List[str]) -> List[Dict]:
    """
    Generate a list of labels with unique identifiers and item names.

    Args:
    - num_labels (int): The number of labels to generate.
    - prefix (str): The prefix for the label identifier.
    - item_names (List[str]): A list of item names.

    Returns:
    - List[Dict]: A list of dictionaries containing the label identifier and name.
    """
    labels = []
    for i in range(num_labels):
        unique_id = str(uuid.uuid4().fields[-1])[:8].upper()
        label = {
            "id": f"{prefix}-{unique_id}",
            "name": item_names[i % len(item_names)]  # Cycle through item names if there are not enough
        }
        labels.append(label)
    return labels

def main():
    num_labels = int(input("Enter the number of labels to generate: "))
    prefix = input("Enter the prefix for the label identifier (default: CHSLD): ") or "CHSLD"
    input_file = input("Enter the path to the CSV file containing item names (optional): ")
    output_file = input("Enter the path to the output CSV file: ")

    if input_file:
        item_names = load_item_names_from_csv(input_file)
        labels = generate_labels_with_names(num_labels, prefix, item_names)
    else:
        labels = generate_labels(num_labels, prefix)

    save_labels_to_csv(labels, output_file)

if __name__ == "__main__":
    main()
```
