"""
Generated Code Metadata:
========================
Original URL: https://front-1.pointech.cloud
Prompt: Create a program to manage PointPay token (PXP) staking and calculate reduced trading fees based on the amount staked.
Generated: DETERMINISTIC_f3791b9edeefb1e7
Batch ID: 20250612_151334
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
from typing import Dict, Optional

# Set precision for Decimal calculations
getcontext().prec = 18

class StakingManager:
    """
    Manages PXP token staking and calculates trading fee discounts based on staked amounts.
    """
    
    def __init__(self, fee_structure: Dict[str, Dict[str, Decimal]], min_stake: Decimal = Decimal('0')):
        """
        Initialize the StakingManager with fee structure and minimum stake amount.
        
        Args:
            fee_structure: Dictionary mapping stake tiers to fee discounts
                          Example: {
                              'tier1': {'min_amount': Decimal('1000'), 'discount': Decimal('0.1')},
                              'tier2': {'min_amount': Decimal('5000'), 'discount': Decimal('0.2')}
                          }
            min_stake: Minimum amount required to stake (default: 0)
        """
        self.fee_structure = fee_structure
        self.min_stake = min_stake
        self.stakes = {}  # user_address: staked_amount
        
        # Validate fee structure
        self._validate_fee_structure()
    
    def _validate_fee_structure(self) -> None:
        """Validate that fee structure is properly formatted."""
        if not isinstance(self.fee_structure, dict):
            raise ValueError("Fee structure must be a dictionary")
        
        for tier_name, tier_data in self.fee_structure.items():
            if not isinstance(tier_data, dict):
                raise ValueError(f"Tier {tier_name} data must be a dictionary")
            
            if 'min_amount' not in tier_data or 'discount' not in tier_data:
                raise ValueError(f"Tier {tier_name} must contain 'min_amount' and 'discount'")
            
            if not isinstance(tier_data['min_amount'], Decimal) or not isinstance(tier_data['discount'], Decimal):
                raise ValueError(f"Tier {tier_name} amounts must be Decimal")
            
            if tier_data['discount'] < Decimal('0') or tier_data['discount'] > Decimal('1'):
                raise ValueError(f"Tier {tier_name} discount must be between 0 and 1")

    def stake_tokens(self, user_address: str, amount: Decimal) -> None:
        """
        Stake PXP tokens for a user.
        
        Args:
            user_address: User's wallet address
            amount: Amount of PXP to stake
            
        Raises:
            ValueError: If amount is invalid or below minimum stake
        """
        if not isinstance(amount, Decimal):
            raise ValueError("Amount must be Decimal")
        
        if amount <= Decimal('0'):
            raise ValueError("Stake amount must be positive")
        
        if amount < self.min_stake:
            raise ValueError(f"Stake amount must be at least {self.min_stake}")
        
        if user_address in self.stakes:
            self.stakes[user_address] += amount
        else:
            self.stakes[user_address] = amount
    
    def unstake_tokens(self, user_address: str, amount: Decimal) -> None:
        """
        Unstake PXP tokens for a user.
        
        Args:
            user_address: User's wallet address
            amount: Amount of PXP to unstake
            
        Raises:
            ValueError: If amount is invalid or exceeds staked amount
        """
        if not isinstance(amount, Decimal):
            raise ValueError("Amount must be Decimal")
        
        if amount <= Decimal('0'):
            raise ValueError("Unstake amount must be positive")
        
        if user_address not in self.stakes:
            raise ValueError("User has no staked tokens")
        
        if amount > self.stakes[user_address]:
            raise ValueError("Cannot unstake more than currently staked")
        
        self.stakes[user_address] -= amount
        
        if self.stakes[user_address] == Decimal('0'):
            del self.stakes[user_address]
    
    def get_staked_amount(self, user_address: str) -> Decimal:
        """
        Get the staked amount for a user.
        
        Args:
            user_address: User's wallet address
            
        Returns:
            Decimal: Amount of PXP staked (0 if no stake)
        """
        return self.stakes.get(user_address, Decimal('0'))
    
    def get_fee_discount(self, user_address: str) -> Decimal:
        """
        Calculate the trading fee discount based on staked amount.
        
        Args:
            user_address: User's wallet address
            
        Returns:
            Decimal: Discount factor (0 to 1)
        """
        staked_amount = self.get_staked_amount(user_address)
        if staked_amount == Decimal('0'):
            return Decimal('0')
        
        # Sort tiers by min_amount in descending order to find highest applicable tier
        sorted_tiers = sorted(
            self.fee_structure.items(),
            key=lambda x: x[1]['min_amount'],
            reverse=True
        )
        
        for tier_name, tier_data in sorted_tiers:
            if staked_amount >= tier_data['min_amount']:
                return tier_data['discount']
        
        return Decimal('0')
    
    def calculate_trading_fee(self, user_address: str, base_fee: Decimal) -> Decimal:
        """
        Calculate the final trading fee after applying discount.
        
        Args:
            user_address: User's wallet address
            base_fee: Base trading fee (as decimal, e.g., 0.001 for 0.1%)
            
        Returns:
            Decimal: Final trading fee after discount
        """
        if not isinstance(base_fee, Decimal):
            raise ValueError("Base fee must be Decimal")
        
        if base_fee < Decimal('0'):
            raise ValueError("Base fee cannot be negative")
        
        discount = self.get_fee_discount(user_address)
        return base_fee * (Decimal('1') - discount)
    
    def save_state(self, file_path: str) -> None:
        """
        Save current staking state to a JSON file.
        
        Args:
            file_path: Path to save the state file
        """
        state = {
            'stakes': {addr: str(amount) for addr, amount in self.stakes.items()},
            'fee_structure': {
                tier: {
                    'min_amount': str(data['min_amount']),
                    'discount': str(data['discount'])
                }
                for tier, data in self.fee_structure.items()
            },
            'min_stake': str(self.min_stake)
        }
        
        with open(file_path, 'w') as f:
            json.dump(state, f, indent=2)
    
    @classmethod
    def load_state(cls, file_path: str) -> 'StakingManager':
        """
        Load staking state from a JSON file.
        
        Args:
            file_path: Path to load the state file
            
        Returns:
            StakingManager: Initialized instance with loaded state
        """
        with open(file_path, 'r') as f:
            state = json.load(f)
        
        fee_structure = {
            tier: {
                'min_amount': Decimal(data['min_amount']),
                'discount': Decimal(data['discount'])
            }
            for tier, data in state['fee_structure'].items()
        }
        
        min_stake = Decimal(state['min_stake'])
        
        instance = cls(fee_structure, min_stake)
        instance.stakes = {
            addr: Decimal(amount) 
            for addr, amount in state['stakes'].items()
        }
        
        return instance

# Example usage
if __name__ == "__main__":
    # Define fee structure
    fee_structure = {
        'bronze': {'min_amount': Decimal('1000'), 'discount': Decimal('0.1')},
        'silver': {'min_amount': Decimal('5000'), 'discount': Decimal('0.2')},
        'gold': {'min_amount': Decimal('10000'), 'discount': Decimal('0.3')},
        'platinum': {'min_amount': Decimal('50000'), 'discount': Decimal('0.5')}
    }
    
    # Initialize staking manager
    staking_manager = StakingManager(fee_structure, min_stake=Decimal('100'))
    
    # Stake tokens for a user
    user_address = "0x1234567890abcdef"
    staking_manager.stake_tokens(user_address, Decimal('7500'))
    
    # Calculate trading fee
    base_fee = Decimal('0.001')  # 0.1% trading fee
    final_fee = staking_manager.calculate_trading_fee(user_address, base_fee)
    print(f"Final trading fee: {final_fee * 100}%")
    
    # Save state
    staking_manager.save_state('staking_state.json')
    
    # Load state
    loaded_manager = StakingManager.load_state('staking_state.json')
    print(f"Loaded staked amount: {loaded_manager.get_staked_amount(user_address)}")
```
