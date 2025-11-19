"""
Generated Code Metadata:
========================
Original URL: https://immediatecodeai.io
Prompt: Create a simple risk tolerance assessment tool using a programming language of your choice, taking into account factors such as investor confidence, risk capacity, and resilience, and provide recommendations for investment education based on the assessment results.
Generated: DETERMINISTIC_e8d95021f7183797
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# risk_tolerance_assessment.py

class RiskToleranceAssessment:
    def __init__(self):
        self.confidence_levels = {
            "very_confident": 5,
            "somewhat_confident": 4,
            "neutral": 3,
            "somewhat_unconfident": 2,
            "not_confident_at_all": 1
        }
        self.risk_capacity_levels = {
            "high": 5,
            "medium": 3,
            "low": 1
        }
        self.resilience_levels = {
            "very_resilient": 5,
            "somewhat_resilient": 4,
            "neutral": 3,
            "somewhat_sensitive": 2,
            "not_resilient_at_all": 1
        }

    def assess_investor_confidence(self):
        print("Investor Confidence Assessment:")
        print("--------------------------------")
        print("1. Very Confident")
        print("2. Somewhat Confident")
        print("3. Neutral")
        print("4. Somewhat Unconfident")
        print("5. Not Confident at All")
        
        while True:
            try:
                choice = int(input("Please select a number: "))
                if 1 <= choice <= 5:
                    return self.confidence_levels[list(self.confidence_levels.keys())[choice - 1]]
                else:
                    print("Invalid choice. Please select a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def assess_risk_capacity(self):
        print("\nRisk Capacity Assessment:")
        print("---------------------------")
        print("1. High")
        print("2. Medium")
        print("3. Low")
        
        while True:
            try:
                choice = int(input("Please select a number: "))
                if 1 <= choice <= 3:
                    return self.risk_capacity_levels[list(self.risk_capacity_levels.keys())[choice - 1]]
                else:
                    print("Invalid choice. Please select a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def assess_resilience(self):
        print("\nResilience Assessment:")
        print("------------------------")
        print("1. Very Resilient")
        print("2. Somewhat Resilient")
        print("3. Neutral")
        print("4. Somewhat Sensitive")
        print("5. Not Resilient at All")
        
        while True:
            try:
                choice = int(input("Please select a number: "))
                if 1 <= choice <= 5:
                    return self.resilience_levels[list(self.resilience_levels.keys())[choice - 1]]
                else:
                    print("Invalid choice. Please select a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def calculate_risk_tolerance(self, confidence, risk_capacity, resilience):
        return (confidence + risk_capacity + resilience) / 3

    def provide_recommendation(self, risk_tolerance):
        if risk_tolerance >= 4:
            return "You have a high risk tolerance. Consider investing in stocks or real estate. We recommend the following education resources: \n- Investopedia's Stock Investing Course\n- Real Estate Investing 101 by BiggerPockets"
        elif risk_tolerance >= 3:
            return "You have a medium risk tolerance. Consider investing in bonds or ETFs. We recommend the following education resources: \n- The Bond Market by The CFA Institute\n- ETF Investing 101 by ETF.com"
        else:
            return "You have a low risk tolerance. Consider investing in savings accounts or government bonds. We recommend the following education resources: \n- Savings Account Basics by NerdWallet\n- Government Bonds 101 by TreasuryDirect"

def main():
    assessment = RiskToleranceAssessment()
    confidence = assessment.assess_investor_confidence()
    risk_capacity = assessment.assess_risk_capacity()
    resilience = assessment.assess_resilience()
    risk_tolerance = assessment.calculate_risk_tolerance(confidence, risk_capacity, resilience)
    print(f"\nYour risk tolerance score is: {risk_tolerance:.2f}")
    print(assessment.provide_recommendation(risk_tolerance))

if __name__ == "__main__":
    main()
```
