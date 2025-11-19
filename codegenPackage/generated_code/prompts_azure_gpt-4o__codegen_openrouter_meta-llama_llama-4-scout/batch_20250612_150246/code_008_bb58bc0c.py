"""
Generated Code Metadata:
========================
Original URL: https://walletconnectairdrop.network
Prompt: Create a program to calculate the distribution of WalletConnect Tokens (WCT) based on engagement levels and criteria thresholds for airdrop participants.
Generated: DETERMINISTIC_bb58bc0c51d7511f
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# wallet_connect_token_distribution.py

from enum import Enum
from typing import List, Dict

class EngagementLevel(Enum):
    """Enum for engagement levels"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Participant:
    """Class to represent an airdrop participant"""
    def __init__(self, id: int, engagement_score: float):
        self.id = id
        self.engagement_score = engagement_score

def calculate_distribution(participants: List[Participant], 
                           low_threshold: float, 
                           medium_threshold: float, 
                           total_tokens: int) -> Dict[int, int]:
    """
    Calculate the distribution of WalletConnect Tokens (WCT) based on engagement levels.

    Args:
    - participants (List[Participant]): List of airdrop participants
    - low_threshold (float): Threshold for low engagement level
    - medium_threshold (float): Threshold for medium engagement level
    - total_tokens (int): Total number of tokens to distribute

    Returns:
    - Dict[int, int]: Dictionary with participant IDs as keys and their allocated tokens as values
    """
    # Initialize token distribution dictionary
    token_distribution = {}

    # Calculate tokens for each engagement level
    low_engagement_tokens = int(total_tokens * 0.3)  # 30% for low engagement
    medium_engagement_tokens = int(total_tokens * 0.4)  # 40% for medium engagement
    high_engagement_tokens = total_tokens - low_engagement_tokens - medium_engagement_tokens

    # Distribute tokens based on engagement levels
    for participant in participants:
        if participant.engagement_score < low_threshold:
            # Low engagement level
            token_distribution[participant.id] = int(low_engagement_tokens / sum(1 for p in participants if p.engagement_score < low_threshold) or 1)
        elif participant.engagement_score < medium_threshold:
            # Medium engagement level
            token_distribution[participant.id] = int(medium_engagement_tokens / sum(1 for p in participants if low_threshold <= p.engagement_score < medium_threshold) or 1)
        else:
            # High engagement level
            token_distribution[participant.id] = int(high_engagement_tokens / sum(1 for p in participants if p.engagement_score >= medium_threshold) or 1)

    return token_distribution

def main():
    try:
        # Example usage
        participants = [
            Participant(1, 0.5),
            Participant(2, 0.8),
            Participant(3, 0.2),
            Participant(4, 0.9),
            Participant(5, 0.6)
        ]

        low_threshold = 0.4
        medium_threshold = 0.7
        total_tokens = 1000

        token_distribution = calculate_distribution(participants, low_threshold, medium_threshold, total_tokens)

        print("Token Distribution:")
        for participant_id, tokens in token_distribution.items():
            print(f"Participant {participant_id}: {tokens} WCT")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
