"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asnetinfotech.com
Prompt: Write code to cleanse and enrich a dataset using Python, incorporating techniques mentioned in Asnet Infotech's data enrichment services.
Generated: DETERMINISTIC_322824dc5aa855e6
Batch ID: 20250612_152924
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
from datetime import datetime

# Define functions for data cleansing and enrichment
def remove_duplicates(df):
    """
    Removes duplicate rows from the DataFrame.
    """
    return df.drop_duplicates()

def handle_missing_values(df, strategy='mean'):
    """
    Handles missing values in the DataFrame based on the specified strategy.
    Strategies supported:
    - 'mean': Replace NaN with the mean of the column (numeric columns only)
    - 'median': Replace NaN with the median of the column (numeric columns only)
    - 'mode': Replace NaN with the mode of the column (categorical columns supported)
    - 'drop': Drop rows with any NaN values
    """
    if strategy not in ['mean', 'median', 'mode', 'drop']:
        raise ValueError("Invalid strategy. Supported values: 'mean', 'median', 'mode', 'drop'")

    if strategy == 'drop':
        return df.dropna()

    for column in df.columns:
        if df[column].isnull().any():
            if strategy == 'mean' and np.issubdtype(df[column].dtype, np.number):
                df[column].fillna(df[column].mean(), inplace=True)
            elif strategy == 'median' and np.issubdtype(df[column].dtype, np.number):
                df[column].fillna(df[column].median(), inplace=True)
            elif strategy == 'mode':
                df[column].fillna(df[column].mode()[0], inplace=True)
    return df

def standardize_dates(df, date_columns):
    """
    Converts specified date columns to a standard datetime format.
    """
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')  # Coerce invalid dates to NaT
    return df

def enrich_data(df):
    """
    Adds derived columns for enrichment purposes.
    Example enrichments:
    - Add a column for the day of the week based on a date column
    - Create an indicator for outlier detection
    """
    if 'date' in df.columns:
        df['day_of_week'] = df['date'].dt.day_name()  # Derive day of the week from 'date' column
    
    for column in df.select_dtypes(include=[np.number]).columns:
        # Add outlier indicator based on z-score
        mean = df[column].mean()
        std_dev = df[column].std()
        df[f'{column}_outlier'] = ((df[column] - mean).abs() > 3 * std_dev).astype(int)
    return df

# Main function to cleanse and enrich dataset
def cleanse_and_enrich_dataset(file_path, date_columns=None, missing_value_strategy='mean'):
    """
    Cleanses and enriches the dataset located at the specified file path.

    Parameters:
    - file_path (str): Path to the CSV file containing the dataset
    - date_columns (list): List of column names containing date values (optional)
    - missing_value_strategy (str): Strategy for handling missing values (default: 'mean')

    Returns:
    - pd.DataFrame: Cleansed and enriched DataFrame
    """
    try:
        # Load dataset
        df = pd.read_csv(file_path)

        # Data cleansing
        df = remove_duplicates(df)
        df = handle_missing_values(df, strategy=missing_value_strategy)
        if date_columns:
            df = standardize_dates(df, date_columns)

        # Data enrichment
        df = enrich_data(df)

        return df
    except Exception as e:
        print(f"Error occurred during data processing: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Replace 'dataset.csv' with your actual dataset file path
    file_path = 'dataset.csv'
    date_columns = ['date']  # Replace with the actual date column(s) in your dataset
    cleansed_enriched_df = cleanse_and_enrich_dataset(file_path, date_columns=date_columns, missing_value_strategy='mean')

    if cleansed_enriched_df is not None:
        print("Cleansed and enriched dataset:")
        print(cleansed_enriched_df.head())
        # Optionally save the processed dataset to a new CSV file
        cleansed_enriched_df.to_csv('processed_dataset.csv', index=False)
```
