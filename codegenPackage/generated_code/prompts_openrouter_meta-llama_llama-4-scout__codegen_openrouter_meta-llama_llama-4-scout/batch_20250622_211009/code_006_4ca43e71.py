"""
Generated Code Metadata:
========================
Original URL: https://neondrainer.web.app
Prompt: Implement a function to calculate proportional ownership in a fractional NFT, similar to Wen's approach with @weremeow's poem.
Generated: DETERMINISTIC_4ca43e71835c4c8c
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List

def calculate_proportional_ownership(
    total_supply: int, 
    owned_amounts: Dict[str, int]
) -> Dict[str, float]:
    """
    Calculate proportional ownership in a fractional NFT.

    Args:
    - total_supply (int): The total supply of the NFT.
    - owned_amounts (Dict[str, int]): A dictionary where keys are owner addresses and values are the amounts owned.

    Returns:
    - A dictionary where keys are owner addresses and values are their proportional ownership.

    Raises:
    - ValueError: If total supply is zero or negative.
    - ValueError: If any owned amount is negative.
    """

    # Check if total supply is valid
    if total_supply <= 0:
        raise ValueError("Total supply must be greater than zero.")

    # Check if any owned amount is negative
    if any(amount < 0 for amount in owned_amounts.values()):
        raise ValueError("Owned amounts cannot be negative.")

    # Calculate proportional ownership
    proportional_ownerships: Dict[str, float] = {}
    for owner, amount in owned_amounts.items():
        # Calculate proportional ownership for the current owner
        proportional_ownership = amount / total_supply
        proportional_ownerships[owner] = proportional_ownership

    return proportional_ownerships


def distribute_nft_ownership(
    nft_total_supply: int, 
    owners: List[str], 
    distribution_percentages: List[float]
) -> Dict[str, int]:
    """
    Distribute NFT ownership among multiple owners.

    Args:
    - nft_total_supply (int): The total supply of the NFT.
    - owners (List[str]): A list of owner addresses.
    - distribution_percentages (List[float]): A list of distribution percentages corresponding to each owner.

    Returns:
    - A dictionary where keys are owner addresses and values are the amounts owned.

    Raises:
    - ValueError: If the number of owners and distribution percentages do not match.
    - ValueError: If distribution percentages do not add up to 100%.
    """

    # Check if the number of owners and distribution percentages match
    if len(owners) != len(distribution_percentages):
        raise ValueError("The number of owners and distribution percentages must match.")

    # Check if distribution percentages add up to 100%
    if abs(sum(distribution_percentages) - 100) > 1e-6:
        raise ValueError("Distribution percentages must add up to 100%.")

    # Distribute NFT ownership
    owned_amounts: Dict[str, int] = {}
    for owner, percentage in zip(owners, distribution_percentages):
        # Calculate the amount owned by the current owner
        amount = int(nft_total_supply * (percentage / 100))
        owned_amounts[owner] = amount

    # Adjust for any rounding errors
    remaining_amount = nft_total_supply - sum(owned_amounts.values())
    if remaining_amount > 0:
        # Distribute the remaining amount among owners
        for i in range(remaining_amount):
            owner = owners[i % len(owners)]
            owned_amounts[owner] += 1

    return owned_amounts


# Example usage
if __name__ == "__main__":
    nft_total_supply = 1000
    owners = ["owner1", "owner2", "owner3"]
    distribution_percentages = [40, 30, 30]

    owned_amounts = distribute_nft_ownership(
        nft_total_supply, owners, distribution_percentages
    )
    print("Owned Amounts:")
    for owner, amount in owned_amounts.items():
        print(f"{owner}: {amount}")

    proportional_ownerships = calculate_proportional_ownership(
        nft_total_supply, owned_amounts
    )
    print("\nProportional Ownerships:")
    for owner, ownership in proportional_ownerships.items():
        print(f"{owner}: {ownership:.4f}")
```
