"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polyhedra-foundation-web.pages.dev
Prompt: Write a script to calculate the staking power for Polyhedra Network tokens based on the amount staked and the remaining lock duration, as described in the Polyhedra Network staking program.
Generated: DETERMINISTIC_2de72cba8c92cb93
Batch ID: 20250612_145503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingPowerCalculator:
    """
    A class to calculate the staking power for Polyhedra Network tokens.
    
    Attributes:
        amount_staked (float): The amount of tokens staked.
        remaining_lock_duration (int): The remaining lock duration in days.
    """

    def __init__(self, amount_staked: float, remaining_lock_duration: int):
        """
        Initializes the StakingPowerCalculator with staked amount and lock duration.

        Parameters:
            amount_staked (float): The amount of tokens staked.
            remaining_lock_duration (int): The remaining lock duration in days.
        """
        self.amount_staked = amount_staked
        self.remaining_lock_duration = remaining_lock_duration

    def calculate_staking_power(self) -> float:
        """
        Calculate the staking power based on the amount staked and remaining lock duration.

        The staking power is calculated as follows:
        staking_power = amount_staked * (1 + (remaining_lock_duration / 365))

        Returns:
            float: The calculated staking power.
        """
        if self.amount_staked < 0:
            raise ValueError("Amount staked must be a non-negative value.")
        if self.remaining_lock_duration < 0:
            raise ValueError("Remaining lock duration must be a non-negative integer.")

        # Calculate staking power
        staking_power = self.amount_staked * (1 + (self.remaining_lock_duration / 365))
        return staking_power

def main():
    """
    Main function to execute the staking power calculation based on user input.
    """
    try:
        # User inputs for the amount staked and remaining lock duration
        amount_staked = float(input("Enter the amount of tokens staked: "))
        remaining_lock_duration = int(input("Enter the remaining lock duration in days: "))

        # Initialize the staking power calculator
        calculator = StakingPowerCalculator(amount_staked, remaining_lock_duration)

        # Calculate and display the staking power
        staking_power = calculator.calculate_staking_power()
        print(f"Calculated Staking Power: {staking_power:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
```
