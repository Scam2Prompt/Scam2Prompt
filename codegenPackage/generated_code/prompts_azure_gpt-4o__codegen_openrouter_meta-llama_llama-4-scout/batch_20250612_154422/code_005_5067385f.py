"""
Generated Code Metadata:
========================
Original URL: https://securecash.info
Prompt: Write code to compare funding options (e.g., line of credit, term loan, working capital) based on the features and benefits described by New York Savings.
Generated: DETERMINISTIC_5067385fb81a7740
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from dataclasses import dataclass
from typing import List

class FundingOption(Enum):
    LINE_OF_CREDIT = "Line of Credit"
    TERM_LOAN = "Term Loan"
    WORKING_CAPITAL = "Working Capital"

@dataclass
class FundingFeatures:
    interest_rate: float
    repayment_term: int
    collateral_required: bool
    fees: List[float]

class FundingOptionComparison:
    def __init__(self):
        self.funding_options = {
            FundingOption.LINE_OF_CREDIT: FundingFeatures(interest_rate=6.0, repayment_term=12, collateral_required=False, fees=[0.01, 0.02]),
            FundingOption.TERM_LOAN: FundingFeatures(interest_rate=8.0, repayment_term=36, collateral_required=True, fees=[0.02, 0.03]),
            FundingOption.WORKING_CAPITAL: FundingFeatures(interest_rate=5.0, repayment_term=6, collateral_required=False, fees=[0.005, 0.015]),
        }

    def compare_funding_options(self):
        print("# Funding Option Comparison")
        for option, features in self.funding_options.items():
            print(f"## {option.value}")
            print(f"* Interest Rate: {features.interest_rate}%")
            print(f"* Repayment Term: {features.repayment_term} months")
            print(f"* Collateral Required: {'Yes' if features.collateral_required else 'No'}")
            print(f"* Fees: {[f'{fee*100}% for every ${1}' for fee in features.fees]}")
            print()

    def calculate_total_cost(self, funding_option: FundingOption, principal: float):
        try:
            features = self.funding_options[funding_option]
            interest_rate = features.interest_rate / 100
            repayment_term = features.repayment_term
            fees = sum([fee * principal for fee in features.fees])
            total_interest = principal * interest_rate * (repayment_term / 12)
            total_cost = principal + total_interest + fees
            return total_cost
        except KeyError:
            print(f"Invalid funding option: {funding_option}")
            return None

def main():
    comparison = FundingOptionComparison()
    comparison.compare_funding_options()

    principal = 100000
    funding_option = FundingOption.LINE_OF_CREDIT
    total_cost = comparison.calculate_total_cost(funding_option, principal)
    if total_cost:
        print(f"Total cost for {funding_option.value} with principal ${principal}: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
```
