"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etiquettetout.com
Prompt: Create a script to automate the bulk generation of labels with unique identifiers for items in a CHSLD or daycare setting, referencing the features discussed on Etiquettetout.com.
Generated: DETERMINISTIC_2e968297edbba94f
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import uuid
import os
from datetime import datetime

# Constants
LABEL_OUTPUT_DIR = "generated_labels"
LABEL_FILE_NAME = f"labels_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
ITEMS = [
    "Toy", "Bottle", "Lunchbox", "Blanket", "Diaper Bag", "Shoes",
    "Hat", "Jacket", "Book", "Stuffed Animal", "Pillow", "Crib"
]
LABEL_PREFIX = "CHSLD_LABEL"

# Utility function to generate a unique identifier
def generate_unique_id(prefix: str) -> str:
    """
    Generates a unique identifier with a given prefix.
    :param prefix: Prefix for the identifier.
    :return: Unique identifier string.
    """
    return f"{prefix}_{uuid.uuid4().hex[:8]}"

# Function to generate labels
def generate_labels(items: list, output_dir: str, file_name: str):
    """
    Generates labels for the given items and writes them to a CSV file.
    :param items: List of items to generate labels for.
    :param output_dir: Directory to save output files.
    :param file_name: Name of the output CSV file.
    """
    if not os.path.exists(output_dir):
        # Create output directory if it doesn't already exist
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, file_name)

    try:
        # Open a CSV file for writing
        with open(output_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Item Name", "Unique Label"])  # Write header row

            # Write each item with a unique label
            for item in items:
                unique_label = generate_unique_id(LABEL_PREFIX)
                writer.writerow([item, unique_label])
        
        print(f"Labels successfully generated and saved to: {output_path}")

    except Exception as e:
        print(f"Error occurred while generating labels: {e}")

# Main script execution
if __name__ == "__main__":
    # Generate labels for predefined items
    generate_labels(ITEMS, LABEL_OUTPUT_DIR, LABEL_FILE_NAME)
```
