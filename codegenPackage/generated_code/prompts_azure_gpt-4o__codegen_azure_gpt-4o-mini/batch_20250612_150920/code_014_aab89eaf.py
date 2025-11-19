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
import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file into a DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The loaded DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}.")
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: There was a parsing error.")
        return None

def clean_data(df):
    """
    Clean the DataFrame by handling missing values and duplicates.

    Parameters:
    df (pd.DataFrame): The DataFrame to clean.

    Returns:
    pd.DataFrame: The cleaned DataFrame.
    """
    # Drop duplicates
    initial_shape = df.shape
    df = df.drop_duplicates()
    print(f"Dropped {initial_shape[0] - df.shape[0]} duplicate rows.")

    # Fill missing values with the mean for numeric columns
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        mean_value = df[column].mean()
        df[column].fillna(mean_value, inplace=True)
        print(f"Filled missing values in column '{column}' with mean value: {mean_value}.")

    return df

def transform_data(df):
    """
    Transform the DataFrame by creating new features.

    Parameters:
    df (pd.DataFrame): The DataFrame to transform.

    Returns:
    pd.DataFrame: The transformed DataFrame.
    """
    # Example transformation: Create a new column based on existing data
    if 'existing_column' in df.columns:
        df['new_feature'] = df['existing_column'] * 2  # Example transformation
        print("New feature 'new_feature' created based on 'existing_column'.")
    else:
        print("Warning: 'existing_column' not found. New feature not created.")

    return df

def save_data(df, output_path):
    """
    Save the cleaned and transformed DataFrame to a CSV file.

    Parameters:
    df (pd.DataFrame): The DataFrame to save.
    output_path (str): The path to save the CSV file.
    """
    try:
        df.to_csv(output_path, index=False)
        print(f"Data saved successfully to {output_path}.")
    except Exception as e:
        print(f"Error saving data: {e}")

def main():
    # Define file paths
    input_file = 'input_data.csv'
    output_file = 'cleaned_data.csv'

    # Load data
    data = load_data(input_file)
    if data is None:
        return  # Exit if data loading failed

    # Clean data
    cleaned_data = clean_data(data)

    # Transform data
    transformed_data = transform_data(cleaned_data)

    # Save cleaned and transformed data
    save_data(transformed_data, output_file)

if __name__ == "__main__":
    main()
```
