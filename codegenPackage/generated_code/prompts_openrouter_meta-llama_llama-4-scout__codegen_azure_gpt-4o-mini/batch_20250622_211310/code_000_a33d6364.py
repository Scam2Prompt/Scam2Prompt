"""
Generated Code Metadata:
========================
Original URL: https://immediate-evista.co
Prompt: Write a Python script to help investors assess their risk tolerance and provide recommendations for investment strategies based on their risk level, considering factors such as investment goals, financial situation, and experience.
Generated: DETERMINISTIC_a33d6364db475023
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class RiskAssessment:
    def __init__(self, investment_goals, financial_situation, experience_level):
        """
        Initialize the RiskAssessment class with user inputs.

        :param investment_goals: List of investment goals (e.g., retirement, education, etc.)
        :param financial_situation: Dictionary containing financial details (income, savings, etc.)
        :param experience_level: User's experience level in investing (e.g., beginner, intermediate, expert)
        """
        self.investment_goals = investment_goals
        self.financial_situation = financial_situation
        self.experience_level = experience_level

    def assess_risk_tolerance(self):
        """
        Assess the risk tolerance based on user inputs.

        :return: Risk tolerance level as a string
        """
        risk_score = 0

        # Assess based on investment goals
        if 'retirement' in self.investment_goals:
            risk_score += 1
        if 'short-term gains' in self.investment_goals:
            risk_score += 2

        # Assess based on financial situation
        if self.financial_situation['savings'] > 100000:
            risk_score += 2
        elif self.financial_situation['savings'] > 50000:
            risk_score += 1

        # Assess based on experience level
        if self.experience_level == 'expert':
            risk_score += 2
        elif self.experience_level == 'intermediate':
            risk_score += 1

        # Determine risk tolerance level
        if risk_score <= 2:
            return 'Low Risk'
        elif risk_score <= 4:
            return 'Moderate Risk'
        else:
            return 'High Risk'

    def recommend_investment_strategy(self):
        """
        Provide investment strategy recommendations based on risk tolerance.

        :return: Recommended investment strategy as a string
        """
        risk_tolerance = self.assess_risk_tolerance()

        if risk_tolerance == 'Low Risk':
            return "Recommended Strategy: Focus on bonds and stable dividend stocks."
        elif risk_tolerance == 'Moderate Risk':
            return "Recommended Strategy: Diversify with a mix of stocks and bonds."
        else:
            return "Recommended Strategy: Invest in growth stocks and high-risk assets."

def main():
    """
    Main function to run the risk assessment program.
    """
    try:
        # Sample user input
        investment_goals = ['retirement', 'education']
        financial_situation = {
            'income': 80000,
            'savings': 120000,
            'debt': 20000
        }
        experience_level = 'intermediate'

        # Create a RiskAssessment instance
        risk_assessment = RiskAssessment(investment_goals, financial_situation, experience_level)

        # Assess risk tolerance and get recommendations
        risk_tolerance = risk_assessment.assess_risk_tolerance()
        investment_strategy = risk_assessment.recommend_investment_strategy()

        # Output results
        print(f"Risk Tolerance: {risk_tolerance}")
        print(investment_strategy)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
