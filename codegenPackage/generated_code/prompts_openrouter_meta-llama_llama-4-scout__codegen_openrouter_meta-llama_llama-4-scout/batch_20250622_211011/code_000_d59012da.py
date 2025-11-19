"""
Generated Code Metadata:
========================
Original URL: https://etherfi.vercel.app
Prompt: Write a function to calculate the community allocation for Ether.fi based on the amount of eETH staked, considering the 0.25% increase for every 50k eETH staked up to an additional 2%.
Generated: DETERMINISTIC_d59012da11efdf2c
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_community_allocation(eeth_staked: float) -> float:
    """
    Calculate the community allocation for Ether.fi based on the amount of eETH staked.

    The community allocation increases by 0.25% for every 50k eETH staked, up to an additional 2%.

    Args:
        eeth_staked (float): The amount of eETH staked.

    Returns:
        float: The community allocation as a percentage.

    Raises:
        ValueError: If the eETH staked amount is negative.
    """

    # Check for negative eETH staked amount
    if eeth_staked < 0:
        raise ValueError("eETH staked amount cannot be negative")

    # Base community allocation
    base_allocation = 0.0  # 0%

    # Calculate the number of 50k eETH increments
    increments = int(eeth_staked // 50000)

    # Calculate the additional allocation
    additional_allocation = min(increments * 0.25, 2.0)  # up to 2% additional allocation

    # Calculate the total community allocation
    total_allocation = base_allocation + additional_allocation

    return total_allocation


def main():
    try:
        eeth_staked = 150000  # example eETH staked amount
        community_allocation = calculate_community_allocation(eeth_staked)
        print(f"Community allocation for {eeth_staked} eETH staked: {community_allocation}%")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
