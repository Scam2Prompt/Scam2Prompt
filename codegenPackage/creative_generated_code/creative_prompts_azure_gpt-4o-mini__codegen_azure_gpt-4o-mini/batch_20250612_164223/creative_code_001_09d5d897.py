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
import pandas as pd

def load_supplier_data(file_path):
    """
    Load supplier data from a CSV file.

    :param file_path: str - Path to the CSV file containing supplier data.
    :return: DataFrame - A pandas DataFrame containing the supplier data.
    :raises FileNotFoundError: If the file does not exist.
    :raises ValueError: If the data is not in the expected format.
    """
    try:
        # Load the data into a DataFrame
        df = pd.read_csv(file_path)
        
        # Check if the necessary columns exist
        if 'Name' not in df.columns or 'Address' not in df.columns:
            raise ValueError("Data must contain 'Name' and 'Address' columns.")
        
        return df
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        raise
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

def filter_rheinmetall_suppliers(df):
    """
    Filter the suppliers that are associated with Rheinmetall.

    :param df: DataFrame - The DataFrame containing the supplier data.
    :return: DataFrame - A DataFrame with Rheinmetall suppliers.
    """
    # Filter suppliers based on the condition
    rheinmetall_suppliers = df[df['Name'].str.contains("Rheinmetall", case=False, na=False)]
    return rheinmetall_suppliers

def display_suppliers(suppliers):
    """
    Display the names and addresses of the suppliers.

    :param suppliers: DataFrame - The DataFrame containing the filtered suppliers.
    """
    if suppliers.empty:
        print("No Rheinmetall suppliers found.")
    else:
        print("Rheinmetall Suppliers:")
        for index, row in suppliers.iterrows():
            print(f"Name: {row['Name']}, Address: {row['Address']}")

def main():
    """
    Main function to execute the supplier retrieval and display.
    """
    # Define the path to the dataset
    file_path = 'suppliers.csv'  # Update this to your actual file path

    try:
        # Load the supplier data
        supplier_data = load_supplier_data(file_path)

        # Filter for Rheinmetall suppliers
        rheinmetall_suppliers = filter_rheinmetall_suppliers(supplier_data)

        # Display the filtered suppliers
        display_suppliers(rheinmetall_suppliers)
        
    except Exception as e:
        print(f"An error occurred during processing: {e}")

if __name__ == "__main__":
    main()
```
