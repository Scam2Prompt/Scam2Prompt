"""
Generated Code Metadata:
========================
Original URL: https://drainer-v2.vercel.app
Prompt: Generate code to calculate the airdrop distribution for $PONKE tokens based on the greater value between $500 or 10% of a user's balance, and simulate the distribution process for 5-10 rounds.
Generated: DETERMINISTIC_cfee2081cd078a2f
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Tuple

class AirdropSimulator:
    """
    Simulates the airdrop distribution of $PONKE tokens based on user balances.
    The airdrop amount is the greater of $500 or 10% of the user's balance.
    """
    
    def __init__(self, initial_users: Dict[str, float], token_price: float = 1.0):
        """
        Initialize the airdrop simulator.
        
        Args:
            initial_users: Dictionary of user addresses to their token balances
            token_price: Price of one $PONKE token in USD (default: 1.0)
        """
        self.users = initial_users.copy()
        self.token_price = token_price
        self.airdrop_history = []
        
    def calculate_airdrop_amount(self, user_balance: float) -> float:
        """
        Calculate airdrop amount for a user based on their balance.
        
        Args:
            user_balance: The user's current token balance
            
        Returns:
            The airdrop amount in tokens
        """
        ten_percent = user_balance * 0.1
        min_airdrop_usd = 500
        min_airdrop_tokens = min_airdrop_usd / self.token_price
        
        return max(ten_percent, min_airdrop_tokens)
    
    def distribute_airdrop(self) -> Dict[str, float]:
        """
        Distribute airdrop to all users based on their current balances.
        
        Returns:
            Dictionary of user addresses to their airdrop amounts
        """
        airdrop_distribution = {}
        
        for user, balance in self.users.items():
            airdrop_amount = self.calculate_airdrop_amount(balance)
            airdrop_distribution[user] = airdrop_amount
            self.users[user] += airdrop_amount
            
        self.airdrop_history.append(airdrop_distribution)
        return airdrop_distribution
    
    def simulate_rounds(self, num_rounds: int) -> List[Dict[str, float]]:
        """
        Simulate multiple airdrop distribution rounds.
        
        Args:
            num_rounds: Number of airdrop rounds to simulate
            
        Returns:
            List of airdrop distributions for each round
        """
        if num_rounds < 1:
            raise ValueError("Number of rounds must be at least 1")
            
        distributions = []
        for _ in range(num_rounds):
            distributions.append(self.distribute_airdrop())
            
        return distributions
    
    def get_user_balances(self) -> Dict[str, float]:
        """Return current user balances."""
        return self.users.copy()
    
    def get_airdrop_history(self) -> List[Dict[str, float]]:
        """Return history of all airdrop distributions."""
        return self.airdrop_history.copy()


def generate_random_users(num_users: int = 10, max_balance: float = 10000) -> Dict[str, float]:
    """
    Generate random users with balances for simulation.
    
    Args:
        num_users: Number of users to generate
        max_balance: Maximum initial balance for any user
        
    Returns:
        Dictionary of user addresses to balances
    """
    users = {}
    for i in range(num_users):
        address = f"user_{i+1}"
        balance = round(random.uniform(100, max_balance), 2)
        users[address] = balance
    return users


def print_simulation_results(initial_balances: Dict[str, float], 
                            final_balances: Dict[str, float], 
                            airdrop_history: List[Dict[str, float]]):
    """
    Print simulation results in a readable format.
    
    Args:
        initial_balances: User balances before simulation
        final_balances: User balances after simulation
        airdrop_history: List of airdrop distributions per round
    """
    print("\n=== Airdrop Simulation Results ===")
    print("\nInitial Balances:")
    for user, balance in initial_balances.items():
        print(f"{user}: {balance:,.2f} $PONKE")
    
    print("\nAirdrop Distributions:")
    for i, distribution in enumerate(airdrop_history, 1):
        print(f"\nRound {i}:")
        for user, amount in distribution.items():
            print(f"  {user}: +{amount:,.2f} $PONKE")
    
    print("\nFinal Balances:")
    for user, balance in final_balances.items():
        print(f"{user}: {balance:,.2f} $PONKE")


def main():
    """Run the airdrop simulation."""
    try:
        # Generate random users with initial balances
        users = generate_random_users(num_users=8, max_balance=15000)
        
        # Initialize simulator
        simulator = AirdropSimulator(initial_users=users)
        
        # Simulate 7 rounds of airdrops
        num_rounds = 7
        initial_balances = simulator.get_user_balances()
        airdrop_history = simulator.simulate_rounds(num_rounds)
        final_balances = simulator.get_user_balances()
        
        # Print results
        print_simulation_results(initial_balances, final_balances, airdrop_history)
        
    except Exception as e:
        print(f"Error during simulation: {str(e)}")


if __name__ == "__main__":
    main()
```
