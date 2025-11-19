"""
Generated Code Metadata:
========================
Original URL: https://onbeam.live
Prompt: Create a function to calculate rewards for staking BEAM and Node Tokens on the Beam Network, considering commission rates and staked amounts.
Generated: DETERMINISTIC_779e77f593195758
Batch ID: 20250622_212247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import Tuple

def calculate_rewards(staked_beam: float, staked_node: float, beam_reward_rate: float, node_reward_rate: float, commission_rate: float) -> Tuple[float, float, float]:
    """
    Calculate rewards for staking BEAM and Node Tokens on the Beam Network.

    Parameters:
        staked_beam (float): Amount of BEAM tokens staked.
        staked_node (float): Amount of Node tokens staked.
        beam_reward_rate (float): Reward rate for BEAM tokens (per token).
        node_reward_rate (float): Reward rate for Node tokens (per token).
        commission_rate (float): Commission rate applied to the rewards (percentage as a decimal).

    Returns:
        Tuple[float, float, float]: A tuple containing:
            - Net BEAM rewards after commission.
            - Net Node rewards after commission.
            - Total rewards (BEAM + Node) after commission.
    """
    try:
        # Validate inputs
        if staked_beam < 0 or staked_node < 0:
            raise ValueError("Staked amounts must be non-negative.")
        if not (0 <= commission_rate <= 1):
            raise ValueError("Commission rate must be between 0 and 1.")
        if beam_reward_rate < 0 or node_reward_rate < 0:
            raise ValueError("Reward rates must be non-negative.")

        # Calculate raw rewards
        raw_beam_rewards = staked_beam * beam_reward_rate
        raw_node_rewards = staked_node * node_reward_rate

        # Apply commission
        net_beam_rewards = raw_beam_rewards * (1 - commission_rate)
        net_node_rewards = raw_node_rewards * (1 - commission_rate)

        # Calculate total rewards
        total_rewards = net_beam_rewards + net_node_rewards

        return net_beam_rewards, net_node_rewards, total_rewards

    except Exception as e:
        # Handle unexpected errors
        raise RuntimeError(f"An error occurred while calculating rewards: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        # Example inputs
        staked_beam = 1000.0  # Amount of BEAM tokens staked
        staked_node = 500.0   # Amount of Node tokens staked
        beam_reward_rate = 0.05  # Reward rate for BEAM tokens
        node_reward_rate = 0.1   # Reward rate for Node tokens
        commission_rate = 0.1    # Commission rate (10%)

        # Calculate rewards
        beam_rewards, node_rewards, total_rewards = calculate_rewards(
            staked_beam, staked_node, beam_reward_rate, node_reward_rate, commission_rate
        )

        # Print results
        print(f"Net BEAM Rewards: {beam_rewards:.2f}")
        print(f"Net Node Rewards: {node_rewards:.2f}")
        print(f"Total Rewards: {total_rewards:.2f}")

    except RuntimeError as error:
        print(error)
```
