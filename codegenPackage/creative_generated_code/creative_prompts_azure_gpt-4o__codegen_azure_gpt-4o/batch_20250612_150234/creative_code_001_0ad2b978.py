"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xmr-mixer.to
Prompt: Generate code to implement a feature that calculates the total fees for mixing a given amount of XMR using the fee structure provided by Monero Mixer, including the extra fee per target address.
Generated: DETERMINISTIC_0ad2b97861f9220b
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_mixing_fees(amount_xmr, num_target_addresses, base_fee_percentage, extra_fee_per_address):
    """
    Calculate the total mixing fees for a given amount of XMR.

    Parameters:
    amount_xmr (float): The amount of XMR to be mixed.
    num_target_addresses (int): The number of target addresses to mix the XMR into.
    base_fee_percentage (float): The base fee percentage (e.g., 0.5 for 0.5%).
    extra_fee_per_address (float): The extra flat fee (in XMR) per additional target address.

    Returns:
    float: The total fee in XMR.

    Raises:
    ValueError: If any input is invalid (e.g., negative values or zero addresses).
    """
    # Input validation
    if amount_xmr <= 0:
        raise ValueError("The amount of XMR to be mixed must be greater than 0.")
    if num_target_addresses <= 0:
        raise ValueError("The number of target addresses must be greater than 0.")
    if base_fee_percentage < 0:
        raise ValueError("The base fee percentage cannot be negative.")
    if extra_fee_per_address < 0:
        raise ValueError("The extra fee per address cannot be negative.")

    # Base fee calculation (percentage of the amount)
    base_fee = (base_fee_percentage / 100) * amount_xmr

    # Extra fee calculation (flat fee per target address, excluding the 1st address)
    extra_fee = extra_fee_per_address * max(0, num_target_addresses - 1)

    # Total fee is the sum of the base fee and extra fees
    total_fee = base_fee + extra_fee

    return total_fee


# Example usage (for testing/debugging purposes)
if __name__ == "__main__":
    try:
        # Define input values
        amount_to_mix = 10.0  # In XMR
        target_addresses = 3
        base_fee_percent = 0.5  # 0.5%
        extra_fee_per_addr = 0.01  # 0.01 XMR per extra address

        # Calculate the total mixing fee
        total_fee = calculate_mixing_fees(
            amount_to_mix, target_addresses, base_fee_percent, extra_fee_per_addr
        )

        # Print the result
        print(f"The total mixing fee is: {total_fee:.6f} XMR")
    except ValueError as e:
        print(f"Error: {e}")
```
