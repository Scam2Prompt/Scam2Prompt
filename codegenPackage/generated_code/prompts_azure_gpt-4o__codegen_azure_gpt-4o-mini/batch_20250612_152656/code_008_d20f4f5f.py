"""
Generated Code Metadata:
========================
Original URL: https://jesse-9y3.pages.dev
Prompt: Generate code to implement a limit on BASE contributions per user during the JESSE presale, ensuring fairness and compliance with the presale cap.
Generated: DETERMINISTIC_d20f4f5ffce873d2
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Presale:
    def __init__(self, presale_cap: float, max_contribution_per_user: float):
        """
        Initialize the presale with a cap and a maximum contribution limit per user.

        :param presale_cap: Total cap for the presale.
        :param max_contribution_per_user: Maximum contribution allowed per user.
        """
        self.presale_cap = presale_cap
        self.max_contribution_per_user = max_contribution_per_user
        self.total_contributions = 0.0
        self.user_contributions = {}

    def contribute(self, user_id: str, amount: float) -> str:
        """
        Allow a user to contribute to the presale.

        :param user_id: Unique identifier for the user.
        :param amount: Amount the user wishes to contribute.
        :return: Confirmation message or error message.
        """
        # Validate input
        if amount <= 0:
            return "Contribution amount must be greater than zero."
        
        if amount > self.max_contribution_per_user:
            return f"Contribution exceeds the maximum limit of {self.max_contribution_per_user} per user."

        # Check if user has already contributed
        current_user_contribution = self.user_contributions.get(user_id, 0.0)
        new_total_contribution = current_user_contribution + amount

        if new_total_contribution > self.max_contribution_per_user:
            return f"User has already contributed {current_user_contribution}. " \
                   f"Total contribution cannot exceed {self.max_contribution_per_user}."

        # Check if presale cap is reached
        if self.total_contributions + amount > self.presale_cap:
            return "Presale cap reached. Contribution cannot be accepted."

        # Process the contribution
        self.user_contributions[user_id] = new_total_contribution
        self.total_contributions += amount

        return f"Contribution of {amount} accepted from user {user_id}. " \
               f"Total contributions: {self.total_contributions}."

    def get_total_contributions(self) -> float:
        """
        Get the total contributions made during the presale.

        :return: Total contributions.
        """
        return self.total_contributions

    def get_user_contribution(self, user_id: str) -> float:
        """
        Get the contribution amount for a specific user.

        :param user_id: Unique identifier for the user.
        :return: Contribution amount for the user.
        """
        return self.user_contributions.get(user_id, 0.0)


# Example usage
if __name__ == "__main__":
    presale = Presale(presale_cap=100000.0, max_contribution_per_user=5000.0)

    print(presale.contribute("user1", 1000))  # Valid contribution
    print(presale.contribute("user1", 6000))  # Exceeds user limit
    print(presale.contribute("user2", 2000))  # Valid contribution
    print(presale.contribute("user1", 4000))  # Valid contribution
    print(presale.contribute("user3", 95000))  # Exceeds presale cap
    print(presale.get_total_contributions())  # Check total contributions
```
