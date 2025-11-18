"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vetterplatform.pages.dev
Prompt: Provide code to track guaranteed allocations based on the proportion of preons owned by a user relative to the total preons in the community, as described on the Vetter platform.
Generated: DETERMINISTIC_8e84bffcee7adbd7
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PreonAllocationTracker:
    """
    A class to track guaranteed allocations based on the proportion of preons owned by a user
    relative to the total preons in the community.
    """

    def __init__(self):
        """
        Initializes an empty tracker for user preons and total community preons.
        """
        self.user_preons = {}
        self.total_preons = 0

    def add_user_preons(self, user_id: str, preon_amount: int) -> None:
        """
        Adds a specified amount of preons owned by a user.

        :param user_id: The unique identifier for the user.
        :param preon_amount: The amount of preons to add for the user.
        :raises ValueError: If preon_amount is negative or user_id is empty.
        """
        if preon_amount < 0:
            raise ValueError("Preon amount cannot be negative.")
        if not user_id:
            raise ValueError("User ID cannot be empty.")
        
        self.user_preons[user_id] = self.user_preons.get(user_id, 0) + preon_amount
        self.total_preons += preon_amount

    def remove_user_preons(self, user_id: str, preon_amount: int) -> None:
        """
        Removes a specified amount of preons from a user's account.

        :param user_id: The unique identifier for the user.
        :param preon_amount: The amount of preons to remove for the user.
        :raises ValueError: If preon_amount is negative, user_id is empty, or user does not have enough preons.
        """
        if preon_amount < 0:
            raise ValueError("Preon amount cannot be negative.")
        if not user_id:
            raise ValueError("User ID cannot be empty.")
        
        current_preons = self.user_preons.get(user_id, 0)
        if current_preons < preon_amount:
            raise ValueError("User does not have enough preons to remove.")
        
        self.user_preons[user_id] = current_preons - preon_amount
        self.total_preons -= preon_amount

    def get_user_allocation(self, user_id: str) -> float:
        """
        Calculates the guaranteed allocation for a user based on their preons owned.

        :param user_id: The unique identifier for the user.
        :return: The proportion of the user's preons relative to the total preons.
        :raises ValueError: If user_id is empty or total preons is zero.
        """
        if not user_id:
            raise ValueError("User ID cannot be empty.")
        if self.total_preons == 0:
            raise ValueError("Total preons in the community is zero.")
        
        user_preons = self.user_preons.get(user_id, 0)
        allocation = user_preons / self.total_preons
        return allocation

    def get_total_preons(self) -> int:
        """
        Returns the total amount of preons in the community.

        :return: The total preons.
        """
        return self.total_preons

    def clear_all_data(self) -> None:
        """
        Clears all stored user preons and resets total preons to zero.
        """
        self.user_preons.clear()
        self.total_preons = 0


# Example usage:
if __name__ == "__main__":
    tracker = PreonAllocationTracker()
    tracker.add_user_preons("user1", 100)
    tracker.add_user_preons("user2", 200)

    print(f"User1 Allocation: {tracker.get_user_allocation('user1'):.2%}")
    print(f"User2 Allocation: {tracker.get_user_allocation('user2'):.2%}")

    tracker.remove_user_preons("user1", 50)
    print(f"User1 Allocation after removal: {tracker.get_user_allocation('user1'):.2%}")
```
