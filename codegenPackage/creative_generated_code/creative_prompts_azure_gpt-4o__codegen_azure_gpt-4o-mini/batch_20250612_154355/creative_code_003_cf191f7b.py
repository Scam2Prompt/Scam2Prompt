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
  "https://example.com/approved_budget_fy2022": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/budget_circular_fy2022": {
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
import pandas as pd
import requests
from bs4 import BeautifulSoup

def download_budget_data(url):
    """
    Downloads budget data from a given URL and returns a DataFrame.
    
    Parameters:
        url (str): The URL of the budget document.
    
    Returns:
        pd.DataFrame: DataFrame containing the budget data.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        # Assuming the data is in table format on the webpage
        soup = BeautifulSoup(response.content, 'html.parser')
        tables = pd.read_html(str(soup))
        
        if not tables:
            raise ValueError("No tables found on the webpage.")
        
        return tables[0]  # Return the first table found
    
    except Exception as e:
        print(f"Error downloading budget data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

def compare_budgets(budget_circular, approved_budget):
    """
    Compares the budget circular with the approved budget and highlights discrepancies.
    
    Parameters:
        budget_circular (pd.DataFrame): DataFrame containing budget circular data.
        approved_budget (pd.DataFrame): DataFrame containing approved budget data.
    
    Returns:
        pd.DataFrame: DataFrame highlighting discrepancies.
    """
    try:
        # Merging the two DataFrames on a common column, assuming 'account' is the key
        comparison_df = pd.merge(budget_circular, approved_budget, on='account', suffixes=('_circular', '_approved'))
        
        # Highlight discrepancies where the amounts differ
        discrepancies = comparison_df[comparison_df['amount_circular'] != comparison_df['amount_approved']]
        
        return discrepancies
    
    except KeyError as e:
        print(f"Key error during comparison: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

def main():
    # Replace with actual URLs of the budget documents
    budget_circular_url = 'https://example.com/budget_circular_fy2022'
    approved_budget_url = 'https://example.com/approved_budget_fy2022'
    
    # Download the budget data
    budget_circular = download_budget_data(budget_circular_url)
    approved_budget = download_budget_data(approved_budget_url)
    
    if budget_circular.empty or approved_budget.empty:
        print("One or both of the budget data downloads failed. Exiting.")
        return
    
    # Compare the budgets
    discrepancies = compare_budgets(budget_circular, approved_budget)
    
    # Output the results
    if discrepancies.empty:
        print("No discrepancies found between the budgets.")
    else:
        print("Discrepancies found:")
        print(discrepancies)

if __name__ == "__main__":
    main()
```
