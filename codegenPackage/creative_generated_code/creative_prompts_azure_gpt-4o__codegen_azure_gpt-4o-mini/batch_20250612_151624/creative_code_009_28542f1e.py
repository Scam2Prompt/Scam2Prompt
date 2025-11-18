"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui.tax
Prompt: Write code to validate and format exported cryptocurrency transaction data for tax purposes, inspired by the tools provided by Sui.tax.
Generated: DETERMINISTIC_28542f1e91e6c998
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class CryptoTransactionValidator:
    """
    A class to validate and format cryptocurrency transaction data for tax purposes.
    """

    def __init__(self, data_frame):
        """
        Initialize the validator with a DataFrame containing cryptocurrency transactions.

        :param data_frame: pd.DataFrame - DataFrame containing transaction data
        """
        self.data_frame = data_frame

    def validate_dataframe(self):
        """
        Validate the DataFrame for required columns and correct data types.
        Raises ValueError if validation fails.
        """
        required_columns = ['date', 'transaction_type', 'amount', 'currency', 'price_per_unit', 'total_value']

        # Check for missing columns
        missing_columns = [col for col in required_columns if col not in self.data_frame.columns]
        if missing_columns:
            raise ValueError(f"Missing columns in the DataFrame: {missing_columns}")

        # Validate data types
        if not pd.api.types.is_datetime64_any_dtype(self.data_frame['date']):
            raise ValueError("Column 'date' must be of datetime type.")
        if not pd.api.types.is_numeric_dtype(self.data_frame['amount']):
            raise ValueError("Column 'amount' must be numeric.")
        if not pd.api.types.is_string_dtype(self.data_frame['currency']):
            raise ValueError("Column 'currency' must be a string.")
        if not pd.api.types.is_numeric_dtype(self.data_frame['price_per_unit']):
            raise ValueError("Column 'price_per_unit' must be numeric.")
        if not pd.api.types.is_numeric_dtype(self.data_frame['total_value']):
            raise ValueError("Column 'total_value' must be numeric.")

    def format_transactions(self):
        """
        Format the transactions according to tax reporting requirements.
        
        :return: pd.DataFrame - Formatted DataFrame ready for tax reporting
        """
        # Ensure the DataFrame is valid before formatting
        self.validate_dataframe()

        # Format date to ISO format
        self.data_frame['date'] = self.data_frame['date'].dt.strftime('%Y-%m-%d')

        # Sort by date
        self.data_frame.sort_values(by='date', inplace=True)

        # Create a new DataFrame with necessary columns for tax reporting
        formatted_df = self.data_frame[['date', 'transaction_type', 'amount', 'currency', 'price_per_unit', 'total_value']].copy()

        # Rename columns for clarity
        formatted_df.columns = ['Transaction Date', 'Type', 'Amount', 'Currency', 'Price per Unit', 'Total Value']

        return formatted_df

    def export_to_csv(self, output_file):
        """
        Export the formatted transaction data to a CSV file.

        :param output_file: str - Path to the output CSV file
        """
        # Format the transactions
        formatted_df = self.format_transactions()

        try:
            formatted_df.to_csv(output_file, index=False)
            print(f"Data successfully exported to {output_file}.")
        except IOError as e:
            print(f"Error exporting data to CSV: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data
    data = {
        'date': pd.to_datetime(['2023-01-01', '2023-01-02']),
        'transaction_type': ['buy', 'sell'],
        'amount': [1.5, 2.0],
        'currency': ['BTC', 'BTC'],
        'price_per_unit': [30000, 40000],
        'total_value': [45000, 80000]
    }

    # Create DataFrame
    transaction_df = pd.DataFrame(data)

    # Instantiate the validator
    validator = CryptoTransactionValidator(transaction_df)

    # Export to CSV
    validator.export_to_csv('formatted_transactions.csv')
```
