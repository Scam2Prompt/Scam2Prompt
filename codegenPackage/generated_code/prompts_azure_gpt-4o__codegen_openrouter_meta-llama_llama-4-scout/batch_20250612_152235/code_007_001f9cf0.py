"""
Generated Code Metadata:
========================
Original URL: https://bafybeifzsc2fqkmtu3f77p3b3xr5mea4rugk5sb3zsww46ufwpltulpw3u.ipfs.dweb.link
Prompt: Write a script to simulate the emission of $SOPH token rewards over 36 months for node operators, ensuring compliance with the 3-month lock-up period after claiming.
Generated: DETERMINISTIC_001f9cf0e2f0a365
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class NodeOperator:
    def __init__(self, name):
        """
        Initialize a NodeOperator.

        Args:
            name (str): The name of the node operator.
        """
        self.name = name
        self.claim_date = None
        self.lock_up_end_date = None
        self.monthly_rewards = []

    def claim_rewards(self, current_date):
        """
        Claim rewards for the node operator.

        Args:
            current_date (datetime.date): The current date.

        Returns:
            bool: Whether the claim was successful.
        """
        if self.claim_date is not None:
            print(f"{self.name} has already claimed rewards on {self.claim_date}.")
            return False

        self.claim_date = current_date
        self.lock_up_end_date = current_date + datetime.timedelta(days=90)  # 3-month lock-up period
        print(f"{self.name} claimed rewards on {self.claim_date}. Lock-up period ends on {self.lock_up_end_date}.")
        return True

    def emit_monthly_rewards(self, current_date, soph_token_rewards):
        """
        Emit monthly rewards for the node operator.

        Args:
            current_date (datetime.date): The current date.
            soph_token_rewards (int): The number of $SOPH token rewards.

        Returns:
            bool: Whether the emission was successful.
        """
        if self.claim_date is None:
            print(f"{self.name} has not claimed rewards yet.")
            return False

        if current_date < self.lock_up_end_date:
            print(f"{self.name} is still in the lock-up period. Rewards cannot be emitted yet.")
            return False

        self.monthly_rewards.append((current_date, soph_token_rewards))
        print(f"Emitted {soph_token_rewards} $SOPH token rewards to {self.name} on {current_date}.")
        return True


def simulate_rewards(node_operators, soph_token_rewards, months):
    """
    Simulate the emission of $SOPH token rewards over a specified period.

    Args:
        node_operators (list[NodeOperator]): The list of node operators.
        soph_token_rewards (int): The number of $SOPH token rewards per month.
        months (int): The number of months to simulate.
    """
    current_date = datetime.date.today()

    for month in range(months):
        new_date = current_date + datetime.timedelta(days=month * 30)  # Approximate months

        for node_operator in node_operators:
            node_operator.emit_monthly_rewards(new_date, soph_token_rewards)


def main():
    node_operators = [
        NodeOperator("Node Operator 1"),
        NodeOperator("Node Operator 2"),
    ]

    soph_token_rewards = 1000
    months = 36

    # Claim rewards for node operators
    current_date = datetime.date.today()
    for node_operator in node_operators:
        node_operator.claim_rewards(current_date)

    # Simulate rewards emission
    simulate_rewards(node_operators, soph_token_rewards, months)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
