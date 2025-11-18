"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimmpeppe.web.app
Prompt: Generate code for a promotional airdrop system that distributes $MPEPE tokens to users based on specific criteria, such as social media engagement.
Generated: DETERMINISTIC_87dcd67d47fed9ab
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json
from typing import List, Dict

class AirdropSystem:
    def __init__(self, token_name: str, total_supply: float):
        """
        Initialize the AirdropSystem with the token name and total supply.
        
        :param token_name: Name of the token to be distributed
        :param total_supply: Total supply of the tokens available for the airdrop
        """
        self.token_name = token_name
        self.total_supply = total_supply
        self.participants = []

    def add_participant(self, user_id: str, engagement_score: float):
        """
        Add a participant to the airdrop if they meet engagement criteria.
        
        :param user_id: Unique identifier for the participant
        :param engagement_score: Score based on social media engagement
        :raises ValueError: If the engagement score is not valid
        """
        if engagement_score < 0:
            raise ValueError("Engagement score must be a non-negative value.")

        if engagement_score >= 10:  # Assuming 10 is the minimum score for eligibility
            self.participants.append({
                'user_id': user_id,
                'engagement_score': engagement_score
            })

    def distribute_tokens(self) -> List[Dict[str, float]]:
        """
        Distribute tokens to participants based on their engagement score.
        
        :return: List of participants and the amount of tokens they receive
        """
        total_engagement = sum(p['engagement_score'] for p in self.participants)

        if total_engagement == 0:
            return []  # No eligible participants

        distributions = []
        for participant in self.participants:
            proportion = participant['engagement_score'] / total_engagement
            tokens_awarded = proportion * self.total_supply
            distributions.append({
                'user_id': participant['user_id'],
                'tokens_awarded': tokens_awarded
            })

        return distributions

    def save_results(self, results: List[Dict[str, float]], filename: str):
        """
        Save the distribution results to a JSON file.
        
        :param results: Distribution results to be saved
        :param filename: Filename where results will be saved
        """
        try:
            with open(filename, 'w') as f:
                json.dump(results, f, indent=4)
        except IOError as e:
            print(f"An error occurred while saving results: {e}")

# Example usage of the AirdropSystem
if __name__ == "__main__":
    airdrop = AirdropSystem(token_name="$MPEPE", total_supply=10000.0)

    # Adding participants with their engagement scores
    try:
        airdrop.add_participant("user_1", 15.0)
        airdrop.add_participant("user_2", 25.0)
        airdrop.add_participant("user_3", 5.0)  # Not eligible
    except ValueError as e:
        print(e)

    # Distributing tokens
    distribution_results = airdrop.distribute_tokens()

    # Saving the results to a file
    airdrop.save_results(distribution_results, "airdrop_results.json")

    # Output to confirm the distribution
    print("Airdrop distribution completed.")
```
