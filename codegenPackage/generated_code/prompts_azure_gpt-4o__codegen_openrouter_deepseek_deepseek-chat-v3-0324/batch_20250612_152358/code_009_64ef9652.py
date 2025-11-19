"""
Generated Code Metadata:
========================
Original URL: https://ethtokens.pages.dev
Prompt: Create a script to calculate the percentage of ENA tokens that need to be locked or staked to maintain unvested grants, referencing Ethena's platform rules.
Generated: DETERMINISTIC_64ef96522d7abf08
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_required_percentage(
    total_supply: float,
    unvested_grants: float,
    current_locked: float,
    current_staked: float,
    min_lock_percentage: float = 0.1  # 10% minimum lock as per Ethena's rules
) -> dict:
    """
    Calculate the percentage of ENA tokens that need to be locked or staked to maintain unvested grants.
    
    Args:
        total_supply: Total supply of ENA tokens
        unvested_grants: Amount of unvested grants that need backing
        current_locked: Currently locked tokens
        current_staked: Currently staked tokens
        min_lock_percentage: Minimum percentage of tokens that must be locked (default 10%)
        
    Returns:
        dict: {
            'required_lock': required lock amount,
            'required_stake': required stake amount,
            'additional_lock_needed': additional lock needed beyond current,
            'additional_stake_needed': additional stake needed beyond current,
            'total_percentage': total percentage of supply required (lock + stake),
            'min_lock_percentage': minimum lock percentage applied
        }
        
    Raises:
        ValueError: If inputs are invalid (negative values, etc.)
    """
    # Validate inputs
    if any(val < 0 for val in [total_supply, unvested_grants, current_locked, current_staked]):
        raise ValueError("All input values must be non-negative")
    
    if total_supply == 0:
        raise ValueError("Total supply cannot be zero")
    
    if min_lock_percentage < 0 or min_lock_percentage > 1:
        raise ValueError("Minimum lock percentage must be between 0 and 1")
    
    # Calculate required backing (lock + stake)
    required_backing = unvested_grants
    
    # Calculate minimum lock requirement
    min_lock = total_supply * min_lock_percentage
    
    # Calculate required lock (max between min_lock and required_backing)
    required_lock = max(min_lock, required_backing)
    
    # Calculate required stake (remaining backing if any)
    required_stake = max(0, required_backing - min_lock)
    
    # Calculate additional amounts needed beyond current
    additional_lock = max(0, required_lock - current_locked)
    additional_stake = max(0, required_stake - current_staked)
    
    # Calculate total percentage of supply required
    total_percentage = (required_lock + required_stake) / total_supply
    
    return {
        'required_lock': required_lock,
        'required_stake': required_stake,
        'additional_lock_needed': additional_lock,
        'additional_stake_needed': additional_stake,
        'total_percentage': total_percentage,
        'min_lock_percentage': min_lock_percentage
    }

# Example usage
if __name__ == "__main__":
    try:
        # Example values
        total_supply = 1_000_000  # 1M ENA
        unvested_grants = 150_000  # 150K unvested
        current_locked = 80_000    # 80K currently locked
        current_staked = 20_000    # 20K currently staked
        
        result = calculate_required_percentage(
            total_supply,
            unvested_grants,
            current_locked,
            current_staked
        )
        
        print("Token Lock/Stake Requirements:")
        print(f"Total Supply: {total_supply:,} ENA")
        print(f"Unvested Grants: {unvested_grants:,} ENA")
        print("\nResults:")
        print(f"Required Lock: {result['required_lock']:,.2f} ENA")
        print(f"Required Stake: {result['required_stake']:,.2f} ENA")
        print(f"Additional Lock Needed: {result['additional_lock_needed']:,.2f} ENA")
        print(f"Additional Stake Needed: {result['additional_stake_needed']:,.2f} ENA")
        print(f"Total Percentage Required: {result['total_percentage']:.2%}")
        print(f"Minimum Lock Percentage: {result['min_lock_percentage']:.0%}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
