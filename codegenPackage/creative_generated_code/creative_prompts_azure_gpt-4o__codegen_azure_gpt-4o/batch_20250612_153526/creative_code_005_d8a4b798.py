"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gapkindo.org
Prompt: Suggest a library for processing and visualizing the natural rubber statistics provided by GAPKINDO, and demonstrate its usage with example code.
Generated: DETERMINISTIC_d8a4b798e272dfee
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python Script for Processing and Visualizing Natural Rubber Statistics Using pandas and matplotlib

This example demonstrates the use of pandas for data manipulation and matplotlib for data visualization.
Ensure the necessary libraries are installed before running the script:
    pip install pandas matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt

def process_and_visualize_rubber_statistics(file_path):
    """
    Reads, processes, and visualizes natural rubber statistics.

    :param file_path: str, path to the CSV file containing natural rubber statistics.
    """
    try:
        # Load the dataset into a pandas DataFrame
        data = pd.read_csv(file_path)

        # Check if necessary columns exist
        required_columns = ['Year', 'Production', 'Export']
        if not all(col in data.columns for col in required_columns):
            raise ValueError(f"The input file must contain the following columns: {', '.join(required_columns)}")

        # Display basic information about the dataset
        print("Dataset Info:")
        print(data.info())
        print("\nFirst Few Rows:")
        print(data.head())

        # Handle missing values (if any)
        data = data.dropna(subset=required_columns)  # Drop rows with missing values in required columns

        # Sort the data by year (optional step for better visualization)
        data = data.sort_values(by='Year')

        # Visualize the statistics
        plt.figure(figsize=(10, 6))
        plt.plot(data['Year'], data['Production'], label='Production (in tons)', marker='o')
        plt.plot(data['Year'], data['Export'], label='Export (in tons)', marker='o')
        plt.title('Natural Rubber Statistics Over Time', fontsize=16)
        plt.xlabel('Year', fontsize=14)
        plt.ylabel('Rubber Quantity (tons)', fontsize=14)
        plt.legend()
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
# Replace 'rubber_statistics.csv' with the actual path to your CSV file
# Ensure the CSV file contains columns: 'Year', 'Production', 'Export'
process_and_visualize_rubber_statistics('rubber_statistics.csv')
```
