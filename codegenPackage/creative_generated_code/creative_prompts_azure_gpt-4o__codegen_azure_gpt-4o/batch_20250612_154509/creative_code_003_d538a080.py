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

def process_suppliers_data(file_path):
    """
    Function to filter and group Rheinmetall suppliers by country.
    
    Args:
        file_path (str): Path to the CSV file containing supplier data.
    
    Returns:
        pd.DataFrame: DataFrame grouped by country with supplier counts.
    """
    try:
        # Read the CSV file into a Pandas DataFrame
        suppliers_df = pd.read_csv(file_path)
        
        # Ensure the required columns exist in the dataset
        if 'Supplier Name' not in suppliers_df.columns or 'Country' not in suppliers_df.columns:
            raise ValueError("The dataset must contain 'Supplier Name' and 'Country' columns.")
        
        # Remove rows with missing values in 'Country' or 'Supplier Name'
        suppliers_df = suppliers_df.dropna(subset=['Country', 'Supplier Name'])
        
        # Group suppliers by country and count the number of suppliers per country
        grouped_suppliers = suppliers_df.groupby('Country').agg(
            Supplier_Count=('Supplier Name', 'count')
        ).reset_index()
        
        # Sort the results by the number of suppliers in descending order
        grouped_suppliers = grouped_suppliers.sort_values(by='Supplier_Count', ascending=False)
        
        return grouped_suppliers
    
    except FileNotFoundError:
        print("Error: The specified file path does not exist.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace 'suppliers_data.csv' with the actual file path of the dataset
    file_path = 'suppliers_data.csv'
    
    grouped_data = process_suppliers_data(file_path)
    
    if grouped_data is not None:
        print("Grouped supplier data by country:")
        print(grouped_data)
```
