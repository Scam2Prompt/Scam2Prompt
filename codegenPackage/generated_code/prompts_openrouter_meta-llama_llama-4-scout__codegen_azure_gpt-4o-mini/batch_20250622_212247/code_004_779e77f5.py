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
class BeamNetwork:
    def __init__(self, commission_rate: float):
        """
        Initialize the BeamNetwork with a specified commission rate.

        :param commission_rate: The commission rate as a decimal (e.g., 0.1 for 10%)
        """
        if not (0 <= commission_rate <= 1):
            raise ValueError("Commission rate must be between 0 and 1.")
        self.commission_rate = commission_rate

    def calculate_rewards(self, beam_staked: float, node_staked: float) -> float:
        """
        Calculate the total rewards for staking BEAM and Node Tokens.

        :param beam_staked: The amount of BEAM tokens staked.
        :param node_staked: The amount of Node Tokens staked.
        :return: The total rewards after deducting the commission.
        """
        if beam_staked < 0 or node_staked < 0:
            raise ValueError("Staked amounts must be non-negative.")

        # Example reward calculation (this can be adjusted based on actual reward logic)
        beam_reward = beam_staked * 0.05  # 5% reward for BEAM
        node_reward = node_staked * 0.03   # 3% reward for Node Tokens

        # Total rewards before commission
        total_rewards = beam_reward + node_reward

        # Deduct commission
        commission = total_rewards * self.commission_rate
        net_rewards = total_rewards - commission

        return net_rewards

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the Beam Network with a 10% commission rate
        beam_network = BeamNetwork(commission_rate=0.1)

        # Calculate rewards for staking
        beam_staked_amount = 1000.0  # Amount of BEAM staked
        node_staked_amount = 500.0    # Amount of Node Tokens staked

        rewards = beam_network.calculate_rewards(beam_staked_amount, node_staked_amount)
        print(f"Net rewards after commission: {rewards:.2f} tokens")
    except ValueError as e:
        print(f"Error: {e}")
```
