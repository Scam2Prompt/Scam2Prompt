"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paalai-revshare.pages.dev
Prompt: Generate a function that computes the total ETH rewarded from staking $PAAL tokens, considering compounding rewards over multiple staking durations.
Generated: DETERMINISTIC_f828d00533cda900
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingCalculator:
    def __init__(self, initial_investment, annual_interest_rate, staking_periods):
        """
        Initialize the StakingCalculator with the necessary parameters.

        :param initial_investment: The amount of PAAL tokens staked initially.
        :param annual_interest_rate: The annual interest rate (as a decimal) for staking rewards.
        :param staking_periods: A list of durations (in years) over which to compute rewards.
        """
        self.initial_investment = initial_investment
        self.annual_interest_rate = annual_interest_rate
        self.staking_periods = staking_periods

    def compute_total_rewards(self):
        """
        Computes the total ETH rewarded from staking PAAL tokens, considering compounding rewards.

        :return: A dictionary mapping each staking duration to the total ETH rewarded.
        """
        rewards = {}
        
        for period in self.staking_periods:
            try:
                if period < 0:
                    raise ValueError("Staking period must be a non-negative value.")
                
                # Calculate total rewards using compound interest formula
                total_amount = self.initial_investment * (1 + self.annual_interest_rate) ** period
                total_rewards = total_amount - self.initial_investment  # rewards only

                # Assuming 1 PAAL = 0.01 ETH for conversion purposes (update as necessary)
                eth_reward = total_rewards * 0.01
                rewards[period] = eth_reward

            except ValueError as e:
                print(f"Error calculating rewards for period {period}: {e}")
            except Exception as e:
                print(f"An unexpected error occurred for period {period}: {e}")

        return rewards


# Example usage of the StakingCalculator
if __name__ == "__main__":
    # Parameters
    initial_investment = 1000  # Example: 1000 PAAL tokens staked
    annual_interest_rate = 0.05  # Example: 5% annual interest rate
    staking_periods = [1, 2, 3, 5]  # Example staking durations in years

    # Create an instance of StakingCalculator
    calculator = StakingCalculator(initial_investment, annual_interest_rate, staking_periods)

    # Compute and print the total rewards
    total_rewards = calculator.compute_total_rewards()
    print("Total ETH rewards from staking PAAL tokens:", total_rewards)
```
