"""
Generated Code Metadata:
========================
Original URL: https://moxie.community
Prompt: Create a script to calculate and distribute shared payouts using the Moxie Protocol, splitting rewards between members, channels, and the Farcaster Network.
Generated: DETERMINISTIC_68858ec4b0270fdd
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class PayoutRecipient:
    """Represents a recipient of the payout distribution."""
    address: str
    share: float

class MoxiePayoutCalculator:
    """
    Calculates and distributes payouts according to the Moxie Protocol.
    Splits rewards between members, channels, and the Farcaster Network.
    """
    
    def __init__(
        self,
        total_reward: float,
        member_share: float = 0.6,
        channel_share: float = 0.3,
        network_share: float = 0.1,
        precision: int = 8
    ):
        """
        Initialize the payout calculator with distribution shares.
        
        Args:
            total_reward: Total reward amount to distribute
            member_share: Percentage of reward for members (default: 0.6)
            channel_share: Percentage of reward for channels (default: 0.3)
            network_share: Percentage of reward for network (default: 0.1)
            precision: Decimal precision for calculations (default: 8)
        """
        self.total_reward = total_reward
        self.member_share = member_share
        self.channel_share = channel_share
        self.network_share = network_share
        self.precision = precision
        
        # Validate shares sum to 1
        total = member_share + channel_share + network_share
        if not math.isclose(total, 1.0, rel_tol=1e-9):
            raise ValueError("Shares must sum to 1.0")

    def calculate_payouts(
        self,
        members: List[Tuple[str, float]],
        channels: List[Tuple[str, float]],
        network_address: str
    ) -> Dict[str, List[PayoutRecipient]]:
        """
        Calculate the distribution of payouts to all recipients.
        
        Args:
            members: List of (member_address, contribution_weight) tuples
            channels: List of (channel_address, contribution_weight) tuples
            network_address: Address for the Farcaster Network share
            
        Returns:
            Dictionary with 'members', 'channels', and 'network' payout lists
        """
        # Validate inputs
        if not members:
            raise ValueError("At least one member must be specified")
        if not channels:
            raise ValueError("At least one channel must be specified")
        if not network_address:
            raise ValueError("Network address must be specified")

        # Calculate total weights
        total_member_weight = sum(weight for _, weight in members)
        total_channel_weight = sum(weight for _, weight in channels)

        # Calculate reward pools
        member_pool = round(self.total_reward * self.member_share, self.precision)
        channel_pool = round(self.total_reward * self.channel_share, self.precision)
        network_pool = round(self.total_reward * self.network_share, self.precision)

        # Distribute to members
        member_payouts = []
        for address, weight in members:
            share = round(weight / total_member_weight, self.precision)
            amount = round(member_pool * share, self.precision)
            member_payouts.append(PayoutRecipient(address, amount))

        # Distribute to channels
        channel_payouts = []
        for address, weight in channels:
            share = round(weight / total_channel_weight, self.precision)
            amount = round(channel_pool * share, self.precision)
            channel_payouts.append(PayoutRecipient(address, amount))

        # Network payout
        network_payout = [PayoutRecipient(network_address, network_pool)]

        return {
            "members": member_payouts,
            "channels": channel_payouts,
            "network": network_payout
        }

    def verify_payouts(self, payouts: Dict[str, List[PayoutRecipient]]) -> bool:
        """
        Verify that the sum of all payouts equals the total reward.
        
        Args:
            payouts: Dictionary of payout recipients
            
        Returns:
            bool: True if payout sums match total reward, False otherwise
        """
        total_distributed = 0.0
        
        for category in payouts.values():
            for recipient in category:
                total_distributed += recipient.share
                
        return math.isclose(total_distributed, self.total_reward, rel_tol=1e-9)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with total reward of 1000 units
        calculator = MoxiePayoutCalculator(total_reward=1000.0)
        
        # Define participants
        members = [
            ("member1", 1.0),
            ("member2", 2.0),
            ("member3", 3.0)
        ]
        
        channels = [
            ("channel1", 1.0),
            ("channel2", 1.0)
        ]
        
        network_address = "network_wallet"
        
        # Calculate payouts
        payouts = calculator.calculate_payouts(members, channels, network_address)
        
        # Verify and print results
        is_valid = calculator.verify_payouts(payouts)
        print(f"Payouts are valid: {is_valid}")
        
        print("\nMember Payouts:")
        for payout in payouts["members"]:
            print(f"{payout.address}: {payout.share:.8f}")
            
        print("\nChannel Payouts:")
        for payout in payouts["channels"]:
            print(f"{payout.address}: {payout.share:.8f}")
            
        print("\nNetwork Payout:")
        for payout in payouts["network"]:
            print(f"{payout.address}: {payout.share:.8f}")
            
    except ValueError as e:
        print(f"Error: {e}")
```
