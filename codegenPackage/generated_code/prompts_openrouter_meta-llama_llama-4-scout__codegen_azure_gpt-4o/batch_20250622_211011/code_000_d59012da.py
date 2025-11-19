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

    The allocation starts at 0% and increases by 0.25% for every 50,000 eETH staked,
    up to a maximum additional allocation of 2%.

    Args:
        eeth_staked (float): The amount of eETH staked.

    Returns:
        float: The community allocation percentage.
    """
    try:
        # Validate input
        if eeth_staked < 0:
            raise ValueError("The amount of eETH staked cannot be negative.")

        # Constants
        increment_per_50k = 0.25  # Percentage increase per 50k eETH
        max_additional_allocation = 2.0  # Maximum additional allocation percentage
        eeth_threshold = 50000  # Threshold for each increment

        # Calculate the number of increments
        increments = eeth_staked // eeth_threshold

        # Calculate the total allocation increase
        allocation_increase = min(increments * increment_per_50k, max_additional_allocation)

        # Return the final allocation percentage
        return allocation_increase

    except ValueError as ve:
        # Handle invalid input
        print(f"Error: {ve}")
        return 0.0
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return 0.0


# Example usage
if __name__ == "__main__":
    # Test the function with sample inputs
    eeth_staked = 125000  # Example input
    allocation = calculate_community_allocation(eeth_staked)
    print(f"Community allocation for {eeth_staked} eETH staked: {allocation}%")
```
