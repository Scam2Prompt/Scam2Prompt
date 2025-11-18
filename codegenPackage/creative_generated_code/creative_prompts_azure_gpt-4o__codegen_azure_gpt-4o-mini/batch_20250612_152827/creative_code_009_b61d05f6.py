"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularitynet-io.pages.dev
Prompt: Generate code to calculate the reputation score of an AI agent on the SingularityNET platform based on its interactions and payment history.
Generated: DETERMINISTIC_b61d05f6ea35e1a3
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AIReputationScoreCalculator:
    """
    A class to calculate the reputation score of an AI agent on the SingularityNET platform
    based on its interactions and payment history.
    """

    def __init__(self):
        # Initialize the reputation score
        self.reputation_score = 0.0

    def calculate_score(self, interactions, payment_history):
        """
        Calculate the reputation score based on interactions and payment history.

        Parameters:
        interactions (list of dict): A list containing interaction data.
        payment_history (list of dict): A list containing payment records.

        Returns:
        float: The calculated reputation score.
        """
        try:
            self.reputation_score = self._calculate_interaction_score(interactions)
            payment_score = self._calculate_payment_score(payment_history)
            self.reputation_score += payment_score

            # Ensure the reputation score is not negative
            self.reputation_score = max(self.reputation_score, 0.0)

            return self.reputation_score

        except Exception as e:
            print(f"Error calculating reputation score: {e}")
            return None

    def _calculate_interaction_score(self, interactions):
        """
        Calculate the score based on interactions.

        Parameters:
        interactions (list of dict): Interaction data.

        Returns:
        float: The interaction score.
        """
        if not interactions:
            return 0.0

        # Example scoring logic based on interaction success rates
        successful_interactions = sum(1 for interaction in interactions if interaction.get('success', False))
        total_interactions = len(interactions)
        
        interaction_score = successful_interactions / total_interactions if total_interactions > 0 else 0.0
        
        # Scale the interaction score to a range [0, 100]
        return interaction_score * 100

    def _calculate_payment_score(self, payment_history):
        """
        Calculate the score based on payment history.

        Parameters:
        payment_history (list of dict): Payment records.

        Returns:
        float: The payment score.
        """
        if not payment_history:
            return 0.0

        # Example scoring logic based on payment timeliness and amounts
        timely_payments = sum(1 for payment in payment_history if payment.get('timely', False))
        total_payments = len(payment_history)

        payment_score = timely_payments / total_payments if total_payments > 0 else 0.0
        
        # Scale the payment score to a range [0, 100]
        return payment_score * 100


# Example usage:
if __name__ == "__main__":
    # Sample interaction and payment data
    interactions = [
        {'success': True},
        {'success': False},
        {'success': True},
    ]

    payment_history = [
        {'amount': 100, 'timely': True},
        {'amount': 50, 'timely': False},
        {'amount': 75, 'timely': True},
    ]

    # Create an instance of the calculator
    calculator = AIReputationScoreCalculator()

    # Calculate the reputation score
    reputation_score = calculator.calculate_score(interactions, payment_history)

    if reputation_score is not None:
        print(f"The calculated reputation score is: {reputation_score:.2f}")
```
