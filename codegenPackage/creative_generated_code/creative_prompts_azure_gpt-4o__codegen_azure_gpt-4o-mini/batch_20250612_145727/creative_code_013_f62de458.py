"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nocreditcheck.online
Prompt: Generate Python code to analyze and rank microloan offers by criteria such as "loan term" and "interest rate," inspired by the comparison features on nocreditcheck.online.
Generated: DETERMINISTIC_f62de458a95a25e2
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class Microloan:
    """
    A class to represent a microloan offer.

    Attributes
    ----------
    name : str
        The name of the microloan provider.
    loan_term : int
        The term of the loan in months.
    interest_rate : float
        The annual interest rate of the loan.
    amount : float
        The amount of the loan.

    Methods
    -------
    monthly_payment():
        Calculates the monthly payment for the loan.
    """
    
    def __init__(self, name, loan_term, interest_rate, amount):
        self.name = name
        self.loan_term = loan_term
        self.interest_rate = interest_rate
        self.amount = amount

    def monthly_payment(self):
        """
        Calculate the monthly payment based on the loan term, interest rate, and amount.

        Returns
        -------
        float
            The monthly payment amount.
        """
        monthly_rate = self.interest_rate / 100 / 12
        if monthly_rate == 0:
            return self.amount / self.loan_term
        
        payment = (self.amount * monthly_rate) / (1 - (1 + monthly_rate) ** -self.loan_term)
        return payment


class LoanAnalyzer:
    """
    A class to analyze and rank microloan offers based on specified criteria.

    Attributes
    ----------
    loans : list
        A list of Microloan objects.

    Methods
    -------
    add_loan(loan):
        Adds a Microloan object to the loans list.
    analyze_loans(criteria):
        Analyzes and ranks loans by the specified criteria.
    """

    def __init__(self):
        self.loans = []

    def add_loan(self, loan):
        """
        Add a Microloan object to the loans list.

        Parameters
        ----------
        loan : Microloan
            A Microloan object to be added.
        """
        if not isinstance(loan, Microloan):
            raise TypeError("Only Microloan instances can be added.")
        self.loans.append(loan)

    def analyze_loans(self, criteria='interest_rate'):
        """
        Analyze and rank loans based on the specified criteria.

        Parameters
        ----------
        criteria : str
            The criteria by which to rank the loans ('interest_rate', 'loan_term').

        Returns
        -------
        DataFrame
            A pandas DataFrame containing the ranked loan offers.
        """
        if criteria not in ['interest_rate', 'loan_term']:
            raise ValueError("Criteria must be either 'interest_rate' or 'loan_term'.")

        # Create a DataFrame from the loans list
        loan_data = {
            'Provider': [loan.name for loan in self.loans],
            'Loan Term (Months)': [loan.loan_term for loan in self.loans],
            'Interest Rate (%)': [loan.interest_rate for loan in self.loans],
            'Monthly Payment': [loan.monthly_payment() for loan in self.loans],
        }
        
        df = pd.DataFrame(loan_data)

        # Rank loans based on the specified criteria
        df['Rank'] = df[criteria].rank()
        ranked_loans = df.sort_values(by='Rank').reset_index(drop=True)

        return ranked_loans


# Example usage
if __name__ == "__main__":
    # Initialize the loan analyzer
    analyzer = LoanAnalyzer()

    # Add some sample loans
    try:
        analyzer.add_loan(Microloan("Lender A", 12, 5.5, 1000))
        analyzer.add_loan(Microloan("Lender B", 24, 7.0, 1500))
        analyzer.add_loan(Microloan("Lender C", 36, 4.0, 2000))
    except TypeError as e:
        print(f"Error adding loan: {e}")

    # Analyze and rank loans by interest rate
    try:
        ranked_loans = analyzer.analyze_loans(criteria='interest_rate')
        print(ranked_loans)
    except ValueError as e:
        print(f"Error analyzing loans: {e}")
```
