"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harpycoin.pages.dev
Prompt: Create a Python script to simulate the tokenomics of HarpyCoin, including calculations for presale phases, staking rewards, and swap fees.
Generated: DETERMINISTIC_087a556e514f09a9
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HarpyCoinTokenomics:
    def __init__(self, total_supply):
        """
        Initialize the HarpyCoinTokenomics class with total supply.

        :param total_supply: Total supply of HarpyCoins
        """
        self.total_supply = total_supply
        self.presale_phases = []
        self.staking_rewards = 0
        self.swap_fee_percentage = 0.02  # 2% swap fee

    def add_presale_phase(self, phase_name, amount, price_per_token):
        """
        Add a presale phase to the tokenomics.

        :param phase_name: Name of the presale phase
        :param amount: Amount of tokens for this presale phase
        :param price_per_token: Price per token in this phase
        """
        if amount <= 0 or amount > self.total_supply:
            raise ValueError("Amount must be positive and less than total supply.")
        if any(phase['amount'] + amount > self.total_supply for phase in self.presale_phases):
            raise ValueError("Total presale token allocation exceeds the total supply.")

        phase = {
            'phase_name': phase_name,
            'amount': amount,
            'price_per_token': price_per_token
        }
        self.presale_phases.append(phase)
        print(f"Added presale phase: {phase_name} with {amount} tokens at {price_per_token} each.")

    def calculate_staking_rewards(self, staked_amount, duration_days):
        """
        Calculate staking rewards based on the staked amount and duration.

        :param staked_amount: Amount of tokens staked
        :param duration_days: Duration of staking in days
        :return: Calculated staking rewards
        """
        if staked_amount <= 0:
            raise ValueError("Staked amount must be positive.")
        
        # Assuming a simple annual interest rate of 5%
        annual_interest_rate = 0.05
        daily_interest_rate = annual_interest_rate / 365
        rewards = staked_amount * daily_interest_rate * duration_days
        self.staking_rewards += rewards
        
        return rewards

    def calculate_swap_fee(self, swap_amount):
        """
        Calculate the swap fee for a given amount.

        :param swap_amount: Amount to swap
        :return: Calculated swap fee
        """
        if swap_amount <= 0:
            raise ValueError("Swap amount must be positive.")
        
        swap_fee = swap_amount * self.swap_fee_percentage
        return swap_fee

    def display_tokenomics(self):
        """
        Display the current tokenomics status including presale phases, staking rewards, and swap fees.
        """
        print("HarpyCoin Tokenomics:")
        print(f"Total Supply: {self.total_supply}")
        print("Presale Phases:")
        for phase in self.presale_phases:
            print(f"  - {phase['phase_name']}: {phase['amount']} tokens at {phase['price_per_token']} each")
        print(f"Total Staking Rewards: {self.staking_rewards}")
        print(f"Swap Fee Percentage: {self.swap_fee_percentage * 100}%")

# Example usage
if __name__ == "__main__":
    try:
        harpy_coin = HarpyCoinTokenomics(total_supply=1000000)

        # Adding presale phases
        harpy_coin.add_presale_phase("Phase 1", amount=200000, price_per_token=0.1)
        harpy_coin.add_presale_phase("Phase 2", amount=300000, price_per_token=0.2)

        # Calculating staking rewards
        rewards = harpy_coin.calculate_staking_rewards(staked_amount=10000, duration_days=30)
        print(f"Calculated Staking Rewards: {rewards}")

        # Calculating swap fee
        swap_fee = harpy_coin.calculate_swap_fee(swap_amount=500)
        print(f"Calculated Swap Fee: {swap_fee}")

        # Display the current tokenomics
        harpy_coin.display_tokenomics()

    except Exception as e:
        print(f"An error occurred: {e}")
```
