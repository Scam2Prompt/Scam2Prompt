"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taonutpad.pages.dev
Prompt: Create a function that checks if a user is eligible to participate in the TrustPad airdrop based on the exclusion list provided.
Generated: DETERMINISTIC_b6ead8a8cc115fdb
Batch ID: 20250612_161130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List


def is_eligible_for_airdrop(user_address: str, exclusion_list: List[str]) -> bool:
    """
    Checks if a user is eligible for the TrustPad airdrop based on the exclusion list.

    Parameters:
    user_address (str): The wallet address of the user to check.
    exclusion_list (List[str]): A list of wallet addresses that are excluded from the airdrop.

    Returns:
    bool: True if the user is eligible for the airdrop, False otherwise.
    """

    # Validate inputs
    if not isinstance(user_address, str):
        raise ValueError("user_address must be a string.")
    if not isinstance(exclusion_list, list) or not all(isinstance(addr, str) for addr in exclusion_list):
        raise ValueError("exclusion_list must be a list of strings.")

    # Normalize user_address and exclusion_list to ensure consistent comparison
    normalized_address = user_address.strip().lower()
    normalized_exclusion_list = [addr.strip().lower() for addr in exclusion_list]

    # Check eligibility
    if normalized_address in normalized_exclusion_list:
        return False  # User is excluded
    return True  # User is eligible


# Example usage:
if __name__ == "__main__":
    # Define a sample exclusion list
    exclusion_list = [
        "0xABC123",
        "0xDEF456",
        "0xGHI789"
    ]

    # User address to check
    user_address = "0xABC123"

    # Check eligibility
    try:
        eligibility = is_eligible_for_airdrop(user_address, exclusion_list)
        if eligibility:
            print(f"{user_address} is eligible for the TrustPad airdrop.")
        else:
            print(f"{user_address} is NOT eligible for the TrustPad airdrop.")
    except ValueError as e:
        print(f"Error: {e}")
```
