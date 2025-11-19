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
import csv
import os
from collections import defaultdict

def load_csv_data(file_path):
    """
    Load data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list[dict]: List of dictionaries representing rows in the CSV file.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is not a valid CSV.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except Exception as e:
        raise ValueError(f"Error reading the CSV file: {e}")

def analyze_demographics(data):
    """
    Analyze demographics from the data.

    Args:
        data (list[dict]): List of dictionaries representing rows in the CSV file.

    Returns:
        dict: Summary of demographic analysis.
    """
    demographics_summary = defaultdict(int)
    
    for row in data:
        # Assuming the CSV has columns like 'Age', 'Gender', 'Region', etc.
        age_group = categorize_age(row.get('Age'))
        gender = row.get('Gender', 'Unknown').strip().capitalize()
        region = row.get('Region', 'Unknown').strip().capitalize()
        
        demographics_summary[f"Age Group: {age_group}"] += 1
        demographics_summary[f"Gender: {gender}"] += 1
        demographics_summary[f"Region: {region}"] += 1
    
    return demographics_summary

def categorize_age(age):
    """
    Categorize age into groups.

    Args:
        age (str): Age as a string.

    Returns:
        str: Age group category.
    """
    try:
        age = int(age)
        if age < 18:
            return "Under 18"
        elif 18 <= age <= 35:
            return "18-35"
        elif 36 <= age <= 60:
            return "36-60"
        else:
            return "60+"
    except (ValueError, TypeError):
        return "Unknown"

def display_summary(summary):
    """
    Display the demographic summary.

    Args:
        summary (dict): Summary of demographic analysis.
    """
    print("Demographic Analysis Summary:")
    print("-" * 30)
    for key, value in summary.items():
        print(f"{key}: {value}")

def main():
    """
    Main function to execute the script.
    """
    # Path to the CSV file
    csv_file_path = 'beneficiaries_data.csv'
    
    try:
        # Load data from the CSV file
        data = load_csv_data(csv_file_path)
        
        # Analyze demographics
        summary = analyze_demographics(data)
        
        # Display the summary
        display_summary(summary)
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except ValueError as val_error:
        print(val_error)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
