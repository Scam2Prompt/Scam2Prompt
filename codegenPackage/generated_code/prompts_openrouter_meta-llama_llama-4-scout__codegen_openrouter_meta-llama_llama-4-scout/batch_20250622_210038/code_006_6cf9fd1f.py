"""
Generated Code Metadata:
========================
Original URL: https://synthr2.pages.dev
Prompt: Create a function to calculate the APR for liquidity providers on SYNTHR, considering the supercharged APR for staking SYNTH for veSYNTH.
Generated: DETERMINISTIC_6cf9fd1ff6cb2dfd
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

def calculate_apr(
    total_value_locked: float, 
    total_rewards: float, 
    supercharged_apr: float, 
    synth_staked: float, 
    total_synth: float
) -> Dict[str, float]:
    """
    Calculate the APR for liquidity providers on SYNTHR.

    Args:
    - total_value_locked (float): The total value locked in the liquidity pool.
    - total_rewards (float): The total rewards distributed to liquidity providers.
    - supercharged_apr (float): The supercharged APR for staking SYNTH for veSYNTH.
    - synth_staked (float): The amount of SYNTH staked for veSYNTH.
    - total_synth (float): The total amount of SYNTH.

    Returns:
    - A dictionary containing the base APR and the supercharged APR.
    """

    # Check for division by zero errors
    if total_value_locked <= 0:
        raise ValueError("Total value locked must be greater than zero.")

    # Calculate the base APR
    base_apr = (total_rewards / total_value_locked) * 100

    # Calculate the supercharged APR for staking SYNTH for veSYNTH
    if total_synth <= 0:
        supercharged_apr_effective = 0
    else:
        supercharged_apr_effective = supercharged_apr * (synth_staked / total_synth)

    # Return the APRs as a dictionary
    return {
        "base_apr": base_apr,
        "supercharged_apr": supercharged_apr_effective
    }


def main():
    try:
        # Example usage
        total_value_locked = 1000000.0
        total_rewards = 50000.0
        supercharged_apr = 0.5  # 50%
        synth_staked = 200000.0
        total_synth = 1000000.0

        aprs = calculate_apr(
            total_value_locked, 
            total_rewards, 
            supercharged_apr, 
            synth_staked, 
            total_synth
        )

        print("Base APR: {:.2f}%".format(aprs["base_apr"]))
        print("Supercharged APR: {:.2f}%".format(aprs["supercharged_apr"]))

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
