"""
Generated Code Metadata:
========================
Original URL: https://bafybeic2ctv7vwt47e6rhckifdcdc2wzxyddiqrge5yfp43c2nk2co6d2u.ipfs.dweb.link
Prompt: Generate a script to calculate APR multipliers for Bedrock stakers with matured positions, using the eligibility criteria described on the Bedrock platform.
Generated: DETERMINISTIC_ebbb02cbc483d36a
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# apr_multiplier_calculator.py

from typing import List, Dict

class BedrockStaker:
    def __init__(self, staker_address: str, matured_positions: List[Dict]):
        """
        Initialize a Bedrock staker.

        Args:
        - staker_address (str): The address of the staker.
        - matured_positions (List[Dict]): A list of matured positions.
        """
        self.staker_address = staker_address
        self.matured_positions = matured_positions

def calculate_apr_multiplier(staker: BedrockStaker) -> float:
    """
    Calculate the APR multiplier for a Bedrock staker with matured positions.

    Args:
    - staker (BedrockStaker): The Bedrock staker.

    Returns:
    - float: The APR multiplier.

    Raises:
    - ValueError: If the staker has no matured positions.
    """
    if not staker.matured_positions:
        raise ValueError("Staker has no matured positions")

    # Calculate the total reward
    total_reward = sum(position["reward"] for position in staker.matured_positions)

    # Calculate the total duration
    total_duration = sum(position["duration"] for position in staker.matured_positions)

    if total_duration == 0:
        raise ValueError("Total duration cannot be zero")

    # Calculate the APR multiplier
    apr_multiplier = total_reward / total_duration

    return apr_multiplier

def check_eligibility(staker: BedrockStaker) -> bool:
    """
    Check if a Bedrock staker is eligible for APR multiplier calculation.

    Args:
    - staker (BedrockStaker): The Bedrock staker.

    Returns:
    - bool: True if the staker is eligible, False otherwise.
    """
    # Eligibility criteria:
    # 1. The staker must have at least one matured position.
    if not staker.matured_positions:
        return False

    # 2. The staker's matured positions must have a total duration greater than 0.
    total_duration = sum(position["duration"] for position in staker.matured_positions)
    if total_duration <= 0:
        return False

    return True

def main():
    try:
        # Example usage:
        staker_address = "0x1234567890abcdef"
        matured_positions = [
            {"reward": 100, "duration": 30},
            {"reward": 200, "duration": 60},
        ]

        staker = BedrockStaker(staker_address, matured_positions)

        if check_eligibility(staker):
            apr_multiplier = calculate_apr_multiplier(staker)
            print(f"APR multiplier for staker {staker_address}: {apr_multiplier}")
        else:
            print(f"Staker {staker_address} is not eligible for APR multiplier calculation")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
