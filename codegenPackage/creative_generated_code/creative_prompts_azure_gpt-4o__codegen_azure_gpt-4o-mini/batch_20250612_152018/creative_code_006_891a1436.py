"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cncrete.pages.dev
Prompt: Create a function to manage waitlist rankings and priority access for users in an appchain environment, similar to Concrete Protocol's approach.
Generated: DETERMINISTIC_891a143610f356f6
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WaitlistManager:
    def __init__(self):
        """
        Initializes the WaitlistManager with an empty waitlist.
        The waitlist is a list of tuples, each containing a user ID and their priority score.
        """
        self.waitlist = []

    def add_user(self, user_id: str, priority_score: int) -> None:
        """
        Adds a user to the waitlist with a given priority score.
        
        Parameters:
            user_id (str): The unique identifier for the user.
            priority_score (int): The priority score of the user (higher means more priority).
        
        Raises:
            ValueError: If the priority score is negative or if the user already exists in the waitlist.
        """
        if priority_score < 0:
            raise ValueError("Priority score must be non-negative.")
        
        if any(user[0] == user_id for user in self.waitlist):
            raise ValueError("User already exists in the waitlist.")

        self.waitlist.append((user_id, priority_score))
        self.waitlist.sort(key=lambda x: x[1], reverse=True)  # Higher scores first

    def remove_user(self, user_id: str) -> None:
        """
        Removes a user from the waitlist by user ID.
        
        Parameters:
            user_id (str): The unique identifier for the user.
        
        Raises:
            ValueError: If the user does not exist in the waitlist.
        """
        for index, (uid, _) in enumerate(self.waitlist):
            if uid == user_id:
                del self.waitlist[index]
                return
        
        raise ValueError("User not found in the waitlist.")

    def get_waitlist(self) -> list:
        """
        Returns a sorted list of users in the waitlist based on their priority scores.
        
        Returns:
            list: A list of tuples containing user IDs and their priority scores.
        """
        return self.waitlist

    def get_next_user(self) -> str:
        """
        Retrieves the user with the highest priority score from the waitlist.
        
        Returns:
            str: The user ID of the next user in line.
        
        Raises:
            IndexError: If the waitlist is empty.
        """
        if not self.waitlist:
            raise IndexError("Waitlist is empty.")
        
        return self.waitlist[0][0]  # Return user ID of the first user in the sorted list

    def prioritize_user(self, user_id: str, new_priority_score: int) -> None:
        """
        Updates the priority score of a user in the waitlist.
        
        Parameters:
            user_id (str): The unique identifier for the user.
            new_priority_score (int): The new priority score for the user.
        
        Raises:
            ValueError: If the priority score is negative or if the user is not found.
        """
        if new_priority_score < 0:
            raise ValueError("Priority score must be non-negative.")
        
        for index, (uid, _) in enumerate(self.waitlist):
            if uid == user_id:
                self.waitlist[index] = (uid, new_priority_score)  # Update priority score
                break
        else:
            raise ValueError("User not found in the waitlist.")
        
        self.waitlist.sort(key=lambda x: x[1], reverse=True)  # Re-sort after update

# Example usage (for demonstration purposes)
if __name__ == "__main__":
    wm = WaitlistManager()
    wm.add_user("user1", 10)
    wm.add_user("user2", 20)
    print(wm.get_waitlist())  # Expected output: [('user2', 20), ('user1', 10)]
    print(wm.get_next_user())  # Expected output: 'user2'
    wm.prioritize_user("user1", 25)
    print(wm.get_waitlist())  # Expected output: [('user1', 25), ('user2', 20)]
    wm.remove_user("user2")
    print(wm.get_waitlist())  # Expected output: [('user1', 25)]
```
