"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pumpkinspicebirds.xyz
Prompt: Create a function that calculates the total donation to givewell.org based on the number of Pumpkin Spice Moonbirds minted.
Generated: DETERMINISTIC_9c6cfb0880cce657
Batch ID: 20250612_135528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Code

def calculate_donation(moonbirds_minted):
    """
    Calculate the total donation amount to GiveWell.org based on the number of Pumpkin Spice Moonbirds minted.

    Args:
        moonbirds_minted (int): The number of Pumpkin Spice Moonbirds minted.

    Returns:
        float: The total donation amount in USD.

    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Constants
    DONATION_PER_MOONBIRD = 50.0  # USD donation for each Moonbird minted

    # Input validation
    if not isinstance(moonbirds_minted, int):
        raise ValueError("The number of Moonbirds minted must be an integer.")
    if moonbirds_minted < 0:
        raise ValueError("The number of Moonbirds minted cannot be negative.")

    # Calculate total donation
    total_donation = moonbirds_minted * DONATION_PER_MOONBIRD

    return total_donation


# Example Usage
if __name__ == "__main__":
    try:
        # Change the value below to test with different inputs
        minted_count = 10
        donation = calculate_donation(minted_count)
        print(f"The total donation for {minted_count} Pumpkin Spice Moonbirds is ${donation:.2f} USD.")
    except ValueError as e:
        print(f"Error: {e}")
```
