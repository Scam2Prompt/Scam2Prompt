"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cokiessnew.pages.dev
Prompt: Write a program to calculate the total points for a user by summing their community points, referral points, and ecosystem points, as per the Cookie Community scoring system.
Generated: DETERMINISTIC_f4efe945dfbca2d3
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class UserPointsCalculator:
    """
    A class to calculate the total points for a user based on
    community points, referral points, and ecosystem points.
    """

    def __init__(self, community_points=0, referral_points=0, ecosystem_points=0):
        """
        Initializes the UserPointsCalculator with the given points.
        
        Parameters:
        community_points (int): The user's community points.
        referral_points (int): The user's referral points.
        ecosystem_points (int): The user's ecosystem points.
        """
        self.community_points = self.validate_points(community_points)
        self.referral_points = self.validate_points(referral_points)
        self.ecosystem_points = self.validate_points(ecosystem_points)

    @staticmethod
    def validate_points(points):
        """
        Validates that the points are integers and non-negative.
        
        Parameters:
        points (int): The points to validate.
        
        Returns:
        int: The validated points.
        
        Raises:
        ValueError: If points is not an integer or is negative.
        """
        if not isinstance(points, int):
            raise ValueError("Points must be an integer.")
        if points < 0:
            raise ValueError("Points cannot be negative.")
        return points

    def calculate_total_points(self):
        """
        Calculates the total points by summing community points,
        referral points, and ecosystem points.
        
        Returns:
        int: The total points for the user.
        """
        total_points = (self.community_points + 
                        self.referral_points + 
                        self.ecosystem_points)
        return total_points

def main():
    """
    Main function to execute the points calculation.
    """
    try:
        # Example input; in production, this could come from user input or other sources
        user = UserPointsCalculator(community_points=100, referral_points=50, ecosystem_points=30)
        
        total_points = user.calculate_total_points()
        print(f"Total points: {total_points}")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
