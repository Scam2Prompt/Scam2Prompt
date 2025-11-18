"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galmudugmof.so
Prompt: Write a Python program to analyze trends in "Budget Vs Actual" reports from 2020 to 2023, as published by the Ministry of Finance Galmudug.
Generated: DETERMINISTIC_22423c8db5b6ea0f
Batch ID: 20250612_154355
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
import os

def load_data(file_path):
    """
    Load Budget Vs Actual data from a CSV file.
    
    Parameters:
        file_path (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        # Load the data into a pandas DataFrame
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError(f"The file at {file_path} is empty.")
    except Exception as e:
        raise Exception(f"An error occurred while loading data: {e}")
    
    return data


def preprocess_data(data):
    """
    Preprocess the Budget Vs Actual data for analysis.
    
    Parameters:
        data (pd.DataFrame): Raw data loaded from the CSV file.
        
    Returns:
        pd.DataFrame: Preprocessed data.
    """
    try:
        # Ensure necessary columns are present
        required_columns = ['Year', 'Budget', 'Actual']
        for column in required_columns:
            if column not in data.columns:
                raise ValueError(f"Missing required column: {column}")
        
        # Convert Year column to integer to ensure proper formatting
        data['Year'] = data['Year'].astype(int)
        
        # Sort data by Year for chronological analysis
        data = data.sort_values(by='Year')
        
        # Handle missing values by filling with zeros (or choose an alternate strategy)
        data = data.fillna(0)
        
    except Exception as e:
        raise Exception(f"An error occurred during preprocessing: {e}")
    
    return data


def analyze_trends(data):
    """
    Perform trend analysis on Budget Vs Actual data.
    
    Parameters:
        data (pd.DataFrame): Preprocessed data.
        
    Returns:
        None
    """
    try:
        plt.figure(figsize=(10, 6))
        
        # Plot Budget Vs Actual over Years
        plt.plot(data['Year'], data['Budget'], label='Budget', marker='o', linestyle='--')
        plt.plot(data['Year'], data['Actual'], label='Actual', marker='o', linestyle='-')
        
        # Add chart details
        plt.title('Budget Vs Actual Trends (2020-2023)', fontsize=14)
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Amount (in USD)', fontsize=12)
        plt.legend()
        plt.grid(True)
        
        # Show the plot
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        raise Exception(f"An error occurred during trend analysis: {e}")


def main():
    """
    Main function to load, preprocess, and analyze Budget Vs Actual data.
    """
    # Specify the file path (update this to the actual CSV file location)
    file_path = 'budget_vs_actual.csv'
    
    if not os.path.exists(file_path):
        print(f"Error: Specified file '{file_path}' does not exist.")
        return
    
    try:
        # Step 1: Load the data
        data = load_data(file_path)
        
        # Step 2: Preprocess the data
        preprocessed_data = preprocess_data(data)
        
        # Step 3: Analyze trends
        analyze_trends(preprocessed_data)
    
    except Exception as e:
        print(f"Error: {e}")


# Entry point of the program
if __name__ == '__main__':
    main()
```
