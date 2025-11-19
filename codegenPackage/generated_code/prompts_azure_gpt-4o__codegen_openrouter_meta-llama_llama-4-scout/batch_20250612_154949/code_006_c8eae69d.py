"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Develop a script to visualize ROI trends for training programs, using insights from Romain Rissoan's consulting practices.
Generated: DETERMINISTIC_c8eae69d63f77422
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_training_data(file_path):
    """
    Load training program data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Training program data.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If the file is malformed.
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
    except pd.errors.ParserError:
        print(f"Error parsing file: {file_path}")
        return None

def calculate_roi(data):
    """
    Calculate ROI for each training program.

    Args:
        data (pd.DataFrame): Training program data.

    Returns:
        pd.DataFrame: Training program data with ROI column.

    Raises:
        ValueError: If required columns are missing.
    """
    required_columns = ['program_name', 'cost', 'revenue']
    if not all(col in data.columns for col in required_columns):
        raise ValueError("Missing required columns")

    data['roi'] = (data['revenue'] - data['cost']) / data['cost']
    return data

def visualize_roi_trends(data):
    """
    Visualize ROI trends for training programs.

    Args:
        data (pd.DataFrame): Training program data with ROI column.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(data['program_name'], data['roi'])
    plt.xlabel('Program Name')
    plt.ylabel('ROI')
    plt.title('ROI Trends for Training Programs')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def main():
    file_path = 'training_data.csv'  # Replace with actual file path
    data = load_training_data(file_path)
    if data is not None:
        data = calculate_roi(data)
        visualize_roi_trends(data)

if __name__ == "__main__":
    main()
```
