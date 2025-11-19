"""
Generated Code Metadata:
========================
Original URL: https://dclinvest-sa.com
Prompt: Write a code snippet to screen potential investments based on environmental, social, and governance (ESG) criteria, as emphasized in DCL Invest's sustainable finance approach.
Generated: DETERMINISTIC_7e5908191eb160b9
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# esg_investment_screen.py

class Investment:
    """Represents a potential investment."""

    def __init__(self, name, esg_score, environmental_score, social_score, governance_score):
        """
        Initializes an Investment object.

        Args:
            name (str): Name of the investment.
            esg_score (float): Overall ESG score (0-100).
            environmental_score (float): Environmental score (0-100).
            social_score (float): Social score (0-100).
            governance_score (float): Governance score (0-100).
        """
        self.name = name
        self.esg_score = esg_score
        self.environmental_score = environmental_score
        self.social_score = social_score
        self.governance_score = governance_score


class ESGInvestmentScreen:
    """Screens potential investments based on ESG criteria."""

    def __init__(self, min_esg_score=50, min_environmental_score=40, min_social_score=40, min_governance_score=40):
        """
        Initializes an ESGInvestmentScreen object.

        Args:
            min_esg_score (int, optional): Minimum overall ESG score. Defaults to 50.
            min_environmental_score (int, optional): Minimum environmental score. Defaults to 40.
            min_social_score (int, optional): Minimum social score. Defaults to 40.
            min_governance_score (int, optional): Minimum governance score. Defaults to 40.
        """
        self.min_esg_score = min_esg_score
        self.min_environmental_score = min_environmental_score
        self.min_social_score = min_social_score
        self.min_governance_score = min_governance_score

    def screen_investments(self, investments):
        """
        Screens a list of investments based on ESG criteria.

        Args:
            investments (list[Investment]): List of Investment objects.

        Returns:
            list[Investment]: List of Investment objects that meet the ESG criteria.
        """
        screened_investments = []
        for investment in investments:
            try:
                if (investment.esg_score >= self.min_esg_score and
                    investment.environmental_score >= self.min_environmental_score and
                    investment.social_score >= self.min_social_score and
                    investment.governance_score >= self.min_governance_score):
                    screened_investments.append(investment)
            except Exception as e:
                print(f"Error screening investment {investment.name}: {str(e)}")
        return screened_investments


def main():
    # Example usage
    investments = [
        Investment("Company A", 70, 60, 80, 70),
        Investment("Company B", 40, 30, 50, 40),
        Investment("Company C", 90, 80, 90, 90),
    ]

    esg_screen = ESGInvestmentScreen(min_esg_score=60, min_environmental_score=50, min_social_score=70, min_governance_score=60)
    screened_investments = esg_screen.screen_investments(investments)

    print("Screened Investments:")
    for investment in screened_investments:
        print(f"Name: {investment.name}, ESG Score: {investment.esg_score}, Environmental Score: {investment.environmental_score}, Social Score: {investment.social_score}, Governance Score: {investment.governance_score}")


if __name__ == "__main__":
    main()
```
