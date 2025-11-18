"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owlto-finance.top
Prompt: Develop a program to display a summary of a user's season stats, including Genesis NFTs staked, total quest points, and Genesis points.
Generated: DETERMINISTIC_21d51cf83194e397
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class UserStats:
    """
    A class to represent a user's season stats in a gaming application.
    Includes information about staked Genesis NFTs, total quest points, and Genesis points.
    """

    def __init__(self, user_id):
        """
        Initialize the UserStats object with the user's ID.
        
        Args:
            user_id (str): Unique identifier for the user.
        """
        self.user_id = user_id
        self.genesis_nfts_staked = 0
        self.total_quest_points = 0
        self.genesis_points = 0

    def update_stats(self, nfts_staked, quest_points, genesis_pts):
        """
        Update the user's stats with new values.
        
        Args:
            nfts_staked (int): The number of Genesis NFTs staked by the user.
            quest_points (int): The total quest points earned by the user.
            genesis_pts (int): The Genesis points accumulated by the user.

        Raises:
            ValueError: If any of the stats are negative.
        """
        if nfts_staked < 0 or quest_points < 0 or genesis_pts < 0:
            raise ValueError("Staked NFTs, quest points, and Genesis points must be non-negative.")
        
        self.genesis_nfts_staked = nfts_staked
        self.total_quest_points = quest_points
        self.genesis_points = genesis_pts

    def display_summary(self):
        """
        Display a summary of the user's season stats.
        """
        print(f"User ID: {self.user_id}")
        print(f"Genesis NFTs Staked: {self.genesis_nfts_staked}")
        print(f"Total Quest Points: {self.total_quest_points}")
        print(f"Genesis Points: {self.genesis_points}")

def main():
    """
    Main function to demonstrate the UserStats functionality.
    """
    try:
        user_id = input("Enter user ID: ")
        user_stats = UserStats(user_id)
        
        # Example data, in practice this data may come from a database or API
        nfts_staked = int(input("Enter number of Genesis NFTs staked: "))
        quest_points = int(input("Enter total quest points: "))
        genesis_pts = int(input("Enter Genesis points: "))
        
        user_stats.update_stats(nfts_staked, quest_points, genesis_pts)
        user_stats.display_summary()
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
