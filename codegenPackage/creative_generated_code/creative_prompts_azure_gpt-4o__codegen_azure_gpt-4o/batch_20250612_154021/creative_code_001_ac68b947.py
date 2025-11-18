"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astrdex.com
Prompt: Generate code to calculate staking rewards for BNB, USDT, BTC, and CAKE on Aster DEX, considering an APY of up to 30%.
Generated: DETERMINISTIC_ac68b9476d792931
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class StakingRewardsCalculator:
    """
    A class to calculate staking rewards for supported cryptocurrencies.
    Supported tokens: BNB, USDT, BTC, CAKE
    """
    
    def __init__(self, token: str, staked_amount: float, apy: float, days_staked: int):
        """
        Initialize the staking rewards calculator.

        :param token: The token being staked (e.g., 'BNB', 'USDT', 'BTC', 'CAKE').
        :param staked_amount: Amount of the token staked.
        :param apy: Annual Percentage Yield (APY) as a percentage (e.g., 30 for 30% APY).
        :param days_staked: Number of days the tokens are staked.
        """
        self.supported_tokens = ['BNB', 'USDT', 'BTC', 'CAKE']
        self.token = token.upper()
        self.staked_amount = staked_amount
        self.apy = apy
        self.days_staked = days_staked

        # Validate input parameters
        self._validate_inputs()

    def _validate_inputs(self):
        """
        Validate the input parameters to ensure correct operation.
        """
        if self.token not in self.supported_tokens:
            raise ValueError(f"Unsupported token: {self.token}. Supported tokens are: {self.supported_tokens}")
        
        if self.staked_amount <= 0:
            raise ValueError("Staked amount must be greater than 0.")
        
        if self.apy <= 0 or self.apy > 30:
            raise ValueError("APY must be greater than 0 and less than or equal to 30%.")
        
        if self.days_staked <= 0:
            raise ValueError("Days staked must be greater than 0.")

    def calculate_rewards(self) -> float:
        """
        Calculate the staking rewards based on provided parameters.

        :return: Total rewards earned during the staking period.
        """
        # Convert APY percentage to a decimal
        apy_decimal = self.apy / 100
        
        # Calculate daily yield
        daily_yield = apy_decimal / 365
        
        # Calculate staking rewards
        rewards = self.staked_amount * daily_yield * self.days_staked
        
        return rewards

    def display_rewards(self):
        """
        Display rewards in a user-friendly format.
        """
        rewards = self.calculate_rewards()
        print(f"Token: {self.token}")
        print(f"Staked Amount: {self.staked_amount} {self.token}")
        print(f"APY: {self.apy}%")
        print(f"Staking Period: {self.days_staked} days")
        print(f"Total Rewards Earned: {rewards:.6f} {self.token}")


if __name__ == "__main__":
    try:
        # Example usage
        token = input("Enter the token (BNB, USDT, BTC, CAKE): ").strip()
        staked_amount = float(input("Enter the staked amount: "))
        apy = float(input("Enter the APY (up to 30%): "))
        days_staked = int(input("Enter the staking period in days: "))
        
        calculator = StakingRewardsCalculator(token, staked_amount, apy, days_staked)
        calculator.display_rewards()

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
