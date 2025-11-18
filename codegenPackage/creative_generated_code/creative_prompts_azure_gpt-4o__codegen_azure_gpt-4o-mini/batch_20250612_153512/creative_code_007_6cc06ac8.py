"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xexchange-portal.pages.dev
Prompt: Generate a function in Python to calculate the "energy" acquired by locking MEX tokens on xExchange, based on the provided locking duration and token amount.
Generated: DETERMINISTIC_6cc06ac84891015f
Batch ID: 20250612_153512
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MEXExchange:
    """
    A class to represent the MEX token exchange and calculate energy based on locking tokens.
    """

    def __init__(self, energy_per_token_per_day):
        """
        Initializes the MEXExchange with a specified energy rate.

        :param energy_per_token_per_day: Energy acquired per token per day.
        """
        if energy_per_token_per_day < 0:
            raise ValueError("Energy per token per day must be a non-negative value.")
        self.energy_per_token_per_day = energy_per_token_per_day

    def calculate_energy(self, token_amount, locking_duration_days):
        """
        Calculates the total energy acquired by locking MEX tokens.

        :param token_amount: The amount of MEX tokens to lock (should be non-negative).
        :param locking_duration_days: The duration for which the tokens are locked (in days, should be non-negative).
        :return: The total energy acquired.
        """
        if token_amount < 0:
            raise ValueError("Token amount must be a non-negative value.")
        if locking_duration_days < 0:
            raise ValueError("Locking duration must be a non-negative value.")

        # Calculate total energy
        total_energy = token_amount * self.energy_per_token_per_day * locking_duration_days
        return total_energy


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the exchange with the energy rate
        mex_exchange = MEXExchange(energy_per_token_per_day=5)  # Example rate

        # Calculate energy for a given amount of tokens and locking duration
        energy = mex_exchange.calculate_energy(token_amount=100, locking_duration_days=30)
        print(f"Total energy acquired: {energy} units")
    
    except ValueError as e:
        print(f"Error: {e}")
```
