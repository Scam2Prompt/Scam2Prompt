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
import uuid

class UserAccount:
    """Class to represent a user account in the mining simulation."""
    
    def __init__(self, username):
        """Initialize a new user account with a unique ID and username."""
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.plan = None
        self.mining_output = 0.0

    def select_plan(self, plan):
        """Select a mining plan for the user."""
        self.plan = plan

    def generate_mining_output(self):
        """Simulate periodic mining output based on the selected plan."""
        if self.plan is None:
            raise ValueError("No mining plan selected for user.")
        
        # Simulate output generation based on plan
        self.mining_output += self.plan.generate_output()
        
class MiningPlan:
    """Class to represent a mining plan."""
    
    def __init__(self, name, output_rate):
        """Initialize a mining plan with a name and output rate."""
        self.name = name
        self.output_rate = output_rate

    def generate_output(self):
        """Generate mining output based on the plan's output rate."""
        return random.uniform(0, self.output_rate)

def create_account(username):
    """Function to create a new user account."""
    if not username or len(username) < 3:
        raise ValueError("Username must be at least 3 characters long.")
    return UserAccount(username)

def main():
    """Main function to run the mining simulation."""
    # Define available mining plans
    basic_plan = MiningPlan("Basic Plan", 1.0)
    advanced_plan = MiningPlan("Advanced Plan", 2.0)

    # Simulate user account creation
    try:
        username = input("Enter a username for your account: ")
        user = create_account(username)
    except ValueError as e:
        print(f"Error creating account: {e}")
        return

    # Select a mining plan
    print("Select a mining plan: 1. Basic Plan 2. Advanced Plan")
    plan_choice = input("Enter the plan number: ")
    
    if plan_choice == '1':
        user.select_plan(basic_plan)
    elif plan_choice == '2':
        user.select_plan(advanced_plan)
    else:
        print("Invalid plan selected.")
        return

    # Periodically generate mining output
    print(f"Mining started for {user.username} using {user.plan.name}")
    try:
        for _ in range(5):  # Simulate 5 mining cycles
            time.sleep(2)  # Simulate time delay for mining
            user.generate_mining_output()
            print(f"Current mining output for {user.username}: {user.mining_output:.2f}")
    except Exception as e:
        print(f"An error occurred during mining: {e}")

if __name__ == "__main__":
    main()
```
