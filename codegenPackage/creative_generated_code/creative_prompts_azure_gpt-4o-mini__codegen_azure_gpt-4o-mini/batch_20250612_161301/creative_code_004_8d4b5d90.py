"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebookkeepingdiaries.com
Prompt: How can I create a monthly financial statement generator in Excel that aligns with the bookkeeping strategies mentioned on The Bookkeeping Diaries?
Generated: DETERMINISTIC_8d4b5d9075c402a1
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import openpyxl
from datetime import datetime

class FinancialStatementGenerator:
    def __init__(self, data_file, output_file):
        """
        Initialize the FinancialStatementGenerator with the given data and output file names.

        :param data_file: Path to the input Excel file containing financial data.
        :param output_file: Path where the output financial statement will be saved.
        """
        self.data_file = data_file
        self.output_file = output_file

    def load_data(self):
        """
        Load financial data from the specified Excel file.

        :return: DataFrame containing the financial data.
        """
        try:
            # Load the data into a DataFrame
            df = pd.read_excel(self.data_file)
            return df
        except Exception as e:
            print(f"Error loading data: {e}")
            raise

    def generate_monthly_statement(self, df):
        """
        Generate a monthly financial statement from the provided DataFrame.

        :param df: DataFrame containing financial transactions.
        :return: DataFrame summarizing the monthly financial statement.
        """
        try:
            # Ensure 'Date' column is in datetime format
            df['Date'] = pd.to_datetime(df['Date'])

            # Set the 'Date' column as the index
            df.set_index('Date', inplace=True)

            # Group data by month and year, summing up the amount for income and expenses
            monthly_statement = df.resample('M').sum()

            return monthly_statement
        except Exception as e:
            print(f"Error generating monthly statement: {e}")
            raise

    def save_statement(self, statement_df):
        """
        Save the generated financial statement to an Excel file.

        :param statement_df: DataFrame containing the financial statement to save.
        """
        try:
            # Write the DataFrame to an Excel file
            with pd.ExcelWriter(self.output_file, engine='openpyxl') as writer:
                statement_df.to_excel(writer, sheet_name='Monthly Statement')
            print(f"Financial statement saved to {self.output_file}")
        except Exception as e:
            print(f"Error saving statement: {e}")
            raise

    def run(self):
        """
        Execute the process of loading data, generating a monthly statement, and saving it.
        """
        df = self.load_data()
        monthly_statement = self.generate_monthly_statement(df)
        self.save_statement(monthly_statement)

if __name__ == "__main__":
    # Define input and output file paths
    input_file = 'financial_data.xlsx'  # Path to the input data file
    output_file = 'monthly_financial_statement.xlsx'  # Path for the output statement

    # Create an instance of the financial statement generator
    generator = FinancialStatementGenerator(input_file, output_file)

    # Run the generator
    generator.run()
```

**Note:** Make sure the input Excel file `financial_data.xlsx` contains a 'Date' column and an 'Amount' column for this code to function correctly. Adjust the paths accordingly based on your setup.
