"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.igeog.uerj.br
Prompt: Write Python code to process and extract information from the list of candidates and results provided in the IGEOG selection process documents, such as "Listagem de inscrições deferidas e indeferidas" and "Resultado Final."
Generated: DETERMINISTIC_b7d5c8d52802e2b6
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import logging

# Configure logging for the module
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    """
    Load data from an Excel file and return a DataFrame.
    
    Args:
        file_path (str): The path to the Excel file containing candidates' data.
    
    Returns:
        pd.DataFrame: A DataFrame containing the loaded data.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file does not contain a valid Excel format.
    """
    try:
        df = pd.read_excel(file_path)
        logging.info(f"Data loaded successfully from {file_path}.")
        return df
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except ValueError:
        logging.error("Invalid Excel file format.")
        raise

def filter_candidates(df):
    """
    Filter candidates based on their status.
    
    Args:
        df (pd.DataFrame): The DataFrame containing candidates' data.
    
    Returns:
        tuple: Two DataFrames, one for approved candidates and one for disapproved candidates.
    """
    approved_candidates = df[df['Status'] == 'Deferido']
    disapproved_candidates = df[df['Status'] == 'Indeferido']
    
    logging.info(f"Filtered candidates: {len(approved_candidates)} approved, {len(disapproved_candidates)} disapproved.")
    
    return approved_candidates, disapproved_candidates

def save_results(approved_df, disapproved_df, output_path):
    """
    Save the filtered results to Excel files.
    
    Args:
        approved_df (pd.DataFrame): DataFrame of approved candidates.
        disapproved_df (pd.DataFrame): DataFrame of disapproved candidates.
        output_path (str): The output path where the results will be saved.
    """
    try:
        with pd.ExcelWriter(output_path) as writer:
            approved_df.to_excel(writer, sheet_name='Approved', index=False)
            disapproved_df.to_excel(writer, sheet_name='Disapproved', index=False)
        logging.info(f"Results saved successfully to {output_path}.")
    except Exception as e:
        logging.error(f"Failed to save results: {e}")
        raise

def main():
    """
    Main function to execute the data processing workflow.
    """
    input_file = 'candidates.xlsx'  # Input Excel file containing candidates
    output_file = 'filtered_candidates.xlsx'  # Output file for results
    
    try:
        # Load the candidates data
        candidates_df = load_data(input_file)

        # Filter candidates into approved and disapproved
        approved, disapproved = filter_candidates(candidates_df)

        # Save the filtered results
        save_results(approved, disapproved, output_file)
        
    except Exception as e:
        logging.critical(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
