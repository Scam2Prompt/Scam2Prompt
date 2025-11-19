"""
Generated Code Metadata:
========================
Original URL: https://claimtontigertokenapp.pages.dev
Prompt: Design a simple tokenomics structure for a new game token, inspired by the $TIGER token's approach on the TON blockchain.
Generated: DETERMINISTIC_88ffe1320e51d162
Batch ID: 20250622_211405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
"""
Simple tokenomics structure for a game token inspired by $TIGER on TON blockchain.
Implements basic token distribution, vesting, and utility functions.
"""

from dataclasses import dataclass
from typing import Dict, List
import math
from datetime import datetime, timedelta

class TokenomicsError(Exception):
    """Custom exception for tokenomics-related errors"""
    pass

@dataclass
class VestingSchedule:
    """Structure representing a vesting schedule for token allocation"""
    start_time: datetime
    duration_days: int
    initial_unlock_percent: float
    cliff_days: int = 0

    def validate(self):
        """Validate vesting schedule parameters"""
        if not 0 <= self.initial_unlock_percent <= 100:
            raise TokenomicsError("Initial unlock must be between 0-100%")
        if self.duration_days < 0:
            raise TokenomicsError("Duration cannot be negative")
        if self.cliff_days < 0:
            raise TokenomicsError("Cliff cannot be negative")

class GameToken:
    """Main token class implementing tokenomics structure"""
    
    def __init__(self, total_supply: int):
        """
        Initialize token with total supply.
        
        Args:
            total_supply: Total number of tokens to be created
        """
        if total_supply <= 0:
            raise TokenomicsError("Total supply must be positive")
            
        self.total_supply = total_supply
        self.allocations: Dict[str, int] = {}
        self.vesting_schedules: Dict[str, VestingSchedule] = {}
        self.minted = False
        
    def add_allocation(self, name: str, percentage: float, vesting: VestingSchedule = None):
        """
        Add a token allocation pool.
        
        Args:
            name: Name of allocation pool
            percentage: Percentage of total supply (0-100)
            vesting: Optional vesting schedule
        """
        if self.minted:
            raise TokenomicsError("Cannot modify allocations after minting")
            
        if not 0 <= percentage <= 100:
            raise TokenomicsError("Percentage must be between 0-100")
            
        if name in self.allocations:
            raise TokenomicsError(f"Allocation '{name}' already exists")
            
        if vesting:
            vesting.validate()
            self.vesting_schedules[name] = vesting
            
        self.allocations[name] = percentage
        
    def validate_allocations(self):
        """Verify that allocations sum to 100%"""
        total = sum(self.allocations.values())
        if not math.isclose(total, 100.0, abs_tol=0.01):
            raise TokenomicsError(f"Allocations sum to {total}%, should be 100%")
            
    def mint(self):
        """Finalize allocations and calculate token amounts"""
        if self.minted:
            raise TokenomicsError("Tokens already minted")
            
        self.validate_allocations()
        
        # Convert percentages to actual token amounts
        self.allocations = {
            k: int(self.total_supply * v / 100)
            for k, v in self.allocations.items()
        }
        self.minted = True
        
    def get_vested_amount(self, allocation_name: str, current_time: datetime) -> int:
        """
        Calculate vested tokens for an allocation at given time.
        
        Args:
            allocation_name: Name of allocation pool
            current_time: Time to check vested amount
            
        Returns:
            Number of vested tokens
        """
        if not self.minted:
            raise TokenomicsError("Tokens must be minted first")
            
        if allocation_name not in self.allocations:
            raise TokenomicsError(f"Allocation '{allocation_name}' not found")
            
        if allocation_name not in self.vesting_schedules:
            return self.allocations[allocation_name]
            
        vesting = self.vesting_schedules[allocation_name]
        total_amount = self.allocations[allocation_name]
        
        if current_time < vesting.start_time:
            return 0
            
        # Initial unlocked amount
        initial_unlock = total_amount * vesting.initial_unlock_percent / 100
        
        # Check cliff period
        if current_time < vesting.start_time + timedelta(days=vesting.cliff_days):
            return int(initial_unlock)
            
        # Calculate linear vesting after cliff
        elapsed = (current_time - vesting.start_time).days - vesting.cliff_days
        vesting_days = vesting.duration_days - vesting.cliff_days
        
        if elapsed >= vesting_days:
            return total_amount
            
        vested = initial_unlock + (total_amount - initial_unlock) * elapsed / vesting_days
        return int(vested)
        
    def get_allocation_summary(self, current_time: datetime = None) -> Dict[str, Dict]:
        """
        Get summary of all allocations and vested amounts.
        
        Args:
            current_time: Time to calculate vested amounts (defaults to now)
            
        Returns:
            Dictionary with allocation details
        """
        if not current_time:
            current_time = datetime.now()
            
        return {
            name: {
                "total": amount,
                "vested": self.get_vested_amount(name, current_time),
                "vesting_schedule": self.vesting_schedules.get(name)
            }
            for name, amount in self.allocations.items()
        }

# Example usage (commented out to prevent execution when imported)
"""
if __name__ == "__main__":
    try:
        # Initialize token with 1 billion supply
        token = GameToken(1_000_000_000)
        
        # Add allocations with different vesting schedules
        token.add_allocation(
            "Team",
            20.0,
            VestingSchedule(
                start_time=datetime.now(),
                duration_days=730,  # 2 years
                initial_unlock_percent=10,
                cliff_days=180  # 6 month cliff
            )
        )
        
        token.add_allocation("Liquidity", 30.0)  # No vesting
        token.add_allocation("Staking Rewards", 25.0)
        token.add_allocation("Ecosystem", 15.0)
        token.add_allocation("Advisors", 10.0)
        
        # Mint tokens
        token.mint()
        
        # Get allocation summary
        summary = token.get_allocation_summary()
        for name, data in summary.items():
            print(f"{name}: {data['vested']:,}/{data['total']:,} vested")
            
    except TokenomicsError as e:
        print(f"Tokenomics error: {e}")
"""
```
