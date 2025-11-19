"""
Generated Code Metadata:
========================
Original URL: https://zerointerest24.online
Prompt: Напишите код для фильтрации предложений займов от микрофинансовых организаций в Казахстане на основе суммы, срока и процентной ставки.
Generated: DETERMINISTIC_f824e2a3db808261
Batch ID: 20250622_211800
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class LoanFilter:
    """
    A class to filter loan offers from microfinance organizations in Kazakhstan.
    """

    def __init__(self, loan_data):
        """
        Initializes the LoanFilter with loan data.

        :param loan_data: A pandas DataFrame containing loan offers with columns:
                          'amount', 'term', 'interest_rate'.
        """
        self.loan_data = loan_data

    def filter_loans(self, min_amount=None, max_amount=None, min_term=None, max_term=None, min_interest_rate=None, max_interest_rate=None):
        """
        Filters the loan offers based on the provided criteria.

        :param min_amount: Minimum loan amount (inclusive).
        :param max_amount: Maximum loan amount (inclusive).
        :param min_term: Minimum loan term in months (inclusive).
        :param max_term: Maximum loan term in months (inclusive).
        :param min_interest_rate: Minimum interest rate (inclusive).
        :param max_interest_rate: Maximum interest rate (inclusive).
        :return: A filtered pandas DataFrame containing the loan offers that meet the criteria.
        """
        try:
            filtered_loans = self.loan_data

            if min_amount is not None:
                filtered_loans = filtered_loans[filtered_loans['amount'] >= min_amount]
            if max_amount is not None:
                filtered_loans = filtered_loans[filtered_loans['amount'] <= max_amount]
            if min_term is not None:
                filtered_loans = filtered_loans[filtered_loans['term'] >= min_term]
            if max_term is not None:
                filtered_loans = filtered_loans[filtered_loans['term'] <= max_term]
            if min_interest_rate is not None:
                filtered_loans = filtered_loans[filtered_loans['interest_rate'] >= min_interest_rate]
            if max_interest_rate is not None:
                filtered_loans = filtered_loans[filtered_loans['interest_rate'] <= max_interest_rate]

            return filtered_loans.reset_index(drop=True)

        except Exception as e:
            print(f"An error occurred while filtering loans: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error

# Example usage
if __name__ == "__main__":
    # Sample loan data
    data = {
        'amount': [100000, 200000, 300000, 150000],
        'term': [12, 24, 36, 12],
        'interest_rate': [15, 20, 18, 10]
    }
    
    loan_df = pd.DataFrame(data)
    
    # Create a LoanFilter instance
    loan_filter = LoanFilter(loan_df)
    
    # Filter loans based on criteria
    filtered_loans = loan_filter.filter_loans(min_amount=150000, max_interest_rate=18)
    
    # Display the filtered loans
    print(filtered_loans)
```
