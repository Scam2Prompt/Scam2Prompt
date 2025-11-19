"""
Generated Code Metadata:
========================
Original URL: https://sardagnapoeta.com.br
Prompt: Create a script in Python to analyze legal case data related to crimes under the Lei de Drogas (drug trafficking law) and generate statistical reports.
Generated: DETERMINISTIC_28c6f175e2b92325
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# lei_de_drogas_analysis.py

import pandas as pd
import numpy as np
from collections import defaultdict
from datetime import datetime

def load_data(file_path):
    """
    Load legal case data from a CSV file.

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
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File '{file_path}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: File '{file_path}' is malformed.")
        return None

def preprocess_data(data):
    """
    Preprocess the data by handling missing values and converting data types.

    Args:
        data (pd.DataFrame): Loaded data.

    Returns:
        pd.DataFrame: Preprocessed data.
    """
    # Handle missing values
    data.fillna({'crime_type': 'Unknown', 'sentence': 0}, inplace=True)

    # Convert data types
    data['date'] = pd.to_datetime(data['date'], errors='coerce')
    data['sentence'] = pd.to_numeric(data['sentence'], errors='coerce')

    return data

def generate_statistics(data):
    """
    Generate statistical reports.

    Args:
        data (pd.DataFrame): Preprocessed data.

    Returns:
        dict: Statistical reports.
    """
    reports = {}

    # Crime type distribution
    crime_types = data['crime_type'].value_counts().to_dict()
    reports['crime_type_distribution'] = crime_types

    # Average sentence by crime type
    avg_sentences = data.groupby('crime_type')['sentence'].mean().to_dict()
    reports['avg_sentence_by_crime_type'] = avg_sentences

    # Total cases by year
    data['year'] = data['date'].dt.year
    total_cases_by_year = data['year'].value_counts().to_dict()
    reports['total_cases_by_year'] = total_cases_by_year

    # Top 5 cities with most cases
    top_cities = data['city'].value_counts().head(5).to_dict()
    reports['top_cities'] = top_cities

    return reports

def save_reports(reports, output_file):
    """
    Save statistical reports to a JSON file.

    Args:
        reports (dict): Statistical reports.
        output_file (str): Path to the output JSON file.

    Raises:
        Exception: If an error occurs while saving the reports.
    """
    try:
        with open(output_file, 'w') as f:
            import json
            json.dump(reports, f, indent=4)
    except Exception as e:
        print(f"Error: Failed to save reports to '{output_file}': {str(e)}")

def main():
    file_path = 'lei_de_drogas_data.csv'  # replace with your data file
    output_file = 'lei_de_drogas_reports.json'

    data = load_data(file_path)
    if data is not None:
        data = preprocess_data(data)
        reports = generate_statistics(data)
        save_reports(reports, output_file)
        print("Statistical reports generated and saved successfully.")

if __name__ == "__main__":
    main()
```
