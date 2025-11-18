"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnectairdrop.network
Prompt: Create a program to calculate the distribution of WalletConnect Tokens (WCT) based on engagement levels and criteria thresholds for airdrop participants.
Generated: DETERMINISTIC_bb58bc0c51d7511f
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from decimal import Decimal, InvalidOperation

class AirdropDistributor:
    """
    A class to calculate the distribution of WalletConnect Tokens (WCT) 
    based on engagement levels and predefined criteria thresholds.
    """

    def __init__(self, total_tokens: Decimal, engagement_thresholds: dict):
        """
        Initializes the AirdropDistributor with total tokens to distribute
        and engagement thresholds.
        
        :param total_tokens: Total number of WCT tokens available for distribution.
        :param engagement_thresholds: Dictionary defining thresholds and 
                                       their corresponding weightings.
        """
        if total_tokens <= 0:
            raise ValueError("Total tokens must be greater than zero.")
        if not engagement_thresholds:
            raise ValueError("Engagement thresholds cannot be empty.")
        
        self.total_tokens = total_tokens
        self.engagement_thresholds = engagement_thresholds

    def calculate_distribution(self, participants: dict) -> dict:
        """
        Calculates the token distribution based on participant engagement levels.
        
        :param participants: Dictionary where keys are participant IDs and values
                             are their engagement scores.
        :return: Dictionary of participant IDs mapped to their token allocation.
        """
        # Validate input
        if not participants:
            raise ValueError("Participants list cannot be empty.")
        
        total_weight = Decimal(0)
        weighted_scores = {}

        # Calculate weights based on thresholds
        for participant, engagement_level in participants.items():
            weight = self.get_weight_for_engagement(engagement_level)
            weighted_scores[participant] = weight
            total_weight += weight

        if total_weight == 0:
            raise ValueError("Total weight is zero. Check engagement thresholds or participant data.")
        
        # Calculate token distribution
        distribution = {}
        for participant, weight in weighted_scores.items():
            distribution[participant] = (weight / total_weight) * self.total_tokens

        return distribution

    def get_weight_for_engagement(self, engagement_level: Decimal) -> Decimal:
        """
        Determines the weight of a participant based on their engagement level.
        
        :param engagement_level: The engagement level of the participant.
        :return: Weight assigned based on engagement level.
        """
        for threshold, weight in sorted(self.engagement_thresholds.items(), key=lambda x: x[0]):
            if engagement_level >= threshold:
                return weight
        return Decimal(0)  # Default weight if below all thresholds


# Example threshold and weighting criteria
engagement_thresholds = {
    Decimal(10): Decimal(1),    # Engagement of 10 or more gets weight 1
    Decimal(50): Decimal(2),    # Engagement of 50 or more gets weight 2
    Decimal(100): Decimal(3)    # Engagement of 100 or more gets weight 3
}

# Example usage
if __name__ == "__main__":
    import json

    # Total tokens to distribute
    TOTAL_TOKENS = Decimal(1000)

    # Engagement data for participants
    participants = {
        "user1": Decimal(15),
        "user2": Decimal(60),
        "user3": Decimal(5),
        "user4": Decimal(120)
    }

    try:
        # Initialize distributor
        distributor = AirdropDistributor(TOTAL_TOKENS, engagement_thresholds)
        
        # Calculate distribution
        distribution = distributor.calculate_distribution(participants)
        
        # Pretty-print the results
        print("Token Distribution:")
        print(json.dumps({k: float(v) for k, v in distribution.items()}, indent=4))

    except (ValueError, InvalidOperation) as e:
        print(f"Error: {e}")
```
