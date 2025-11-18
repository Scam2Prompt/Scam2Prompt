"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yehudit-taxes.co.il
Prompt: Generate code to compare initial and subsequent capital declarations for tax purposes, ensuring accuracy as emphasized by Yehudit Benedict's firm.
Generated: DETERMINISTIC_5ecf740d24b6b3fa
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class CapitalDeclarationComparator:
    """
    A class to compare initial and subsequent capital declarations for tax purposes.
    """

    def __init__(self, initial_declaration: pd.DataFrame, subsequent_declaration: pd.DataFrame):
        """
        Initializes the CapitalDeclarationComparator with initial and subsequent declarations.

        :param initial_declaration: A DataFrame containing the initial capital declaration.
        :param subsequent_declaration: A DataFrame containing the subsequent capital declaration.
        """
        self.initial_declaration = initial_declaration
        self.subsequent_declaration = subsequent_declaration

    def validate_dataframes(self):
        """
        Validates that the input DataFrames contain the necessary columns and are not empty.

        :raises ValueError: If the DataFrames are empty or do not contain required columns.
        """
        required_columns = {'Capital Item', 'Amount'}
        
        if self.initial_declaration.empty or self.subsequent_declaration.empty:
            raise ValueError("Declarations cannot be empty.")
        
        if not required_columns.issubset(self.initial_declaration.columns):
            raise ValueError("Initial declaration must contain columns: 'Capital Item', 'Amount'.")
        
        if not required_columns.issubset(self.subsequent_declaration.columns):
            raise ValueError("Subsequent declaration must contain columns: 'Capital Item', 'Amount'.")

    def compare_declarations(self):
        """
        Compares the initial and subsequent capital declarations.

        :return: A DataFrame showing differences between initial and subsequent declarations.
        """
        self.validate_dataframes()  # Validate the input dataframes
        
        # Merging the two DataFrames on 'Capital Item' to compare amounts
        comparison = pd.merge(
            self.initial_declaration,
            self.subsequent_declaration,
            on='Capital Item',
            how='outer',
            suffixes=('_initial', '_subsequent')
        )
        
        # Create a column to show the difference
        comparison['Difference'] = comparison['Amount_subsequent'] - comparison['Amount_initial']
        
        return comparison

    def generate_report(self, comparison: pd.DataFrame):
        """
        Generates a report of the comparison results.

        :param comparison: The DataFrame containing the comparison results.
        :return: A string report.
        """
        report = comparison.to_string(index=False)
        return report

# Example Usage
if __name__ == "__main__":
    try:
        # Sample data for initial and subsequent declarations
        initial_data = {
            'Capital Item': ['Investment A', 'Investment B', 'Investment C'],
            'Amount': [10000, 15000, 20000]
        }
        
        subsequent_data = {
            'Capital Item': ['Investment A', 'Investment B', 'Investment D'],
            'Amount': [12000, 15000, 25000]
        }

        # Creating DataFrames
        initial_declaration_df = pd.DataFrame(initial_data)
        subsequent_declaration_df = pd.DataFrame(subsequent_data)

        # Creating an instance of the comparator
        comparator = CapitalDeclarationComparator(initial_declaration_df, subsequent_declaration_df)

        # Comparing declarations
        comparison_result = comparator.compare_declarations()

        # Generating the report
        report = comparator.generate_report(comparison_result)
        print("Comparison Report:")
        print(report)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
