"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afco-federation.fr
Prompt: Develop a script to analyze and visualize data related to workplace accidents, focusing on risks like falls from heights and road accidents, as highlighted in AFCO's content.
Generated: DETERMINISTIC_b775952f0da2e54c
Batch ID: 20250612_151739
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
from pathlib import Path

# Function to load data safely
def load_data(file_path):
    """
    Load workplace accident data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: DataFrame containing the data.
    
    Raises:
        FileNotFoundError: If the file is not found.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If there's a parsing error.
    """
    try:
        # Ensure the file exists before proceeding
        if not Path(file_path).is_file():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Load the CSV data
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError as fnf_err:
        print(fnf_err)
        raise
    except pd.errors.EmptyDataError as ede_err:
        print("The file is empty. Please provide a valid CSV file.")
        raise
    except pd.errors.ParserError as parse_err:
        print("Failed to parse the file. Ensure it is in valid CSV format.")
        raise

# Function to preprocess and validate data
def preprocess_data(data):
    """
    Preprocess the workplace accident data.
    
    Args:
        data (pd.DataFrame): Raw data.
    
    Returns:
        pd.DataFrame: Cleaned and validated data.
    """
    # Check required columns exist
    required_columns = ['Date', 'Type', 'Injuries', 'Fatalities']
    for column in required_columns:
        if column not in data.columns:
            raise ValueError(f"Missing required column: {column}")
    
    # Drop rows with missing values in required columns
    data = data.dropna(subset=required_columns)
    
    # Ensure proper data types
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data = data.dropna(subset=['Date'])  # Drop rows with invalid dates
    data['Injuries'] = data['Injuries'].astype(int)
    data['Fatalities'] = data['Fatalities'].astype(int)
    
    return data

# Function to analyze accident data
def analyze_data(data):
    """
    Analyze workplace accident data and return aggregated statistics.
    
    Args:
        data (pd.DataFrame): Cleaned data.
    
    Returns:
        pd.DataFrame: Aggregated statistics by type of accident.
    """
    # Group by type of accident and compute total injuries and fatalities
    summary = data.groupby('Type').agg(
        Total_Injuries=('Injuries', 'sum'),
        Total_Fatalities=('Fatalities', 'sum')
    ).reset_index()
    return summary

# Function to visualize accident data
def visualize_data(summary):
    """
    Visualize workplace accident data using bar plots.
    
    Args:
        summary (pd.DataFrame): Aggregated statistics.
    """
    plt.figure(figsize=(12, 6))
    
    # Injuries bar plot
    sns.barplot(x='Type', y='Total_Injuries', data=summary, palette='Blues_d')
    plt.title('Total Injuries by Type of Accident', fontsize=16)
    plt.xlabel('Type of Accident', fontsize=14)
    plt.ylabel('Total Injuries', fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Fatalities bar plot
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Type', y='Total_Fatalities', data=summary, palette='Reds_d')
    plt.title('Total Fatalities by Type of Accident', fontsize=16)
    plt.xlabel('Type of Accident', fontsize=14)
    plt.ylabel('Total Fatalities', fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main function to orchestrate the workflow
def main():
    """
    Main function to analyze and visualize workplace accident data.
    """
    try:
        # Load the data
        file_path = 'workplace_accidents.csv'  # Replace with your file path
        raw_data = load_data(file_path)
        
        # Preprocess the data
        cleaned_data = preprocess_data(raw_data)
        
        # Analyze the data
        summary = analyze_data(cleaned_data)
        print("Aggregated Statistics:")
        print(summary)
        
        # Visualize the data
        visualize_data(summary)
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point for the script
if __name__ == '__main__':
    main()
```
