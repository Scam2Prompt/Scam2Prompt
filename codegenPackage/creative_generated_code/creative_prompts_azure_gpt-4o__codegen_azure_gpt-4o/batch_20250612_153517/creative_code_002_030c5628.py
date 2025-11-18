"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedrip-apps.pages.dev
Prompt: Create a function that calculates the total value locked (TVL) in the Base Drip Garden using the provided $BDRIP price and supply details.
Generated: DETERMINISTIC_030c562887835850
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_tvl(bdrip_price, total_supply):
    """
    Calculates the Total Value Locked (TVL) in the Base Drip Garden.

    Parameters:
        bdrip_price (float): The price of 1 BDRIP token in USD.
        total_supply (float): The total supply of BDRIP tokens.

    Returns:
        float: The Total Value Locked (TVL) in USD.

    Raises:
        ValueError: If bdrip_price or total_supply is not a positive number.
    """
    try:
        # Validate inputs
        if bdrip_price <= 0 or total_supply <= 0:
            raise ValueError("Both bdrip_price and total_supply must be positive numbers.")

        # Calculate TVL
        tvl = bdrip_price * total_supply

        return tvl

    except ValueError as ve:
        # Handle any validation errors
        print(f"Input Error: {ve}")
        raise

    except Exception as e:
        # Catch-all for unexpected errors
        print(f"An unexpected error occurred: {e}")
        raise


# Example usage:
if __name__ == "__main__":
    try:
        # Example inputs
        current_bdrip_price = 5.25  # USD value of 1 BDRIP
        current_total_supply = 1000000  # Total supply of BDRIP tokens

        # Calculate TVL
        tvl = calculate_tvl(current_bdrip_price, current_total_supply)
        print(f"Total Value Locked (TVL): ${tvl:.2f}")
    except Exception as e:
        print("Failed to calculate TVL:", e)
```
