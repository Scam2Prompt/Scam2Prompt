"""
Generated Code Metadata:
========================
Original URL: https://immediatexport.co
Prompt: Create a function that evaluates an investor's readiness to start investing based on the criteria mentioned by Starlight Stakemarket.
Generated: DETERMINISTIC_7663be760ed8fdb8
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentReadinessEvaluator:
    def __init__(self, financial_stability, investment_knowledge, risk_tolerance, financial_goals):
        """
        Initializes the InvestmentReadinessEvaluator with the necessary criteria.

        :param financial_stability: bool - Indicates if the investor has stable finances.
        :param investment_knowledge: bool - Indicates if the investor has sufficient knowledge about investing.
        :param risk_tolerance: str - The investor's risk tolerance level ('low', 'medium', 'high').
        :param financial_goals: list - A list of financial goals the investor aims to achieve.
        """
        self.financial_stability = financial_stability
        self.investment_knowledge = investment_knowledge
        self.risk_tolerance = risk_tolerance
        self.financial_goals = financial_goals

    def evaluate_readiness(self):
        """
        Evaluates the investor's readiness to start investing based on the provided criteria.

        :return: str - A message indicating the investor's readiness status.
        """
        try:
            # Check if the investor has stable finances
            if not self.financial_stability:
                return "You should stabilize your finances before investing."

            # Check if the investor has sufficient investment knowledge
            if not self.investment_knowledge:
                return "Consider gaining more knowledge about investing before proceeding."

            # Check risk tolerance
            if self.risk_tolerance not in ['low', 'medium', 'high']:
                raise ValueError("Risk tolerance must be 'low', 'medium', or 'high'.")

            # Check if the investor has defined financial goals
            if not self.financial_goals:
                return "Define your financial goals to guide your investment strategy."

            # If all criteria are met, the investor is ready
            return "You are ready to start investing!"

        except Exception as e:
            return f"An error occurred during evaluation: {str(e)}"


# Example usage
if __name__ == "__main__":
    evaluator = InvestmentReadinessEvaluator(
        financial_stability=True,
        investment_knowledge=True,
        risk_tolerance='medium',
        financial_goals=['retirement', 'buying a house']
    )
    
    readiness_message = evaluator.evaluate_readiness()
    print(readiness_message)
```
