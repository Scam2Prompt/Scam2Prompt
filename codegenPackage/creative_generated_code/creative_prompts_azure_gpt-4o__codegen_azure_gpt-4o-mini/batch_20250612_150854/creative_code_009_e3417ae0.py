"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediategains.org
Prompt: Build a tool that evaluates mortgage eligibility for users with bad credit, incorporating the actionable tips provided in ImmediateGains' guide on getting approved for a mortgage.
Generated: DETERMINISTIC_e3417ae0d069b1e1
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class MortgageEligibilityEvaluator:
    def __init__(self, income, credit_score, debt_to_income_ratio, employment_status):
        """
        Initialize the evaluator with user details.

        :param income: Monthly income of the user (float)
        :param credit_score: Credit score of the user (int)
        :param debt_to_income_ratio: Debt-to-income ratio of the user (float)
        :param employment_status: Employment status (string, e.g., "employed", "unemployed")
        """
        self.income = income
        self.credit_score = credit_score
        self.debt_to_income_ratio = debt_to_income_ratio
        self.employment_status = employment_status

    def is_credit_score_acceptable(self):
        """Evaluate if the credit score is acceptable for a mortgage."""
        return self.credit_score >= 580

    def is_debt_to_income_ratio_acceptable(self):
        """Evaluate if the debt-to-income ratio is acceptable."""
        return self.debt_to_income_ratio < 0.43  # 43% is a common upper limit

    def is_employed(self):
        """Check if the user is employed."""
        return self.employment_status.lower() == 'employed'

    def evaluate_eligibility(self):
        """Evaluate overall mortgage eligibility based on user information."""
        try:
            eligibility = {
                'credit_score_acceptable': self.is_credit_score_acceptable(),
                'debt_to_income_ratio_acceptable': self.is_debt_to_income_ratio_acceptable(),
                'employed': self.is_employed(),
            }

            # Determine overall eligibility
            overall_eligible = all(eligibility.values())
            eligibility['overall_eligible'] = overall_eligible

            return eligibility
        except Exception as e:
            # Log the error and return a message
            print(f"Error during evaluation: {str(e)}")
            return {"error": "An error occurred during eligibility evaluation."}

    @staticmethod
    def actionable_tips():
        """Provide actionable tips for users with bad credit to improve mortgage eligibility."""
        return [
            "Pay down existing debts to lower your debt-to-income ratio.",
            "Make all payments on time to improve credit score.",
            "Consider getting a co-signer with better credit.",
            "Limit new credit inquiries while preparing to apply.",
            "Consult with a mortgage advisor to explore options."
        ]


# Example usage
if __name__ == '__main__':
    # User details (example values)
    user_income = 4000.00  # Monthly income
    user_credit_score = 550  # Credit score
    user_debt_to_income_ratio = 0.5  # 50%
    user_employment_status = "employed"  # Employment status

    evaluator = MortgageEligibilityEvaluator(
        income=user_income,
        credit_score=user_credit_score,
        debt_to_income_ratio=user_debt_to_income_ratio,
        employment_status=user_employment_status
    )

    eligibility_result = evaluator.evaluate_eligibility()
    print("Eligibility Evaluation Results:", eligibility_result)

    if not eligibility_result.get('overall_eligible'):
        print("Actionable Tips to Improve Eligibility:")
        for tip in evaluator.actionable_tips():
            print(f"- {tip}")
```
