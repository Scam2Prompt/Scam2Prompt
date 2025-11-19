"""
Generated Code Metadata:
========================
Original URL: https://kraken-energy.com
Prompt: Write a Python script to automate the process of collecting mineral rights data from sellers in Oklahoma, including fields for first name, last name, email, and comments, as described on Kraken Energy's website.
Generated: DETERMINISTIC_87564f88d9d27a4b
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mineral_rights_collector.py

import csv
import datetime
import os

def collect_mineral_rights_data(seller_info):
    """
    Collects mineral rights data from a seller.

    Args:
        seller_info (dict): Dictionary containing seller's information.

    Returns:
        dict: Dictionary containing collected mineral rights data.
    """
    required_fields = ['first_name', 'last_name', 'email', 'comments']

    # Validate input data
    if not all(field in seller_info for field in required_fields):
        raise ValueError("Seller information is missing required fields.")

    # Initialize mineral rights data dictionary
    mineral_rights_data = {
        'collection_date': datetime.date.today().strftime("%Y-%m-%d"),
        'first_name': seller_info['first_name'],
        'last_name': seller_info['last_name'],
        'email': seller_info['email'],
        'comments': seller_info['comments']
    }

    return mineral_rights_data

def save_to_csv(mineral_rights_data, output_file):
    """
    Saves mineral rights data to a CSV file.

    Args:
        mineral_rights_data (dict): Dictionary containing mineral rights data.
        output_file (str): Path to the output CSV file.

    Returns:
        None
    """
    fieldnames = ['collection_date', 'first_name', 'last_name', 'email', 'comments']

    # Check if output file exists, if not create it
    if not os.path.exists(output_file):
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    # Append data to CSV file
    with open(output_file, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(mineral_rights_data)

def main():
    output_file = 'mineral_rights_data.csv'

    # Example seller information
    seller_info = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'comments': 'This is an example comment.'
    }

    try:
        mineral_rights_data = collect_mineral_rights_data(seller_info)
        save_to_csv(mineral_rights_data, output_file)
        print(f"Mineral rights data saved to {output_file} successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
