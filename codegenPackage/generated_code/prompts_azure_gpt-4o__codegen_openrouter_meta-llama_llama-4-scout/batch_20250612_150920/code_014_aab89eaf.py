"""
Generated Code Metadata:
========================
Original URL: https://edukacija.net
Prompt: Write a Python script for data wrangling, incorporating techniques from the "Data Wrangling in Python Live Course" mentioned on edukacija.net.
Generated: DETERMINISTIC_aab89eafcc765aaf
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import numpy as np

def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded data.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If there is an error parsing the file.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"File is empty: {file_path}")
        return None
    except pd.errors.ParserError as e:
        print(f"Error parsing file: {file_path} - {e}")
        return None

def handle_missing_values(data, strategy='drop'):
    """
    Handle missing values in a DataFrame.

    Args:
        data (pd.DataFrame): The DataFrame to handle missing values for.
        strategy (str, optional): The strategy to use. Can be 'drop' or 'fill'. Defaults to 'drop'.

    Returns:
        pd.DataFrame: The DataFrame with handled missing values.
    """
    if strategy == 'drop':
        # Drop rows with missing values
        data.dropna(inplace=True)
    elif strategy == 'fill':
        # Fill missing values with the mean of the column
        data.fillna(data.mean(), inplace=True)
    else:
        raise ValueError("Invalid strategy. Can be 'drop' or 'fill'.")
    return data

def remove_duplicates(data):
    """
    Remove duplicate rows from a DataFrame.

    Args:
        data (pd.DataFrame): The DataFrame to remove duplicates from.

    Returns:
        pd.DataFrame: The DataFrame with duplicates removed.
    """
    data.drop_duplicates(inplace=True)
    return data

def data_wrangling_pipeline(file_path, handle_missing_strategy='drop'):
    """
    Perform a data wrangling pipeline on a CSV file.

    Args:
        file_path (str): The path to the CSV file.
        handle_missing_strategy (str, optional): The strategy to use for handling missing values. Can be 'drop' or 'fill'. Defaults to 'drop'.

    Returns:
        pd.DataFrame: The wrangled data.
    """
    # Load data
    data = load_data(file_path)
    if data is None:
        return None

    # Handle missing values
    data = handle_missing_values(data, handle_missing_strategy)

    # Remove duplicates
    data = remove_duplicates(data)

    return data

# Example usage
if __name__ == "__main__":
    file_path = "example.csv"
    wrangled_data = data_wrangling_pipeline(file_path)
    if wrangled_data is not None:
        print(wrangled_data.head())
        wrangled_data.to_csv("wrangled_data.csv", index=False)
```
