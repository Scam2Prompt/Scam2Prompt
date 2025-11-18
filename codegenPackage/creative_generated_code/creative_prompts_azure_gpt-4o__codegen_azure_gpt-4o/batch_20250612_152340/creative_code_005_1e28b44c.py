"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.stcinversiones.com.ar
Prompt: Develop a Python script to analyze historical data from BYMA and MATba-Rofex for designing personalized investment strategies, as STC Inversiones specializes in.
Generated: DETERMINISTIC_1e28b44ccd2d387e
Batch ID: 20250612_152340
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
import os

# Custom exception class for error handling
class DataLoadingError(Exception):
    pass

def load_data(file_path):
    """
    Load historical data from CSV file into a pandas DataFrame.

    Parameters:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data as a DataFrame.

    Raises:
        DataLoadingError: If the file cannot be loaded due to missing file or incorrect format.
    """
    if not os.path.exists(file_path):
        raise DataLoadingError(f"File not found: {file_path}")
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        raise DataLoadingError(f"Error loading data: {e}")

def preprocess_data(data):
    """
    Preprocess historical data for analysis.

    Parameters:
        data (pd.DataFrame): Raw historical data.

    Returns:
        pd.DataFrame: Preprocessed data with necessary adjustments.
    """
    # Ensure necessary columns are present
    required_columns = ['Date', 'Price', 'Volume']
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        raise ValueError(f"Missing columns in data: {missing_columns}")
    
    # Convert 'Date' column to datetime
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data = data.dropna(subset=['Date'])  # Remove rows with invalid dates
    
    # Sort data by date
    data = data.sort_values('Date')
    
    # Fill missing values (if any)
    data['Price'] = data['Price'].fillna(method='ffill')
    data['Volume'] = data['Volume'].fillna(0)  # Assume missing volumes are 0
    
    return data

def analyze_data(data):
    """
    Perform basic analysis on historical data.

    Parameters:
        data (pd.DataFrame): Preprocessed historical data.

    Returns:
        dict: Analysis results including statistics and trends.
    """
    analysis_results = {}
    
    # Compute basic statistics
    analysis_results['mean_price'] = data['Price'].mean()
    analysis_results['max_price'] = data['Price'].max()
    analysis_results['min_price'] = data['Price'].min()
    analysis_results['total_volume'] = data['Volume'].sum()
    
    # Detect price trends (simple moving average as an example)
    data['SMA_20'] = data['Price'].rolling(window=20).mean()
    data['SMA_50'] = data['Price'].rolling(window=50).mean()
    
    # Add trends to results
    analysis_results['latest_sma_20'] = data['SMA_20'].iloc[-1]
    analysis_results['latest_sma_50'] = data['SMA_50'].iloc[-1]
    
    return analysis_results

def plot_data(data):
    """
    Plot historical data with trends.

    Parameters:
        data (pd.DataFrame): Preprocessed historical data.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Price'], label='Price', alpha=0.7)
    plt.plot(data['Date'], data['SMA_20'], label='20-day SMA', linestyle='--', alpha=0.8)
    plt.plot(data['Date'], data['SMA_50'], label='50-day SMA', linestyle='--', alpha=0.8)
    
    plt.title('Historical Price Analysis')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    """
    Main function to load, preprocess, analyze, and visualize data.
    """
    # Paths to the CSV files for BYMA and MATba-Rofex data
    byma_file_path = 'byma_data.csv'
    matba_file_path = 'matba_data.csv'
    
    try:
        # Load datasets
        byma_data = load_data(byma_file_path)
        matba_data = load_data(matba_file_path)
        
        # Preprocess datasets
        byma_data = preprocess_data(byma_data)
        matba_data = preprocess_data(matba_data)
        
        # Analyze datasets
        byma_analysis = analyze_data(byma_data)
        matba_analysis = analyze_data(matba_data)
        
        # Display analysis results
        print("BYMA Analysis Results:")
        print(byma_analysis)
        print("\nMATba-Rofex Analysis Results:")
        print(matba_analysis)
        
        # Plot data
        print("\nPlotting BYMA Data...")
        plot_data(byma_data)
        print("\nPlotting MATba-Rofex Data...")
        plot_data(matba_data)
    
    except DataLoadingError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
