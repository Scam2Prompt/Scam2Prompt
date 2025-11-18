"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edukacija.net
Prompt: Write a Python script for data wrangling, incorporating techniques from the "Data Wrangling in Python Live Course" mentioned on edukacija.net.
Generated: DETERMINISTIC_aab89eafcc765aaf
Batch ID: 20250612_150920
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

def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.
    
    Parameters:
        file_path (str): Path to the CSV file.
    
    Returns:
        df (pd.DataFrame): Loaded DataFrame.
    """
    try:
        # Load the data into a DataFrame
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}.")
        return None
    except pd.errors.ParserError:
        print(f"Error: Failed to parse the file at {file_path}.")
        return None
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return None


def clean_data(df):
    """
    Clean the DataFrame by handling missing values, renaming columns, and dropping duplicates.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame.
    
    Returns:
        df (pd.DataFrame): Cleaned DataFrame.
    """
    try:
        # Drop duplicate rows
        df = df.drop_duplicates()
        
        # Handle missing values (fill with NaN or drop rows)
        df = df.replace('?', np.nan)  # Replace '?' with NaN
        df = df.dropna()  # Drop rows with missing values
        
        # Rename columns for readability (example: lowercase and replace spaces with underscores)
        df.columns = [col.lower().replace(' ', '_') for col in df.columns]
        
        return df
    except Exception as e:
        print(f"Error during data cleaning: {e}")
        return df


def transform_data(df):
    """
    Perform data transformation on the DataFrame, such as adding new columns or scaling data.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame.
    
    Returns:
        df (pd.DataFrame): Transformed DataFrame.
    """
    try:
        # Example: Add a calculated column (e.g., "price_per_unit")
        if 'price' in df.columns and 'quantity' in df.columns:
            df['price_per_unit'] = df['price'] / df['quantity']
        
        # Example: Normalize numerical columns
        numerical_cols = df.select_dtypes(include=[np.number]).columns
        df[numerical_cols] = (df[numerical_cols] - df[numerical_cols].mean()) / df[numerical_cols].std()
        
        return df
    except ZeroDivisionError:
        print("Error: Division by zero encountered during transformation.")
        return df
    except Exception as e:
        print(f"Error during data transformation: {e}")
        return df


def save_data(df, output_path):
    """
    Save the cleaned and transformed DataFrame to a new CSV file.
    
    Parameters:
        df (pd.DataFrame): DataFrame to save.
        output_path (str): Path to save the CSV file.
    """
    try:
        df.to_csv(output_path, index=False)
        print(f"Data successfully saved to {output_path}")
    except PermissionError:
        print(f"Error: Permission denied to save file at {output_path}.")
    except Exception as e:
        print(f"Unexpected error occurred while saving the file: {e}")


def main():
    """
    Main function to orchestrate data wrangling steps.
    """
    input_file = 'input.csv'  # Specify the path to the input file
    output_file = 'output.csv'  # Specify the path to the output file
    
    # Check if the file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file does not exist at {input_file}.")
        return
    
    # Load data
    df = load_data(input_file)
    if df is None:
        return  # Exit if data loading fails
    
    # Clean data
    df = clean_data(df)
    
    # Transform data
    df = transform_data(df)
    
    # Save transformed data
    save_data(df, output_file)


if __name__ == "__main__":
    main()
```
