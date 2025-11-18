"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asdadw3qqd.pages.dev
Prompt: Create a function to calculate Puffer Points earned based on staking multipliers and user activity in Chapter 3 of the Puffy Rewards program.
Generated: DETERMINISTIC_a22be3699c356b40
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PufferPointsCalculator:
    """
    A class to calculate Puffer Points for the Puffy Rewards program based on staking multipliers and user activity.
    """

    def __init__(self, base_points: int):
        """
        Initializes the PufferPointsCalculator with a base point value.

        Args:
            base_points (int): The base points to calculate from.
        """
        if base_points < 0:
            raise ValueError("Base points must be a non-negative integer.")
        self.base_points = base_points

    def calculate_points(self, staking_multiplier: float, user_activity_score: float) -> int:
        """
        Calculates the total Puffer Points earned based on staking multipliers and user activity.

        Args:
            staking_multiplier (float): The multiplier based on staking level, should be greater than 0.
            user_activity_score (float): The score based on user activity, should be between 0 and 1.

        Returns:
            int: The total Puffer Points earned, rounded down to the nearest integer.

        Raises:
            ValueError: If staking_multiplier is not greater than 0, or if user_activity_score is not in range [0, 1].
        """
        if staking_multiplier <= 0:
            raise ValueError("Staking multiplier must be greater than 0.")
        if not (0 <= user_activity_score <= 1):
            raise ValueError("User activity score must be between 0 and 1.")

        # Calculate total points before rounding
        total_points = self.base_points * staking_multiplier * user_activity_score
        
        # Return the total points as an integer (rounded down)
        return int(total_points)

# Example usage:
if __name__ == "__main__":
    try:
        base_points = 100  # Example base points
        staking_multiplier = 2.5  # Example staking multiplier
        user_activity_score = 0.8  # Example user activity score

        calculator = PufferPointsCalculator(base_points)
        total_points = calculator.calculate_points(staking_multiplier, user_activity_score)

        print(f"Total Puffer Points earned: {total_points}")
    except ValueError as e:
        print(f"Error: {e}")
```
