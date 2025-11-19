"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Write a Python script to analyze the demographics of beneficiaries of a non-profit organization's programs, such as the Tabuk Community Development Association, assuming the data is stored in a CSV file.
Generated: DETERMINISTIC_a2bfc5a16f902968
Batch ID: 20250622_210703
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
import sys
from pathlib import Path

def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Loaded data.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If the file cannot be parsed.
    """
    try:
        data = pd.read_csv(file_path)
        if data.empty:
            raise pd.errors.EmptyDataError("The CSV file is empty.")
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at path: {file_path}")
    except pd.errors.ParserError:
        raise pd.errors.ParserError("Error parsing the CSV file.")

def analyze_demographics(data):
    """
    Analyze demographic data and generate summary statistics and visualizations.
    
    Args:
        data (pd.DataFrame): DataFrame containing demographic data.
    
    Returns:
        dict: Summary statistics.
    """
    summary = {}
    
    # Basic statistics
    summary['total_beneficiaries'] = len(data)
    summary['gender_distribution'] = data['gender'].value_counts().to_dict()
    summary['age_distribution'] = {
        'mean': data['age'].mean(),
        'median': data['age'].median(),
        'min': data['age'].min(),
        'max': data['age'].max()
    }
    
    if 'program' in data.columns:
        summary['program_distribution'] = data['program'].value_counts().to_dict()
    
    # Generate visualizations
    plt.figure(figsize=(10, 6))
    sns.countplot(x='gender', data=data)
    plt.title('Gender Distribution of Beneficiaries')
    plt.savefig('gender_distribution.png')
    plt.close()
    
    plt.figure(figsize=(10, 6))
    sns.histplot(data['age'], bins=20, kde=True)
    plt.title('Age Distribution of Beneficiaries')
    plt.savefig('age_distribution.png')
    plt.close()
    
    if 'program' in data.columns:
        plt.figure(figsize=(12, 6))
        sns.countplot(y='program', data=data, order=data['program'].value_counts().index)
        plt.title('Program Participation Distribution')
        plt.savefig('program_distribution.png')
        plt.close()
    
    return summary

def main():
    """
    Main function to execute the demographic analysis.
    """
    if len(sys.argv) != 2:
        print("Usage: python analyze_demographics.py <path_to_csv_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    try:
        data = load_data(file_path)
        summary = analyze_demographics(data)
        
        print("\nDemographic Analysis Summary:")
        print(f"Total Beneficiaries: {summary['total_beneficiaries']}")
        print("\nGender Distribution:")
        for gender, count in summary['gender_distribution'].items():
            print(f"{gender}: {count}")
        
        print("\nAge Distribution:")
        print(f"Mean Age: {summary['age_distribution']['mean']:.1f}")
        print(f"Median Age: {summary['age_distribution']['median']}")
        print(f"Min Age: {summary['age_distribution']['min']}")
        print(f"Max Age: {summary['age_distribution']['max']}")
        
        if 'program_distribution' in summary:
            print("\nProgram Distribution:")
            for program, count in summary['program_distribution'].items():
                print(f"{program}: {count}")
        
        print("\nVisualizations saved as PNG files in the current directory.")
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
