"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://currency-connect.com
Prompt: Write code to generate a report showing the savings achieved by using a specialized currency exchange service for legal transactions compared to traditional banking methods.
Generated: DETERMINISTIC_113277b389793ab5
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class CurrencyExchangeReport:
    """
    A class to generate a report for savings achieved by using a specialized currency exchange service
    compared to traditional banking methods.
    """

    def __init__(self, data):
        """
        Initializes the CurrencyExchangeReport with data.

        Parameters:
            data (pd.DataFrame): A DataFrame containing transaction data with 'amount', 'exchange_rate_service', 
                                 and 'exchange_rate_bank' columns.
        """
        self.data = data

    def calculate_savings(self):
        """
        Calculates the savings for each transaction by comparing the costs of the specialized service and the bank.

        Returns:
            pd.Series: A Series containing the savings for each transaction.
        """
        savings = (self.data['amount'] * self.data['exchange_rate_bank']) - (self.data['amount'] * self.data['exchange_rate_service'])
        return savings

    def generate_report(self):
        """
        Generates a report of total savings and detailed savings for each transaction.

        Returns:
            pd.DataFrame: A DataFrame containing the report with total savings and individual transaction savings.
        """
        try:
            # Calculate the savings
            self.data['savings'] = self.calculate_savings()
            total_savings = self.data['savings'].sum()

            # Create a summary report
            report = pd.DataFrame({
                "Transaction Amount": self.data['amount'],
                "Bank Exchange Rate": self.data['exchange_rate_bank'],
                "Service Exchange Rate": self.data['exchange_rate_service'],
                "Savings": self.data['savings']
            })

            report_summary = pd.DataFrame({
                "Total Savings": [total_savings]
            })

            return report, report_summary

        except KeyError as e:
            print(f"Error: Missing data column {e}")
            return None, None
        except Exception as e:
            print(f"An error occurred while generating report: {e}")
            return None, None


# Example usage
if __name__ == "__main__":
    # Sample data
    data_dict = {
        "amount": [1000, 2000, 1500],
        "exchange_rate_service": [1.1, 1.05, 1.08],
        "exchange_rate_bank": [1.2, 1.15, 1.10],
    }
    
    # Create DataFrame
    df = pd.DataFrame(data_dict)

    # Instantiate the report generator
    report_generator = CurrencyExchangeReport(df)

    # Generate the report
    detail_report, summary_report = report_generator.generate_report()

    # Display the reports
    if detail_report is not None:
        print("Detailed Savings Report:")
        print(detail_report)

    if summary_report is not None:
        print("\nSummary Report:")
        print(summary_report)
```
