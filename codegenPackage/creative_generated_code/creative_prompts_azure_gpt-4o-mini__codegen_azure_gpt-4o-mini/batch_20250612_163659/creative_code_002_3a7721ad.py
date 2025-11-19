"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iqratechpoint.pages.dev
Prompt: What are the steps to implement a rewards system for educators using IQRA Token on a learning management system?
Generated: DETERMINISTIC_3a7721ad688a53f6
Batch ID: 20250612_163659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rewards_system.py

class Educator:
    """Class representing an educator in the learning management system."""
    
    def __init__(self, name, iqra_token_balance=0):
        self.name = name
        self.iqra_token_balance = iqra_token_balance

    def add_tokens(self, amount):
        """Add IQRA tokens to the educator's balance."""
        if amount < 0:
            raise ValueError("Amount to add must be non-negative.")
        self.iqra_token_balance += amount
        print(f"{amount} IQRA tokens added. New balance: {self.iqra_token_balance}.")

    def deduct_tokens(self, amount):
        """Deduct IQRA tokens from the educator's balance."""
        if amount < 0:
            raise ValueError("Amount to deduct must be non-negative.")
        if amount > self.iqra_token_balance:
            raise ValueError("Insufficient balance to deduct tokens.")
        self.iqra_token_balance -= amount
        print(f"{amount} IQRA tokens deducted. New balance: {self.iqra_token_balance}.")

class RewardsSystem:
    """Class to manage the rewards system for educators."""
    
    def __init__(self):
        self.educators = {}

    def register_educator(self, educator_name):
        """Register a new educator in the rewards system."""
        if educator_name in self.educators:
            raise ValueError("Educator already registered.")
        self.educators[educator_name] = Educator(educator_name)
        print(f"Educator '{educator_name}' registered successfully.")

    def reward_educator(self, educator_name, amount):
        """Reward an educator with IQRA tokens."""
        if educator_name not in self.educators:
            raise ValueError("Educator not found.")
        if amount <= 0:
            raise ValueError("Reward amount must be greater than zero.")
        
        self.educators[educator_name].add_tokens(amount)

    def penalize_educator(self, educator_name, amount):
        """Penalize an educator by deducting IQRA tokens."""
        if educator_name not in self.educators:
            raise ValueError("Educator not found.")
        if amount <= 0:
            raise ValueError("Penalty amount must be greater than zero.")

        self.educators[educator_name].deduct_tokens(amount)

    def get_educator_balance(self, educator_name):
        """Retrieve the current IQRA token balance of an educator."""
        if educator_name not in self.educators:
            raise ValueError("Educator not found.")
        return self.educators[educator_name].iqra_token_balance

# Example usage
if __name__ == "__main__":
    # Create the rewards system
    rewards_system = RewardsSystem()

    # Register educators
    try:
        rewards_system.register_educator("Alice")
        rewards_system.register_educator("Bob")
        
        # Reward educators
        rewards_system.reward_educator("Alice", 50)
        rewards_system.reward_educator("Bob", 30)

        # Penalize an educator
        rewards_system.penalize_educator("Alice", 20)

        # Check balances
        print(f"Alice's balance: {rewards_system.get_educator_balance('Alice')}")
        print(f"Bob's balance: {rewards_system.get_educator_balance('Bob')}")

    except ValueError as e:
        print(f"Error: {e}")
```
