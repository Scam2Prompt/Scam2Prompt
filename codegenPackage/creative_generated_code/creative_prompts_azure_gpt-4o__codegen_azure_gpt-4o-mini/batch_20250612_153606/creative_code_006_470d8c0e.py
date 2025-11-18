"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-99bitcoin.pages.dev
Prompt: Develop a function to calculate and display the user's estimated rewards for staking $99BTC tokens, including monthly and daily breakdowns.
Generated: DETERMINISTIC_470d8c0e2e29c047
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingCalculator:
    def __init__(self, staking_amount, annual_yield):
        """
        Initialize the StakingCalculator with the staking amount and annual yield.
        
        :param staking_amount: Amount of tokens staked (float)
        :param annual_yield: Annual yield percentage (float)
        """
        self.staking_amount = staking_amount
        self.annual_yield = annual_yield / 100  # Convert percentage to decimal

    def calculate_rewards(self):
        """
        Calculate daily and monthly rewards based on staking amount and annual yield.

        :return: A tuple containing daily and monthly rewards (float, float)
        """
        try:
            # Calculate daily and monthly rewards
            daily_rewards = (self.staking_amount * self.annual_yield) / 365
            monthly_rewards = (self.staking_amount * self.annual_yield) / 12
            
            return daily_rewards, monthly_rewards
        except Exception as e:
            # Handle any unexpected errors
            print(f"Error calculating rewards: {e}")
            return None, None

    def display_rewards(self):
        """
        Display the calculated daily and monthly rewards.
        """
        daily_rewards, monthly_rewards = self.calculate_rewards()
        
        if daily_rewards is not None and monthly_rewards is not None:
            print(f"Staking Amount: ${self.staking_amount} BTC")
            print(f"Estimated Daily Rewards: ${daily_rewards:.2f} BTC")
            print(f"Estimated Monthly Rewards: ${monthly_rewards:.2f} BTC")
        else:
            print("Could not calculate rewards due to an error.")

# Example usage
if __name__ == "__main__":
    try:
        staking_amount = 99.0  # Example staking amount in BTC
        annual_yield = 5.0  # Example annual yield in percentage

        calculator = StakingCalculator(staking_amount, annual_yield)
        calculator.display_rewards()
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
