"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethena-transactions.pages.dev
Prompt: Create a leaderboard system that ranks users based on their $ENA token holdings using Ethena's data structure.
Generated: DETERMINISTIC_b76000e3c04cb45a
Batch ID: 20250612_151333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import heapq
from typing import List, Dict, Tuple

class Leaderboard:
    """
    A class to manage a leaderboard ranking users based on $ENA token holdings.
    """
    def __init__(self):
        # Dictionary to store user balances {user_id: balance}
        self.user_balances: Dict[str, float] = {}
        # Priority queue (min-heap) for efficient leaderboard queries
        self.leaderboard_heap: List[Tuple[float, str]] = []
        # Flag to track if the leaderboard needs rebuilding
        self.dirty: bool = False

    def update_user_balance(self, user_id: str, balance: float) -> None:
        """
        Updates the balance of a user.

        :param user_id: Unique identifier for the user.
        :param balance: The user's updated $ENA token balance.
        """
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        
        # Update the user's balance in the dictionary
        self.user_balances[user_id] = balance
        # Mark the leaderboard as dirty
        self.dirty = True

    def rebuild_leaderboard(self) -> None:
        """
        Rebuilds the leaderboard heap from the user balances.
        """
        # Convert the user balances dictionary into a list of tuples
        # Multiply balances by -1 so the heap works as a max-heap
        self.leaderboard_heap = [(-balance, user_id) for user_id, balance in self.user_balances.items()]
        # Heapify the list to create a valid heap
        heapq.heapify(self.leaderboard_heap)
        # Reset dirty flag
        self.dirty = False

    def get_top_users(self, top_n: int = 10) -> List[Tuple[str, float]]:
        """
        Retrieves the top users ranked by their $ENA token holdings.

        :param top_n: The number of top users to retrieve (default is 10).
        :return: A list of tuples containing user_id and balance, sorted from highest to lowest.
        """
        if top_n <= 0:
            raise ValueError("Parameter 'top_n' must be greater than 0.")
        
        # Rebuild the leaderboard heap if it's marked as dirty
        if self.dirty:
            self.rebuild_leaderboard()
        
        # Use nlargest to efficiently fetch the top N users from the heap
        top_users_heap = heapq.nlargest(top_n, self.leaderboard_heap)
        # Convert back to positive balance and return user_id with balance
        return [(user_id, -balance) for balance, user_id in top_users_heap]

# Example usage
if __name__ == "__main__":
    try:
        # Create the leaderboard instance
        leaderboard = Leaderboard()
        
        # Update user balances
        leaderboard.update_user_balance("user1", 150.5)
        leaderboard.update_user_balance("user2", 200.0)
        leaderboard.update_user_balance("user3", 50.0)
        leaderboard.update_user_balance("user4", 300.0)
        
        # Fetch the top users
        top_users = leaderboard.get_top_users(top_n=3)
        print("Top Users:", top_users)
    except Exception as e:
        print(f"Error: {e}")
```
