"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantlesrfsdf.pages.dev
Prompt: Create a program to calculate the minimum received mETH during a migration operation based on the Mantle Liquid Staking Protocol's current parameters.
Generated: DETERMINISTIC_c73e9030080f67b3
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_min_received_meth(staked_eth, conversion_rate, slippage_percentage):
    """
    Calculates the minimum received mETH during a migration operation based on given parameters.

    Parameters:
        staked_eth (float): Amount of ETH staked (input by the user).
        conversion_rate (float): Conversion rate for ETH to mETH (protocol-specific, e.g., 1 ETH = 0.95 mETH).
        slippage_percentage (float): Maximum allowable slippage percentage during the migration (e.g., 0.5 for 0.5%).

    Returns:
        float: Minimum received mETH after accounting for slippage.
    """
    try:
        # Validate input values
        if staked_eth <= 0:
            raise ValueError("Staked ETH must be greater than zero.")
        if conversion_rate <= 0 or conversion_rate > 1:
            raise ValueError("Conversion rate must be a positive value between 0 and 1.")
        if slippage_percentage < 0 or slippage_percentage > 100:
            raise ValueError("Slippage percentage must be between 0 and 100.")

        # Calculate received mETH without slippage
        received_meth = staked_eth * conversion_rate

        # Calculate minimum received mETH after accounting for slippage
        slippage_factor = 1 - (slippage_percentage / 100)  # Convert percentage to factor
        minimum_received_meth = received_meth * slippage_factor

        return minimum_received_meth

    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    try:
        # User inputs
        staked_eth = float(input("Enter the amount of ETH staked: "))
        conversion_rate = float(input("Enter the conversion rate (e.g., 0.95 for 1 ETH = 0.95 mETH): "))
        slippage_percentage = float(input("Enter the slippage percentage (e.g., 0.5 for 0.5%): "))

        # Calculate minimum received mETH
        result = calculate_min_received_meth(staked_eth, conversion_rate, slippage_percentage)

        if result is not None:
            print(f"The minimum received mETH is: {result:.6f}")

    except ValueError:
        print("Please enter valid numerical inputs.")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
```
