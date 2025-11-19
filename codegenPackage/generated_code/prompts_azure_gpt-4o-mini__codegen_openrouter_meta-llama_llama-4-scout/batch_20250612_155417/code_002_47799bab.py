"""
Generated Code Metadata:
========================
Original URL: https://45ybook.ueh.edu.vn
Prompt: Write a Python script that analyzes data on multi-disciplinary programs in universities, inspired by the themes in the UEH publication.
Generated: DETERMINISTIC_47799bab94aa44db
Batch ID: 20250612_155417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# multi_disciplinary_programs.py

import pandas as pd
import numpy as np

def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads data from a CSV file.

    Args:
    - file_path (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: Loaded data.

    Raises:
    - FileNotFoundError: If the file does not exist.
    - pd.errors.EmptyDataError: If the file is empty.
    - pd.errors.ParserError: If there is an error parsing the file.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"File is empty: {file_path}")
        return None
    except pd.errors.ParserError as e:
        print(f"Error parsing file: {file_path} - {e}")
        return None

def analyze_programs(data: pd.DataFrame) -> dict:
    """
    Analyzes data on multi-disciplinary programs in universities.

    Args:
    - data (pd.DataFrame): Data to analyze.

    Returns:
    - dict: Analysis results.
    """
    # Check if required columns exist
    required_columns = ['University', 'Program', 'Disciplines']
    if not all(col in data.columns for col in required_columns):
        raise ValueError("Data is missing required columns")

    # Group programs by university and count the number of programs
    university_program_counts = data.groupby('University')['Program'].count().to_dict()

    # Group programs by discipline and count the number of programs
    discipline_program_counts = data['Disciplines'].explode().value_counts().to_dict()

    # Calculate the average number of disciplines per program
    avg_disciplines_per_program = data['Disciplines'].apply(lambda x: len(x)).mean()

    analysis_results = {
        'university_program_counts': university_program_counts,
        'discipline_program_counts': discipline_program_counts,
        'avg_disciplines_per_program': avg_disciplines_per_program
    }

    return analysis_results

def save_results(results: dict, output_file: str) -> None:
    """
    Saves analysis results to a JSON file.

    Args:
    - results (dict): Analysis results.
    - output_file (str): Path to the output JSON file.
    """
    import json
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)

def main() -> None:
    data_file = 'ueh_publication_data.csv'  # replace with actual file path
    output_file = 'analysis_results.json'

    data = load_data(data_file)
    if data is not None:
        results = analyze_programs(data)
        save_results(results, output_file)
        print("Analysis complete. Results saved to", output_file)

if __name__ == '__main__':
    main()
```
