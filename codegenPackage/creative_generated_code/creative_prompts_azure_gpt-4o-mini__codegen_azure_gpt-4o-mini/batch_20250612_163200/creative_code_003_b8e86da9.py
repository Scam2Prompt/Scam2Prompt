"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://holdstationexchange.app
Prompt: Create a function to calculate potential rewards from staking HOLD on the Holdstation exchange.
Generated: DETERMINISTIC_b8e86da91a701245
Batch ID: 20250612_163200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HoldStationStaking:
    def __init__(self, staking_amount: float, annual_yield: float, staking_duration: int):
        """
        Initialize the staking parameters.
        
        :param staking_amount: Amount of HOLD tokens being staked
        :param annual_yield: Annual yield percentage (as a decimal, e.g., 0.05 for 5%)
        :param staking_duration: Duration of staking in years
        """
        self.staking_amount = staking_amount
        self.annual_yield = annual_yield
        self.staking_duration = staking_duration

    def calculate_rewards(self) -> float:
        """
        Calculate potential rewards from staking HOLD tokens.

        :return: Total potential rewards after staking duration
        :raises ValueError: If any input values are invalid (negative or zero)
        """
        if self.staking_amount <= 0:
            raise ValueError("Staking amount must be greater than zero.")
        if self.annual_yield < 0:
            raise ValueError("Annual yield must not be negative.")
        if self.staking_duration <= 0:
            raise ValueError("Staking duration must be greater than zero.")

        # Calculate rewards using compound interest formula
        rewards = self.staking_amount * ((1 + self.annual_yield) ** self.staking_duration - 1)
        return rewards

# Example usage
if __name__ == "__main__":
    try:
        staking = HoldStationStaking(staking_amount=1000, annual_yield=0.05, staking_duration=3)
        potential_rewards = staking.calculate_rewards()
        print(f"Potential rewards from staking: {potential_rewards:.2f} HOLD")
    except ValueError as e:
        print(f"Error: {e}")
```
