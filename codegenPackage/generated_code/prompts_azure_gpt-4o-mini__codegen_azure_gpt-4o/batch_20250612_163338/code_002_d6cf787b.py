"""
Generated Code Metadata:
========================
Original URL: https://cybercoclaim.pages.dev
Prompt: Generate a script that calculates CYBER Points based on the staking details provided for Ethereum, OP Mainnet, and BNB Smart Chain.
Generated: DETERMINISTIC_d6cf787b5ce4c932
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_cyber_points(staking_details):
    """
    Calculate CYBER Points based on staking details for Ethereum, OP Mainnet, and BNB Smart Chain.

    Parameters:
        staking_details (dict): A dictionary containing staking details for each chain.
                                Example:
                                {
                                    "Ethereum": {"staked_amount": 100, "multiplier": 1.5},
                                    "OP Mainnet": {"staked_amount": 200, "multiplier": 1.2},
                                    "BNB Smart Chain": {"staked_amount": 300, "multiplier": 1.1}
                                }

    Returns:
        dict: A dictionary containing CYBER Points for each chain and the total CYBER Points.
    """
    try:
        # Validate input
        if not isinstance(staking_details, dict):
            raise ValueError("staking_details must be a dictionary.")

        # Initialize result dictionary
        cyber_points = {}
        total_points = 0

        # Calculate CYBER Points for each chain
        for chain, details in staking_details.items():
            if not isinstance(details, dict) or "staked_amount" not in details or "multiplier" not in details:
                raise ValueError(f"Invalid staking details for {chain}. Must contain 'staked_amount' and 'multiplier'.")

            staked_amount = details["staked_amount"]
            multiplier = details["multiplier"]

            if not isinstance(staked_amount, (int, float)) or not isinstance(multiplier, (int, float)):
                raise ValueError(f"Invalid data types for {chain}. 'staked_amount' and 'multiplier' must be numeric.")

            # Calculate points for the chain
            points = staked_amount * multiplier
            cyber_points[chain] = points
            total_points += points

        # Add total points to the result
        cyber_points["Total"] = total_points

        return cyber_points

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return None


if __name__ == "__main__":
    # Example staking details
    staking_details = {
        "Ethereum": {"staked_amount": 100, "multiplier": 1.5},
        "OP Mainnet": {"staked_amount": 200, "multiplier": 1.2},
        "BNB Smart Chain": {"staked_amount": 300, "multiplier": 1.1}
    }

    # Calculate CYBER Points
    result = calculate_cyber_points(staking_details)

    if result:
        print("CYBER Points Calculation:")
        for chain, points in result.items():
            print(f"{chain}: {points}")
```
