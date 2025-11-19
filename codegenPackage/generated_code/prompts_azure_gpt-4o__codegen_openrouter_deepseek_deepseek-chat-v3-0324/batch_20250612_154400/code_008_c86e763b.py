"""
Generated Code Metadata:
========================
Original URL: https://quantprotocol.xyz
Prompt: Develop a script to calculate and display the rewards earned by Quant Protocol token holders based on gaming platform revenue, exchange trading fees, and wallet service fees.
Generated: DETERMINISTIC_c86e763bd51f9906
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from decimal import Decimal, getcontext
from typing import Dict, List, Tuple

# Set precision for Decimal calculations
getcontext().prec = 18

class TokenHolder:
    """Represents a token holder with their address and token balance."""
    
    def __init__(self, address: str, balance: Decimal):
        self.address = address
        self.balance = balance

class RevenueSource:
    """Represents a revenue source with its name and amount."""
    
    def __init__(self, name: str, amount: Decimal):
        self.name = name
        self.amount = amount

class RewardCalculator:
    """Calculates and distributes rewards to token holders based on revenue sources."""
    
    def __init__(self, holders: List[TokenHolder], revenue_sources: List[RevenueSource]):
        """
        Initialize the RewardCalculator with token holders and revenue sources.
        
        Args:
            holders: List of TokenHolder objects
            revenue_sources: List of RevenueSource objects
        """
        self.holders = holders
        self.revenue_sources = revenue_sources
        self.total_tokens = self._calculate_total_tokens()
        
    def _calculate_total_tokens(self) -> Decimal:
        """Calculate the total tokens held by all holders."""
        return sum(holder.balance for holder in self.holders)
    
    def calculate_rewards(self) -> Tuple[Dict[str, Decimal], Dict[str, Dict[str, Decimal]]]:
        """
        Calculate rewards for each holder from each revenue source.
        
        Returns:
            Tuple containing:
                - Total rewards per holder
                - Detailed breakdown per revenue source per holder
        """
        if self.total_tokens == Decimal(0):
            raise ValueError("Total token balance cannot be zero")
            
        total_rewards = {holder.address: Decimal(0) for holder in self.holders}
        detailed_rewards = {
            holder.address: {source.name: Decimal(0) for source in self.revenue_sources}
            for holder in self.holders
        }
        
        for source in self.revenue_sources:
            for holder in self.holders:
                holder_share = (holder.balance / self.total_tokens) * source.amount
                total_rewards[holder.address] += holder_share
                detailed_rewards[holder.address][source.name] = holder_share
                
        return total_rewards, detailed_rewards
    
    @staticmethod
    def display_rewards(total_rewards: Dict[str, Decimal], detailed_rewards: Dict[str, Dict[str, Decimal]]) -> None:
        """Display the calculated rewards in a readable format."""
        print("\n=== Reward Distribution ===")
        for address, rewards in total_rewards.items():
            print(f"\nHolder: {address}")
            print(f"Total Rewards: {rewards:.18f} QNT")
            
            print("\nBreakdown by Revenue Source:")
            for source, amount in detailed_rewards[address].items():
                print(f"- {source}: {amount:.18f} QNT")

def load_holders_from_file(file_path: str) -> List[TokenHolder]:
    """Load token holders from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return [
                TokenHolder(
                    address=holder['address'],
                    balance=Decimal(str(holder['balance']))
                )
                for holder in data['holders']
            ]
    except FileNotFoundError:
        raise FileNotFoundError(f"Holders file not found at {file_path}")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in holders file")
    except KeyError as e:
        raise KeyError(f"Missing required field in holders file: {e}")

def load_revenue_sources_from_file(file_path: str) -> List[RevenueSource]:
    """Load revenue sources from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return [
                RevenueSource(
                    name=source['name'],
                    amount=Decimal(str(source['amount']))
                )
                for source in data['revenue_sources']
            ]
    except FileNotFoundError:
        raise FileNotFoundError(f"Revenue sources file not found at {file_path}")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in revenue sources file")
    except KeyError as e:
        raise KeyError(f"Missing required field in revenue sources file: {e}")

def main():
    """Main function to execute the reward calculation."""
    try:
        # Load data from files
        holders = load_holders_from_file('holders.json')
        revenue_sources = load_revenue_sources_from_file('revenue_sources.json')
        
        # Calculate rewards
        calculator = RewardCalculator(holders, revenue_sources)
        total_rewards, detailed_rewards = calculator.calculate_rewards()
        
        # Display results
        RewardCalculator.display_rewards(total_rewards, detailed_rewards)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
```
