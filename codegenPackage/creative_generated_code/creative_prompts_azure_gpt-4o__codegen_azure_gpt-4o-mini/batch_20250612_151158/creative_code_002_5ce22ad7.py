"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zivoe.pages.dev
Prompt: Create a function to calculate the balance after depositing USDC into the Senior or Junior Tranche on the Zivoe platform, factoring in the launch bonus multipliers for pZVE tokens.
Generated: DETERMINISTIC_5ce22ad72c019e5d
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ZivoePlatform:
    def __init__(self):
        # Initialize the balances for Senior and Junior Tranche
        self.senior_tranche_balance = 0.0
        self.junior_tranche_balance = 0.0
        self.launch_bonus_multiplier = 1.0  # Default multiplier

    def set_launch_bonus_multiplier(self, multiplier: float):
        """
        Set the launch bonus multiplier for pZVE tokens.
        
        :param multiplier: A float representing the launch bonus multiplier.
        :raises ValueError: If the multiplier is not greater than zero.
        """
        if multiplier <= 0:
            raise ValueError("Multiplier must be greater than zero.")
        self.launch_bonus_multiplier = multiplier

    def deposit(self, tranche: str, amount: float) -> float:
        """
        Deposit USDC into the specified tranche and calculate the balance after applying the bonus multiplier.

        :param tranche: A string indicating the tranche type ('Senior' or 'Junior').
        :param amount: A float representing the amount of USDC to deposit.
        :raises ValueError: If the tranche type is invalid or amount is not positive.
        :return: The new balance for the specified tranche after deposit.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        if tranche not in ['Senior', 'Junior']:
            raise ValueError("Tranche must be either 'Senior' or 'Junior'.")

        # Apply the launch bonus multiplier to the deposit amount
        adjusted_amount = amount * self.launch_bonus_multiplier

        # Update the respective tranche balance
        if tranche == 'Senior':
            self.senior_tranche_balance += adjusted_amount
            return self.senior_tranche_balance
        else:  # tranche == 'Junior'
            self.junior_tranche_balance += adjusted_amount
            return self.junior_tranche_balance

# Example usage
if __name__ == '__main__':
    platform = ZivoePlatform()

    try:
        platform.set_launch_bonus_multiplier(1.5)  # Set a 50% bonus
        new_balance_senior = platform.deposit('Senior', 100.0)
        print(f"New Senior Tranche Balance: {new_balance_senior}")

        new_balance_junior = platform.deposit('Junior', 200.0)
        print(f"New Junior Tranche Balance: {new_balance_junior}")

    except ValueError as e:
        print(f"Error: {e}")
```
