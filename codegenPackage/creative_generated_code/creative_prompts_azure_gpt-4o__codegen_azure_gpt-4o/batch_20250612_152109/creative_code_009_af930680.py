"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://papeairdropclaim.pages.dev
Prompt: Create a function in Python or JavaScript to calculate the equivalent amount of $PAPE tokens received for a given amount of ETH, based on the presale stage price.
Generated: DETERMINISTIC_af93068052126b66
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the requested Python code for calculating the equivalent amount of $PAPE tokens for a given amount of ETH based on the presale stage price:

```python
def calculate_pape_tokens(eth_amount, presale_stage_prices):
    """
    Calculate the equivalent amount of $PAPE tokens for a given amount of ETH.

    Args:
        eth_amount (float): The amount of ETH to calculate tokens for.
        presale_stage_prices (dict): A dictionary with presale stages as keys and prices (ETH per token) as values.
                                     For example: {1: 0.0004, 2: 0.0005, 3: 0.0006}

    Returns:
        dict: A dictionary containing the number of tokens for each presale stage.
              For example: {'Stage 1': 2500.0, 'Stage 2': 2000.0, 'Stage 3': 1666.67}

    Raises:
        ValueError: If `eth_amount` is negative or if `presale_stage_prices` is empty.
    """
    # Validate input
    if eth_amount < 0:
        raise ValueError("ETH amount cannot be negative.")
    if not presale_stage_prices:
        raise ValueError("Presale stage prices cannot be empty.")

    # Calculate $PAPE tokens for each stage
    tokens_per_stage = {}
    for stage, price in presale_stage_prices.items():
        if price <= 0:  # Ensure price is positive
            raise ValueError(f"Invalid price {price} for Stage {stage}. Prices must be greater than zero.")
        tokens = eth_amount / price
        tokens_per_stage[f"Stage {stage}"] = round(tokens, 2)  # Round to 2 decimal places for readability

    return tokens_per_stage


# Example usage:
if __name__ == "__main__":
    try:
        # Define presale stage prices (ETH per $PAPE token)
        presale_prices = {1: 0.0004, 2: 0.0005, 3: 0.0006}
        
        # Input: Amount of ETH
        eth_amount_input = 1.0  # Example: 1 ETH
        
        # Calculate equivalent $PAPE tokens
        result = calculate_pape_tokens(eth_amount_input, presale_prices)
        
        # Output result
        for stage, tokens in result.items():
            print(f"{stage}: {tokens} tokens")
    except ValueError as e:
        print(f"Error: {e}")
```

Let me know if you need a JavaScript version!
