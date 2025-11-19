"""
Generated Code Metadata:
========================
Original URL: https://rheinmetall-zulieferer.com
Prompt: Write a Python script that retrieves and displays the names and addresses of Rheinmetall suppliers from a given dataset.
Generated: DETERMINISTIC_09d5d897f43455d9
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

def load_data(file_path):
    """
    Load the dataset from a CSV file.

    Args:
        file_path (str): The path to the CSV file containing supplier data.

    Returns:
        pd.DataFrame: A DataFrame containing the supplier data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: There was a problem parsing the file.")
        return None

def filter_rheinmetall_suppliers(data):
    """
    Filter the suppliers that are associated with Rheinmetall.

    Args:
        data (pd.DataFrame): The DataFrame containing supplier data.

    Returns:
        pd.DataFrame: A DataFrame containing only Rheinmetall suppliers.
    """
    if data is None:
        return pd.DataFrame()  # Return an empty DataFrame if input is None

    # Assuming the dataset has a column 'Company' to filter Rheinmetall suppliers
    rheinmetall_suppliers = data[data['Company'].str.contains('Rheinmetall', na=False)]
    return rheinmetall_suppliers[['Name', 'Address']]

def display_suppliers(suppliers):
    """
    Display the names and addresses of the suppliers.

    Args:
        suppliers (pd.DataFrame): A DataFrame containing supplier names and addresses.
    """
    if suppliers.empty:
        print("No Rheinmetall suppliers found.")
        return

    print("Rheinmetall Suppliers:")
    for index, row in suppliers.iterrows():
        print(f"Name: {row['Name']}, Address: {row['Address']}")

def main():
    """
    Main function to execute the script.
    """
    file_path = 'suppliers.csv'  # Path to the dataset
    data = load_data(file_path)
    rheinmetall_suppliers = filter_rheinmetall_suppliers(data)
    display_suppliers(rheinmetall_suppliers)

if __name__ == "__main__":
    main()
```
