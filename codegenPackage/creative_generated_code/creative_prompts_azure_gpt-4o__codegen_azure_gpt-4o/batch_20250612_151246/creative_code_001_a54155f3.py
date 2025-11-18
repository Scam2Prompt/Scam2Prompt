"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itsnottestingitstestingblockusa.pages.dev
Prompt: Generate code to implement a leaderboard system that updates every minute, displaying user rankings based on credits earned through social media engagement tasks.
Generated: DETERMINISTIC_a54155f390483bdf
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from threading import Timer
import heapq

class Leaderboard:
    """
    Leaderboard system to track and update user rankings based on credits earned.
    """

    def __init__(self):
        # Dictionary to store user data in the format {user_id: credits}
        self.user_credits = {}
        # Min-heap to efficiently keep track of top performers
        self.leaderboard = []

    def add_or_update_user(self, user_id, credits):
        """
        Add a new user or update the credits of an existing user.
        
        Args:
            user_id (str): Unique identifier for the user.
            credits (int): Credits earned by the user.
        """
        if user_id in self.user_credits:
            # Update the user's credits
            self.user_credits[user_id] += credits
        else:
            # Add a new user
            self.user_credits[user_id] = credits
        
        # Rebuild the leaderboard to reflect updated credits
        self.update_leaderboard()

    def update_leaderboard(self):
        """
        Updates the leaderboard to reflect the current rankings.
        """
        # Transform the user_credits dictionary into a list of tuples (credits, user_id)
        self.leaderboard = [(-credits, user_id) for user_id, credits in self.user_credits.items()]
        # Use heapq to manage the min-heap for top rankings
        heapq.heapify(self.leaderboard)

    def get_top_users(self, n=10):
        """
        Retrieves the top N users based on credits.
        
        Args:
            n (int): The number of top users to retrieve. Defaults to 10.
        
        Returns:
            List[Tuple[str, int]]: A list of tuples in the format (user_id, credits).
        """
        top_users = heapq.nsmallest(n, self.leaderboard)
        return [(user_id, -credits) for credits, user_id in top_users]

    def display_leaderboard(self):
        """
        Displays the current leaderboard.
        """
        print("Leaderboard - Top Rankings:")
        top_users = self.get_top_users()
        for rank, (user_id, credits) in enumerate(top_users, start=1):
            print(f"Rank {rank}: User {user_id} - {credits} Credits")

# Function to simulate periodic updates
def periodic_update(leaderboard):
    """
    Function to simulate updating the leaderboard every minute.
    
    Args:
        leaderboard (Leaderboard): The Leaderboard instance to update.
    """
    # This simulates adding credits for users; in a real application,
    # this data would come from social media engagement tasks.
    simulated_data = {
        "user1": 15,
        "user2": 10,
        "user3": 25,
        "user4": 5,
        "user5": 30
    }
    print("Updating leaderboard...")
    for user_id, credits in simulated_data.items():
        leaderboard.add_or_update_user(user_id, credits)
    leaderboard.display_leaderboard()

# Main program entry point
def main():
    try:
        # Initialize the leaderboard
        leaderboard = Leaderboard()

        # Schedule updates every minute using a Timer loop
        def schedule_updates():
            periodic_update(leaderboard)
            Timer(60, schedule_updates).start()

        # Start the update loop
        schedule_updates()

    except KeyboardInterrupt:
        print("\nLeaderboard system terminated.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
