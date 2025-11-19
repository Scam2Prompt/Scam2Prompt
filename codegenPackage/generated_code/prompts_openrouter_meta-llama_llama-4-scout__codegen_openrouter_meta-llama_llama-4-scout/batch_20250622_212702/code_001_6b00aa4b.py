"""
Generated Code Metadata:
========================
Original URL: https://www.thefishfinder.com
Prompt: "Write a Python script to categorize fishing tackle manufacturers listed in a directory like The Fish Finder."
Generated: DETERMINISTIC_6b00aa4bb7ec2a43
Batch ID: 20250622_212702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Fishing Tackle Manufacturer Categorizer

This script categorizes fishing tackle manufacturers listed in a directory.

Usage:
    python categorize_manufacturers.py --input_file input.txt --output_file output.csv

Requirements:
    - Python 3.8+
    - pandas library
"""

import argparse
import pandas as pd
import re

def load_manufacturers(input_file):
    """
    Load manufacturers from input file.

    Args:
        input_file (str): Path to input file.

    Returns:
        list: List of manufacturer names.
    """
    try:
        with open(input_file, 'r') as f:
            manufacturers = [line.strip() for line in f.readlines()]
        return manufacturers
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return []

def categorize_manufacturers(manufacturers):
    """
    Categorize manufacturers based on their product categories.

    Args:
        manufacturers (list): List of manufacturer names.

    Returns:
        dict: Dictionary with categories as keys and lists of manufacturers as values.
    """
    categories = {
        'Lure': [],
        'Rod': [],
        'Reel': [],
        'Line': [],
        'Hook': [],
        'Other': []
    }

    # Define keywords for each category
    keywords = {
        'Lure': ['lure', 'soft plastic', 'crankbait', 'jig'],
        'Rod': ['rod', 'graphite', 'fishing rod'],
        'Reel': ['reel', 'spinning reel', 'baitcasting reel'],
        'Line': ['line', 'monofilament', 'fluorocarbon', 'braided'],
        'Hook': ['hook', 'jig hook', 'baitholder']
    }

    for manufacturer in manufacturers:
        categorized = False
        for category, keyword_list in keywords.items():
            for keyword in keyword_list:
                if re.search(keyword, manufacturer, re.IGNORECASE):
                    categories[category].append(manufacturer)
                    categorized = True
                    break
            if categorized:
                break
        if not categorized:
            categories['Other'].append(manufacturer)

    return categories

def save_to_csv(categories, output_file):
    """
    Save categorized manufacturers to CSV file.

    Args:
        categories (dict): Dictionary with categories as keys and lists of manufacturers as values.
        output_file (str): Path to output file.
    """
    try:
        data = []
        for category, manufacturers in categories.items():
            for manufacturer in manufacturers:
                data.append({'Category': category, 'Manufacturer': manufacturer})

        df = pd.DataFrame(data)
        df.to_csv(output_file, index=False)
        print(f"Output saved to '{output_file}'")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def main():
    parser = argparse.ArgumentParser(description='Categorize fishing tackle manufacturers')
    parser.add_argument('--input_file', required=True, help='Path to input file')
    parser.add_argument('--output_file', required=True, help='Path to output file')
    args = parser.parse_args()

    manufacturers = load_manufacturers(args.input_file)
    categories = categorize_manufacturers(manufacturers)
    save_to_csv(categories, args.output_file)

if __name__ == '__main__':
    main()
```
