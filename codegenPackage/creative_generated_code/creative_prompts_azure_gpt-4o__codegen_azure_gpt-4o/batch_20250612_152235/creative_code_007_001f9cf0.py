"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifzsc2fqkmtu3f77p3b3xr5mea4rugk5sb3zsww46ufwpltulpw3u.ipfs.dweb.link
Prompt: Write a script to simulate the emission of $SOPH token rewards over 36 months for node operators, ensuring compliance with the 3-month lock-up period after claiming.
Generated: DETERMINISTIC_001f9cf0e2f0a365
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from datetime import datetime, timedelta

class TokenEmissionSimulator:
    def __init__(self, total_supply, emission_period_months, lockup_period_months):
        """
        Initialize the Token Emission Simulator.
        
        :param total_supply: Total amount of SOPH tokens available for rewards.
        :param emission_period_months: The total period (in months) over which tokens are emitted.
        :param lockup_period_months: The lock-up period (in months) for tokens after claiming.
        """
        self.total_supply = total_supply
        self.emission_period_months = emission_period_months
        self.lockup_period_months = lockup_period_months
        self.monthly_reward = total_supply / emission_period_months
        self.node_operators = {}

    def register_node_operator(self, operator_id):
        """
        Register a new node operator.
        
        :param operator_id: Unique identifier for the node operator.
        """
        if operator_id in self.node_operators:
            raise ValueError(f"Node operator {operator_id} is already registered.")
        self.node_operators[operator_id] = {
            "last_claimed": None,
            "reward_balance": 0,
            "locked_until": None
        }

    def distribute_rewards(self):
        """
        Distribute monthly rewards to all registered node operators.
        """
        for operator_id, data in self.node_operators.items():
            data["reward_balance"] += self.monthly_reward

    def claim_rewards(self, operator_id):
        """
        Allow a node operator to claim their rewards, observing the lock-up period.
        
        :param operator_id: Unique identifier for the node operator.
        """
        if operator_id not in self.node_operators:
            raise ValueError(f"Node operator {operator_id} is not registered.")
        
        operator_data = self.node_operators[operator_id]
        current_time = datetime.now()
        
        # Check lock-up period
        if operator_data["last_claimed"] and current_time < operator_data["locked_until"]:
            raise ValueError("Cannot claim rewards yet. Lock-up period is still active.")
        
        # Claim rewards
        claimed_rewards = operator_data["reward_balance"]
        operator_data["reward_balance"] = 0
        operator_data["last_claimed"] = current_time
        operator_data["locked_until"] = current_time + timedelta(days=self.lockup_period_months * 30)
        
        return claimed_rewards

    def simulate_emission(self):
        """
        Simulate the emission process over the entire emission period.
        """
        start_time = datetime.now()
        print(f"Emission started: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        for month in range(1, self.emission_period_months + 1):
            # Simulate monthly reward distribution
            self.distribute_rewards()
            print(f"Month {month}: Rewards distributed.")
            
            # Simulate a monthly time progression
            time.sleep(0.1)  # Short sleep to simulate the passage of time
        
        end_time = datetime.now()
        print(f"Emission ended: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")

# Example usage:
if __name__ == "__main__":
    # Initialize the simulator
    total_tokens = 1000000  # Total SOPH tokens
    emission_period = 36  # Emission period in months
    lockup_period = 3  # Lock-up period in months
    
    simulator = TokenEmissionSimulator(total_tokens, emission_period, lockup_period)
    
    # Register node operators
    simulator.register_node_operator("node1")
    simulator.register_node_operator("node2")
    
    # Simulate emission
    simulator.simulate_emission()
    
    # Example claiming rewards (after lock-up period)
    try:
        rewards = simulator.claim_rewards("node1")
        print(f"Node1 claimed {rewards} tokens.")
    except ValueError as e:
        print(e)
    
    try:
        rewards = simulator.claim_rewards("node2")
        print(f"Node2 claimed {rewards} tokens.")
    except ValueError as e:
        print(e)
```
