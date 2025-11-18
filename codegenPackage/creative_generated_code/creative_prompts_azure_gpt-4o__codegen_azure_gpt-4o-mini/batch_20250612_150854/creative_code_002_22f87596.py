"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediategains.org
Prompt: Create a step-by-step implementation plan for the debt snowball strategy mentioned on ImmediateGains, including code to prioritize and track debt payments.
Generated: DETERMINISTIC_22f8759631b8af12
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Debt:
    """
    Class to represent a debt with a name, amount owed, and interest rate.
    """
    def __init__(self, name, amount, interest_rate):
        self.name = name
        self.amount = amount
        self.interest_rate = interest_rate

    def __repr__(self):
        return f"{self.name}: ${self.amount:.2f} at {self.interest_rate}%"

class DebtSnowball:
    """
    Class to implement the Debt Snowball strategy for tracking and prioritizing debt payments.
    """
    def __init__(self):
        self.debts = []

    def add_debt(self, name, amount, interest_rate):
        """
        Adds a new debt to the list.

        :param name: Name of the debt
        :param amount: Amount owed
        :param interest_rate: Interest rate of the debt
        """
        if amount < 0:
            raise ValueError("Amount owed must be a non-negative value.")
        if interest_rate < 0:
            raise ValueError("Interest rate must be a non-negative value.")
        new_debt = Debt(name, amount, interest_rate)
        self.debts.append(new_debt)
        self.debts.sort(key=lambda x: x.amount)  # Sort debts by amount owed

    def pay_debt(self, debt_name, payment_amount):
        """
        Make a payment towards a specified debt.

        :param debt_name: The name of the debt to pay
        :param payment_amount: The amount to pay towards the debt
        """
        for debt in self.debts:
            if debt.name == debt_name:
                if payment_amount <= 0:
                    raise ValueError("Payment amount must be greater than zero.")
                if payment_amount > debt.amount:
                    raise ValueError("Payment amount exceeds the amount owed.")
                debt.amount -= payment_amount
                print(f"Paid ${payment_amount:.2f} towards {debt.name}. Remaining balance: ${debt.amount:.2f}")
                if debt.amount == 0:
                    self.debts.remove(debt)  # Remove debt if fully paid
                return
        raise ValueError("Debt not found.")

    def get_debts(self):
        """
        Returns a list of current debts.
        
        :return: List of current debts
        """
        return self.debts

    def total_debt(self):
        """
        Returns the total amount of remaining debt.

        :return: Total amount of remaining debt
        """
        return sum(debt.amount for debt in self.debts)

# Example usage
if __name__ == "__main__":
    try:
        debt_snowball = DebtSnowball()
        debt_snowball.add_debt("Credit Card 1", 5000, 20)
        debt_snowball.add_debt("Credit Card 2", 3000, 15)
        debt_snowball.add_debt("Car Loan", 15000, 5)

        print("Initial Debts:")
        for debt in debt_snowball.get_debts():
            print(debt)

        # Example payments
        debt_snowball.pay_debt("Credit Card 2", 500)
        debt_snowball.pay_debt("Credit Card 1", 2000)
        
        print("\nRemaining Debts after Payments:")
        for debt in debt_snowball.get_debts():
            print(debt)

        print(f"\nTotal Remaining Debt: ${debt_snowball.total_debt():.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
