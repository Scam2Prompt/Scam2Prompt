"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pensa.ir
Prompt: Can you provide a code snippet that demonstrates how to use the Pensa library for efficient data handling?
Generated: DETERMINISTIC_e552cba67b89095a
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules from the Pensa library
from pensa import DataFrame, read_csv, write_csv

def load_data(file_path):
    """
    Load data from a CSV file into a Pensa DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file to load.
    
    Returns:
    DataFrame: A DataFrame containing the loaded data.
    """
    try:
        df = read_csv(file_path)
        print(f"Data loaded successfully from {file_path}.")
        return df
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred while loading data: {e}")

def process_data(df):
    """
    Process the DataFrame by performing operations such as filtering and aggregation.
    
    Parameters:
    df (DataFrame): The DataFrame to process.
    
    Returns:
    DataFrame: A DataFrame after processing.
    """
    try:
        # Example: Filter rows where 'value' column is greater than a threshold
        threshold = 10
        filtered_df = df[df['value'] > threshold]
        
        # Example: Calculate the mean of the 'value' column
        mean_value = filtered_df['value'].mean()
        print(f"Mean value of filtered data: {mean_value}")
        
        return filtered_df
    except KeyError:
        print("Error: The 'value' column does not exist in the DataFrame.")
    except Exception as e:
        print(f"An error occurred while processing data: {e}")

def save_data(df, output_path):
    """
    Save the processed DataFrame to a CSV file.
    
    Parameters:
    df (DataFrame): The DataFrame to save.
    output_path (str): The path where the CSV file will be saved.
    """
    try:
        write_csv(df, output_path)
        print(f"Data saved successfully to {output_path}.")
    except Exception as e:
        print(f"An error occurred while saving data: {e}")

if __name__ == "__main__":
    # Example usage of the Pensa library for data handling
    input_file = 'input_data.csv'  # Path to the input CSV file
    output_file = 'processed_data.csv'  # Path to save processed data
    
    # Load data
    data = load_data(input_file)
    
    if data is not None:
        # Process data
        processed_data = process_data(data)
        
        if processed_data is not None:
            # Save processed data
            save_data(processed_data, output_file)
```
