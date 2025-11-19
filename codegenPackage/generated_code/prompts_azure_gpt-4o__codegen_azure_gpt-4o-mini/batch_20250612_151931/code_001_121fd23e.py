"""
Generated Code Metadata:
========================
Original URL: https://bananagunn.io
Prompt: Create a function that checks if a user's $BANANA holdings meet the minimum threshold of 50 tokens and ensures rewards forfeiture rules are applied if holdings drop below the required amount.
Generated: DETERMINISTIC_121fd23e744740a6
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class User:
    def __init__(self, username, banana_holdings):
        """
        Initialize a User instance.

        :param username: str - The username of the user.
        :param banana_holdings: float - The amount of BANANA tokens the user holds.
        """
        self.username = username
        self.banana_holdings = banana_holdings
        self.rewards_forfeited = False

    def check_banana_holdings(self):
        """
        Check if the user's BANANA holdings meet the minimum threshold of 50 tokens.
        If holdings drop below the threshold, apply rewards forfeiture rules.

        :return: str - A message indicating the status of the user's holdings.
        """
        MINIMUM_HOLDINGS = 50

        try:
            if self.banana_holdings >= MINIMUM_HOLDINGS:
                return f"{self.username} has sufficient BANANA holdings: {self.banana_holdings} tokens."
            else:
                self.forfeit_rewards()
                return (f"{self.username} has insufficient BANANA holdings: {self.banana_holdings} tokens. "
                        "Rewards have been forfeited.")
        except Exception as e:
            return f"An error occurred while checking holdings: {str(e)}"

    def forfeit_rewards(self):
        """
        Apply rewards forfeiture rules if holdings drop below the minimum threshold.
        """
        if not self.rewards_forfeited:
            # Logic to forfeit rewards can be implemented here
            self.rewards_forfeited = True
            print(f"{self.username}'s rewards have been forfeited due to insufficient holdings.")

# Example usage
if __name__ == "__main__":
    user1 = User("Alice", 60)
    print(user1.check_banana_holdings())  # Should indicate sufficient holdings

    user2 = User("Bob", 30)
    print(user2.check_banana_holdings())  # Should indicate insufficient holdings and forfeiture
```
