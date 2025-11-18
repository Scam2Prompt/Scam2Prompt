"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wagmicoins.web.app
Prompt: Write a function to calculate the number of $WAGMI tokens a user can receive for a given amount of ETH, considering the tokenomics described on the website.
Generated: DETERMINISTIC_2e4170672686a87c
Batch ID: 20250612_145521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Function to calculate the number of WAGMI tokens for a given ETH amount
# Tokenomics:
# - Base exchange rate: 1 ETH = 1000 WAGMI tokens
# - Bonus tiers:
#   - If ETH >= 10, bonus: +10% WAGMI tokens
#   - If ETH >= 50, bonus: +20% WAGMI tokens
# - Limitations:
#   - Maximum WAGMI tokens per transaction = 100,000
#   - Minimum ETH required: 0.01 ETH

def calculate_wagmi_tokens(eth_amount):
    """
    Calculate the number of WAGMI tokens a user can receive for a given ETH amount.

    :param eth_amount: float - The amount of ETH provided by the user.
    :return: int - Number of WAGMI tokens the user receives.
    :raises ValueError: If the input ETH amount is invalid.
    """
    # Constants
    BASE_EXCHANGE_RATE = 1000  # 1 ETH = 1000 WAGMI
    BONUS_TIER1_THRESHOLD = 10  # ETH threshold for +10% bonus
    BONUS_TIER2_THRESHOLD = 50  # ETH threshold for +20% bonus
    BONUS_TIER1_MULTIPLIER = 1.10  # +10% bonus
    BONUS_TIER2_MULTIPLIER = 1.20  # +20% bonus
    MAX_WAGMI_TOKENS = 100000  # Maximum tokens per transaction
    MIN_ETH_REQUIRED = 0.01  # Minimum ETH required

    # Input validation
    if eth_amount < MIN_ETH_REQUIRED:
        raise ValueError(f"Minimum ETH required is {MIN_ETH_REQUIRED}. Provided: {eth_amount}")

    # Calculate base token amount
    wagmi_tokens = eth_amount * BASE_EXCHANGE_RATE

    # Apply bonus tiers based on ETH amount
    if eth_amount >= BONUS_TIER2_THRESHOLD:
        wagmi_tokens *= BONUS_TIER2_MULTIPLIER
    elif eth_amount >= BONUS_TIER1_THRESHOLD:
        wagmi_tokens *= BONUS_TIER1_MULTIPLIER

    # Enforce maximum token limit
    if wagmi_tokens > MAX_WAGMI_TOKENS:
        wagmi_tokens = MAX_WAGMI_TOKENS

    # Return the number of tokens as an integer (rounded down)
    return int(wagmi_tokens)


# Example usage
if __name__ == "__main__":
    try:
        eth_input = float(input("Enter the amount of ETH: "))
        tokens = calculate_wagmi_tokens(eth_input)
        print(f"You will receive {tokens} WAGMI tokens.")
    except ValueError as e:
        print(f"Error: {e}")
```
