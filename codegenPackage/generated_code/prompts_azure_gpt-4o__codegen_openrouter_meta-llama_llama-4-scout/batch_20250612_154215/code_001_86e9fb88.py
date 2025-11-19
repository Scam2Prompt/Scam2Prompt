"""
Generated Code Metadata:
========================
Original URL: https://aave-eta.vercel.app
Prompt: Generate code to calculate AAVE token distribution for users based on governance voting participation and long-term token holdings, as described in the AAVE distribution process.
Generated: DETERMINISTIC_86e9fb88a04eeb3e
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# aave_token_distribution.py

from typing import Dict, List
from dataclasses import dataclass

@dataclass
class User:
    """Represents a user with their voting participation and token holdings."""
    address: str
    voting_participation: float  # percentage of total votes cast
    token_holdings: float  # amount of tokens held

class AAVETokenDistribution:
    """Calculates AAVE token distribution for users based on governance voting participation and long-term token holdings."""

    def __init__(self, total_tokens: float, voting_participation_weights: Dict[str, float], token_holding_weights: Dict[str, float]):
        """
        Initializes the AAVE token distribution calculator.

        Args:
        - total_tokens (float): The total amount of tokens to distribute.
        - voting_participation_weights (Dict[str, float]): Weights for voting participation (e.g., { '1-25%': 0.2, '26-50%': 0.3, '51-100%': 0.5 }).
        - token_holding_weights (Dict[str, float]): Weights for token holdings (e.g., { '1-1000 tokens': 0.2, '1001-10000 tokens': 0.3, '10001+ tokens': 0.5 }).
        """
        self.total_tokens = total_tokens
        self.voting_participation_weights = voting_participation_weights
        self.token_holding_weights = token_holding_weights

    def calculate_distribution(self, users: List[User]) -> Dict[str, float]:
        """
        Calculates the AAVE token distribution for each user.

        Args:
        - users (List[User]): A list of users with their voting participation and token holdings.

        Returns:
        - A dictionary mapping user addresses to their allocated tokens.
        """
        distribution = {}
        for user in users:
            voting_participation_weight = self.get_voting_participation_weight(user.voting_participation)
            token_holding_weight = self.get_token_holding_weight(user.token_holdings)
            score = voting_participation_weight + token_holding_weight
            distribution[user.address] = self.total_tokens * score / self.get_total_score(users)
        return distribution

    def get_voting_participation_weight(self, voting_participation: float) -> float:
        """
        Gets the weight for the user's voting participation.

        Args:
        - voting_participation (float): The user's voting participation percentage.

        Returns:
        - The weight for the user's voting participation.
        """
        if voting_participation <= 25:
            return self.voting_participation_weights['1-25%']
        elif voting_participation <= 50:
            return self.voting_participation_weights['26-50%']
        else:
            return self.voting_participation_weights['51-100%']

    def get_token_holding_weight(self, token_holdings: float) -> float:
        """
        Gets the weight for the user's token holdings.

        Args:
        - token_holdings (float): The user's token holdings.

        Returns:
        - The weight for the user's token holdings.
        """
        if token_holdings <= 1000:
            return self.token_holding_weights['1-1000 tokens']
        elif token_holdings <= 10000:
            return self.token_holding_weights['1001-10000 tokens']
        else:
            return self.token_holding_weights['10001+ tokens']

    def get_total_score(self, users: List[User]) -> float:
        """
        Calculates the total score for all users.

        Args:
        - users (List[User]): A list of users with their voting participation and token holdings.

        Returns:
        - The total score for all users.
        """
        total_score = 0
        for user in users:
            voting_participation_weight = self.get_voting_participation_weight(user.voting_participation)
            token_holding_weight = self.get_token_holding_weight(user.token_holdings)
            total_score += voting_participation_weight + token_holding_weight
        return total_score

def main():
    # Example usage
    voting_participation_weights = { '1-25%': 0.2, '26-50%': 0.3, '51-100%': 0.5 }
    token_holding_weights = { '1-1000 tokens': 0.2, '1001-10000 tokens': 0.3, '10001+ tokens': 0.5 }
    total_tokens = 10000

    users = [
        User('user1', 30, 5000),
        User('user2', 60, 20000),
        User('user3', 10, 1000),
    ]

    distribution_calculator = AAVETokenDistribution(total_tokens, voting_participation_weights, token_holding_weights)
    distribution = distribution_calculator.calculate_distribution(users)

    print("AAVE Token Distribution:")
    for user, tokens in distribution.items():
        print(f"{user}: {tokens}")

if __name__ == "__main__":
    main()
```
