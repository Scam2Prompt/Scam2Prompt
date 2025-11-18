"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jesse-9y3.pages.dev
Prompt: Generate code to implement a limit on BASE contributions per user during the JESSE presale, ensuring fairness and compliance with the presale cap.
Generated: DETERMINISTIC_d20f4f5ffce873d2
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Presale:
    def __init__(self, presale_cap, max_contribution_per_user):
        """
        Initializes the presale with a specified cap and contribution limit per user.

        :param presale_cap: Total cap for the presale.
        :param max_contribution_per_user: Maximum contribution allowed per user.
        """
        self.presale_cap = presale_cap
        self.max_contribution_per_user = max_contribution_per_user
        self.total_contributed = 0
        self.user_contributions = {}

    def contribute(self, user_id, amount):
        """
        Allows a user to contribute to the presale.

        :param user_id: Identifier for the user.
        :param amount: Amount the user wants to contribute.
        :raises ValueError: If the contribution exceeds limits.
        :raises Exception: If the presale cap is reached.
        """
        if amount <= 0:
            raise ValueError("Contribution amount must be greater than zero.")
        
        if user_id in self.user_contributions:
            if self.user_contributions[user_id] + amount > self.max_contribution_per_user:
                raise ValueError("Contribution exceeds maximum allowed per user.")
        
        # Check if the total contributions exceed the presale cap
        if self.total_contributed + amount > self.presale_cap:
            raise Exception("Presale cap has been reached. No further contributions allowed.")
        
        # Update contributions
        self.total_contributed += amount
        self.user_contributions[user_id] = self.user_contributions.get(user_id, 0) + amount

        print(f"User {user_id} successfully contributed {amount}. Total contributed: {self.total_contributed}")

    def get_total_contributions(self):
        """
        Returns the total contributions made in the presale.

        :return: Total contributions.
        """
        return self.total_contributed

    def get_user_contribution(self, user_id):
        """
        Returns the contribution made by a specific user.

        :param user_id: Identifier for the user.
        :return: User's contribution amount.
        """
        return self.user_contributions.get(user_id, 0)


# Example Usage
if __name__ == "__main__":
    # Presale configuration
    presale = Presale(presale_cap=100000, max_contribution_per_user=5000)

    try:
        presale.contribute("user1", 2000)
        presale.contribute("user2", 6000)  # This will raise an error
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"Exception: {e}")

    # Display total contributions and individual contributions
    print(f"Total contributions: {presale.get_total_contributions()}")
    print(f"User1 contribution: {presale.get_user_contribution('user1')}")
    print(f"User2 contribution: {presale.get_user_contribution('user2')}")
```
