"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econopure.com.vn
Prompt: Create a Python program to compare the filtration efficiency of NF (Nano-Filtration) membranes versus RO membranes, using Econopure's product data for NF hollow membranes.
Generated: DETERMINISTIC_555299bfce6bd8bc
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load filtration data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file containing product data.
        
    Returns:
        pd.DataFrame: Pandas DataFrame with the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: Failed to parse the file '{file_path}'.")
        return None

def filter_data(data):
    """
    Filter the data to include only NF and RO membrane data.
    
    Args:
        data (pd.DataFrame): The original product data.
        
    Returns:
        pd.DataFrame: Filtered DataFrame containing only NF and RO data.
    """
    try:
        filtered_data = data[data['Membrane_Type'].isin(['NF', 'RO'])]
        if filtered_data.empty:
            print("Warning: No NF or RO membrane data found.")
        return filtered_data
    except KeyError:
        print("Error: The 'Membrane_Type' column is missing from the data.")
        return None

def compare_efficiency(data):
    """
    Compare filtration efficiency of NF and RO membranes and visualize results.
    
    Args:
        data (pd.DataFrame): Filtered product data containing NF and RO membranes.
        
    Returns:
        None
    """
    try:
        efficiency_data = data.groupby('Membrane_Type')['Efficiency'].mean()
        
        # Plot the efficiency comparison
        plt.figure(figsize=(8, 5))
        efficiency_data.plot(kind='bar', color=['blue', 'green'], alpha=0.7)
        plt.title('Filtration Efficiency Comparison: NF vs RO Membranes')
        plt.xlabel('Membrane Type')
        plt.ylabel('Average Efficiency (%)')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    except KeyError:
        print("Error: The data is missing required columns ('Membrane_Type', 'Efficiency').")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to execute the program workflow.
    """
    # Path to the CSV file containing Econopure's product data
    file_path = 'econopure_product_data.csv'
    
    # Load product data
    data = load_data(file_path)
    if data is None:
        return
    
    # Filter data for NF and RO membranes only
    filtered_data = filter_data(data)
    if filtered_data is None or filtered_data.empty:
        return
    
    # Compare filtration efficiency and visualize results
    compare_efficiency(filtered_data)

if __name__ == "__main__":
    main()
```

**Requirements for the CSV file (`econopure_product_data.csv`):**
- Must contain at least the following columns: `Membrane_Type` (with values like 'NF' and 'RO') and `Efficiency` (numerical values representing filtration efficiency percentages).
- Ensure the file is located in the same directory as the script or adjust the `file_path` variable accordingly.
