"""
Generated Code Metadata:
========================
Original URL: https://nexus-mutual.xyz
Prompt: Create a function that calculates the rewards for members staking NXM tokens based on the risk level of smart contracts in Nexus Mutual.
Generated: DETERMINISTIC_86f1f94191ae62ee
Batch ID: 20250612_155956
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List, Dict

# Define a function to calculate staking rewards
def calculate_staking_rewards(staked_tokens: float, risk_levels: List[Dict[str, float]]) -> float:
    """
    Calculate rewards for members staking NXM tokens based on the risk level of smart contracts.

    Args:
        staked_tokens (float): The number of NXM tokens staked by the member.
        risk_levels (List[Dict[str, float]]): A list of dictionaries containing risk level information.
            Each dictionary should have:
                - 'contract': Name of the smart contract (str)
                - 'risk_factor': Risk factor associated with the contract (float, between 0 and 1)

    Returns:
        float: Total rewards earned by the member.
    """
    # Validate inputs
    if staked_tokens <= 0:
        raise ValueError("Staked tokens must be greater than zero.")
    if not isinstance(risk_levels, list) or not all(isinstance(risk, dict) for risk in risk_levels):
        raise ValueError("Risk levels must be a list of dictionaries.")
    
    # Initialize total rewards
    total_rewards = 0.0

    # Iterate through each risk level and calculate rewards
    for risk in risk_levels:
        # Validate risk dictionary structure
        if 'contract' not in risk or 'risk_factor' not in risk:
            raise ValueError("Each risk level must contain 'contract' and 'risk_factor' keys.")
        if not isinstance(risk['risk_factor'], float) or not (0 <= risk['risk_factor'] <= 1):
            raise ValueError("Risk factor must be a float between 0 and 1.")
        
        # Calculate rewards for the current contract
        contract_rewards = staked_tokens * risk['risk_factor']
        total_rewards += contract_rewards

    return total_rewards

# Example usage
if __name__ == "__main__":
    # Example staked tokens
    staked_tokens = 1000.0

    # Example risk levels
    risk_levels = [
        {"contract": "ContractA", "risk_factor": 0.2},
        {"contract": "ContractB", "risk_factor": 0.5},
        {"contract": "ContractC", "risk_factor": 0.1},
    ]

    try:
        # Calculate rewards
        rewards = calculate_staking_rewards(staked_tokens, risk_levels)
        print(f"Total rewards earned: {rewards:.2f} NXM tokens")
    except ValueError as e:
        print(f"Error: {e}")
```
