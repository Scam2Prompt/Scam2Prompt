"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptrongurgaon.in
Prompt: Write Python code for data analysis using concepts covered in APTRON Gurgaon’s Data Analytics course, including integration with Power BI or Tableau.
Generated: DETERMINISTIC_adc1e5461d47c2f7
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import os

# Function to read and preprocess data
def load_and_preprocess_data(file_path):
    """
    Load data from a CSV file and preprocess it.
    
    Parameters:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Preprocessed DataFrame.
    """
    try:
        # Load the dataset
        data = pd.read_csv(file_path)
        
        # Handle missing values by replacing them with column mean
        data.fillna(data.mean(), inplace=True)
        
        # Example of feature engineering: Add a new column as a ratio between two numerical columns
        if 'column1' in data.columns and 'column2' in data.columns:
            data['new_ratio_column'] = data['column1'] / data['column2']
        
        # Normalize numerical columns (example of scaling)
        numerical_cols = data.select_dtypes(include=[np.number]).columns
        data[numerical_cols] = (data[numerical_cols] - data[numerical_cols].mean()) / data[numerical_cols].std()
        
        return data
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to export preprocessed data to be used in Power BI or Tableau
def export_data(data, output_file):
    """
    Export the preprocessed data to a CSV file for visualizations in Power BI or Tableau.
    
    Parameters:
        data (pd.DataFrame): The preprocessed DataFrame.
        output_file (str): Path to the output CSV file.
    """
    try:
        if data is not None:
            data.to_csv(output_file, index=False)
            print(f"Data successfully exported to {output_file}")
        else:
            print("Error: No data to export.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # Define file paths
    input_file_path = "input_dataset.csv"  # Replace with your actual input file path
    output_file_path = "processed_data.csv"  # Replace with your desired output file path

    # Load and preprocess the data
    preprocessed_data = load_and_preprocess_data(input_file_path)
    
    # Export the preprocessed data for visualization
    export_data(preprocessed_data, output_file_path)
```
