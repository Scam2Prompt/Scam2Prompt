"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mintether.netlify.app
Prompt: Develop a tool to create custom Ethereum visual coins and simulate market rewards, inspired by Mintether's "mint your way to wealth" functionality.
Generated: DETERMINISTIC_58ee6d385d3394b2
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json
from datetime import datetime

class EthereumCoin:
    """
    A class to represent a custom Ethereum-based visual coin.
    """

    def __init__(self, name, symbol, initial_supply):
        """
        Initializes a new Ethereum visual coin.

        :param name: The name of the coin.
        :param symbol: The symbol of the coin (e.g., ETH).
        :param initial_supply: The initial supply of the coin.
        """
        if not name or not symbol or initial_supply <= 0:
            raise ValueError("Invalid coin parameters.")
        
        self.name = name
        self.symbol = symbol
        self.supply = initial_supply
        self.holders = {}  # A mapping of addresses to balances
        self.market_rewards = []

    def mint(self, address, amount):
        """
        Mints new coins to a specified address.

        :param address: The wallet address to mint coins to.
        :param amount: The amount of coins to mint.
        """
        if amount <= 0:
            raise ValueError("Mint amount must be greater than zero.")
        if not address:
            raise ValueError("Invalid address.")
        
        self.holders[address] = self.holders.get(address, 0) + amount
        self.supply += amount

    def transfer(self, from_address, to_address, amount):
        """
        Transfers coins from one address to another.

        :param from_address: The sending wallet address.
        :param to_address: The receiving wallet address.
        :param amount: The amount of coins to transfer.
        """
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero.")
        if from_address not in self.holders or self.holders[from_address] < amount:
            raise ValueError("Insufficient balance.")
        if not to_address:
            raise ValueError("Invalid receiving address.")
        
        self.holders[from_address] -= amount
        if self.holders[from_address] == 0:
            del self.holders[from_address]  # Remove empty accounts
        self.holders[to_address] = self.holders.get(to_address, 0) + amount

    def simulate_market_reward(self, reward_pool):
        """
        Simulates market rewards by distributing a reward pool among holders.

        :param reward_pool: The total amount of rewards to distribute.
        """
        if reward_pool <= 0:
            raise ValueError("Reward pool must be greater than zero.")
        if not self.holders:
            raise ValueError("No coin holders to distribute rewards.")

        total_balance = sum(self.holders.values())
        if total_balance == 0:
            raise ValueError("Total balance of holders is zero.")

        rewards = {}
        for address, balance in self.holders.items():
            # Reward proportional to holder's balance
            rewards[address] = (balance / total_balance) * reward_pool
        
        for address, reward in rewards.items():
            self.holders[address] += reward
        
        self.market_rewards.append({
            "timestamp": datetime.now().isoformat(),
            "reward_pool": reward_pool,
            "distribution": rewards
        })

    def to_json(self):
        """
        Serializes the EthereumCoin object to JSON format.

        :return: A JSON representation of the EthereumCoin object.
        """
        return json.dumps({
            "name": self.name,
            "symbol": self.symbol,
            "supply": self.supply,
            "holders": self.holders,
            "market_rewards": self.market_rewards
        }, indent=4)


# Example usage:
if __name__ == "__main__":
    try:
        # Create a new custom Ethereum coin
        my_coin = EthereumCoin(name="CryptoWealth", symbol="CWTH", initial_supply=10000)
        
        # Mint new coins to addresses
        my_coin.mint("0xA1B2C3D4E5F6G7H8I9J0", 5000)
        my_coin.mint("0xB1C2D3E4F5G6H7I8J9K0", 3000)
        
        # Transfer coins between addresses
        my_coin.transfer("0xA1B2C3D4E5F6G7H8I9J0", "0xC1D2E3F4G5H6I7J8K9L0", 1000)
        
        # Simulate market rewards
        my_coin.simulate_market_reward(2000)
        
        # Serialize the coin object to JSON for inspection
        print(my_coin.to_json())
    
    except Exception as e:
        # Catch and print any errors
        print(f"Error: {e}")
```
