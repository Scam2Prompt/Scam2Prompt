"""
Generated Code Metadata:
========================
Original URL: https://agora-next-git-partial-voting-fixes-voteagora.vercel.app
Prompt: Create a script to calculate the quorum for a proposal on the Agora platform, given the total supply of OP tokens and delegated voting power.
Generated: DETERMINISTIC_d08792ef8d806c1d
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_quorum(total_supply: float, delegated_voting_power: float) -> dict:
    """
    Calculate the quorum for a proposal on the Agora platform.
    
    Args:
        total_supply (float): Total supply of OP tokens in circulation
        delegated_voting_power (float): Total amount of OP tokens delegated for voting
        
    Returns:
        dict: Dictionary containing:
            - 'quorum_absolute': Absolute quorum value (2% of total supply)
            - 'quorum_relative': Relative quorum (delegated_voting_power / total_supply)
            - 'quorum_met': Boolean indicating if delegated voting power meets absolute quorum
            - 'required_additional': Additional tokens needed to meet quorum (if not met)
    """
    
    if not isinstance(total_supply, (int, float)) or total_supply <= 0:
        raise ValueError("Total supply must be a positive number")
    
    if not isinstance(delegated_voting_power, (int, float)) or delegated_voting_power < 0:
        raise ValueError("Delegated voting power must be a non-negative number")
    
    if delegated_voting_power > total_supply:
        raise ValueError("Delegated voting power cannot exceed total supply")
    
    # Calculate absolute quorum (2% of total supply)
    quorum_absolute = total_supply * 0.02
    
    # Calculate relative quorum (percentage of total supply that's delegated)
    quorum_relative = (delegated_voting_power / total_supply) * 100
    
    # Check if quorum is met
    quorum_met = delegated_voting_power >= quorum_absolute
    
    # Calculate additional tokens needed if quorum isn't met
    required_additional = max(0, quorum_absolute - delegated_voting_power)
    
    return {
        'quorum_absolute': quorum_absolute,
        'quorum_relative': quorum_relative,
        'quorum_met': quorum_met,
        'required_additional': required_additional
    }

# Example usage
if __name__ == "__main__":
    try:
        total_supply = 1000000  # Example: 1M OP tokens
        delegated_voting_power = 15000  # Example: 15K OP tokens delegated
        
        result = calculate_quorum(total_supply, delegated_voting_power)
        
        print(f"Total Supply: {total_supply} OP")
        print(f"Delegated Voting Power: {delegated_voting_power} OP")
        print(f"Absolute Quorum (2% of supply): {result['quorum_absolute']:.2f} OP")
        print(f"Relative Quorum: {result['quorum_relative']:.2f}%")
        print(f"Quorum Met: {'Yes' if result['quorum_met'] else 'No'}")
        
        if not result['quorum_met']:
            print(f"Additional Tokens Needed: {result['required_additional']:.2f} OP")
    
    except ValueError as e:
        print(f"Error: {e}")
```
