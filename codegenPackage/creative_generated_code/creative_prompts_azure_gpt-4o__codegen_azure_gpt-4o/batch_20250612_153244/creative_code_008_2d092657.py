"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapppeflobite.pages.dev
Prompt: Create a program to manage DeFi farming operations on the Swift Network, including validation and error handling for staking and unstaking.
Generated: DETERMINISTIC_2d09265787d745b5
Batch ID: 20250612_153244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import sys

# Define the supported operations and error messages
SUPPORTED_OPERATIONS = ["stake", "unstake"]
ERROR_MESSAGES = {
    "invalid_operation": "Invalid operation! Supported operations are 'stake' and 'unstake'.",
    "invalid_amount": "Invalid amount! Amount must be a positive number.",
    "amount_exceeds_balance": "Unstaking amount exceeds staked balance.",
}

# Initialize user balance for farming operations
class UserBalance:
    def __init__(self):
        self.staked_balance = 0.0

    def stake(self, amount):
        if amount <= 0:
            raise ValueError(ERROR_MESSAGES["invalid_amount"])
        self.staked_balance += amount
        return f"Successfully staked {amount}! Current staked balance: {self.staked_balance}"

    def unstake(self, amount):
        if amount <= 0:
            raise ValueError(ERROR_MESSAGES["invalid_amount"])
        if amount > self.staked_balance:
            raise ValueError(ERROR_MESSAGES["amount_exceeds_balance"])
        self.staked_balance -= amount
        return f"Successfully unstaked {amount}! Current staked balance: {self.staked_balance}"


# Function to manage DeFi farming operations
def manage_farming_operations(operation, amount):
    user_balance = UserBalance()

    try:
        if operation not in SUPPORTED_OPERATIONS:
            raise ValueError(ERROR_MESSAGES["invalid_operation"])
        if operation == "stake":
            return user_balance.stake(amount)
        elif operation == "unstake":
            return user_balance.unstake(amount)
    except ValueError as ve:
        return str(ve)
```
