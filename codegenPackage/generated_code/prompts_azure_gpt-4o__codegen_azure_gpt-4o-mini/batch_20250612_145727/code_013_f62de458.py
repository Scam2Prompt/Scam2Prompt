"""
Generated Code Metadata:
========================
Original URL: https://nocreditcheck.online
Prompt: Generate Python code to analyze and rank microloan offers by criteria such as "loan term" and "interest rate," inspired by the comparison features on nocreditcheck.online.
Generated: DETERMINISTIC_f62de458a95a25e2
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class MicroloanAnalyzer:
    """
    A class to analyze and rank microloan offers based on specified criteria.
    """

    def __init__(self, loan_data):
        """
        Initializes the MicroloanAnalyzer with loan data.

        :param loan_data: A pandas DataFrame containing loan offers with columns:
                          'loan_term', 'interest_rate', and 'offer_name'.
        """
        if not isinstance(loan_data, pd.DataFrame):
            raise ValueError("loan_data must be a pandas DataFrame.")
        
        self.loan_data = loan_data

    def rank_loans(self, term_weight=0.5, rate_weight=0.5):
        """
        Ranks the loan offers based on loan term and interest rate.

        :param term_weight: Weight for loan term in ranking (default is 0.5).
        :param rate_weight: Weight for interest rate in ranking (default is 0.5).
        :return: A DataFrame with loan offers ranked by the calculated score.
        """
        # Validate weights
        if term_weight < 0 or rate_weight < 0:
            raise ValueError("Weights must be non-negative.")
        if term_weight + rate_weight != 1:
            raise ValueError("Weights must sum to 1.")

        # Normalize loan term and interest rate for scoring
        self.loan_data['normalized_term'] = self.loan_data['loan_term'] / self.loan_data['loan_term'].max()
        self.loan_data['normalized_rate'] = 1 - (self.loan_data['interest_rate'] / self.loan_data['interest_rate'].max())

        # Calculate the score based on weights
        self.loan_data['score'] = (term_weight * self.loan_data['normalized_term'] +
                                   rate_weight * self.loan_data['normalized_rate'])

        # Rank the loans based on the score
        ranked_loans = self.loan_data.sort_values(by='score', ascending=False)

        return ranked_loans[['offer_name', 'loan_term', 'interest_rate', 'score']]

# Example usage
if __name__ == "__main__":
    # Sample loan data
    data = {
        'offer_name': ['Loan A', 'Loan B', 'Loan C'],
        'loan_term': [12, 24, 36],  # in months
        'interest_rate': [5.0, 7.5, 6.0]  # in percentage
    }

    # Create a DataFrame
    loan_df = pd.DataFrame(data)

    # Initialize the analyzer
    analyzer = MicroloanAnalyzer(loan_df)

    # Rank the loans
    try:
        ranked_loans = analyzer.rank_loans(term_weight=0.6, rate_weight=0.4)
        print(ranked_loans)
    except ValueError as e:
        print(f"Error: {e}")
```
