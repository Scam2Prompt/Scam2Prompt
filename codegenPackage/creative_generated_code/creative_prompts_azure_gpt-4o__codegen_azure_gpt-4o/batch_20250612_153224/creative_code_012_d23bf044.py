"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elagrocorrentino.com.ar
Prompt: Generate Python code to analyze the economic effects of the intervention in INTA on agricultural productivity, using data from "El Agro Correntino."
Generated: DETERMINISTIC_d23bf044e46aeb32
Batch ID: 20250612_153224
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
import numpy as np

def load_data(file_path):
    """
    Load the dataset from the given file path.
    
    Parameters:
        file_path (str): Path to the dataset file.
        
    Returns:
        pd.DataFrame: Loaded dataset as a DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at the path: {file_path}")
    except pd.errors.EmptyDataError:
        raise ValueError("The file is empty or not readable.")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")


def preprocess_data(data):
    """
    Preprocess the data by handling missing values and filtering necessary columns.
    
    Parameters:
        data (pd.DataFrame): Raw dataset.
    
    Returns:
        pd.DataFrame: Cleaned and preprocessed dataset.
    """
    # Drop rows with missing values
    data = data.dropna()
    
    # Ensure relevant columns are present
    required_columns = ['Year', 'INTA_Intervention', 'Agricultural_Productivity']
    if not set(required_columns).issubset(data.columns):
        raise ValueError(f"Dataset must include the following columns: {required_columns}")
    
    # Filter necessary columns
    data = data[required_columns]
    return data


def analyze_data(data):
    """
    Analyze the relationship between INTA intervention and agricultural productivity.
    
    Parameters:
        data (pd.DataFrame): Preprocessed dataset.
    
    Returns:
        pd.DataFrame: Summary statistics and correlation results.
    """
    try:
        # Compute summary statistics
        summary_stats = data.describe()
        
        # Compute correlation between INTA intervention and agricultural productivity
        correlation = data[['INTA_Intervention', 'Agricultural_Productivity']].corr()
        
        return summary_stats, correlation
    except Exception as e:
        raise RuntimeError(f"Error during analysis: {e}")


def visualize_data(data):
    """
    Generate visualizations for the relationship between INTA intervention and agricultural productivity.
    
    Parameters:
        data (pd.DataFrame): Preprocessed dataset.
    
    Returns:
        None
    """
    try:
        plt.figure(figsize=(10, 6))
        
        # Plot Agricultural Productivity vs Year
        plt.subplot(1, 2, 1)
        plt.plot(data['Year'], data['Agricultural_Productivity'], marker='o', label='Productivity')
        plt.title('Agricultural Productivity Over Time')
        plt.xlabel('Year')
        plt.ylabel('Productivity')
        plt.legend()
        
        # Scatter plot for INTA Intervention vs Agricultural Productivity
        plt.subplot(1, 2, 2)
        plt.scatter(data['INTA_Intervention'], data['Agricultural_Productivity'], alpha=0.7)
        plt.title('INTA Intervention vs Agricultural Productivity')
        plt.xlabel('INTA Intervention')
        plt.ylabel('Productivity')
        
        plt.tight_layout()
        plt.show()
    except Exception as e:
        raise RuntimeError(f"Error during visualization: {e}")


def main():
    """
    Main function to execute data analysis workflow.
    
    Returns:
        None
    """
    # Define the path to the dataset
    file_path = "El_Agro_Correntino.csv"
    
    try:
        # Load and preprocess data
        raw_data = load_data(file_path)
        clean_data = preprocess_data(raw_data)
        
        # Analyze the data
        summary_stats, correlation = analyze_data(clean_data)
        
        # Display analysis results
        print("Summary Statistics:")
        print(summary_stats)
        print("\nCorrelation between INTA Intervention and Agricultural Productivity:")
        print(correlation)
        
        # Visualize the data
        visualize_data(clean_data)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
