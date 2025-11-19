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
    Load the CSV data into a pandas DataFrame.

    :param file_path: str - Path to the CSV file
    :return: DataFrame - Loaded data
    :raises FileNotFoundError: If the file does not exist
    :raises pd.errors.EmptyDataError: If the file is empty
    :raises pd.errors.ParserError: If the file cannot be parsed
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError as e:
        print(f"Error: The file {file_path} was not found.")
        raise e
    except pd.errors.EmptyDataError as e:
        print("Error: The file is empty.")
        raise e
    except pd.errors.ParserError as e:
        print("Error: The file could not be parsed.")
        raise e

def analyze_demographics(data):
    """
    Analyze the demographics of beneficiaries.

    :param data: DataFrame - The data containing beneficiary information
    :return: dict - Summary statistics of demographics
    """
    demographics_summary = {
        'total_beneficiaries': len(data),
        'age_distribution': data['age'].value_counts().to_dict(),
        'gender_distribution': data['gender'].value_counts().to_dict(),
        'location_distribution': data['location'].value_counts().to_dict(),
    }
    return demographics_summary

def main(file_path):
    """
    Main function to load data and analyze demographics.

    :param file_path: str - Path to the CSV file
    """
    # Load the data
    data = load_data(file_path)

    # Analyze demographics
    demographics_summary = analyze_demographics(data)

    # Print the summary
    print("Demographics Summary:")
    for key, value in demographics_summary.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    # Specify the path to the CSV file
    csv_file_path = 'beneficiaries_data.csv'
    
    # Run the main function
    main(csv_file_path)
```
