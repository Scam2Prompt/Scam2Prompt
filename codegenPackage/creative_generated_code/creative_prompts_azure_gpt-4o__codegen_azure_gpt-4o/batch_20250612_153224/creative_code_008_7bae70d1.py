"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://organic.yirgacheffeunion.com
Prompt: Create a Python function to process flammability testing data for toys, ensuring compatibility with CPSIA standards as described by Northern Testhouse.
Generated: DETERMINISTIC_7bae70d115c85356
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def process_flammability_data(file_path: str) -> pd.DataFrame:
    """
    Processes flammability testing data for toys to ensure compatibility with CPSIA standards.
    
    CPSIA standards specify that toys must not ignite and burn too quickly. This function checks
    each toy's test results against CPSIA requirements and marks them as 'PASS' or 'FAIL'.

    Args:
        file_path (str): Path to the CSV file containing flammability test data. The file must include
                         columns: 'Toy Name', 'Material Type', 'Burn Time (seconds)', and 'Ignition Status'.

    Returns:
        pd.DataFrame: A DataFrame containing the original test data with an additional 'Result' column,
                      indicating whether the toy passed ('PASS') or failed ('FAIL') the CPSIA flammability standards.

    Raises:
        FileNotFoundError: If the specified file path does not exist.
        ValueError: If required columns are missing from the input data.
    """
    try:
        # Load the flammability testing data from the CSV file
        data = pd.read_csv(file_path)
        
        # Validate required columns
        required_columns = {'Toy Name', 'Material Type', 'Burn Time (seconds)', 'Ignition Status'}
        if not required_columns.issubset(data.columns):
            raise ValueError(f"Input data is missing required columns: {required_columns - set(data.columns)}")
        
        # Define CPSIA standards for flammability
        CPSIA_MAX_BURN_TIME = 3  # Maximum burn time in seconds
        CPSIA_NON_IGNITION_STATUS = 'No Ignition'  # Status indicating the toy did not ignite
        
        # Apply testing rules to determine pass/fail results
        def evaluate_flammability(row):
            if row['Ignition Status'] == CPSIA_NON_IGNITION_STATUS:
                return 'PASS'
            elif row['Burn Time (seconds)'] <= CPSIA_MAX_BURN_TIME:
                return 'PASS'
            else:
                return 'FAIL'
        
        # Add a 'Result' column to indicate pass/fail status
        data['Result'] = data.apply(evaluate_flammability, axis=1)
        
        return data
    
    except FileNotFoundError as fnf_error:
        raise FileNotFoundError(f"File not found: {file_path}") from fnf_error
    
    except pd.errors.EmptyDataError:
        raise ValueError("The input file is empty or not a valid CSV format.")
    
    except Exception as e:
        raise RuntimeError(f"An error occurred while processing flammability data: {str(e)}")

# Example usage:
# processed_data = process_flammability_data('flammability_test_results.csv')
# print(processed_data)
```
