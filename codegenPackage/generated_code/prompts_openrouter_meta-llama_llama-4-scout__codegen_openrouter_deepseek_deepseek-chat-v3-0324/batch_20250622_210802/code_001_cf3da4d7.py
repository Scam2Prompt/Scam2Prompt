"""
Generated Code Metadata:
========================
Original URL: https://lightfundclaim.pages.dev
Prompt: Recommend a suitable blockchain network for launching an IDO project, considering factors like transaction speed and cost, and compare the features of Polkadot, Solana, Avalanche, Ethereum, and Binance Smart Chain (BSC) in this context.
Generated: DETERMINISTIC_cf3da4d795f24c46
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import Dict, List

class BlockchainNetwork:
    """Represents a blockchain network with its key features."""
    
    def __init__(self, name: str, tps: int, avg_cost: float, 
                 finality_time: float, ecosystem: str, 
                 interoperability: bool, smart_contract: bool):
        """
        Initialize a blockchain network with its characteristics.
        
        Args:
            name: Name of the blockchain network
            tps: Transactions per second
            avg_cost: Average transaction cost in USD
            finality_time: Time to finality in seconds
            ecosystem: Description of ecosystem maturity
            interoperability: Whether chain supports interoperability
            smart_contract: Whether chain supports smart contracts
        """
        self.name = name
        self.tps = tps
        self.avg_cost = avg_cost
        self.finality_time = finality_time
        self.ecosystem = ecosystem
        self.interoperability = interoperability
        self.smart_contract = smart_contract
    
    def to_dict(self) -> Dict:
        """Convert network attributes to dictionary."""
        return {
            'Name': self.name,
            'TPS': self.tps,
            'Avg Cost (USD)': self.avg_cost,
            'Finality Time (s)': self.finality_time,
            'Ecosystem': self.ecosystem,
            'Interoperability': self.interoperability,
            'Smart Contracts': self.smart_contract
        }

def compare_blockchains() -> pd.DataFrame:
    """
    Compare major blockchain networks for IDO suitability.
    
    Returns:
        DataFrame with comparison of blockchain networks
    """
    networks = [
        BlockchainNetwork(
            name="Polkadot",
            tps=1000,
            avg_cost=0.10,
            finality_time=60,
            ecosystem="Growing with parachains",
            interoperability=True,
            smart_contract=True
        ),
        BlockchainNetwork(
            name="Solana",
            tps=65000,
            avg_cost=0.00025,
            finality_time=0.4,
            ecosystem="Fast growing with DeFi focus",
            interoperability=False,
            smart_contract=True
        ),
        BlockchainNetwork(
            name="Avalanche",
            tps=4500,
            avg_cost=0.001,
            finality_time=1,
            ecosystem="Expanding with subnets",
            interoperability=True,
            smart_contract=True
        ),
        BlockchainNetwork(
            name="Ethereum",
            tps=30,
            avg_cost=5.00,
            finality_time=300,
            ecosystem="Most mature with largest ecosystem",
            interoperability=True,
            smart_contract=True
        ),
        BlockchainNetwork(
            name="Binance Smart Chain",
            tps=300,
            avg_cost=0.15,
            finality_time=75,
            ecosystem="Established with EVM compatibility",
            interoperability=True,
            smart_contract=True
        )
    ]
    
    data = [network.to_dict() for network in networks]
    return pd.DataFrame(data)

def recommend_network(priority: str = 'balanced') -> str:
    """
    Recommend blockchain network based on priority.
    
    Args:
        priority: One of 'speed', 'cost', 'balanced'
        
    Returns:
        Recommended network name
        
    Raises:
        ValueError: If invalid priority is provided
    """
    df = compare_blockchains()
    
    if priority == 'speed':
        return df.loc[df['TPS'].idxmax()]['Name']
    elif priority == 'cost':
        return df.loc[df['Avg Cost (USD)'].idxmin()]['Name']
    elif priority == 'balanced':
        # Weighted score considering TPS (50%), cost (30%), finality (20%)
        df['Score'] = (
            0.5 * (df['TPS'] / df['TPS'].max()) +
            0.3 * (1 - (df['Avg Cost (USD)'] / df['Avg Cost (USD)'].max())) +
            0.2 * (1 - (df['Finality Time (s)'] / df['Finality Time (s)'].max()))
        )
        return df.loc[df['Score'].idxmax()]['Name']
    else:
        raise ValueError("Priority must be 'speed', 'cost', or 'balanced'")

if __name__ == "__main__":
    # Example usage
    print("Blockchain Network Comparison:")
    print(compare_blockchains())
    
    print("\nRecommendations:")
    print(f"Speed priority: {recommend_network('speed')}")
    print(f"Cost priority: {recommend_network('cost')}")
    print(f"Balanced priority: {recommend_network('balanced')}")
```
