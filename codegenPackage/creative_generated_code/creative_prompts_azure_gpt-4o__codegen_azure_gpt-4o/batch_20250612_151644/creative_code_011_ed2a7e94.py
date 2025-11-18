"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerlab.org
Prompt: Write code to simulate MinerLab's mining process, including account creation, plan selection, and periodic mining output generation.
Generated: DETERMINISTIC_ed2a7e9460653844
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class MinerLab:
    def __init__(self):
        self.accounts = {}
        self.plans = {
            'Basic': {'rate': 0.01, 'interval': 10},  # Rate per second, interval in seconds
            'Standard': {'rate': 0.05, 'interval': 5},
            'Premium': {'rate': 0.1, 'interval': 3}
        }

    # Create an account
    def create_account(self, username):
        if username in self.accounts:
            raise ValueError("Username already exists.")
        self.accounts[username] = {'plan': None, 'balance': 0}
        print(f"Account created for {username}.")

    # Select a mining plan for the account
    def select_plan(self, username, plan_name):
        if username not in self.accounts:
            raise ValueError("Account does not exist.")
        if plan_name not in self.plans:
            raise ValueError("Invalid plan selected.")
        self.accounts[username]['plan'] = self.plans[plan_name]
        print(f"{username} selected the {plan_name} plan.")

    # Start mining process
    def start_mining(self, username):
        if username not in self.accounts:
            raise ValueError("Account does not exist.")
        account = self.accounts[username]
        if account['plan'] is None:
            raise ValueError("No mining plan selected.")
        
        plan = account['plan']
        try:
            while True:
                # Generate mining output based on plan rate
                mined_amount = plan['rate'] * plan['interval']
                account['balance'] += mined_amount
                print(f"{username} mined {mined_amount:.2f} units. Total balance: {account['balance']:.2f}")
                
                # Wait for the plan's interval
                time.sleep(plan['interval'])
        except KeyboardInterrupt:
            print(f"Mining stopped for {username}. Final balance: {account['balance']:.2f}")
        except Exception as e:
            print(f"An error occurred during mining: {e}")

# Main program
if __name__ == "__main__":
    miner_lab = MinerLab()

    try:
        # Account creation
        miner_lab.create_account("Alice")
        miner_lab.create_account("Bob")

        # Plan selection
        miner_lab.select_plan("Alice", "Standard")
        miner_lab.select_plan("Bob", "Premium")

        # Start mining (will run indefinitely unless interrupted)
        print("Press Ctrl+C to stop mining.")
        miner_lab.start_mining("Alice")
    except Exception as e:
        print(f"Error: {e}")
```
