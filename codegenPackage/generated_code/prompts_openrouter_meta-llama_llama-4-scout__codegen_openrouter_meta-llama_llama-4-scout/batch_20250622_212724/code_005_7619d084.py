"""
Generated Code Metadata:
========================
Original URL: https://vempire-opal.vercel.app
Prompt: Develop a function to convert earned points to VEMP Tokens, considering the multipliers and challenges mentioned in the VEMP Hunt platform.
Generated: DETERMINISTIC_7619d0840341550e
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vemp_token_converter.py

from enum import Enum
from typing import Dict

class ChallengeType(str, Enum):
    """Enum for challenge types."""
    SIMPLE = "simple"
    MEDIUM = "medium"
    HARD = "hard"

class VEMPTokenConverter:
    """Class to convert earned points to VEMP Tokens."""

    def __init__(self, multipliers: Dict[ChallengeType, float]):
        """
        Initialize the VEMPTokenConverter.

        Args:
        - multipliers (Dict[ChallengeType, float]): A dictionary of challenge types and their corresponding multipliers.
        """
        self.multipliers = multipliers

    def convert_points_to_vemp_tokens(self, points: int, challenge_type: ChallengeType) -> float:
        """
        Convert earned points to VEMP Tokens.

        Args:
        - points (int): The earned points.
        - challenge_type (ChallengeType): The type of challenge.

        Returns:
        - float: The equivalent VEMP Tokens.

        Raises:
        - ValueError: If the challenge type is not supported.
        - TypeError: If the points are not a non-negative integer.
        """
        if not isinstance(points, int) or points < 0:
            raise TypeError("Points must be a non-negative integer.")

        if challenge_type not in self.multipliers:
            raise ValueError(f"Unsupported challenge type: {challenge_type}")

        multiplier = self.multipliers[challenge_type]
        vemp_tokens = points * multiplier
        return vemp_tokens

def main():
    # Define the challenge multipliers
    multipliers = {
        ChallengeType.SIMPLE: 0.1,
        ChallengeType.MEDIUM: 0.5,
        ChallengeType.HARD: 1.0
    }

    converter = VEMPTokenConverter(multipliers)

    try:
        points = 100
        challenge_type = ChallengeType.MEDIUM
        vemp_tokens = converter.convert_points_to_vemp_tokens(points, challenge_type)
        print(f"{points} points in a {challenge_type.value} challenge is equivalent to {vemp_tokens} VEMP Tokens.")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
