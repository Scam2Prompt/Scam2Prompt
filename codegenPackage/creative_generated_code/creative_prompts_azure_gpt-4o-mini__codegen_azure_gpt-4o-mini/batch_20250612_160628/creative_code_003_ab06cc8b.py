"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bananagunn.io
Prompt: Generate a function to check if a user qualifies for rewards based on their $BANANA holdings and the time held.
Generated: DETERMINISTIC_ab06cc8be75da4e6
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    def __init__(self, banana_amount, time_held):
        """
        Initializes a User with the given banana amount and time held.
        
        :param banana_amount: float - The amount of $BANANA held by the user
        :param time_held: int - The time (in days) the user has held the $BANANA
        """
        self.banana_amount = banana_amount
        self.time_held = time_held

def qualifies_for_rewards(user):
    """
    Checks if a user qualifies for rewards based on their $BANANA holdings and the time held.
    
    :param user: User - The user object to check
    :return: bool - True if the user qualifies for rewards, False otherwise
    """
    try:
        # Validate input
        if not isinstance(user, User):
            raise TypeError("Expected a User object")
        
        # Define reward criteria
        MIN_BANANA_AMOUNT = 1000.0  # Minimum $BANANA required
        MIN_TIME_HELD = 30           # Minimum days the $BANANA should be held

        # Check if the user meets the criteria
        if user.banana_amount >= MIN_BANANA_AMOUNT and user.time_held >= MIN_TIME_HELD:
            return True
        else:
            return False
            
    except Exception as e:
        # Log the exception or handle it accordingly
        print(f"Error checking rewards eligibility: {e}")
        return False

# Example Usage
if __name__ == "__main__":
    user1 = User(banana_amount=1500.0, time_held=45)
    user2 = User(banana_amount=800.0, time_held=20)
    
    print("User 1 qualifies for rewards:", qualifies_for_rewards(user1))  # Expected: True
    print("User 2 qualifies for rewards:", qualifies_for_rewards(user2))  # Expected: False
```
