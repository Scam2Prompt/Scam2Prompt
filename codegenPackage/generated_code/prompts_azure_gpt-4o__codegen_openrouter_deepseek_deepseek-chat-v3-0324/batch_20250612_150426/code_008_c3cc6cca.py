"""
Generated Code Metadata:
========================
Original URL: https://usdcprinter.xyz
Prompt: Create a Python script to simulate $UPRINT token transactions and calculate the USDC rewards distributed to holders based on the tokenomics described.
Generated: DETERMINISTIC_c3cc6cca9ace4915
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Tuple
from decimal import Decimal, getcontext
import random
from datetime import datetime, timedelta

# Set precision for Decimal calculations
getcontext().prec = 18

class UPRINTTokenSimulator:
    """
    Simulates UPRINT token transactions and calculates USDC rewards for holders based on tokenomics.
    
    Tokenomics:
    - 2% of every transaction is distributed as USDC rewards to holders proportionally.
    - 1% of every transaction is burned.
    - 1% of every transaction goes to the treasury.
    """
    
    def __init__(self, initial_supply: Decimal, initial_holders: Dict[str, Decimal], usdc_per_transaction: Decimal = Decimal('0.02')):
        """
        Initialize the simulator with initial token supply and holders.
        
        Args:
            initial_supply: Total initial supply of UPRINT tokens
            initial_holders: Dictionary of holder addresses and their balances
            usdc_per_transaction: Percentage of each transaction distributed as USDC rewards (default 2%)
        """
        self.total_supply = initial_supply
        self.holders = initial_holders.copy()
        self.usdc_rewards_pool = Decimal('0')
        self.usdc_per_transaction = usdc_per_transaction
        self.transaction_history = []
        self.reward_distribution_history = []
        
        # Validate initial holders
        total_allocated = sum(self.holders.values())
        if total_allocated > initial_supply:
            raise ValueError("Initial holders' balances exceed total supply")
    
    def execute_transaction(self, sender: str, recipient: str, amount: Decimal) -> bool:
        """
        Execute a token transaction between two addresses.
        
        Args:
            sender: Address sending tokens
            recipient: Address receiving tokens
            amount: Amount of tokens to transfer
            
        Returns:
            bool: True if transaction succeeded, False otherwise
        """
        try:
            # Validate transaction
            if sender not in self.holders:
                raise ValueError(f"Sender {sender} not found in holders")
            if self.holders[sender] < amount:
                raise ValueError(f"Insufficient balance for {sender}")
            if amount <= Decimal('0'):
                raise ValueError("Transaction amount must be positive")
            
            # Calculate fees and amounts
            burn_amount = amount * Decimal('0.01')
            treasury_amount = amount * Decimal('0.01')
            reward_amount = amount * self.usdc_per_transaction
            transfer_amount = amount - burn_amount - treasury_amount - reward_amount
            
            # Update balances
            self.holders[sender] -= amount
            self.holders[recipient] = self.holders.get(recipient, Decimal('0')) + transfer_amount
            
            # Handle burn (reduce total supply)
            self.total_supply -= burn_amount
            
            # Add to treasury (assuming treasury is a holder)
            self.holders['treasury'] = self.holders.get('treasury', Decimal('0')) + treasury_amount
            
            # Add to USDC rewards pool
            self.usdc_rewards_pool += reward_amount
            
            # Record transaction
            timestamp = datetime.now().isoformat()
            self.transaction_history.append({
                'timestamp': timestamp,
                'sender': sender,
                'recipient': recipient,
                'amount': float(amount),
                'burned': float(burn_amount),
                'treasury': float(treasury_amount),
                'rewards': float(reward_amount)
            })
            
            return True
        
        except Exception as e:
            print(f"Transaction failed: {str(e)}")
            return False
    
    def distribute_rewards(self) -> Dict[str, Decimal]:
        """
        Distribute accumulated USDC rewards to holders proportionally.
        
        Returns:
            Dict of addresses and their USDC rewards
        """
        if self.usdc_rewards_pool <= Decimal('0'):
            return {}
        
        total_tokens = sum(self.holders.values())
        if total_tokens <= Decimal('0'):
            return {}
        
        rewards = {}
        for address, balance in self.holders.items():
            if address == 'treasury':
                continue  # Treasury doesn't receive rewards
            
            share = balance / total_tokens
            reward = share * self.usdc_rewards_pool
            rewards[address] = reward
        
        # Record distribution
        timestamp = datetime.now().isoformat()
        self.reward_distribution_history.append({
            'timestamp': timestamp,
            'total_distributed': float(self.usdc_rewards_pool),
            'rewards': {k: float(v) for k, v in rewards.items()}
        })
        
        # Reset rewards pool
        self.usdc_rewards_pool = Decimal('0')
        
        return rewards
    
    def generate_random_transactions(self, num_transactions: int, holder_addresses: List[str]) -> None:
        """
        Generate random transactions between holders for simulation purposes.
        
        Args:
            num_transactions: Number of transactions to generate
            holder_addresses: List of holder addresses to include in transactions
        """
        if len(holder_addresses) < 2:
            raise ValueError("Need at least 2 holders for transactions")
        
        for _ in range(num_transactions):
            sender, recipient = random.sample(holder_addresses, 2)
            max_amount = self.holders[sender] * Decimal('0.1')  # Don't transfer more than 10% of balance
            amount = Decimal(random.uniform(0.1, float(max_amount)))
            self.execute_transaction(sender, recipient, amount)
    
    def get_holder_balances(self) -> Dict[str, Decimal]:
        """Return current holder balances."""
        return self.holders.copy()
    
    def get_total_supply(self) -> Decimal:
        """Return current total token supply."""
        return self.total_supply
    
    def get_transaction_history(self) -> List[Dict]:
        """Return transaction history."""
        return self.transaction_history.copy()
    
    def get_reward_distribution_history(self) -> List[Dict]:
        """Return reward distribution history."""
        return self.reward_distribution_history.copy()
    
    def save_state_to_file(self, filename: str) -> None:
        """Save current simulator state to a JSON file."""
        state = {
            'total_supply': str(self.total_supply),
            'holders': {k: str(v) for k, v in self.holders.items()},
            'usdc_rewards_pool': str(self.usdc_rewards_pool),
            'transaction_history': self.transaction_history,
            'reward_distribution_history': self.reward_distribution_history
        }
        
        with open(filename, 'w') as f:
            json.dump(state, f, indent=2)
    
    @classmethod
    def load_state_from_file(cls, filename: str) -> 'UPRINTTokenSimulator':
        """Load simulator state from a JSON file."""
        with open(filename, 'r') as f:
            state = json.load(f)
        
        initial_supply = Decimal(state['total_supply'])
        initial_holders = {k: Decimal(v) for k, v in state['holders'].items()}
        
        simulator = cls(initial_supply, initial_holders)
        simulator.usdc_rewards_pool = Decimal(state['usdc_rewards_pool'])
        simulator.transaction_history = state['transaction_history']
        simulator.reward_distribution_history = state['reward_distribution_history']
        
        return simulator


# Example usage
if __name__ == "__main__":
    # Initialize with 1,000,000 tokens and 10 holders
    initial_supply = Decimal('1000000')
    initial_holders = {
        f'holder_{i}': Decimal('100000') for i in range(1, 11)
    }
    
    simulator = UPRINTTokenSimulator(initial_supply, initial_holders)
    
    # Generate some random transactions
    holder_addresses = list(initial_holders.keys())
    simulator.generate_random_transactions(100, holder_addresses)
    
    # Distribute rewards
    rewards = simulator.distribute_rewards()
    print(f"Distributed rewards: {sum(rewards.values()):.2f} USDC")
    
    # Save state
    simulator.save_state_to_file('uprint_simulator_state.json')
    
    # Print final balances
    print("\nFinal holder balances:")
    for address, balance in simulator.get_holder_balances().items():
        print(f"{address}: {balance:.2f} UPRINT")
    
    print(f"\nTotal supply: {simulator.get_total_supply():.2f} UPRINT")
```
