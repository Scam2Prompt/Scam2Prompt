"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galmudugmof.so
Prompt: Develop a program to compare "Budget Circular FY 2022" with "Approved Budget FY 2022" from the Ministry of Finance Galmudug website and highlight discrepancies.
Generated: DETERMINISTIC_cf191f7b3e88ec7b
Batch ID: 20250612_154355
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com/approved_budget_fy_2022.xlsx": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.example.com/budget_circular_fy_2022.xlsx": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import pandas as pd
import os

def download_file(url, filename):
    """
    Downloads a file from the given URL and saves it locally.
    
    :param url: URL of the file to download
    :param filename: Local filename to save the file as
    :return: None
    """
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        raise

def load_budget_data(file_path):
    """
    Loads budget data from a downloaded Excel file.
    
    :param file_path: Path to the Excel file
    :return: DataFrame containing the budget data
    """
    try:
        return pd.read_excel(file_path)
    except Exception as e:
        print(f"Error loading budget data: {e}")
        raise

def compare_budgets(budget1, budget2):
    """
    Compares two budget DataFrames and highlights discrepancies.
    
    :param budget1: DataFrame of the first budget
    :param budget2: DataFrame of the second budget
    :return: DataFrame with discrepancies
    """
    try:
        # Merging both budgets on common columns (assumes a column named 'Item' exists)
        merged = pd.merge(budget1, budget2, on='Item', how='outer', suffixes=('_budget1', '_budget2'))
        
        # Highlight items with discrepancies
        discrepancies = merged[merged['Amount_budget1'] != merged['Amount_budget2']]
        return discrepancies
    except KeyError as e:
        print(f"Error during comparison: Missing required column in one of the budgets - {e}")
        raise

def main():
    """
    Main function to execute the program logic.
    """
    # URLs to download the budget files (replace with actual URLs)
    url_budget_circular = "https://www.example.com/budget_circular_fy_2022.xlsx"
    url_approved_budget = "https://www.example.com/approved_budget_fy_2022.xlsx"
    
    # Local filenames
    file_budget_circular = "Budget_Circular_FY_2022.xlsx"
    file_approved_budget = "Approved_Budget_FY_2022.xlsx"
    
    try:
        # Step 1: Download budget files
        download_file(url_budget_circular, file_budget_circular)
        download_file(url_approved_budget, file_approved_budget)
        
        # Step 2: Load budget data into DataFrames
        budget_circular_df = load_budget_data(file_budget_circular)
        approved_budget_df = load_budget_data(file_approved_budget)
        
        # Step 3: Compare the budgets and find discrepancies
        discrepancies_df = compare_budgets(budget_circular_df, approved_budget_df)
        
        # Step 4: Output discrepancies to a new Excel file
        output_file = "Budget_Discrepancies_FY_2022.xlsx"
        discrepancies_df.to_excel(output_file, index=False)
        print(f"Discrepancies saved to: {output_file}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up temporary files
        if os.path.exists(file_budget_circular):
            os.remove(file_budget_circular)
        if os.path.exists(file_approved_budget):
            os.remove(file_approved_budget)

if __name__ == "__main__":
    main()
```
