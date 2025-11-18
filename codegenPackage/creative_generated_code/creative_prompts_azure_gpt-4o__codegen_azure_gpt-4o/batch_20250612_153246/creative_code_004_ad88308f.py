"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalinski-energia.pl
Prompt: Generate code to automate energy consumption analysis for enterprises, using Python and Excel, based on the solutions provided by Jacek Kaliński.
Generated: DETERMINISTIC_ad88308f168fcafc
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import os

def load_energy_data(file_path):
    """
    Load energy consumption data from an Excel file.
    
    Args:
        file_path (str): Path to the Excel file containing energy data.
    
    Returns:
        pd.DataFrame: DataFrame containing energy consumption data.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file cannot be read as an Excel file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    
    try:
        data = pd.read_excel(file_path)
    except Exception as e:
        raise ValueError(f"Error reading Excel file: {e}")
    
    return data


def analyze_energy_consumption(data):
    """
    Analyze energy consumption data for enterprises.
    
    Args:
        data (pd.DataFrame): DataFrame containing energy consumption data.
    
    Returns:
        dict: Dictionary containing analysis results (e.g., total, average, peak usage).
    """
    if 'Consumption' not in data.columns:
        raise ValueError("The required column 'Consumption' is missing in the data.")
    
    analysis_results = {
        'Total Consumption': data['Consumption'].sum(),
        'Average Consumption': data['Consumption'].mean(),
        'Peak Consumption': data['Consumption'].max(),
        'Peak Consumption Time': data.loc[data['Consumption'].idxmax(), 'Time'] if 'Time' in data.columns else None
    }
    
    return analysis_results


def save_analysis_results(results, output_file):
    """
    Save energy consumption analysis results to an Excel file.
    
    Args:
        results (dict): Dictionary containing analysis results.
        output_file (str): Path to save the output Excel file.
    """
    result_df = pd.DataFrame.from_dict(results, orient='index', columns=['Value'])
    
    try:
        result_df.to_excel(output_file, index=True)
        print(f"Analysis results saved successfully to {output_file}")
    except Exception as e:
        print(f"Error saving results to Excel file: {e}")


if __name__ == "__main__":
    # File paths
    input_file = "energy_data.xlsx"  # Path to the input Excel file
    output_file = "analysis_results.xlsx"  # Path to save the analysis results

    try:
        # Load energy data
        energy_data = load_energy_data(input_file)
        
        # Perform energy consumption analysis
        analysis_results = analyze_energy_consumption(energy_data)
        
        # Save the analysis results
        save_analysis_results(analysis_results, output_file)
        
    except Exception as error:
        print(f"An error occurred: {error}")
```
