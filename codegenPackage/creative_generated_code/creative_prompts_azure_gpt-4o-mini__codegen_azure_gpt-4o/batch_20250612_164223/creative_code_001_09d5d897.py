"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rheinmetall-zulieferer.com
Prompt: Write a Python script that retrieves and displays the names and addresses of Rheinmetall suppliers from a given dataset.
Generated: DETERMINISTIC_09d5d897f43455d9
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import sys

def load_supplier_data(file_path):
    """
    Load supplier data from a CSV file.

    Parameters:
        file_path (str): Path to the CSV file containing supplier data.

    Returns:
        list[dict]: A list of dictionaries, each containing supplier information.
    """
    suppliers = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                suppliers.append(row)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        sys.exit(1)
    except csv.Error:
        print("Error: Failed to parse the CSV file")
        sys.exit(1)
    return suppliers

def filter_rheinmetall_suppliers(suppliers):
    """
    Filter suppliers related to Rheinmetall.

    Parameters:
        suppliers (list[dict]): A list of supplier data dictionaries.

    Returns:
        list[dict]: A filtered list containing Rheinmetall supplier data.
    """
    return [supplier for supplier in suppliers if supplier.get('Company') == 'Rheinmetall']

def display_suppliers(suppliers):
    """
    Display the names and addresses of suppliers.

    Parameters:
        suppliers (list[dict]): A list of supplier data dictionaries.
    """
    print("Rheinmetall Suppliers:")
    print("-" * 30)
    for supplier in suppliers:
        name = supplier.get('Name', 'Unknown')
        address = supplier.get('Address', 'Unknown')
        print(f"Name: {name}, Address: {address}")

def main():
    """
    Main function to retrieve and display Rheinmetall suppliers.
    """
    # Path to the CSV file containing supplier data
    file_path = "suppliers.csv"

    # Load supplier data
    suppliers = load_supplier_data(file_path)

    # Filter Rheinmetall suppliers
    rheinmetall_suppliers = filter_rheinmetall_suppliers(suppliers)

    # Display Rheinmetall suppliers
    display_suppliers(rheinmetall_suppliers)

if __name__ == "__main__":
    main()
```

### Notes:
1. Ensure the input CSV file (`suppliers.csv`) contains columns such as `Company`, `Name`, and `Address` for proper script functionality.
2. This script assumes a standard CSV format with headers in the first row. Adjust the code if your dataset differs.
