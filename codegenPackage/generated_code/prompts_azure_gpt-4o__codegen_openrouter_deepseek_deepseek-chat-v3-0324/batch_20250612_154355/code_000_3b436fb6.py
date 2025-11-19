"""
Generated Code Metadata:
========================
Original URL: https://galmudugmof.so
Prompt: Write Python code to parse and analyze budget data from the "Approved Budget FY 2025" document provided by the Ministry of Finance Galmudug. Include functionality to extract fiscal year details and expenditure categories.
Generated: DETERMINISTIC_3b436fb601b1059b
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import re
from typing import Dict, List, Optional, Tuple
from pathlib import Path

class BudgetAnalyzer:
    """
    A class to parse and analyze budget data from the "Approved Budget FY 2025" document.
    
    Attributes:
        file_path (str): Path to the budget document.
        fiscal_year (Optional[str]): Extracted fiscal year from the document.
        expenditure_categories (Optional[List[str]]): List of expenditure categories.
        budget_data (Optional[pd.DataFrame]): Parsed budget data in a DataFrame.
    """
    
    def __init__(self, file_path: str):
        """
        Initialize the BudgetAnalyzer with the path to the budget document.
        
        Args:
            file_path (str): Path to the budget document.
        """
        self.file_path = file_path
        self.fiscal_year = None
        self.expenditure_categories = None
        self.budget_data = None
        
    def parse_document(self) -> None:
        """
        Parse the budget document to extract fiscal year and expenditure categories.
        
        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file format is not supported or parsing fails.
        """
        try:
            # Check if file exists
            if not Path(self.file_path).exists():
                raise FileNotFoundError(f"File not found: {self.file_path}")
            
            # Read the file based on its extension
            if self.file_path.endswith('.csv'):
                self.budget_data = pd.read_csv(self.file_path)
            elif self.file_path.endswith('.xlsx') or self.file_path.endswith('.xls'):
                self.budget_data = pd.read_excel(self.file_path)
            else:
                raise ValueError("Unsupported file format. Only CSV and Excel files are supported.")
            
            # Extract fiscal year from the document (assuming it's in the first few rows)
            self._extract_fiscal_year()
            
            # Extract expenditure categories (assuming they are column headers or in a specific column)
            self._extract_expenditure_categories()
            
        except Exception as e:
            raise ValueError(f"Failed to parse document: {str(e)}")
    
    def _extract_fiscal_year(self) -> None:
        """
        Extract the fiscal year from the budget document.
        
        Assumes the fiscal year is mentioned in the first few rows or in a specific format.
        """
        # Sample regex pattern to match fiscal year (e.g., FY 2025, Fiscal Year 2025)
        fiscal_year_pattern = r'(?:FY|Fiscal Year)\s*(\d{4})'
        
        # Check the first few rows for the fiscal year
        for _, row in self.budget_data.head(5).iterrows():
            for value in row.values:
                if isinstance(value, str):
                    match = re.search(fiscal_year_pattern, value, re.IGNORECASE)
                    if match:
                        self.fiscal_year = match.group(1)
                        return
        
        # If not found, check column names
        for col in self.budget_data.columns:
            if isinstance(col, str):
                match = re.search(fiscal_year_pattern, col, re.IGNORECASE)
                if match:
                    self.fiscal_year = match.group(1)
                    return
        
        raise ValueError("Fiscal year not found in the document.")
    
    def _extract_expenditure_categories(self) -> None:
        """
        Extract expenditure categories from the budget document.
        
        Assumes categories are either column headers or in a specific column.
        """
        # Try to get categories from column headers
        self.expenditure_categories = [col for col in self.budget_data.columns if isinstance(col, str)]
        
        if not self.expenditure_categories:
            raise ValueError("No expenditure categories found in the document.")
    
    def get_fiscal_year(self) -> str:
        """
        Get the extracted fiscal year.
        
        Returns:
            str: The fiscal year.
            
        Raises:
            ValueError: If fiscal year has not been extracted yet.
        """
        if self.fiscal_year is None:
            raise ValueError("Fiscal year not extracted. Call parse_document() first.")
        return self.fiscal_year
    
    def get_expenditure_categories(self) -> List[str]:
        """
        Get the extracted expenditure categories.
        
        Returns:
            List[str]: List of expenditure categories.
            
        Raises:
            ValueError: If categories have not been extracted yet.
        """
        if self.expenditure_categories is None:
            raise ValueError("Expenditure categories not extracted. Call parse_document() first.")
        return self.expenditure_categories
    
    def get_budget_data(self) -> pd.DataFrame:
        """
        Get the parsed budget data.
        
        Returns:
            pd.DataFrame: The budget data.
            
        Raises:
            ValueError: If data has not been parsed yet.
        """
        if self.budget_data is None:
            raise ValueError("Budget data not parsed. Call parse_document() first.")
        return self.budget_data

# Example usage
if __name__ == "__main__":
    try:
        analyzer = BudgetAnalyzer("Approved Budget FY 2025.xlsx")
        analyzer.parse_document()
        
        print(f"Fiscal Year: {analyzer.get_fiscal_year()}")
        print(f"Expenditure Categories: {analyzer.get_expenditure_categories()}")
        print("\nBudget Data Sample:")
        print(analyzer.get_budget_data().head())
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
