"""
Generated Code Metadata:
========================
Original URL: https://minerlab.org
Prompt: Write code to simulate MinerLab's mining process, including account creation, plan selection, and periodic mining output generation.
Generated: DETERMINISTIC_ed2a7e9460653844
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict

class Plan(Enum):
    """ Enum for mining plans """
    BASIC = 1
    PREMIUM = 2
    ENTERPRISE = 3

class MinerLab:
    """ Simulates MinerLab's mining process """

    def __init__(self):
        """ Initializes MinerLab with an empty accounts dictionary """
        self.accounts = {}

    def create_account(self, username: str, email: str) -> str:
        """ Creates a new account and returns the account ID """
        if username in self.accounts:
            raise ValueError("Username already exists")

        account_id = len(self.accounts) + 1
        self.accounts[account_id] = {
            "username": username,
            "email": email,
            "plan": None,
            "last_mining": None,
            "mining_output": []
        }
        return account_id

    def select_plan(self, account_id: int, plan: Plan) -> None:
        """ Selects a mining plan for the given account """
        if account_id not in self.accounts:
            raise ValueError("Account not found")

        self.accounts[account_id]["plan"] = plan

    def start_mining(self, account_id: int) -> None:
        """ Starts the mining process for the given account """
        if account_id not in self.accounts:
            raise ValueError("Account not found")

        account = self.accounts[account_id]
        if account["plan"] is None:
            raise ValueError("Plan not selected")

        account["last_mining"] = datetime.now()
        self.generate_mining_output(account_id)

    def generate_mining_output(self, account_id: int) -> None:
        """ Generates periodic mining output for the given account """
        if account_id not in self.accounts:
            raise ValueError("Account not found")

        account = self.accounts[account_id]
        plan = account["plan"]

        # Simulate mining output generation based on plan
        if plan == Plan.BASIC:
            output = 10
        elif plan == Plan.PREMIUM:
            output = 50
        elif plan == Plan.ENTERPRISE:
            output = 100
        else:
            raise ValueError("Invalid plan")

        account["mining_output"].append({
            "timestamp": datetime.now(),
            "output": output
        })

        # Schedule next mining output generation
        last_mining = account["last_mining"]
        account["last_mining"] = last_mining + timedelta(minutes=10)
        print(f"Account {account_id} mining output: {output}")

        # Run generate_mining_output every 10 minutes
        delay = 10 * 60  # 10 minutes in seconds
        time.sleep(delay)
        self.generate_mining_output(account_id)

    def get_account_info(self, account_id: int) -> Dict:
        """ Returns account information """
        if account_id not in self.accounts:
            raise ValueError("Account not found")

        account = self.accounts[account_id]
        return {
            "username": account["username"],
            "email": account["email"],
            "plan": account["plan"].name if account["plan"] else None,
            "mining_output": account["mining_output"]
        }

def main():
    miner_lab = MinerLab()

    # Create account
    account_id = miner_lab.create_account("john_doe", "john@example.com")
    print(f"Account created with ID: {account_id}")

    # Select plan
    miner_lab.select_plan(account_id, Plan.PREMIUM)
    print(f"Plan selected for account {account_id}: PREMIUM")

    # Start mining
    miner_lab.start_mining(account_id)

    # Get account info
    account_info = miner_lab.get_account_info(account_id)
    print("Account info:")
    print(account_info)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
```
