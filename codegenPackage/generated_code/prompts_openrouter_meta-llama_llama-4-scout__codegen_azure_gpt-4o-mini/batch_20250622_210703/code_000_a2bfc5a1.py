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

def load_data(file_path):
    """
    Load demographic data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    DataFrame: A pandas DataFrame containing the loaded data.
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
        print("Error: There was a problem parsing the file.")
        return None

def analyze_demographics(data):
    """
    Analyze the demographics of beneficiaries.

    Parameters:
    data (DataFrame): A pandas DataFrame containing demographic data.

    Returns:
    dict: A dictionary containing demographic analysis results.
    """
    if data is None or data.empty:
        return {}

    analysis_results = {
        'total_beneficiaries': len(data),
        'age_distribution': data['age'].value_counts().to_dict(),
        'gender_distribution': data['gender'].value_counts().to_dict(),
        'location_distribution': data['location'].value_counts().to_dict(),
    }
    
    return analysis_results

def main():
    """
    Main function to execute the demographic analysis.
    """
    file_path = 'beneficiaries_data.csv'  # Path to the CSV file
    data = load_data(file_path)

    if data is not None:
        results = analyze_demographics(data)
        print("Demographic Analysis Results:")
        print(results)

if __name__ == "__main__":
    main()
```
