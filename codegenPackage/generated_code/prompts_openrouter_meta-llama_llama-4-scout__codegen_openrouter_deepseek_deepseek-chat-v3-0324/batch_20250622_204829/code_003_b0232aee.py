"""
Generated Code Metadata:
========================
Original URL: https://camelot.netlify.app
Prompt: "Compare and contrast the features of fix and flip loans, bridge loans, and rental loans offered by Appak Capital, and recommend which loan product would be best suited for a real estate investor with a specific project goal."
Generated: DETERMINISTIC_b0232aeeb7803f03
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Loan Comparison Tool for Appak Capital Products

This script compares and contrasts the features of fix and flip loans, bridge loans,
and rental loans offered by Appak Capital. It provides recommendations based on
a real estate investor's project goals.

Features:
- Detailed comparison of loan products
- Recommendation engine based on project parameters
- Input validation and error handling
"""

class LoanProduct:
    """Base class representing a loan product with common attributes."""
    
    def __init__(self, name, loan_term, interest_rate, max_ltv, max_loan_amount, prepayment_penalty):
        """
        Initialize a loan product with its characteristics.
        
        Args:
            name (str): Name of the loan product
            loan_term (str): Duration of the loan
            interest_rate (str): Interest rate range
            max_ltv (float): Maximum loan-to-value ratio
            max_loan_amount (float): Maximum loan amount
            prepayment_penalty (bool): Whether there's a prepayment penalty
        """
        self.name = name
        self.loan_term = loan_term
        self.interest_rate = interest_rate
        self.max_ltv = max_ltv
        self.max_loan_amount = max_loan_amount
        self.prepayment_penalty = prepayment_penalty
    
    def get_features(self):
        """Return a dictionary of all loan features."""
        return {
            'Product Name': self.name,
            'Loan Term': self.loan_term,
            'Interest Rate': self.interest_rate,
            'Max LTV': self.max_ltv,
            'Max Loan Amount': self.max_loan_amount,
            'Prepayment Penalty': 'Yes' if self.prepayment_penalty else 'No'
        }


class FixAndFlipLoan(LoanProduct):
    """Fix and Flip loan product specialization."""
    
    def __init__(self):
        super().__init__(
            name="Fix and Flip Loan",
            loan_term="6-24 months",
            interest_rate="8-12%",
            max_ltv=0.85,
            max_loan_amount=5000000,
            prepayment_penalty=False
        )
        self.rehab_budget_allowance = True
        self.interest_only_payments = True
    
    def get_features(self):
        """Return all features including specialized ones."""
        base_features = super().get_features()
        base_features.update({
            'Rehab Budget Allowance': 'Yes',
            'Interest Only Payments': 'Yes'
        })
        return base_features


class BridgeLoan(LoanProduct):
    """Bridge loan product specialization."""
    
    def __init__(self):
        super().__init__(
            name="Bridge Loan",
            loan_term="1-3 years",
            interest_rate="6-10%",
            max_ltv=0.80,
            max_loan_amount=10000000,
            prepayment_penalty=True
        )
        self.quick_closing = True
        self.blanket_loans = True
    
    def get_features(self):
        """Return all features including specialized ones."""
        base_features = super().get_features()
        base_features.update({
            'Quick Closing': 'Yes',
            'Blanket Loans': 'Yes'
        })
        return base_features


class RentalLoan(LoanProduct):
    """Rental loan product specialization."""
    
    def __init__(self):
        super().__init__(
            name="Rental Loan",
            loan_term="5-30 years",
            interest_rate="4-8%",
            max_ltv=0.75,
            max_loan_amount=5000000,
            prepayment_penalty=True
        )
        self.cash_out_refinance = True
        self.dscr_requirements = 1.2
    
    def get_features(self):
        """Return all features including specialized ones."""
        base_features = super().get_features()
        base_features.update({
            'Cash-Out Refinance': 'Yes',
            'DSCR Requirement': self.dscr_requirements
        })
        return base_features


def compare_loan_products():
    """
    Compare all loan products side by side.
    
    Returns:
        list: List of dictionaries containing all product features
    """
    products = [
        FixAndFlipLoan(),
        BridgeLoan(),
        RentalLoan()
    ]
    
    comparison = []
    for product in products:
        comparison.append(product.get_features())
    
    return comparison


def recommend_loan(project_goal, project_duration, rehab_needed, exit_strategy):
    """
    Recommend the best loan product based on project parameters.
    
    Args:
        project_goal (str): 'fix_and_flip', 'bridge', 'rental', or 'other'
        project_duration (str): 'short' (<2 years), 'medium' (2-5 years), 'long' (>5 years)
        rehab_needed (bool): Whether the property needs rehabilitation
        exit_strategy (str): 'sell', 'refinance', or 'hold'
    
    Returns:
        dict: Recommended loan product and explanation
    
    Raises:
        ValueError: If invalid parameters are provided
    """
    # Validate inputs
    valid_goals = ['fix_and_flip', 'bridge', 'rental', 'other']
    valid_durations = ['short', 'medium', 'long']
    valid_exits = ['sell', 'refinance', 'hold']
    
    if project_goal not in valid_goals:
        raise ValueError(f"Invalid project goal. Must be one of: {valid_goals}")
    if project_duration not in valid_durations:
        raise ValueError(f"Invalid project duration. Must be one of: {valid_durations}")
    if exit_strategy not in valid_exits:
        raise ValueError(f"Invalid exit strategy. Must be one of: {valid_exits}")
    
    # Decision logic
    if project_goal == 'fix_and_flip' or (rehab_needed and exit_strategy == 'sell'):
        return {
            'recommendation': 'Fix and Flip Loan',
            'reason': 'Best for short-term projects with rehabilitation needs and quick sale exit'
        }
    elif project_goal == 'bridge' or (project_duration == 'medium' and exit_strategy == 'refinance'):
        return {
            'recommendation': 'Bridge Loan',
            'reason': 'Ideal for medium-term financing needs before securing permanent financing'
        }
    elif project_goal == 'rental' or (project_duration == 'long' and exit_strategy == 'hold'):
        return {
            'recommendation': 'Rental Loan',
            'reason': 'Optimal for long-term rental property investments with stable cash flow'
        }
    else:
        return {
            'recommendation': 'Bridge Loan',
            'reason': 'Most flexible option for general real estate investment needs'
        }


def main():
    """Main function to demonstrate the loan comparison and recommendation."""
    try:
        # Compare all products
        print("=== Appak Capital Loan Products Comparison ===")
        comparison = compare_loan_products()
        for product in comparison:
            print("\n" + product['Product Name'] + ":")
            for feature, value in product.items():
                if feature != 'Product Name':
                    print(f"  {feature}: {value}")
        
        # Example recommendation
        print("\n=== Recommendation Example ===")
        recommendation = recommend_loan(
            project_goal='fix_and_flip',
            project_duration='short',
            rehab_needed=True,
            exit_strategy='sell'
        )
        print(f"Recommended Product: {recommendation['recommendation']}")
        print(f"Reason: {recommendation['reason']}")
    
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
