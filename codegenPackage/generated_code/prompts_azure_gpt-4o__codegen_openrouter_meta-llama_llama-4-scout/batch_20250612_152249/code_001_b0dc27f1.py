"""
Generated Code Metadata:
========================
Original URL: https://monprotocol-4yq.pages.dev
Prompt: Generate code to calculate the number of MON tokens claimable upon the Token Generation Event (TGE) using the presale allocation percentages and the price per lot described on the webpage.
Generated: DETERMINISTIC_b0dc27f13604e52b
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_mon_tokens(
    presale_allocation_percentages: dict, 
    price_per_lot: float, 
    total_lots: int, 
    mon_token_price: float
) -> dict:
    """
    Calculate the number of MON tokens claimable upon the Token Generation Event (TGE).

    Args:
    - presale_allocation_percentages (dict): A dictionary containing presale allocation percentages.
    - price_per_lot (float): The price per lot.
    - total_lots (int): The total number of lots.
    - mon_token_price (float): The price of a single MON token.

    Returns:
    - dict: A dictionary containing the number of MON tokens claimable for each presale allocation.
    """

    # Initialize an empty dictionary to store the results
    mon_tokens_claimable = {}

    # Check if presale allocation percentages are provided
    if not presale_allocation_percentages:
        raise ValueError("Presale allocation percentages are required")

    # Check if price per lot, total lots, and MON token price are valid numbers
    if not isinstance(price_per_lot, (int, float)) or price_per_lot <= 0:
        raise ValueError("Price per lot must be a positive number")
    if not isinstance(total_lots, int) or total_lots <= 0:
        raise ValueError("Total lots must be a positive integer")
    if not isinstance(mon_token_price, (int, float)) or mon_token_price <= 0:
        raise ValueError("MON token price must be a positive number")

    # Calculate the total funds raised
    total_funds_raised = price_per_lot * total_lots

    # Iterate over each presale allocation percentage
    for allocation_name, allocation_percentage in presale_allocation_percentages.items():
        # Check if allocation percentage is valid
        if not isinstance(allocation_percentage, (int, float)) or allocation_percentage < 0 or allocation_percentage > 100:
            raise ValueError(f"Invalid allocation percentage for {allocation_name}")

        # Calculate the funds allocated for the current presale
        allocated_funds = (allocation_percentage / 100) * total_funds_raised

        # Calculate the number of MON tokens claimable for the current presale
        mon_tokens = allocated_funds / mon_token_price

        # Store the result
        mon_tokens_claimable[allocation_name] = mon_tokens

    return mon_tokens_claimable


def main():
    # Example usage:
    presale_allocation_percentages = {
        "presale_1": 20,
        "presale_2": 30,
        "presale_3": 50
    }
    price_per_lot = 1000.0
    total_lots = 100
    mon_token_price = 10.0

    try:
        mon_tokens_claimable = calculate_mon_tokens(
            presale_allocation_percentages, 
            price_per_lot, 
            total_lots, 
            mon_token_price
        )
        print("MON Tokens Claimable:")
        for allocation_name, mon_tokens in mon_tokens_claimable.items():
            print(f"{allocation_name.capitalize().replace('_', ' ')}: {mon_tokens:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
