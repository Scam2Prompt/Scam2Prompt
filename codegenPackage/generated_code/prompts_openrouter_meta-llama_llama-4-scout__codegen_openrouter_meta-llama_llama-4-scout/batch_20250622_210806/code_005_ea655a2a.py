"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-presales.pages.dev
Prompt: Design a function to evaluate the eligibility of an AI start-up for listing on the InQubeta NFT marketplace, based on the platform's evaluation criteria.
Generated: DETERMINISTIC_ea655a2aca1b2348
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# evaluation_criteria.py

class EvaluationCriteria:
    """Evaluation criteria for AI start-up eligibility on InQubeta NFT marketplace."""

    def __init__(self, 
                 team_experience: int, 
                 ai_technology: str, 
                 market_potential: int, 
                 prototype_status: str, 
                 funding_history: list):
        """
        Initialize evaluation criteria.

        Args:
        team_experience (int): Average team experience in years.
        ai_technology (str): Type of AI technology used.
        market_potential (int): Market potential score (1-10).
        prototype_status (str): Prototype status (e.g., 'concept', 'prototype', 'product').
        funding_history (list): List of funding rounds with amounts.
        """
        self.team_experience = team_experience
        self.ai_technology = ai_technology
        self.market_potential = market_potential
        self.prototype_status = prototype_status
        self.funding_history = funding_history

    def evaluate_team_experience(self) -> bool:
        """Evaluate team experience eligibility criterion."""
        # Assuming 5+ years of experience is required
        return self.team_experience >= 5

    def evaluate_ai_technology(self) -> bool:
        """Evaluate AI technology eligibility criterion."""
        # Assuming only 'machine_learning', 'deep_learning', 'natural_language_processing' are eligible
        eligible_technologies = ['machine_learning', 'deep_learning', 'natural_language_processing']
        return self.ai_technology in eligible_technologies

    def evaluate_market_potential(self) -> bool:
        """Evaluate market potential eligibility criterion."""
        # Assuming a market potential score of 7+ is required
        return self.market_potential >= 7

    def evaluate_prototype_status(self) -> bool:
        """Evaluate prototype status eligibility criterion."""
        # Assuming 'prototype' or 'product' status is required
        eligible_statuses = ['prototype', 'product']
        return self.prototype_status in eligible_statuses

    def evaluate_funding_history(self) -> bool:
        """Evaluate funding history eligibility criterion."""
        # Assuming at least 2 funding rounds with a total of $1M+ is required
        total_funding = sum(self.funding_history)
        return len(self.funding_history) >= 2 and total_funding >= 1000000

    def evaluate_eligibility(self) -> dict:
        """Evaluate overall eligibility of AI start-up."""
        eligibility_criteria = {
            'team_experience': self.evaluate_team_experience(),
            'ai_technology': self.evaluate_ai_technology(),
            'market_potential': self.evaluate_market_potential(),
            'prototype_status': self.evaluate_prototype_status(),
            'funding_history': self.evaluate_funding_history(),
        }

        eligible = all(eligibility_criteria.values())

        return {
            'eligible': eligible,
            'eligibility_criteria': eligibility_criteria,
        }


def main():
    try:
        evaluation_criteria = EvaluationCriteria(
            team_experience=7,
            ai_technology='machine_learning',
            market_potential=8,
            prototype_status='product',
            funding_history=[500000, 750000],
        )

        eligibility = evaluation_criteria.evaluate_eligibility()
        print("Eligible:", eligibility['eligible'])
        print("Eligibility Criteria:")
        for criterion, result in eligibility['eligibility_criteria'].items():
            print(f"{criterion.capitalize().replace('_', ' ')}: {result}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
