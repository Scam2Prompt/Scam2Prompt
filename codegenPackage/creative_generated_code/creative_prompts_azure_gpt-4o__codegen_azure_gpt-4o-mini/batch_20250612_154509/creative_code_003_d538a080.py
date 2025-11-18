"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rheinmetall-zulieferer.com
Prompt: Write a script using the Pandas library to filter and group Rheinmetall suppliers by country from a dataset extracted from their supplier webpage.
Generated: DETERMINISTIC_d538a080bc8939e2
Batch ID: 20250612_154509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def load_data(file_path):
    """
    Load supplier data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing supplier data.

    Returns:
    pd.DataFrame: A DataFrame containing the loaded supplier data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError("The specified file was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("The provided file is empty.")
    except pd.errors.ParserError:
        raise ValueError("Error parsing the data file. Please check the file format.")

def filter_and_group_suppliers(data):
    """
    Filter and group Rheinmetall suppliers by country.

    Parameters:
    data (pd.DataFrame): The DataFrame containing supplier data.

    Returns:
    pd.DataFrame: A DataFrame grouped by country with supplier counts.
    """
    if 'Country' not in data.columns or 'Supplier' not in data.columns:
        raise ValueError("Data must contain 'Country' and 'Supplier' columns.")

    # Group suppliers by country and count them
    grouped_data = data.groupby('Country')['Supplier'].count().reset_index()
    grouped_data.columns = ['Country', 'Supplier Count']  # Renaming columns for clarity

    return grouped_data

def main(file_path):
    """
    Main function to load, filter, and group supplier data.

    Parameters:
    file_path (str): The path to the CSV file containing supplier data.
    """
    # Load the supplier data
    suppliers_data = load_data(file_path)
    
    # Filter and group the suppliers
    grouped_suppliers = filter_and_group_suppliers(suppliers_data)
    
    # Display the result
    print(grouped_suppliers)

if __name__ == "__main__":
    # Example usage
    file_path = 'rheinmetall_suppliers.csv'  # Replace with your actual file path
    main(file_path)
```
