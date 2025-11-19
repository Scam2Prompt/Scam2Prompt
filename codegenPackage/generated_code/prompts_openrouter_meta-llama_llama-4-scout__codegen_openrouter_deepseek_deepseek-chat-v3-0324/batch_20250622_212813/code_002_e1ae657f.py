"""
Generated Code Metadata:
========================
Original URL: https://stailoud.io
Prompt: "Write a Python script to calculate weekly rewards distribution based on the Loud fee split mechanism."
Generated: DETERMINISTIC_e1ae657fc317a6c8
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Tuple

def calculate_loud_fee_split(
    total_fees: float,
    participants: List[Dict[str, float]],
    alpha: float = 0.5,
    beta: float = 0.5
) -> Dict[str, float]:
    """
    Calculate the Loud fee split distribution among participants.
    
    Args:
        total_fees: Total fees to be distributed
        participants: List of participants with their 'stake' and 'contribution' values
        alpha: Weight for stake (default: 0.5)
        beta: Weight for contribution (default: 0.5)
    
    Returns:
        Dictionary mapping participant IDs to their reward amounts
    
    Raises:
        ValueError: If input validation fails
    """
    # Input validation
    if total_fees <= 0:
        raise ValueError("Total fees must be positive")
    if not participants:
        raise ValueError("Participants list cannot be empty")
    if alpha < 0 or beta < 0 or (alpha + beta) != 1.0:
        raise ValueError("Alpha and beta must be non-negative and sum to 1.0")
    
    # Calculate total stake and contribution
    total_stake = sum(p['stake'] for p in participants)
    total_contribution = sum(p['contribution'] for p in participants)
    
    if total_stake <= 0:
        raise ValueError("Total stake must be positive")
    if total_contribution <= 0:
        raise ValueError("Total contribution must be positive")
    
    rewards = {}
    for participant in participants:
        stake_ratio = participant['stake'] / total_stake
        contribution_ratio = participant['contribution'] / total_contribution
        
        # Calculate weighted score
        score = (alpha * stake_ratio) + (beta * contribution_ratio)
        
        # Calculate reward proportional to score
        reward = total_fees * score
        
        # Store reward with participant ID
        rewards[participant['id']] = reward
    
    return rewards

def validate_participants(participants: List[Dict[str, float]]) -> None:
    """
    Validate participant data structure and values.
    
    Args:
        participants: List of participants to validate
    
    Raises:
        ValueError: If validation fails
    """
    required_keys = {'id', 'stake', 'contribution'}
    for i, p in enumerate(participants):
        if not isinstance(p, dict):
            raise ValueError(f"Participant at index {i} must be a dictionary")
        if not required_keys.issubset(p.keys()):
            raise ValueError(f"Participant at index {i} missing required keys")
        if p['stake'] < 0:
            raise ValueError(f"Participant {p['id']} has negative stake")
        if p['contribution'] < 0:
            raise ValueError(f"Participant {p['id']} has negative contribution")

def main():
    """Example usage of the Loud fee split calculator."""
    try:
        # Example data
        total_fees = 1000.0
        participants = [
            {'id': 'A', 'stake': 500.0, 'contribution': 200.0},
            {'id': 'B', 'stake': 300.0, 'contribution': 400.0},
            {'id': 'C', 'stake': 200.0, 'contribution': 400.0}
        ]
        
        # Validate participants
        validate_participants(participants)
        
        # Calculate rewards
        rewards = calculate_loud_fee_split(total_fees, participants)
        
        # Print results
        print("Rewards Distribution:")
        for participant_id, amount in rewards.items():
            print(f"{participant_id}: {amount:.2f}")
    
    except ValueError as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    main()
```
