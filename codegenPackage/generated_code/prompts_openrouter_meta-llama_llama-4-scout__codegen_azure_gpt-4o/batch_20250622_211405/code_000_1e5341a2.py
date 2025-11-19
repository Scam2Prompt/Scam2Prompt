"""
Generated Code Metadata:
========================
Original URL: https://clearpool.pages.dev
Prompt: Write a Python script to calculate the APR for staking CPOOL tokens with different oracles on Clearpool, considering the oracle size and relative voting power.
Generated: DETERMINISTIC_1e5341a2b23ce329
Batch ID: 20250622_211405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_apr(staked_tokens, oracle_size, voting_power):
    """
    Calculate the Annual Percentage Rate (APR) for staking CPOOL tokens.

    Parameters:
        staked_tokens (float): The number of CPOOL tokens staked.
        oracle_size (int): The size of the oracle (number of participants).
        voting_power (float): The relative voting power of the oracle.

    Returns:
        float: The calculated APR as a percentage.
    """
    try:
        # Validate inputs
        if staked_tokens <= 0:
            raise ValueError("Staked tokens must be greater than zero.")
        if oracle_size <= 0:
            raise ValueError("Oracle size must be greater than zero.")
        if not (0 <= voting_power <= 1):
            raise ValueError("Voting power must be between 0 and 1.")

        # Base APR calculation
        base_apr = 10.0  # Example base APR percentage
        apr_multiplier = 1 + (voting_power * 0.5)  # Adjust APR based on voting power
        size_factor = 1 + (oracle_size / 100)  # Adjust APR based on oracle size

        # Final APR calculation
        apr = base_apr * apr_multiplier * size_factor

        return apr

    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to interact with the user and calculate APR.
    """
    print("Welcome to the CPOOL Staking APR Calculator!")

    try:
        # Get user inputs
        staked_tokens = float(input("Enter the number of CPOOL tokens staked: "))
        oracle_size = int(input("Enter the size of the oracle (number of participants): "))
        voting_power = float(input("Enter the relative voting power (0 to 1): "))

        # Calculate APR
        apr = calculate_apr(staked_tokens, oracle_size, voting_power)

        if apr is not None:
            print(f"The calculated APR for staking CPOOL tokens is: {apr:.2f}%")
        else:
            print("Failed to calculate APR due to invalid inputs.")

    except ValueError:
        print("Invalid input. Please enter numeric values where required.", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
