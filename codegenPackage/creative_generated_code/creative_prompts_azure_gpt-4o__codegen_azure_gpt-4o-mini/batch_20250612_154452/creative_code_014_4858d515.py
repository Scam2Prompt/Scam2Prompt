"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retinabd.org
Prompt: Create a Python script to visualize enrollment trends and success rates for a coaching center like Retina over the past 45 years.
Generated: DETERMINISTIC_4858d51538d5f5d7
Batch ID: 20250612_154452
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
import seaborn as sns
from datetime import datetime
import numpy as np

# Set the style for the plots
sns.set(style="whitegrid")

def load_data(file_path):
    """
    Load enrollment data from a CSV file.
    
    Args:
        file_path (str): The path to the CSV file containing enrollment data.
        
    Returns:
        DataFrame: A pandas DataFrame containing the enrollment data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        raise
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        raise
    except pd.errors.ParserError:
        print("Error: There was a parsing error with the file.")
        raise

def preprocess_data(data):
    """
    Preprocess the enrollment data to extract relevant information.
    
    Args:
        data (DataFrame): The raw enrollment data.
        
    Returns:
        DataFrame: A cleaned DataFrame with the necessary information for analysis.
    """
    # Assuming the DataFrame has columns 'Year', 'Enrollments', 'SuccessRate'
    data['Year'] = pd.to_datetime(data['Year'], format='%Y', errors='coerce').dt.year
    data = data.dropna(subset=['Year', 'Enrollments', 'SuccessRate'])
    return data

def plot_enrollment_trends(data):
    """
    Plot enrollment trends over the years.
    
    Args:
        data (DataFrame): The cleaned DataFrame containing enrollment data.
    """
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=data, x='Year', y='Enrollments', marker='o')
    plt.title('Enrollment Trends Over the Last 45 Years', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Number of Enrollments', fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_success_rates(data):
    """
    Plot success rates over the years.
    
    Args:
        data (DataFrame): The cleaned DataFrame containing enrollment data.
    """
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=data, x='Year', y='SuccessRate', marker='o', color='orange')
    plt.title('Success Rates Over the Last 45 Years', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Success Rate (%)', fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to load data, preprocess it, and visualize trends.
    """
    file_path = 'enrollment_data.csv'  # Replace with your data file path
    try:
        raw_data = load_data(file_path)
        cleaned_data = preprocess_data(raw_data)
        plot_enrollment_trends(cleaned_data)
        plot_success_rates(cleaned_data)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
```
