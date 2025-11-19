"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://slo.finance
Prompt: Create a function that calculates the total value locked (TVL) in Silo Finance based on the provided APRs and total supplies of various markets.
Generated: DETERMINISTIC_eba23114d9362570
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_tvl(aprs, total_supplies):
    """
    Calculate the Total Value Locked (TVL) in Silo Finance.

    Parameters:
        aprs (dict): A dictionary where keys are market names and values are their respective APRs (Annual Percentage Rates).
        total_supplies (dict): A dictionary where keys are market names and values are the total supply (in USD) for each market.

    Returns:
        float: The total value locked (TVL) across all markets.
    
    Raises:
        ValueError: If the input dictionaries have mismatched market names or invalid data.
    """
    # Input validation
    if not isinstance(aprs, dict) or not isinstance(total_supplies, dict):
        raise ValueError("Both aprs and total_supplies must be dictionaries.")
    
    if set(aprs.keys()) != set(total_supplies.keys()):
        raise ValueError("Market names in 'aprs' and 'total_supplies' must match.")
    
    tvl = 0.0  # Initialize the TVL accumulator

    for market in aprs:
        apr = aprs[market]
        supply = total_supplies[market]

        # Validating APR and total supply values
        if not isinstance(apr, (int, float)) or apr < 0:
            raise ValueError(f"APR for market '{market}' must be a non-negative number.")
        if not isinstance(supply, (int, float)) or supply < 0:
            raise ValueError(f"Total supply for market '{market}' must be a non-negative number.")
        
        # Accumulate the total supply into TVL
        tvl += supply

    return round(tvl, 2)  # Return the TVL rounded to two decimal places


# Example usage
if __name__ == "__main__":
    # Example market data
    aprs = {
        "ETH": 5.0,
        "BTC": 3.0,
        "USDC": 2.5
    }
    total_supplies = {
        "ETH": 1500000.00,
        "BTC": 1000000.00,
        "USDC": 2000000.00
    }

    try:
        tvl = calculate_tvl(aprs, total_supplies)
        print(f"Total Value Locked (TVL): ${tvl}")
    except ValueError as e:
        # Handle any errors gracefully
        print(f"Error: {e}")
```
