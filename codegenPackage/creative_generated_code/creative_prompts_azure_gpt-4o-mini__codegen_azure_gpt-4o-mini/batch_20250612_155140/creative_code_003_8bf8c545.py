"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-altvenusio-git-hotfix-zksync-bridge-limits-venus-protocol.vercel.app
Prompt: Generate a script to calculate interest rates using the Venus Protocol's lending mechanics.
Generated: DETERMINISTIC_8bf8c54531c85117
Batch ID: 20250612_155140
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class VenusProtocol:
    """
    A class to represent the Venus Protocol lending mechanics for calculating interest rates.

    Attributes
    ----------
    base_rate : float
        The base interest rate applicable to the loan
    utilization_rate : float
        The utilization rate of the asset
    reserve_factor : float
        The percentage of interest that goes to reserves
    
    Methods
    -------
    calculate_interest_rate(utilization_rate: float) -> float:
        Calculates the effective interest rate based on the utilization rate.
    """

    def __init__(self, base_rate: float, reserve_factor: float):
        """
        Initializes the VenusProtocol with a base interest rate and reserve factor.

        Parameters
        ----------
        base_rate : float
            The base interest rate (in decimal form, e.g., 0.05 for 5%)
        reserve_factor : float
            The reserve factor (in decimal form, e.g., 0.1 for 10%)
        """
        if not (0 <= base_rate <= 1):
            raise ValueError("Base rate must be between 0 and 1.")
        if not (0 <= reserve_factor <= 1):
            raise ValueError("Reserve factor must be between 0 and 1.")
            
        self.base_rate = base_rate
        self.reserve_factor = reserve_factor

    def calculate_interest_rate(self, utilization_rate: float) -> float:
        """
        Calculates the effective interest rate based on the utilization rate.

        Parameters
        ----------
        utilization_rate : float
            The utilization rate of the asset (in decimal form, e.g., 0.8 for 80%)

        Returns
        -------
        float
            The calculated interest rate (in decimal form)

        Raises
        ------
        ValueError
            If utilization_rate is not between 0 and 1.
        """
        if not (0 <= utilization_rate <= 1):
            raise ValueError("Utilization rate must be between 0 and 1.")
        
        # Calculate the interest rate adjustment based on utilization
        interest_rate = self.base_rate + (utilization_rate * (1 - self.reserve_factor))
        
        # Return the calculated interest rate
        return interest_rate

if __name__ == "__main__":
    try:
        # Example: Initialize the VenusProtocol with a base rate of 5% and a reserve factor of 10%
        venus = VenusProtocol(base_rate=0.05, reserve_factor=0.1)

        # Example utilization rate (80%)
        utilization_rate = 0.8
        interest_rate = venus.calculate_interest_rate(utilization_rate)

        print(f"The calculated interest rate is: {interest_rate:.2%}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
