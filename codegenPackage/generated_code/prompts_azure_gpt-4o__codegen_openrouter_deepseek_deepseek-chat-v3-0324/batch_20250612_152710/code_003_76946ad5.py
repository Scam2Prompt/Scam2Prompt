"""
Generated Code Metadata:
========================
Original URL: https://moonedge-finance-io.web.app
Prompt: Create a tokenomics design for a blockchain project, including token utility, distribution, vesting schedule, and liquidity mechanisms, as described in MoonEdge's incubation program.
Generated: DETERMINISTIC_76946ad575e45942
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class TokenomicsDesign:
    """
    A class to design and manage tokenomics for a blockchain project.
    Includes token utility, distribution, vesting schedule, and liquidity mechanisms.
    """
    
    def __init__(self, token_name: str, token_symbol: str, total_supply: int):
        """
        Initialize the tokenomics design with basic token parameters.
        
        Args:
            token_name: Name of the token
            token_symbol: Symbol of the token
            total_supply: Total supply of tokens (in smallest unit)
        """
        self.token_name = token_name
        self.token_symbol = token_symbol
        self.total_supply = total_supply
        self.token_utility = {}
        self.distribution = {}
        self.vesting_schedules = {}
        self.liquidity_mechanisms = {}
        
    def add_token_utility(self, utility_name: str, description: str, percentage: float):
        """
        Add a token utility with its description and allocation percentage.
        
        Args:
            utility_name: Name of the utility (e.g., "Staking Rewards")
            description: Description of the utility
            percentage: Percentage of total supply allocated (0-100)
        """
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100")
            
        self.token_utility[utility_name] = {
            "description": description,
            "percentage": percentage,
            "amount": int(self.total_supply * (percentage / 100))
        }
        
    def add_distribution(self, category: str, percentage: float, recipients: List[str]):
        """
        Add a distribution category with percentage and recipients.
        
        Args:
            category: Distribution category (e.g., "Team", "Investors")
            percentage: Percentage of total supply allocated (0-100)
            recipients: List of recipient addresses
        """
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100")
            
        self.distribution[category] = {
            "percentage": percentage,
            "amount": int(self.total_supply * (percentage / 100)),
            "recipients": recipients
        }
        
    def add_vesting_schedule(
        self,
        category: str,
        cliff_period: int,
        vesting_period: int,
        vesting_interval: int,
        initial_unlock: float = 0
    ):
        """
        Add a vesting schedule for a distribution category.
        
        Args:
            category: Distribution category this applies to
            cliff_period: Days until vesting starts (cliff)
            vesting_period: Total days of vesting
            vesting_interval: Days between vesting events
            initial_unlock: Percentage unlocked at cliff (0-100)
        """
        if category not in self.distribution:
            raise ValueError(f"Distribution category {category} not found")
            
        if initial_unlock < 0 or initial_unlock > 100:
            raise ValueError("Initial unlock must be between 0 and 100")
            
        self.vesting_schedules[category] = {
            "cliff_period": cliff_period,
            "vesting_period": vesting_period,
            "vesting_interval": vesting_interval,
            "initial_unlock": initial_unlock
        }
        
    def add_liquidity_mechanism(
        self,
        name: str,
        description: str,
        percentage: float,
        lock_period: Optional[int] = None
    ):
        """
        Add a liquidity mechanism with optional lock period.
        
        Args:
            name: Name of the mechanism (e.g., "DEX Liquidity")
            description: Description of the mechanism
            percentage: Percentage of total supply allocated (0-100)
            lock_period: Optional days tokens are locked (None if no lock)
        """
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100")
            
        self.liquidity_mechanisms[name] = {
            "description": description,
            "percentage": percentage,
            "amount": int(self.total_supply * (percentage / 100)),
            "lock_period": lock_period
        }
        
    def calculate_vesting_schedule(self, category: str, start_date: datetime) -> Dict:
        """
        Calculate the detailed vesting schedule for a category.
        
        Args:
            category: Distribution category
            start_date: Project start date
            
        Returns:
            Dictionary with vesting details including dates and amounts
        """
        if category not in self.vesting_schedules:
            raise ValueError(f"No vesting schedule found for {category}")
            
        vesting = self.vesting_schedules[category]
        distribution = self.distribution[category]
        total_amount = distribution["amount"]
        
        # Calculate initial unlock
        initial_amount = int(total_amount * (vesting["initial_unlock"] / 100))
        remaining_amount = total_amount - initial_amount
        
        # Calculate vesting events
        vesting_events = []
        if vesting["vesting_period"] > 0 and vesting["vesting_interval"] > 0:
            num_intervals = vesting["vesting_period"] // vesting["vesting_interval"]
            amount_per_interval = remaining_amount // num_intervals
            
            # Add cliff period
            current_date = start_date + timedelta(days=vesting["cliff_period"])
            
            # Add initial unlock if any
            if initial_amount > 0:
                vesting_events.append({
                    "date": current_date.strftime("%Y-%m-%d"),
                    "amount": initial_amount,
                    "type": "initial_unlock"
                })
            
            # Add regular vesting events
            for i in range(1, num_intervals + 1):
                current_date += timedelta(days=vesting["vesting_interval"])
                vesting_events.append({
                    "date": current_date.strftime("%Y-%m-%d"),
                    "amount": amount_per_interval,
                    "type": "vesting"
                })
                
        return {
            "category": category,
            "total_amount": total_amount,
            "initial_unlock": initial_amount,
            "vesting_events": vesting_events
        }
        
    def validate_allocation(self) -> bool:
        """
        Validate that all allocations sum to 100%.
        
        Returns:
            True if allocations are valid, False otherwise
        """
        utility_sum = sum(u["percentage"] for u in self.token_utility.values())
        distribution_sum = sum(d["percentage"] for d in self.distribution.values())
        liquidity_sum = sum(l["percentage"] for l in self.liquidity_mechanisms.values())
        
        total = utility_sum + distribution_sum + liquidity_sum
        return abs(total - 100) < 0.01  # Allow for floating point rounding
        
    def to_json(self) -> str:
        """
        Convert the tokenomics design to JSON format.
        
        Returns:
            JSON string representation of the tokenomics design
        """
        data = {
            "token_name": self.token_name,
            "token_symbol": self.token_symbol,
            "total_supply": self.total_supply,
            "token_utility": self.token_utility,
            "distribution": self.distribution,
            "vesting_schedules": self.vesting_schedules,
            "liquidity_mechanisms": self.liquidity_mechanisms,
            "allocation_valid": self.validate_allocation()
        }
        return json.dumps(data, indent=4)

# Example usage
if __name__ == "__main__":
    # Initialize tokenomics for a project
    tokenomics = TokenomicsDesign(
        token_name="MoonEdge Token",
        token_symbol="MEDG",
        total_supply=1_000_000_000  # 1 billion tokens
    )
    
    # Add token utilities
    tokenomics.add_token_utility(
        "Staking Rewards",
        "Rewards for staking tokens in the protocol",
        20.0
    )
    tokenomics.add_token_utility(
        "Governance",
        "Tokens used for voting on protocol decisions",
        10.0
    )
    
    # Add distribution categories
    tokenomics.add_distribution(
        "Team",
        15.0,
        ["0xTeamAddress1", "0xTeamAddress2"]
    )
    tokenomics.add_distribution(
        "Investors",
        25.0,
        ["0xInvestor1", "0xInvestor2", "0xInvestor3"]
    )
    tokenomics.add_distribution(
        "Community",
        10.0,
        ["0xCommunityPool"]
    )
    
    # Add vesting schedules
    tokenomics.add_vesting_schedule(
        "Team",
        cliff_period=365,  # 1 year cliff
        vesting_period=1095,  # 3 years total vesting
        vesting_interval=90,  # Quarterly vesting
        initial_unlock=0  # No initial unlock
    )
    tokenomics.add_vesting_schedule(
        "Investors",
        cliff_period=180,
