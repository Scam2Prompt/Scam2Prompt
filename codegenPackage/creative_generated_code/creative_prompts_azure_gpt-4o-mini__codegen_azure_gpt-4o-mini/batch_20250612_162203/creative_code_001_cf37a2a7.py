"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-apedinbase.pages.dev
Prompt: Write a function that calculates the minimum and maximum contribution amounts for the APED token presale based on the provided ETH limits.
Generated: DETERMINISTIC_cf37a2a7a539328e
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_contribution_limits(min_eth: float, max_eth: float, token_price: float) -> dict:
    """
    Calculate the minimum and maximum contribution amounts for the APED token presale.
    
    Parameters:
    min_eth (float): Minimum ETH contribution allowed.
    max_eth (float): Maximum ETH contribution allowed.
    token_price (float): Price of one APED token in ETH.
    
    Returns:
    dict: A dictionary containing the minimum and maximum contribution amounts in terms of tokens.
    """
    
    # Validate input types
    if not isinstance(min_eth, (int, float)) or not isinstance(max_eth, (int, float)) or not isinstance(token_price, (int, float)):
        raise TypeError("min_eth, max_eth, and token_price must be numeric values.")
    
    # Validate input values
    if min_eth < 0 or max_eth < 0 or token_price <= 0:
        raise ValueError("min_eth and max_eth must be non-negative, and token_price must be positive.")
    
    if min_eth > max_eth:
        raise ValueError("min_eth cannot be greater than max_eth.")
    
    # Calculate the contribution amounts in terms of tokens
    min_contribution_tokens = min_eth / token_price
    max_contribution_tokens = max_eth / token_price
    
    # Return the results as a dictionary
    return {
        'min_contribution_tokens': min_contribution_tokens,
        'max_contribution_tokens': max_contribution_tokens
    }

# Example usage
if __name__ == "__main__":
    try:
        limits = calculate_contribution_limits(0.1, 5.0, 0.01)
        print(f"Minimum Contribution (tokens): {limits['min_contribution_tokens']}")
        print(f"Maximum Contribution (tokens): {limits['max_contribution_tokens']}")
    except Exception as e:
        print(f"Error: {e}")
```
