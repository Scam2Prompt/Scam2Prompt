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
    Load beneficiary data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If the file is malformed.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: Failed to parse the file '{file_path}'.")
        return None

def analyze_demographics(data):
    """
    Analyze the demographics of beneficiaries.

    Args:
        data (pd.DataFrame): Beneficiary data.

    Returns:
        dict: Demographic analysis results.
    """
    # Ensure required columns exist
    required_columns = ['age', 'gender', 'location']
    if not all(column in data.columns for column in required_columns):
        print("Error: The data is missing required columns.")
        return None

    # Calculate age distribution
    age_distribution = data['age'].value_counts(bins=[0, 18, 25, 35, 45, 55, 100])

    # Calculate gender distribution
    gender_distribution = data['gender'].value_counts()

    # Calculate location distribution
    location_distribution = data['location'].value_counts()

    return {
        'age_distribution': age_distribution,
        'gender_distribution': gender_distribution,
        'location_distribution': location_distribution
    }

def print_results(results):
    """
    Print demographic analysis results.

    Args:
        results (dict): Demographic analysis results.
    """
    if results is not None:
        print("Age Distribution:")
        print(results['age_distribution'])
        print("\nGender Distribution:")
        print(results['gender_distribution'])
        print("\nLocation Distribution:")
        print(results['location_distribution'])

def main():
    file_path = 'beneficiaries.csv'  # Replace with your CSV file path
    data = load_data(file_path)
    if data is not None:
        results = analyze_demographics(data)
        print_results(results)

if __name__ == "__main__":
    main()
```
