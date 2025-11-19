"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jesse-presale-8r8.pages.dev
Prompt: Write a function that determines the amount of BASE needed to purchase a specific number of JESSE tokens based on the presale cap.
Generated: DETERMINISTIC_ce81c1de7f5ea37c
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_base_for_jesse(presale_cap: float, jesse_token_price: float, desired_jesse_tokens: int) -> float:
    """
    Calculate the amount of BASE needed to purchase a specific number of JESSE tokens.
    
    Parameters:
    presale_cap (float): The maximum amount of BASE that can be spent in the presale.
    jesse_token_price (float): The price of one JESSE token in BASE.
    desired_jesse_tokens (int): The number of JESSE tokens the user wants to purchase.
    
    Returns:
    float: The amount of BASE needed to purchase the desired number of JESSE tokens.
    
    Raises:
    ValueError: If any of the input values are invalid (negative or zero).
    """
    
    # Validate input parameters
    if presale_cap <= 0:
        raise ValueError("Presale cap must be greater than zero.")
    if jesse_token_price <= 0:
        raise ValueError("JESSE token price must be greater than zero.")
    if desired_jesse_tokens <= 0:
        raise ValueError("Desired JESSE tokens must be greater than zero.")
    
    # Calculate the total cost in BASE for the desired JESSE tokens
    total_cost = jesse_token_price * desired_jesse_tokens
    
    # Check if the total cost exceeds the presale cap
    if total_cost > presale_cap:
        raise ValueError("Total cost exceeds the presale cap.")
    
    return total_cost

# Example usage (remove or comment out in production):
if __name__ == '__main__':
    try:
        presale_cap = 1000.0  # Example presale cap in BASE
        jesse_token_price = 5.0  # Example price of one JESSE token in BASE
        desired_jesse_tokens = 50  # Example desired number of JESSE tokens
        
        amount_needed = calculate_base_for_jesse(presale_cap, jesse_token_price, desired_jesse_tokens)
        print(f"Amount of BASE needed: {amount_needed}")
    except ValueError as e:
        print(f"Error: {e}")
```
