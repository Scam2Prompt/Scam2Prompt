"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.klar.com.mx
Prompt: Generate code to implement Klar's "Tarjeta de Crédito con Garantía" feature, ensuring approval for users without a credit history.
Generated: DETERMINISTIC_4d65e12023e9829a
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    def __init__(self, user_id, credit_history=None):
        """
        Initialize a User instance.

        :param user_id: Unique identifier for the user.
        :param credit_history: List of past credit activities, if any.
        """
        self.user_id = user_id
        self.credit_history = credit_history or []

    def has_credit_history(self):
        """
        Check if the user has any credit history.

        :return: True if there is credit history, False otherwise.
        """
        return len(self.credit_history) > 0


class CreditCardWithGuarantee:
    def __init__(self, guarantee_amount):
        """
        Initialize the CreditCardWithGuarantee instance.

        :param guarantee_amount: The amount of guarantee set for the credit card.
        """
        self.guarantee_amount = guarantee_amount

    def approve_user(self, user):
        """
        Approve the user for the credit card based on their credit history.

        :param user: User instance to be approved.
        :return: Approval message.
        """
        if not isinstance(user, User):
            raise ValueError("Invalid user object provided.")

        if user.has_credit_history():
            return f"User {user.user_id} approved for Credit Card with Guarantee."
        else:
            return f"User {user.user_id} approved without credit history for Credit Card with Guarantee."


def main():
    # Example user with no credit history
    user1 = User(user_id='12345')
    
    # Example user with credit history
    user2 = User(user_id='67890', credit_history=['Loan', 'Credit Card'])

    # Instantiate the credit card feature
    credit_card_feature = CreditCardWithGuarantee(guarantee_amount=1000)

    # Attempt to approve users
    try:
        print(credit_card_feature.approve_user(user1))  # Expected to approve without credit history
        print(credit_card_feature.approve_user(user2))  # Expected to approve with credit history
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
