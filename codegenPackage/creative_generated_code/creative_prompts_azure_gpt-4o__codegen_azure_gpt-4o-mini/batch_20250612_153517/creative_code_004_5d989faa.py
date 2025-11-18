"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://babywif-io.pages.dev
Prompt: Write a Python function to calculate the distribution of Baby WIF ($BIF) tokens based on the tokenomics provided (95% for presale+liquidity and 5% for CEX listing).
Generated: DETERMINISTIC_5d989faa5de4eaa1
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_baby_wif_distribution(total_amount: float) -> dict:
    """
    Calculate the distribution of Baby WIF ($BIF) tokens based on predefined tokenomics.

    Tokenomics:
    - 95% for presale and liquidity
    - 5% for CEX listing

    Parameters:
    total_amount (float): The total amount of $BIF tokens to distribute.

    Returns:
    dict: A dictionary containing the distribution of tokens for presale, liquidity, and CEX listing.

    Raises:
    ValueError: If total_amount is negative or not a number.
    """

    # Validate the input
    if not isinstance(total_amount, (int, float)) or total_amount < 0:
        raise ValueError("total_amount must be a non-negative number")

    # Calculate the distribution
    presale_liquidity_amount = total_amount * 0.95
    cex_listing_amount = total_amount * 0.05

    # Create a distribution dictionary
    distribution = {
        "presale_liquidity": presale_liquidity_amount,
        "cex_listing": cex_listing_amount,
        "total": total_amount
    }

    return distribution

# Example usage
if __name__ == "__main__":
    try:
        total_tokens = 1000000  # Example total amount of tokens
        distribution = calculate_baby_wif_distribution(total_tokens)
        print(distribution)
    except ValueError as e:
        print(f"Error: {e}")
```
