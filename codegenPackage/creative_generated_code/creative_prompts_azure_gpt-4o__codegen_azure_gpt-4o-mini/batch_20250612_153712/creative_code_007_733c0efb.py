"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-faqs.gitbook.io
Prompt: Write a program to calculate the marks cutoff for $SCR airdrop eligibility based on participation in Scroll activities, including Sessions and Canvas/badges.
Generated: DETERMINISTIC_733c0efb79c66bff
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AirdropEligibility:
    """
    A class to determine eligibility for SCR airdrop based on user participation
    in Scroll activities, such as Sessions and Canvas/badges.
    """

    def __init__(self):
        self.session_points = 0
        self.canvas_points = 0
        self.cutoff = 100  # Minimum points required for eligibility

    def add_session_points(self, points):
        """
        Add points based on the user's participation in sessions.

        :param points: Integer points earned from sessions, must be non-negative.
        :raises ValueError: If points are negative.
        """
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.session_points += points

    def add_canvas_points(self, points):
        """
        Add points based on the user's participation in canvas/badge activities.

        :param points: Integer points earned from canvas/badges, must be non-negative.
        :raises ValueError: If points are negative.
        """
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.canvas_points += points

    def total_points(self):
        """
        Calculate the total points accumulated from sessions and canvas activities.

        :return: Total points as an integer.
        """
        return self.session_points + self.canvas_points

    def is_eligible(self):
        """
        Determine if the user is eligible for the SCR airdrop based on total points.

        :return: Boolean indicating eligibility.
        """
        return self.total_points() >= self.cutoff

    def eligibility_status(self):
        """
        Provide a status message regarding airdrop eligibility.

        :return: A string message indicating eligibility status.
        """
        if self.is_eligible():
            return "Eligible for SCR airdrop."
        else:
            return "Not eligible for SCR airdrop. " \
                   f"You need {self.cutoff - self.total_points()} more points."

# Example usage:
if __name__ == "__main__":
    eligibility_checker = AirdropEligibility()
    
    try:
        eligibility_checker.add_session_points(60)
        eligibility_checker.add_canvas_points(50)

        print("Total Points:", eligibility_checker.total_points())
        print(eligibility_checker.eligibility_status())
    except ValueError as e:
        print(f"Error: {e}")
```
