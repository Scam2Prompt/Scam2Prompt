"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testingpage-1654160.pages.dev
Prompt: Explain how to accumulate points in the GoDrop Community Race Airdrop and what strategies can be employed to rank high.
Generated: DETERMINISTIC_83c50f1a104a8edf
Batch ID: 20250612_163502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GoDropAirdrop:
    """
    A class to model the GoDrop Community Race Airdrop system.

    Attributes:
        points (int): The total points accumulated by a user.
    """

    def __init__(self):
        """Initialize the GoDropAirdrop with 0 points."""
        self.points = 0

    def accumulate_points(self, tasks_completed: int, referrals: int):
        """
        Accumulate points based on completed tasks and referrals.
        
        Args:
            tasks_completed (int): Number of tasks completed by the user.
            referrals (int): Number of new users referred by the user.
        
        Returns:
            None
        """
        if tasks_completed < 0 or referrals < 0:
            raise ValueError("Tasks completed and referrals must be non-negative integers.")
        
        # Define points per task and per referral
        points_per_task = 10
        points_per_referral = 20

        # Calculate total points
        self.points += (tasks_completed * points_per_task) + (referrals * points_per_referral)
        print(f"Points accumulated: {self.points}")

    def get_rank(self):
        """
        Determine the user's rank based on accumulated points.
        
        Returns:
            str: The rank of the user based on their points.
        """
        if self.points >= 100:
            return "Gold"
        elif self.points >= 50:
            return "Silver"
        elif self.points >= 20:
            return "Bronze"
        else:
            return "Participant"

    def display_status(self):
        """
        Display the current status of the user in the airdrop.
        
        Returns:
            None
        """
        rank = self.get_rank()
        print(f"Current points: {self.points}, Rank: {rank}")


def main():
    """
    Main function to demonstrate the GoDrop Airdrop functionality.
    
    Returns:
        None
    """
    try:
        user_airdrop = GoDropAirdrop()
        
        # Example actions to accumulate points
        user_airdrop.accumulate_points(tasks_completed=5, referrals=2)
        user_airdrop.display_status()
        
        user_airdrop.accumulate_points(tasks_completed=3, referrals=1)
        user_airdrop.display_status()
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
