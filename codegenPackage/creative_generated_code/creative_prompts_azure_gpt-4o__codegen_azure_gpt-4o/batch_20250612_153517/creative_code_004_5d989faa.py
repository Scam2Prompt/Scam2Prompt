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
def calculate_bif_distribution(total_supply):
    """
    Calculates the distribution of Baby WIF ($BIF) tokens based on tokenomics.

    Tokenomics:
    - 95% of tokens for presale and liquidity
    - 5% of tokens for Centralized Exchange (CEX) listing

    Args:
        total_supply (int or float): The total supply of $BIF tokens.

    Returns:
        dict: A dictionary containing the distribution:
              {
                  "presale_liquidity": <amount for presale and liquidity>,
                  "cex_listing": <amount for CEX listing>
              }

    Raises:
        ValueError: If the total_supply is not a positive number.
    """
    # Validate the input
    if not isinstance(total_supply, (int, float)) or total_supply <= 0:
        raise ValueError("Total supply must be a positive number.")

    # Calculate distribution
    presale_liquidity = total_supply * 0.95
    cex_listing = total_supply * 0.05

    # Return the distribution as a dictionary
    return {
        "presale_liquidity": presale_liquidity,
        "cex_listing": cex_listing
    }


# Example usage
if __name__ == "__main__":
    try:
        total_tokens = 1000000  # Example total supply
        distribution = calculate_bif_distribution(total_tokens)
        print("Token Distribution:")
        print(f"Presale & Liquidity: {distribution['presale_liquidity']:.2f}")
        print(f"CEX Listing: {distribution['cex_listing']:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
