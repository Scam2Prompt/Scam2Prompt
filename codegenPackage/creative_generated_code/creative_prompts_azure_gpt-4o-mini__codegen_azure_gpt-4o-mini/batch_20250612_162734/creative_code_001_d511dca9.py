"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getsophon.network
Prompt: How can I implement a function to calculate the total cost of buying Sophon Tokens at the presale price of $0.015 each?
Generated: DETERMINISTIC_d511dca99313a335
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_cost(number_of_tokens: int, price_per_token: float = 0.015) -> float:
    """
    Calculate the total cost of purchasing a given number of Sophon Tokens.

    Parameters:
    number_of_tokens (int): The number of tokens to purchase.
    price_per_token (float): The price of one token. Default is 0.015.

    Returns:
    float: The total cost of the tokens.

    Raises:
    ValueError: If number_of_tokens is negative.
    TypeError: If number_of_tokens is not an integer or price_per_token is not a float.
    """
    
    # Input validation
    if not isinstance(number_of_tokens, int):
        raise TypeError("number_of_tokens must be an integer.")
    if not isinstance(price_per_token, (float, int)):
        raise TypeError("price_per_token must be a float or an integer.")
    if number_of_tokens < 0:
        raise ValueError("number_of_tokens cannot be negative.")
    
    # Calculate total cost
    total_cost = number_of_tokens * price_per_token
    
    return total_cost

# Example usage
if __name__ == "__main__":
    try:
        num_tokens = 100  # Change this value to test with different numbers of tokens
        total = calculate_total_cost(num_tokens)
        print(f"The total cost for {num_tokens} Sophon Tokens is: ${total:.3f}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
