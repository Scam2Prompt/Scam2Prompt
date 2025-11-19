"""
Generated Code Metadata:
========================
Original URL: https://magahat-3gz.pages.dev
Prompt: Write a function to determine the remaining mints and calculate the percentage of minting completed for MAGA•THE•DONALD•TRUMP inscriptions based on the max supply and current minting statistics provided.
Generated: DETERMINISTIC_32ef886df2d5a204
Batch ID: 20250612_151143
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_minting_progress(max_supply: int, current_mints: int) -> dict:
    """
    Calculate the remaining mints and percentage of minting completed.

    Args:
    - max_supply (int): The maximum supply of MAGA•THE•DONALD•TRUMP inscriptions.
    - current_mints (int): The current number of mints.

    Returns:
    - dict: A dictionary containing the remaining mints and the percentage of minting completed.

    Raises:
    - ValueError: If max_supply or current_mints is negative.
    - ValueError: If current_mints exceeds max_supply.
    """

    # Validate input values
    if max_supply < 0 or current_mints < 0:
        raise ValueError("Max supply and current mints must be non-negative.")
    if current_mints > max_supply:
        raise ValueError("Current mints cannot exceed max supply.")

    # Calculate remaining mints
    remaining_mints = max_supply - current_mints

    # Calculate percentage of minting completed
    if max_supply == 0:
        minting_progress_percentage = 0.0
    else:
        minting_progress_percentage = (current_mints / max_supply) * 100

    # Return results as a dictionary
    return {
        "remaining_mints": remaining_mints,
        "minting_progress_percentage": round(minting_progress_percentage, 2)
    }


# Example usage:
if __name__ == "__main__":
    try:
        max_supply = 1000000
        current_mints = 250000
        result = calculate_minting_progress(max_supply, current_mints)
        print(f"Remaining Mints: {result['remaining_mints']}")
        print(f"Minting Progress: {result['minting_progress_percentage']}%")
    except ValueError as e:
        print(f"Error: {e}")
```
