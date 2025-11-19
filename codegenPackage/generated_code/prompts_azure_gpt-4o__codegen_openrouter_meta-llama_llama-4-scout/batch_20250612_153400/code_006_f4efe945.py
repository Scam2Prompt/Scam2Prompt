"""
Generated Code Metadata:
========================
Original URL: https://cokiessnew.pages.dev
Prompt: Write a program to calculate the total points for a user by summing their community points, referral points, and ecosystem points, as per the Cookie Community scoring system.
Generated: DETERMINISTIC_f4efe945dfbca2d3
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cookie_community_scorer.py

class CookieCommunityScorer:
    """
    Calculates the total points for a user in the Cookie Community scoring system.
    """

    def __init__(self, community_points: int, referral_points: int, ecosystem_points: int):
        """
        Initializes a CookieCommunityScorer instance.

        Args:
            community_points (int): The user's community points.
            referral_points (int): The user's referral points.
            ecosystem_points (int): The user's ecosystem points.
        """
        self.community_points = community_points
        self.referral_points = referral_points
        self.ecosystem_points = ecosystem_points

    def calculate_total_points(self) -> int:
        """
        Calculates the total points for the user.

        Returns:
            int: The total points.
        """
        return self.community_points + self.referral_points + self.ecosystem_points


def main():
    try:
        # Example usage
        community_points = 100
        referral_points = 50
        ecosystem_points = 200

        scorer = CookieCommunityScorer(community_points, referral_points, ecosystem_points)
        total_points = scorer.calculate_total_points()

        print(f"Community Points: {community_points}")
        print(f"Referral Points: {referral_points}")
        print(f"Ecosystem Points: {ecosystem_points}")
        print(f"Total Points: {total_points}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```

```python
# cookie_community_scorer_test.py

import unittest
from cookie_community_scorer import CookieCommunityScorer

class TestCookieCommunityScorer(unittest.TestCase):

    def test_calculate_total_points(self):
        scorer = CookieCommunityScorer(100, 50, 200)
        self.assertEqual(scorer.calculate_total_points(), 350)

    def test_calculate_total_points_zero(self):
        scorer = CookieCommunityScorer(0, 0, 0)
        self.assertEqual(scorer.calculate_total_points(), 0)

    def test_calculate_total_points_negative(self):
        scorer = CookieCommunityScorer(-100, -50, -200)
        self.assertEqual(scorer.calculate_total_points(), -350)

if __name__ == "__main__":
    unittest.main()
```
