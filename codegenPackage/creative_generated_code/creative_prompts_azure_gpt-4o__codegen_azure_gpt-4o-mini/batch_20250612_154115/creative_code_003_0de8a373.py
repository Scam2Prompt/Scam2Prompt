"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim.leyeredgen.network
Prompt: Create a function to calculate accrued rewards for Phase 3 of the LayerEdge airdrop based on user points and wallet activity.
Generated: DETERMINISTIC_0de8a37349dc38ea
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AirdropCalculator:
    """
    A class to calculate accrued rewards for the LayerEdge airdrop based on user points and wallet activity.
    """

    def __init__(self, base_reward_rate: float, activity_multiplier: float):
        """
        Initializes the AirdropCalculator with base reward rate and activity multiplier.

        Args:
            base_reward_rate (float): The base rate for rewards calculation.
            activity_multiplier (float): Multiplier based on wallet activity to adjust rewards.
        """
        self.base_reward_rate = base_reward_rate
        self.activity_multiplier = activity_multiplier

    def calculate_rewards(self, user_points: int, wallet_activity: float) -> float:
        """
        Calculates the accrued rewards based on user points and wallet activity.

        Args:
            user_points (int): The total points accumulated by the user.
            wallet_activity (float): The activity level of the user's wallet.

        Returns:
            float: The total accrued rewards.

        Raises:
            ValueError: If user_points is negative or wallet_activity is negative.
        """
        if user_points < 0:
            raise ValueError("User points cannot be negative.")
        if wallet_activity < 0:
            raise ValueError("Wallet activity cannot be negative.")

        # Calculate base rewards from user points
        base_rewards = user_points * self.base_reward_rate
        
        # Adjust rewards based on wallet activity
        accrued_rewards = base_rewards * (1 + (wallet_activity * self.activity_multiplier))

        return accrued_rewards

# Example usage
if __name__ == "__main__":
    # Create an instance of AirdropCalculator with a base reward rate and activity multiplier
    calculator = AirdropCalculator(base_reward_rate=0.1, activity_multiplier=0.5)

    try:
        # Example values for user points and wallet activity
        user_points = 1000
        wallet_activity = 0.2  # 20% activity

        # Calculate and print the accrued rewards
        rewards = calculator.calculate_rewards(user_points, wallet_activity)
        print(f"Accrued rewards: {rewards:.2f}")
    except ValueError as e:
        print(f"Error calculating rewards: {e}")
```
