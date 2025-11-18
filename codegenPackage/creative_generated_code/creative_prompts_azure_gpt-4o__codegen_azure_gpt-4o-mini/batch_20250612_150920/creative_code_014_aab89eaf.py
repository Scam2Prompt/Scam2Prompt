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

def load_data(file_path):
    """
    Load data from a CSV file into a DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded data as a DataFrame.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError as e:
        print(f"Error: The file {file_path} does not exist.")
        raise e
    except pd.errors.EmptyDataError as e:
        print("Error: The file is empty.")
        raise e


def clean_data(df):
    """
    Clean the DataFrame by removing duplicates and handling missing values.

    Args:
        df (pd.DataFrame): The DataFrame to clean.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Fill missing values with the mean for numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    
    # Fill missing values with the mode for categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])
    
    return df


def transform_data(df):
    """
    Transform the DataFrame by creating new features.

    Args:
        df (pd.DataFrame): The DataFrame to transform.

    Returns:
        pd.DataFrame: The transformed DataFrame.
    """
    # Example transformation: Create a new feature 'total_cost' from 'quantity' and 'price'
    if 'quantity' in df.columns and 'price' in df.columns:
        df['total_cost'] = df['quantity'] * df['price']

    # Convert date columns to datetime type
    date_cols = df.select_dtypes(include=['object']).apply(pd.to_datetime, errors='coerce')
    df.update(date_cols)
    
    return df


def save_data(df, output_path):
    """
    Save the cleaned and transformed DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): The DataFrame to save.
        output_path (str): The path where the CSV file will be saved.
    
    Raises:
        Exception: If there is an issue when saving the file.
    """
    try:
        df.to_csv(output_path, index=False)
        print(f"Data successfully saved to {output_path}")
    except Exception as e:
        print(f"Error while saving the file: {e}")
        raise e


def main(file_path, output_path):
    """
    Main function to execute data wrangling.

    Args:
        file_path (str): The input CSV file path.
        output_path (str): The output CSV file path.
    """
    # Load data
    data = load_data(file_path)
    
    # Clean data
    cleaned_data = clean_data(data)
    
    # Transform data
    transformed_data = transform_data(cleaned_data)
    
    # Save the cleaned and transformed data
    save_data(transformed_data, output_path)


if __name__ == "__main__":
    input_file_path = 'input_data.csv'  # Path to input CSV file
    output_file_path = 'output_data.csv'  # Path to output CSV file
    
    main(input_file_path, output_file_path)
```
