"""
Generated Code Metadata:
========================
Original URL: https://immediate-orbirex.com
Prompt: Write code to implement a basic investment risk assessment tool that evaluates market risk, credit risk, and liquidity risk, inspired by Immediate Orbirex's content.
Generated: DETERMINISTIC_c4d780f28e7ccaf1
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_risk_assessment_tool.py

class InvestmentRiskAssessmentTool:
    """
    A basic investment risk assessment tool that evaluates market risk, credit risk, and liquidity risk.
    """

    def __init__(self, investment_amount, market_volatility, credit_score, liquidity_ratio):
        """
        Initializes the investment risk assessment tool.

        Args:
        - investment_amount (float): The amount of investment.
        - market_volatility (float): The market volatility (in percentage).
        - credit_score (int): The credit score of the borrower (if applicable).
        - liquidity_ratio (float): The liquidity ratio of the investment.
        """
        self.investment_amount = investment_amount
        self.market_volatility = market_volatility
        self.credit_score = credit_score
        self.liquidity_ratio = liquidity_ratio

    def assess_market_risk(self):
        """
        Assesses the market risk based on the market volatility.

        Returns:
        - market_risk_score (float): The market risk score (between 0 and 1).
        """
        # Map market volatility to market risk score
        if self.market_volatility < 5:
            market_risk_score = 0.2
        elif self.market_volatility < 10:
            market_risk_score = 0.5
        else:
            market_risk_score = 0.8

        return market_risk_score

    def assess_credit_risk(self):
        """
        Assesses the credit risk based on the credit score.

        Returns:
        - credit_risk_score (float): The credit risk score (between 0 and 1).
        """
        # Map credit score to credit risk score
        if self.credit_score >= 750:
            credit_risk_score = 0.2
        elif self.credit_score >= 700:
            credit_risk_score = 0.4
        elif self.credit_score >= 650:
            credit_risk_score = 0.6
        else:
            credit_risk_score = 0.8

        return credit_risk_score

    def assess_liquidity_risk(self):
        """
        Assesses the liquidity risk based on the liquidity ratio.

        Returns:
        - liquidity_risk_score (float): The liquidity risk score (between 0 and 1).
        """
        # Map liquidity ratio to liquidity risk score
        if self.liquidity_ratio > 2:
            liquidity_risk_score = 0.2
        elif self.liquidity_ratio > 1.5:
            liquidity_risk_score = 0.4
        elif self.liquidity_ratio > 1:
            liquidity_risk_score = 0.6
        else:
            liquidity_risk_score = 0.8

        return liquidity_risk_score

    def calculate_overall_risk_score(self):
        """
        Calculates the overall risk score based on market risk, credit risk, and liquidity risk.

        Returns:
        - overall_risk_score (float): The overall risk score (between 0 and 1).
        """
        market_risk_score = self.assess_market_risk()
        credit_risk_score = self.assess_credit_risk()
        liquidity_risk_score = self.assess_liquidity_risk()

        overall_risk_score = (market_risk_score + credit_risk_score + liquidity_risk_score) / 3

        return overall_risk_score


def main():
    try:
        investment_amount = float(input("Enter the investment amount: "))
        market_volatility = float(input("Enter the market volatility (in percentage): "))
        credit_score = int(input("Enter the credit score: "))
        liquidity_ratio = float(input("Enter the liquidity ratio: "))

        risk_assessment_tool = InvestmentRiskAssessmentTool(investment_amount, market_volatility, credit_score, liquidity_ratio)

        market_risk_score = risk_assessment_tool.assess_market_risk()
        credit_risk_score = risk_assessment_tool.assess_credit_risk()
        liquidity_risk_score = risk_assessment_tool.assess_liquidity_risk()
        overall_risk_score = risk_assessment_tool.calculate_overall_risk_score()

        print("Market Risk Score: {:.2f}".format(market_risk_score))
        print("Credit Risk Score: {:.2f}".format(credit_risk_score))
        print("Liquidity Risk Score: {:.2f}".format(liquidity_risk_score))
        print("Overall Risk Score: {:.2f}".format(overall_risk_score))

        if overall_risk_score < 0.4:
            print("Risk Level: Low")
        elif overall_risk_score < 0.7:
            print("Risk Level: Moderate")
        else:
            print("Risk Level: High")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")


if __name__ == "__main__":
    main()
```
