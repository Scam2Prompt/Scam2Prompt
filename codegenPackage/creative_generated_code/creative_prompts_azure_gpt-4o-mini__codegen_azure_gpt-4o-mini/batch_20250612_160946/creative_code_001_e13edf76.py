"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://promantleclaim.pages.dev
Prompt: Write a function to calculate the estimated $COOK rewards based on the MNT locked in the Mantle LSP.
Generated: DETERMINISTIC_e13edf76dd28708d
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class COOKRewardCalculator:
    """
    A class to calculate the estimated COOK rewards based on the MNT locked in the Mantle LSP.
    """

    def __init__(self, mnt_locked: float, annual_yield_rate: float = 0.1):
        """
        Initializes the calculator with the amount of MNT locked and the annual yield rate.
        
        :param mnt_locked: The amount of MNT locked in the Mantle LSP.
        :param annual_yield_rate: The annual yield rate (default is 10%).
        """
        if mnt_locked < 0:
            raise ValueError("MNT locked cannot be negative.")
        if not (0 <= annual_yield_rate <= 1):
            raise ValueError("Annual yield rate must be between 0 and 1.")
        
        self.mnt_locked = mnt_locked
        self.annual_yield_rate = annual_yield_rate

    def calculate_annual_rewards(self) -> float:
        """
        Calculates the estimated annual COOK rewards based on the MNT locked.
        
        :return: Estimated annual COOK rewards.
        """
        rewards = self.mnt_locked * self.annual_yield_rate
        return rewards

    def calculate_monthly_rewards(self) -> float:
        """
        Calculates the estimated monthly COOK rewards based on the MNT locked.
        
        :return: Estimated monthly COOK rewards.
        """
        annual_rewards = self.calculate_annual_rewards()
        monthly_rewards = annual_rewards / 12
        return monthly_rewards

# Example usage (uncomment to run):
# try:
#     calculator = COOKRewardCalculator(mnt_locked=1000, annual_yield_rate=0.1)
#     print(f"Estimated Annual COOK Rewards: {calculator.calculate_annual_rewards()} COOK")
#     print(f"Estimated Monthly COOK Rewards: {calculator.calculate_monthly_rewards()} COOK")
# except ValueError as e:
#     print(f"Error: {e}")
```
