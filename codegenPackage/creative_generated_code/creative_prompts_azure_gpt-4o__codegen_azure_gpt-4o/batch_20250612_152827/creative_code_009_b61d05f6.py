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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AIReputationCalculator:
    """
    A class to calculate the reputation score for an AI agent
    on the SingularityNET platform based on interactions and payment history.
    """

    def __init__(self):
        """
        Initialize the reputation calculator with default weights.
        """
        self.interaction_weight = 0.7  # Weight for interaction score
        self.payment_weight = 0.3      # Weight for payment score

    def calculate_interaction_score(self, interactions):
        """
        Calculate interaction score based on user ratings.
        
        Args:
            interactions (list of dict): List of interaction records, where each record
                                         contains 'rating' (int, 0-5) and 'interaction_count' (int).

        Returns:
            float: Normalized interaction score between 0 and 1.
        """
        try:
            total_rating = sum(interaction['rating'] * interaction['interaction_count'] for interaction in interactions)
            total_interactions = sum(interaction['interaction_count'] for interaction in interactions)
            
            if total_interactions == 0:
                return 0.0  # Avoid division by zero
            
            return total_rating / (total_interactions * 5)  # Normalize to range [0, 1]
        except Exception as e:
            logging.error("Error calculating interaction score: %s", e)
            raise

    def calculate_payment_score(self, payments):
        """
        Calculate payment score based on successful payments.
        
        Args:
            payments (list of dict): List of payment records, where each record contains 'amount' (float)
                                     and 'status' (str, 'successful' or 'failed').

        Returns:
            float: Normalized payment score between 0 and 1.
        """
        try:
            successful_payments = sum(payment['amount'] for payment in payments if payment['status'] == 'successful')
            total_payments = sum(payment['amount'] for payment in payments)
            
            if total_payments == 0:
                return 0.0  # Avoid division by zero
            
            return successful_payments / total_payments  # Normalize to range [0, 1]
        except Exception as e:
            logging.error("Error calculating payment score: %s", e)
            raise

    def calculate_reputation(self, interactions, payments):
        """
        Calculate the overall reputation score of the AI agent.
        
        Args:
            interactions (list of dict): List of interaction records.
            payments (list of dict): List of payment records.

        Returns:
            float: Overall reputation score between 0 and 1.
        """
        try:
            interaction_score = self.calculate_interaction_score(interactions)
            payment_score = self.calculate_payment_score(payments)
            
            # Weighted average of interaction and payment scores
            reputation_score = (
                self.interaction_weight * interaction_score +
                self.payment_weight * payment_score
            )
            
            return round(reputation_score, 4)  # Return score rounded to 4 decimal places
        except Exception as e:
            logging.error("Error calculating reputation score: %s", e)
            raise


# Example usage
if __name__ == "__main__":
    # Sample data
    interaction_data = [
        {'rating': 5, 'interaction_count': 10},
        {'rating': 4, 'interaction_count': 7},
        {'rating': 3, 'interaction_count': 3}
    ]

    payment_data = [
        {'amount': 100.0, 'status': 'successful'},
        {'amount': 50.0, 'status': 'failed'},
        {'amount': 150.0, 'status': 'successful'}
    ]

    # Create calculator instance
    calculator = AIReputationCalculator()

    # Calculate reputation score
    reputation_score = calculator.calculate_reputation(interaction_data, payment_data)

    # Output the result
    logging.info("The AI agent's reputation score is: %.4f", reputation_score)
```
