"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galmudugmof.so
Prompt: Write Python code to parse and analyze budget data from the "Approved Budget FY 2025" document provided by the Ministry of Finance Galmudug. Include functionality to extract fiscal year details and expenditure categories.
Generated: DETERMINISTIC_3b436fb601b1059b
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class BudgetDataParser:
    """
    A class to parse and analyze budget data from a given Excel file.

    Attributes:
        file_path (str): The file path to the budget document.
        budget_data (pd.DataFrame): Dataframe containing the budget data.
    """

    def __init__(self, file_path):
        """
        Initializes the BudgetDataParser with the path to the budget document.

        Parameters:
            file_path (str): Path to the Excel file containing budget data.
        """
        self.file_path = file_path
        self.budget_data = None

    def load_data(self):
        """
        Loads budget data from the Excel file and stores it in a DataFrame.
        
        Raises:
            FileNotFoundError: If the specified file does not exist.
            ValueError: If the data cannot be loaded or is empty.
        """
        try:
            self.budget_data = pd.read_excel(self.file_path)
            if self.budget_data.empty:
                raise ValueError("Loaded data is empty.")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File not found: {self.file_path}") from e
        except ValueError as e:
            raise ValueError(f"Error loading data: {str(e)}") from e

    def extract_fiscal_year(self):
        """
        Extracts fiscal year details from the budget data.

        Returns:
            list: A list of unique fiscal years found in the data.
        """
        if self.budget_data is None:
            raise ValueError("Budget data not loaded. Call load_data() before extracting fiscal year.")
        
        # Assuming the fiscal year is contained in a column named 'Fiscal Year'
        if 'Fiscal Year' not in self.budget_data.columns:
            raise KeyError("Column 'Fiscal Year' not found in the budget data.")
        
        return self.budget_data['Fiscal Year'].unique().tolist()

    def analyze_expenditure_categories(self):
        """
        Analyzes expenditure categories from the budget data.

        Returns:
            pd.DataFrame: A DataFrame summarizing total expenditures by category.
        """
        if self.budget_data is None:
            raise ValueError("Budget data not loaded. Call load_data() before analyzing expenditure categories.")
        
        # Assuming expenditure categories are in a column named 'Expenditure Category' 
        # and their values are in a column named 'Amount'
        if 'Expenditure Category' not in self.budget_data.columns or 'Amount' not in self.budget_data.columns:
            raise KeyError("Required columns 'Expenditure Category' or 'Amount' not found in the budget data.")

        # Grouping by 'Expenditure Category' and summing the 'Amount'
        return self.budget_data.groupby('Expenditure Category')['Amount'].sum().reset_index()

def main():
    """
    Main function to execute budget data parsing and analysis.
    """
    file_path = 'Approved_Budget_FY_2025.xlsx'  # Replace with the actual file path

    # Create an instance of the BudgetDataParser
    parser = BudgetDataParser(file_path)

    try:
        # Load the budget data
        parser.load_data()

        # Extract fiscal years
        fiscal_years = parser.extract_fiscal_year()
        print("Fiscal Years:", fiscal_years)

        # Analyze expenditure categories
        expenditure_summary = parser.analyze_expenditure_categories()
        print("Expenditure Summary:")
        print(expenditure_summary)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
