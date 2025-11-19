"""
Generated Code Metadata:
========================
Original URL: https://uni4kashmir.com
Prompt: Write a Python script that analyzes data related to student enrollment in emerging fields such as Artificial Intelligence and Cybersecurity at a university like Uni4Kashmir.
Generated: DETERMINISTIC_c2cc0b236f373867
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# student_enrollment_analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_enrollment_data(file_path: str) -> pd.DataFrame:
    """
    Load student enrollment data from a CSV file.

    Args:
    - file_path (str): Path to the CSV file containing enrollment data.

    Returns:
    - pd.DataFrame: A DataFrame containing the enrollment data.
    """
    try:
        # Load data from CSV file
        data = pd.read_csv(file_path)

        # Validate required columns
        required_columns = ['Student ID', 'Field of Study', 'Enrollment Date', 'Program']
        if not all(column in data.columns for column in required_columns):
            raise ValueError("The CSV file is missing required columns.")

        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty.")
        return None
    except pd.errors.ParserError as e:
        print(f"Error: Failed to parse the file '{file_path}'. {e}")
        return None

def analyze_enrollment_data(data: pd.DataFrame) -> dict:
    """
    Analyze student enrollment data.

    Args:
    - data (pd.DataFrame): A DataFrame containing the enrollment data.

    Returns:
    - dict: A dictionary containing analysis results.
    """
    # Filter data for emerging fields
    emerging_fields = ['Artificial Intelligence', 'Cybersecurity']
    emerging_fields_data = data[data['Field of Study'].isin(emerging_fields)]

    # Calculate total enrollments in emerging fields
    total_enrollments = emerging_fields_data.shape[0]

    # Calculate enrollments by field
    enrollments_by_field = emerging_fields_data['Field of Study'].value_counts().to_dict()

    # Calculate enrollments by program
    enrollments_by_program = emerging_fields_data['Program'].value_counts().to_dict()

    # Calculate average enrollment per month
    emerging_fields_data['Enrollment Date'] = pd.to_datetime(emerging_fields_data['Enrollment Date'])
    enrollments_per_month = emerging_fields_data.groupby(pd.Grouper(key='Enrollment Date', freq='M'))['Student ID'].count().mean()

    analysis_results = {
        'total_enrollments': total_enrollments,
        'enrollments_by_field': enrollments_by_field,
        'enrollments_by_program': enrollments_by_program,
        'enrollments_per_month': enrollments_per_month
    }

    return analysis_results

def visualize_enrollment_data(data: pd.DataFrame) -> None:
    """
    Visualize student enrollment data.

    Args:
    - data (pd.DataFrame): A DataFrame containing the enrollment data.
    """
    # Filter data for emerging fields
    emerging_fields = ['Artificial Intelligence', 'Cybersecurity']
    emerging_fields_data = data[data['Field of Study'].isin(emerging_fields)]

    # Plot enrollments by field
    enrollments_by_field = emerging_fields_data['Field of Study'].value_counts()
    plt.figure(figsize=(8, 6))
    plt.bar(enrollments_by_field.index, enrollments_by_field.values)
    plt.xlabel('Field of Study')
    plt.ylabel('Number of Enrollments')
    plt.title('Enrollments by Field')
    plt.show()

def main() -> None:
    file_path = 'enrollment_data.csv'  # Update with your file path
    data = load_enrollment_data(file_path)

    if data is not None:
        analysis_results = analyze_enrollment_data(data)
        print("Analysis Results:")
        print(f"Total Enrollments: {analysis_results['total_enrollments']}")
        print("Enrollments by Field:")
        for field, count in analysis_results['enrollments_by_field'].items():
            print(f"- {field}: {count}")
        print("Enrollments by Program:")
        for program, count in analysis_results['enrollments_by_program'].items():
            print(f"- {program}: {count}")
        print(f"Average Enrollment per Month: {analysis_results['enrollments_per_month']:.2f}")

        visualize_enrollment_data(data)

if __name__ == "__main__":
    main()
```
