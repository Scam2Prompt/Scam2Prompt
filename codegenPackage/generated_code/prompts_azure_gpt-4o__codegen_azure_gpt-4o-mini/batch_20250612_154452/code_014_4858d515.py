"""
Generated Code Metadata:
========================
Original URL: https://retinabd.org
Prompt: Create a Python script to visualize enrollment trends and success rates for a coaching center like Retina over the past 45 years.
Generated: DETERMINISTIC_4858d51538d5f5d7
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set the style for seaborn
sns.set(style="whitegrid")

def load_data(file_path):
    """
    Load enrollment and success rate data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing the data.

    Returns:
    pd.DataFrame: A DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
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

def preprocess_data(df):
    """
    Preprocess the data for visualization.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the raw data.

    Returns:
    pd.DataFrame: A DataFrame with processed data.
    """
    # Check if the DataFrame is valid
    if df is None or df.empty:
        raise ValueError("DataFrame is empty or None.")

    # Convert 'Year' to datetime format if necessary
    if 'Year' in df.columns:
        df['Year'] = pd.to_datetime(df['Year'], format='%Y')

    # Fill missing values with the mean of the column
    df.fillna(df.mean(), inplace=True)

    return df

def visualize_data(df):
    """
    Visualize enrollment trends and success rates.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the processed data.
    """
    plt.figure(figsize=(14, 7))

    # Plot enrollment trends
    plt.subplot(2, 1, 1)
    sns.lineplot(data=df, x='Year', y='Enrollment', marker='o', label='Enrollment', color='blue')
    plt.title('Enrollment Trends Over 45 Years')
    plt.xlabel('Year')
    plt.ylabel('Number of Enrollments')
    plt.xticks(rotation=45)
    plt.legend()

    # Plot success rates
    plt.subplot(2, 1, 2)
    sns.lineplot(data=df, x='Year', y='SuccessRate', marker='o', label='Success Rate', color='green')
    plt.title('Success Rates Over 45 Years')
    plt.xlabel('Year')
    plt.ylabel('Success Rate (%)')
    plt.xticks(rotation=45)
    plt.legend()

    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the script.
    """
    # Path to the CSV file containing enrollment and success rate data
    file_path = 'enrollment_data.csv'

    # Load the data
    data = load_data(file_path)

    # Preprocess the data
    try:
        processed_data = preprocess_data(data)

        # Visualize the data
        visualize_data(processed_data)

    except ValueError as ve:
        print(f"ValueError: {ve}")

if __name__ == "__main__":
    main()
```
