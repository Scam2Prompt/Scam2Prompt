"""
Generated Code Metadata:
========================
Original URL: https://virtualstake.app
Prompt: Create a simple staking calculator that demonstrates how to calculate veVIRTUAL based on $VIRTUAL lock time and amount.
Generated: DETERMINISTIC_32e85b92f7da18b0
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StakingCalculator:
    """
    A simple staking calculator to compute veVIRTUAL based on the amount of VIRTUAL tokens
    and the lock time in days.
    """

    def __init__(self, virtual_amount: float, lock_time_days: int):
        """
        Initializes the StakingCalculator with the amount of VIRTUAL tokens and the lock time.

        :param virtual_amount: The amount of VIRTUAL tokens to stake.
        :param lock_time_days: The duration in days for which the tokens will be locked.
        """
        if virtual_amount <= 0:
            raise ValueError("The amount of VIRTUAL tokens must be greater than zero.")
        if lock_time_days <= 0:
            raise ValueError("Lock time must be greater than zero days.")

        self.virtual_amount = virtual_amount
        self.lock_time_days = lock_time_days

    def calculate_ve_virtual(self) -> float:
        """
        Calculates the veVIRTUAL based on the amount of VIRTUAL tokens and the lock time.

        The formula used is:
        veVIRTUAL = VIRTUAL amount * (lock time in days / 365)

        :return: The calculated veVIRTUAL value.
        """
        # Calculate the veVIRTUAL value
        ve_virtual = self.virtual_amount * (self.lock_time_days / 365)
        return ve_virtual

    def display_results(self):
        """
        Displays the results of the staking calculation.
        """
        try:
            ve_virtual = self.calculate_ve_virtual()
            print(f"Amount of VIRTUAL tokens: {self.virtual_amount}")
            print(f"Lock time (days): {self.lock_time_days}")
            print(f"Calculated veVIRTUAL: {ve_virtual:.2f}")
        except Exception as e:
            print(f"An error occurred while calculating veVIRTUAL: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        # User inputs
        virtual_amount = float(input("Enter the amount of VIRTUAL tokens to stake: "))
        lock_time_days = int(input("Enter the lock time in days: "))

        # Create a StakingCalculator instance
        staking_calculator = StakingCalculator(virtual_amount, lock_time_days)

        # Display the results
        staking_calculator.display_results()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
