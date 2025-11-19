"""
Generated Code Metadata:
========================
Original URL: https://quecko.com
Prompt: Design a tokenomics model for a new cryptocurrency project using Quecko's expertise in tokenization and compliance, ensuring regulatory adherence.
Generated: DETERMINISTIC_1b0abe3eb778ff77
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime, timedelta

class TokenomicsModel:
    """
    A class to represent the tokenomics model for a cryptocurrency project.
    """

    def __init__(self, total_supply, compliance_rules):
        """
        Initialize the tokenomics model.

        :param total_supply: Total supply of tokens for the project.
        :param compliance_rules: A dictionary of compliance rules to ensure regulatory adherence.
        """
        self.total_supply = total_supply
        self.compliance_rules = compliance_rules
        self.token_distribution = {}
        self.locked_tokens = {}

    def distribute_tokens(self, entity, amount):
        """
        Distribute tokens to an entity.

        :param entity: The name of the entity receiving the tokens.
        :param amount: The number of tokens to distribute.
        :raises ValueError: If the amount exceeds the available supply or violates compliance rules.
        """
        if amount > self.get_available_supply():
            raise ValueError("Insufficient token supply for distribution.")
        
        if not self._check_compliance(entity, amount):
            raise ValueError("Distribution violates compliance rules.")
        
        self.token_distribution[entity] = self.token_distribution.get(entity, 0) + amount

    def lock_tokens(self, entity, amount, lock_period_days):
        """
        Lock tokens for a specified period.

        :param entity: The name of the entity whose tokens are being locked.
        :param amount: The number of tokens to lock.
        :param lock_period_days: The number of days the tokens will be locked.
        :raises ValueError: If the entity does not have enough tokens to lock.
        """
        if self.token_distribution.get(entity, 0) < amount:
            raise ValueError("Insufficient tokens to lock.")
        
        lock_id = str(uuid.uuid4())
        unlock_date = datetime.now() + timedelta(days=lock_period_days)
        self.locked_tokens[lock_id] = {
            "entity": entity,
            "amount": amount,
            "unlock_date": unlock_date
        }
        self.token_distribution[entity] -= amount

    def unlock_tokens(self):
        """
        Unlock tokens that have reached their unlock date.
        """
        current_time = datetime.now()
        unlocked = []
        for lock_id, lock_info in list(self.locked_tokens.items()):
            if lock_info["unlock_date"] <= current_time:
                entity = lock_info["entity"]
                amount = lock_info["amount"]
                self.token_distribution[entity] = self.token_distribution.get(entity, 0) + amount
                unlocked.append(lock_id)
        
        for lock_id in unlocked:
            del self.locked_tokens[lock_id]

    def get_available_supply(self):
        """
        Get the available token supply.

        :return: The number of tokens available for distribution.
        """
        distributed = sum(self.token_distribution.values())
        locked = sum(lock_info["amount"] for lock_info in self.locked_tokens.values())
        return self.total_supply - distributed - locked

    def _check_compliance(self, entity, amount):
        """
        Check compliance rules for token distribution.

        :param entity: The name of the entity receiving the tokens.
        :param amount: The number of tokens to distribute.
        :return: True if the distribution complies with the rules, False otherwise.
        """
        # Example compliance rule: No single entity can hold more than 20% of the total supply.
        max_allowed = self.total_supply * 0.2
        current_balance = self.token_distribution.get(entity, 0)
        return (current_balance + amount) <= max_allowed

    def get_token_distribution(self):
        """
        Get the current token distribution.

        :return: A dictionary of entities and their token balances.
        """
        return self.token_distribution

    def get_locked_tokens(self):
        """
        Get the current locked tokens.

        :return: A dictionary of locked tokens with lock details.
        """
        return self.locked_tokens


# Example usage
if __name__ == "__main__":
    # Initialize tokenomics model with a total supply of 1,000,000 tokens
    compliance_rules = {"max_entity_hold_percentage": 20}  # Example compliance rule
    tokenomics = TokenomicsModel(total_supply=1_000_000, compliance_rules=compliance_rules)

    try:
        # Distribute tokens
        tokenomics.distribute_tokens(entity="EntityA", amount=100_000)
        tokenomics.distribute_tokens(entity="EntityB", amount=150_000)

        # Lock tokens
        tokenomics.lock_tokens(entity="EntityA", amount=50_000, lock_period_days=30)

        # Unlock tokens after the lock period
        tokenomics.unlock_tokens()

        # Print token distribution and locked tokens
        print("Token Distribution:", tokenomics.get_token_distribution())
        print("Locked Tokens:", tokenomics.get_locked_tokens())

    except ValueError as e:
        print("Error:", e)
```
