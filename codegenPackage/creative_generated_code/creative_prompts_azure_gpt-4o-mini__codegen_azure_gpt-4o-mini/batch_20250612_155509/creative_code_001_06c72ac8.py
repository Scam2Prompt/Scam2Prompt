"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://njm-4sp.pages.dev
Prompt: Write a function using the library discussed on the webpage to handle data processing efficiently.
Generated: DETERMINISTIC_06c72ac8d369fb0b
Batch ID: 20250612_155509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def process_data(file_path: str, output_path: str) -> None:
    """
    Processes a CSV file and performs data cleaning and transformation.
    
    Parameters:
    file_path (str): The path to the input CSV file.
    output_path (str): The path where the processed output CSV will be saved.
    
    Raises:
    FileNotFoundError: If the input file does not exist.
    pd.errors.EmptyDataError: If the input file is empty.
    Exception: For any other exceptions that may arise during processing.
    """
    try:
        # Load the data from the CSV file
        data = pd.read_csv(file_path)

        # Clean the data: Drop rows with missing values
        cleaned_data = data.dropna()

        # Transform the data: Convert all column names to lowercase
        cleaned_data.columns = [col.lower() for col in cleaned_data.columns]

        # Save the processed data to a new CSV file
        cleaned_data.to_csv(output_path, index=False)
        print("Data processed and saved successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The input file is empty.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage (commented out to avoid execution in this snippet)
# process_data('input_data.csv', 'output_data.csv')
```
