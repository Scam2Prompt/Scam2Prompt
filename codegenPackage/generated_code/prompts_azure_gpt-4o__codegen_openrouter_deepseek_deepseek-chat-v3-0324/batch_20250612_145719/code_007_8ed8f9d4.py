"""
Generated Code Metadata:
========================
Original URL: https://nft-eth30.vercel.app
Prompt: Write a program that simulates the redistribution of gETH tokens based on gas fees spent by multiple wallet addresses, using the proportional rewards model described on the website.
Generated: DETERMINISTIC_8ed8f9d439221b13
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from collections import defaultdict
from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 18

class TokenRedistribution:
    """
    Simulates the redistribution of gETH tokens based on gas fees spent by multiple wallet addresses.
    Uses a proportional rewards model where rewards are distributed based on the proportion of total gas spent.
    """
    
    def __init__(self, total_rewards):
        """
        Initialize the TokenRedistribution with the total rewards to be distributed.
        
        Args:
            total_rewards (Decimal): Total amount of gETH tokens to be redistributed
        """
        self.total_rewards = Decimal(total_rewards)
        self.wallet_data = defaultdict(Decimal)
        self.total_gas_spent = Decimal(0)
    
    def add_wallet_data(self, wallet_address, gas_spent):
        """
        Add wallet address and its corresponding gas spent to the dataset.
        
        Args:
            wallet_address (str): Wallet address
            gas_spent (Decimal or str): Amount of gas spent by the wallet
        """
        gas_spent = Decimal(gas_spent)
        self.wallet_data[wallet_address] += gas_spent
        self.total_gas_spent += gas_spent
    
    def calculate_rewards(self):
        """
        Calculate the proportional rewards for each wallet based on gas spent.
        
        Returns:
            dict: Dictionary mapping wallet addresses to their calculated rewards
        """
        if self.total_gas_spent == 0:
            raise ValueError("Total gas spent cannot be zero")
        
        rewards = {}
        for wallet, gas in self.wallet_data.items():
            proportion = gas / self.total_gas_spent
            reward = proportion * self.total_rewards
            rewards[wallet] = reward.normalize()  # Normalize to remove trailing zeros
        
        return rewards
    
    def save_results_to_file(self, rewards, filename="redistribution_results.json"):
        """
        Save the redistribution results to a JSON file.
        
        Args:
            rewards (dict): Dictionary of wallet addresses and their rewards
            filename (str): Name of the output file
        """
        # Convert Decimal to string for JSON serialization
        serializable_rewards = {wallet: str(reward) for wallet, reward in rewards.items()}
        
        with open(filename, 'w') as f:
            json.dump(serializable_rewards, f, indent=4)
    
    @staticmethod
    def load_wallet_data_from_file(filename):
        """
        Static method to load wallet data from a JSON file.
        
        Args:
            filename (str): Name of the input file
            
        Returns:
            tuple: (wallet_data, total_gas_spent)
        """
        with open(filename, 'r') as f:
            data = json.load(f)
        
        wallet_data = defaultdict(Decimal)
        total_gas = Decimal(0)
        
        for wallet, gas in data.items():
            gas = Decimal(gas)
            wallet_data[wallet] = gas
            total_gas += gas
        
        return wallet_data, total_gas

def main():
    try:
        # Example usage
        redistributor = TokenRedistribution(total_rewards="1000.0")  # 1000 gETH to redistribute
        
        # Add wallet data (could be loaded from file in production)
        redistributor.add_wallet_data("0xWallet1", "150.5")
        redistributor.add_wallet_data("0xWallet2", "230.75")
        redistributor.add_wallet_data("0xWallet3", "89.25")
        redistributor.add_wallet_data("0xWallet1", "50.0")  # Additional gas for Wallet1
        
        # Calculate and print rewards
        rewards = redistributor.calculate_rewards()
        print("Rewards Distribution:")
        for wallet, reward in rewards.items():
            print(f"{wallet}: {reward} gETH")
        
        # Save results to file
        redistributor.save_results_to_file(rewards)
        print("\nResults saved to 'redistribution_results.json'")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
