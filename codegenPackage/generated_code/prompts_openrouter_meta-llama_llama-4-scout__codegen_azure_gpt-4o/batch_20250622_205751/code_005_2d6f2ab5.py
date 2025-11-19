"""
Generated Code Metadata:
========================
Original URL: https://creocollective.io
Prompt: "Write a Python script to analyze marketing campaign data from various channels, including social media, email, and lead generation, using libraries like Pandas and NumPy."
Generated: DETERMINISTIC_2d6f2ab596342594
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np

def load_data(file_path):
    """
    Load marketing campaign data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def clean_data(data):
    """
    Clean the marketing campaign data.

    Args:
        data (pd.DataFrame): Raw data.

    Returns:
        pd.DataFrame: Cleaned data.
    """
    if data is None or data.empty:
        print("Error: No data to clean.")
        return None

    # Drop rows with missing values
    data = data.dropna()

    # Remove duplicate rows
    data = data.drop_duplicates()

    # Ensure numeric columns are properly formatted
    numeric_columns = ['Spend', 'Clicks', 'Conversions']
    for col in numeric_columns:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors='coerce')

    # Drop rows with invalid numeric values
    data = data.dropna(subset=numeric_columns)

    return data


def analyze_data(data):
    """
    Analyze the marketing campaign data.

    Args:
        data (pd.DataFrame): Cleaned data.

    Returns:
        dict: Dictionary containing analysis results.
    """
    if data is None or data.empty:
        print("Error: No data to analyze.")
        return None

    analysis_results = {}

    # Calculate total spend per channel
    if 'Channel' in data.columns and 'Spend' in data.columns:
        analysis_results['Total Spend by Channel'] = data.groupby('Channel')['Spend'].sum().to_dict()

    # Calculate average cost per click (CPC) per channel
    if 'Channel' in data.columns and 'Spend' in data.columns and 'Clicks' in data.columns:
        data['CPC'] = data['Spend'] / data['Clicks']
        analysis_results['Average CPC by Channel'] = data.groupby('Channel')['CPC'].mean().to_dict()

    # Calculate conversion rate per channel
    if 'Channel' in data.columns and 'Conversions' in data.columns and 'Clicks' in data.columns:
        data['Conversion Rate'] = (data['Conversions'] / data['Clicks']) * 100
        analysis_results['Conversion Rate by Channel'] = data.groupby('Channel')['Conversion Rate'].mean().to_dict()

    return analysis_results


def main():
    """
    Main function to execute the script.
    """
    # File path to the marketing campaign data
    file_path = 'marketing_campaign_data.csv'

    # Load the data
    raw_data = load_data(file_path)

    # Clean the data
    cleaned_data = clean_data(raw_data)

    # Analyze the data
    analysis_results = analyze_data(cleaned_data)

    # Display the analysis results
    if analysis_results:
        print("Marketing Campaign Analysis Results:")
        for key, value in analysis_results.items():
            print(f"{key}:")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key}: {sub_value:.2f}")


if __name__ == "__main__":
    main()
```
