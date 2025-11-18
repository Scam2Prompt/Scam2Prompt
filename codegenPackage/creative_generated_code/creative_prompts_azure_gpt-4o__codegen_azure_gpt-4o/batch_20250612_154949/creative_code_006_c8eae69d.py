"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://romain-rissoan.fr
Prompt: Develop a script to visualize ROI trends for training programs, using insights from Romain Rissoan's consulting practices.
Generated: DETERMINISTIC_c8eae69d63f77422
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define a function to read and validate data
def load_data(file_path):
    """
    Load data from a CSV file and validate its structure.

    Args:
        file_path (str): Path to the CSV file containing ROI data.

    Returns:
        pd.DataFrame: A cleaned DataFrame containing ROI data.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file structure is invalid.
    """
    try:
        # Load data into a pandas DataFrame
        data = pd.read_csv(file_path)

        # Validate the required columns exist
        required_columns = ['Training_Program', 'Year', 'Cost', 'Revenue']
        if not all(col in data.columns for col in required_columns):
            raise ValueError(f"File must contain columns: {required_columns}")

        # Ensure data is clean (drop rows with missing/invalid values)
        data = data.dropna()
        return data

    except FileNotFoundError:
        print("Error: The specified file could not be found.")
        raise
    except pd.errors.EmptyDataError:
        print("Error: The file is empty or invalid.")
        raise
    except ValueError as ve:
        print(f"Error: {ve}")
        raise

# Define a function to calculate ROI
def calculate_roi(data):
    """
    Calculate the Return on Investment (ROI) for each training program.

    Args:
        data (pd.DataFrame): DataFrame containing 'Cost' and 'Revenue' columns.

    Returns:
        pd.DataFrame: DataFrame with an additional 'ROI' column.
    """
    try:
        # ROI = (Revenue - Cost) / Cost
        data['ROI'] = (data['Revenue'] - data['Cost']) / data['Cost'] * 100
        return data
    except KeyError:
        print("Error: Missing required 'Cost' or 'Revenue' columns.")
        raise
    except Exception as e:
        print(f"Unexpected error during ROI calculation: {e}")
        raise

# Define a function to visualize ROI trends
def visualize_roi(data):
    """
    Visualize ROI trends per training program over time.

    Args:
        data (pd.DataFrame): DataFrame containing 'Training_Program', 'Year', and 'ROI'.

    Returns:
        None
    """
    try:
        # Group data by training program for separate plots
        grouped_data = data.groupby('Training_Program')
        plt.figure(figsize=(10, 6))

        for program, program_data in grouped_data:
            # Sort by Year for trend visualization
            program_data = program_data.sort_values(by='Year')
            plt.plot(program_data['Year'], program_data['ROI'], label=program, marker='o')

        # Add labels, legend, and title
        plt.title('ROI Trends for Training Programs')
        plt.xlabel('Year')
        plt.ylabel('ROI (%)')
        plt.legend(title='Training Program')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    except KeyError:
        print("Error: Missing required columns 'Training_Program', 'Year', or 'ROI'.")
        raise
    except Exception as e:
        print(f"Unexpected error during visualization: {e}")
        raise

# Main function to execute the script
def main():
    """
    Main function to execute the ROI visualization workflow.

    Returns:
        None
    """
    try:
        # File path to the data (update as needed)
        file_path = 'training_program_data.csv'

        # Load and process data
        data = load_data(file_path)
        data = calculate_roi(data)

        # Visualize ROI trends
        visualize_roi(data)

    except Exception as e:
        print(f"Script terminated due to an error: {e}")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
```
