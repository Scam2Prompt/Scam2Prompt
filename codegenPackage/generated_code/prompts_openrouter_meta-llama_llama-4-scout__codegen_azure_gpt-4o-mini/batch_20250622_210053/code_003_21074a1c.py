"""
Generated Code Metadata:
========================
Original URL: https://everyworld-app.pages.dev
Prompt: Develop a function to calculate user points and rewards on a platform like Everyworld, considering factors such as user engagement, ad views, and environmental impact.
Generated: DETERMINISTIC_21074a1c7b7f9dd0
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class User:
    """
    A class to represent a user on the platform.
    """

    def __init__(self, user_id, engagement_score, ad_views, environmental_impact):
        """
        Initializes a new user with the given parameters.

        :param user_id: Unique identifier for the user
        :param engagement_score: Score representing user engagement (0-100)
        :param ad_views: Number of ads viewed by the user
        :param environmental_impact: Score representing the user's environmental impact (0-100)
        """
        self.user_id = user_id
        self.engagement_score = engagement_score
        self.ad_views = ad_views
        self.environmental_impact = environmental_impact

    def calculate_points(self):
        """
        Calculates the user points based on engagement, ad views, and environmental impact.

        :return: Total points calculated for the user
        :raises ValueError: If any input score is out of the expected range
        """
        # Validate input scores
        if not (0 <= self.engagement_score <= 100):
            raise ValueError("Engagement score must be between 0 and 100.")
        if self.ad_views < 0:
            raise ValueError("Ad views cannot be negative.")
        if not (0 <= self.environmental_impact <= 100):
            raise ValueError("Environmental impact score must be between 0 and 100.")

        # Calculate points based on defined weights
        engagement_weight = 0.5
        ad_view_weight = 0.3
        environmental_weight = 0.2

        points = (self.engagement_score * engagement_weight +
                  self.ad_views * ad_view_weight +
                  (100 - self.environmental_impact) * environmental_weight)

        return round(points, 2)  # Return points rounded to 2 decimal places


def main():
    """
    Main function to demonstrate the User points calculation.
    """
    try:
        # Example user data
        user = User(user_id=1, engagement_score=85, ad_views=50, environmental_impact=20)
        total_points = user.calculate_points()
        print(f"User ID: {user.user_id}, Total Points: {total_points}")

    except ValueError as e:
        print(f"Error calculating points: {e}")


if __name__ == "__main__":
    main()
```
