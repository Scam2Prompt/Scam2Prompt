"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pdma.io
Prompt: Develop a data analysis pipeline in Python using techniques from PDMA's Data Analysis training, including data cleaning and visualization.
Generated: DETERMINISTIC_3ed63e00b87d54be
Batch ID: 20250612_145730
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
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """
    Load data from a CSV file into a Pandas DataFrame.
    
    Args:
        file_path (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError as e:
        print(f"Error: File not found at {file_path}. Exception: {e}")
        return None
    except pd.errors.ParserError as e:
        print(f"Error: Failed to parse file at {file_path}. Exception: {e}")
        return None

def clean_data(df):
    """
    Perform data cleaning operations on the DataFrame.
    
    Args:
        df (pd.DataFrame): The input DataFrame.
        
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    # Remove duplicate rows
    df = df.drop_duplicates()
    
    # Handle missing values
    df = df.fillna(method='ffill').fillna(method='bfill')  # Forward and backward fill
    
    # Drop columns with too many missing values (e.g., > 50%)
    threshold = 0.5
    df = df.dropna(axis=1, thresh=int(threshold * len(df)))
    
    # Rename columns to ensure consistency
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    
    return df

def generate_summary_statistics(df):
    """
    Generate and print summary statistics for the DataFrame.
    
    Args:
        df (pd.DataFrame): The input DataFrame.
    """
    print("Summary Statistics:")
    print(df.describe())
    print("\nMissing Values per Column:")
    print(df.isnull().sum())

def visualize_data(df, columns):
    """
    Generate basic visualizations for specified columns of the DataFrame.
    
    Args:
        df (pd.DataFrame): The input DataFrame.
        columns (list): List of columns to visualize.
    """
    for col in columns:
        if df[col].dtype in [np.int64, np.float64]:
            plt.figure(figsize=(10, 6))
            sns.histplot(df[col], kde=True, bins=30)
            plt.title(f'Distribution of {col}')
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.show()
        else:
            plt.figure(figsize=(10, 6))
            sns.countplot(y=df[col], order=df[col].value_counts().index)
            plt.title(f'Count Plot of {col}')
            plt.xlabel('Frequency')
            plt.ylabel(col)
            plt.show()

def run_analysis_pipeline(file_path, visualization_columns=None):
    """
    Run the complete data analysis pipeline.
    
    Args:
        file_path (str): Path to the CSV file.
        visualization_columns (list): Columns to visualize. If None, no visualization is performed.
    """
    print("Loading data...")
    df = load_data(file_path)
    if df is None:
        return
    
    print("Cleaning data...")
    df = clean_data(df)
    
    print("Generating summary statistics...")
    generate_summary_statistics(df)
    
    if visualization_columns:
        print("Visualizing data...")
        visualize_data(df, visualization_columns)

# Example usage of the pipeline
if __name__ == "__main__":
    # Replace 'your_file.csv' with the path to your data file
    file_path = 'your_file.csv'
    
    # Specify columns to visualize (replace with actual column names in your data)
    visualization_columns = ['column1', 'column2']
    
    run_analysis_pipeline(file_path, visualization_columns)
```
