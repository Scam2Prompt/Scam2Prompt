"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard.smartglobalwealthfx.com
Prompt: Write code to simulate the principal return and instant withdrawal functionality for the investment plans offered by SmartglobalwealthFx.
Generated: DETERMINISTIC_4348dee728243746
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime

class InvestmentPlan:
    """
    Represents an investment plan with principal return and instant withdrawal functionality.
    """
    def __init__(self, investor_name, amount, duration):
        """
        Initialize an investment plan.

        :param investor_name: Name of the investor
        :param amount: Investment amount (principal)
        :param duration: Duration of the investment in days
        """
        self.investor_name = investor_name
        self.amount = amount
        self.duration = duration
        self.start_date = datetime.now()
        self.maturity_date = self.start_date + timedelta(days=duration)
        self.id = str(uuid.uuid4())  # Unique ID for the investment plan
        self.is_withdrawn = False  # Tracks if the investment has been withdrawn

    def return_principal(self):
        """
        Returns the principal amount to the investor after the plan matures.

        :return: Principal amount if the plan has matured, else an appropriate message
        """
        if self.is_withdrawn:
            return f"Investment ID {self.id}: Principal has already been returned."

        if datetime.now() >= self.maturity_date:
            self.is_withdrawn = True
            return f"Investment ID {self.id}: Principal amount ${self.amount} has been returned to {self.investor_name}."
        else:
            remaining_days = (self.maturity_date - datetime.now()).days
            return f"Investment ID {self.id}: Plan has not matured yet. {remaining_days} days remain."

    def instant_withdrawal(self):
        """
        Allows the investor to instantly withdraw the principal before maturity.

        :return: Confirmation of withdrawal
        """
        if self.is_withdrawn:
            return f"Investment ID {self.id}: Principal has already been withdrawn."

        self.is_withdrawn = True
        return f"Investment ID {self.id}: Principal amount ${self.amount} has been instantly withdrawn by {self.investor_name}."


# Example usage:
if __name__ == "__main__":
    try:
        # Create an investment plan
        plan = InvestmentPlan(investor_name="John Doe", amount=1000, duration=30)

        # Attempt to return principal before maturity
        print(plan.return_principal())

        # Perform an instant withdrawal
        print(plan.instant_withdrawal())

        # Attempt to return principal after withdrawal
        print(plan.return_principal())

    except Exception as e:
        # General error handling
        print(f"An error occurred: {e}")
```
