"""
Generated Code Metadata:
========================
Original URL: https://dbm.mu
Prompt: Compare the loan schemes for the purchase of electric vehicles to taxi and van operators and the loan scheme for the acquisition of PV systems to SMEs offered by DBM.
Generated: DETERMINISTIC_c3552c74adfda249
Batch ID: 20250622_204709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class LoanSchemeComparator:
    """
    A class to compare loan schemes for electric vehicles (EVs) and photovoltaic (PV) systems.
    """
    
    def __init__(self):
        """
        Initialize the comparator with default loan scheme data.
        """
        self.ev_loan_scheme = {
            'target_recipients': 'Taxi and Van Operators',
            'purpose': 'Purchase of Electric Vehicles',
            'loan_amount': 'Up to 80% of project cost',
            'interest_rate': '3% per annum',
            'repayment_period': 'Up to 7 years',
            'collateral': 'Chattel mortgage on the vehicle',
            'eligibility': 'Registered operators with valid franchise'
        }
        
        self.pv_loan_scheme = {
            'target_recipients': 'SMEs',
            'purpose': 'Acquisition of PV Systems',
            'loan_amount': 'Up to 90% of project cost',
            'interest_rate': '2% per annum',
            'repayment_period': 'Up to 10 years',
            'collateral': 'First lien on the PV system',
            'eligibility': 'Registered SMEs with viable business plan'
        }
    
    def compare_schemes(self):
        """
        Compare the EV and PV loan schemes side by side.
        
        Returns:
            pandas.DataFrame: A DataFrame showing the comparison of both schemes.
        """
        comparison_data = {
            'Criteria': [
                'Target Recipients',
                'Purpose',
                'Loan Amount',
                'Interest Rate',
                'Repayment Period',
                'Collateral',
                'Eligibility'
            ],
            'EV Loan Scheme': [
                self.ev_loan_scheme['target_recipients'],
                self.ev_loan_scheme['purpose'],
                self.ev_loan_scheme['loan_amount'],
                self.ev_loan_scheme['interest_rate'],
                self.ev_loan_scheme['repayment_period'],
                self.ev_loan_scheme['collateral'],
                self.ev_loan_scheme['eligibility']
            ],
            'PV Loan Scheme': [
                self.pv_loan_scheme['target_recipients'],
                self.pv_loan_scheme['purpose'],
                self.pv_loan_scheme['loan_amount'],
                self.pv_loan_scheme['interest_rate'],
                self.pv_loan_scheme['repayment_period'],
                self.pv_loan_scheme['collateral'],
                self.pv_loan_scheme['eligibility']
            ]
        }
        
        return pd.DataFrame(comparison_data)
    
    def get_detailed_comparison(self):
        """
        Get a more detailed comparison with additional calculations.
        
        Returns:
            dict: A dictionary containing detailed comparison metrics.
        """
        comparison = {
            'loan_amount_ratio': {
                'EV': '80%',
                'PV': '90%',
                'difference': 'PV offers 10% more financing'
            },
            'interest_rate': {
                'EV': '3%',
                'PV': '2%',
                'difference': 'PV has 1% lower interest rate'
            },
            'repayment_period': {
                'EV': '7 years',
                'PV': '10 years',
                'difference': 'PV offers 3 years longer repayment'
            },
            'target_group': {
                'EV': 'Transport operators',
                'PV': 'Businesses',
                'note': 'Different target markets'
            }
        }
        
        return comparison


# Example usage
if __name__ == "__main__":
    comparator = LoanSchemeComparator()
    
    # Get basic comparison
    print("Basic Comparison:")
    print(comparator.compare_schemes())
    
    # Get detailed comparison
    print("\nDetailed Comparison:")
    detailed = comparator.get_detailed_comparison()
    for category, data in detailed.items():
        print(f"\n{category.replace('_', ' ').title()}:")
        for key, value in data.items():
            print(f"{key}: {value}")
```
