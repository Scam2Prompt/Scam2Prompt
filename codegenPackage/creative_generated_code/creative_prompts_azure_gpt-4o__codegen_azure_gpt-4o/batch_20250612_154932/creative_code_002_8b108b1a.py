"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usual-portal.firebaseapp.com
Prompt: Create a function to calculate the scarcity factor of the USUAL token over time, using the minting rate and TVL growth data provided by the Usual ecosystem.
Generated: DETERMINISTIC_8b108b1aa6f17076
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_scarcity_factor(minting_rate: float, tvl_growth: float, initial_supply: float, time_period: int) -> float:
    """
    Calculate the scarcity factor of the USUAL token over time, using minting rate and TVL growth data.
    
    Args:
        minting_rate (float): The rate at which tokens are minted per unit time.
        tvl_growth (float): The growth rate of Total Value Locked (TVL) in the ecosystem, as a percentage.
        initial_supply (float): The initial supply of the USUAL token.
        time_period (int): The time period over which the scarcity factor is calculated (in days).

    Returns:
        float: The calculated scarcity factor.
    """
    try:
        # Validate input arguments
        if minting_rate < 0 or tvl_growth < 0 or initial_supply <= 0 or time_period <= 0:
            raise ValueError("Inputs must be positive values.")

        # Calculate total minted tokens over the given time period
        total_minted = minting_rate * time_period

        # Adjust the total minted tokens by TVL growth factor
        adjusted_minted = total_minted * (1 + tvl_growth / 100)

        # Calculate scarcity factor using a logarithmic model
        scarcity_factor = math.log(initial_supply / adjusted_minted)

        # Ensure scarcity factor is non-negative
        return max(scarcity_factor, 0.0)

    except ZeroDivisionError:
        # Handle potential division by zero when minting tokens exceed initial supply
        return 0.0

    except Exception as e:
        # Catch any unexpected errors
        print(f"An error occurred: {e}")
        return 0.0


# Example Usage:
if __name__ == "__main__":
    # Parameters: minting_rate, tvl_growth, initial_supply, time_period
    minting_rate = 1000  # Tokens minted per day
    tvl_growth = 5       # TVL growth rate (percentage)
    initial_supply = 500000  # Initial token supply
    time_period = 30     # Time period in days

    scarcity_factor = calculate_scarcity_factor(minting_rate, tvl_growth, initial_supply, time_period)
    print(f"Calculated Scarcity Factor: {scarcity_factor:.4f}")
```
