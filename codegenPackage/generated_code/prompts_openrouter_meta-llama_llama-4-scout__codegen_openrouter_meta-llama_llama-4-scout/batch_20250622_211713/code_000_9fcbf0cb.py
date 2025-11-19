"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Write a Python script to analyze the selection process for professor positions at the Instituto de Geografia, Universidade do Estado do Rio de Janeiro (UERJ), including calculating the number of applicants and interviewees for each position.
Generated: DETERMINISTIC_9fcbf0cb94a38c9b
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Instituto de Geografia, UERJ Professor Position Selection Process Analyzer

This script analyzes the selection process for professor positions at the Instituto de Geografia, 
Universidade do Estado do Rio de Janeiro (UERJ), including calculating the number of applicants 
and interviewees for each position.

Author: [Your Name]
Date: [Today's Date]
"""

import pandas as pd

def load_data(file_path):
    """
    Loads selection process data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing the data.

    Returns:
        pd.DataFrame: A DataFrame containing the selection process data.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If an error occurs while parsing the file.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty.")
        return None
    except pd.errors.ParserError as e:
        print(f"Error: An error occurred while parsing the file '{file_path}': {e}")
        return None

def analyze_selection_process(data):
    """
    Analyzes the selection process data and calculates the number of applicants and interviewees for each position.

    Args:
        data (pd.DataFrame): A DataFrame containing the selection process data.

    Returns:
        dict: A dictionary containing the number of applicants and interviewees for each position.
    """
    # Assuming the data has columns 'position', 'applicant', and 'interviewed'
    # Adjust column names as necessary
    required_columns = ['position', 'applicant', 'interviewed']
    if not all(column in data.columns for column in required_columns):
        print("Error: The data is missing required columns.")
        return None

    # Group by position and calculate the number of applicants and interviewees
    applicants = data['position'].value_counts().to_dict()
    interviewees = data[data['interviewed'] == True]['position'].value_counts().to_dict()

    # Initialize a dictionary to store the results
    results = {}

    # Iterate over unique positions
    for position in applicants:
        results[position] = {
            'applicants': applicants[position],
            'interviewees': interviewees.get(position, 0)
        }

    return results

def main():
    file_path = 'selection_process_data.csv'  # Update with your file path
    data = load_data(file_path)

    if data is not None:
        results = analyze_selection_process(data)
        if results is not None:
            for position, metrics in results.items():
                print(f"Position: {position}")
                print(f"Applicants: {metrics['applicants']}")
                print(f"Interviewees: {metrics['interviewees']}")
                print(f"Ratio: {metrics['interviewees'] / metrics['applicants'] * 100 if metrics['applicants'] > 0 else 0:.2f}%")
                print("------------------------")

if __name__ == "__main__":
    main()
```
