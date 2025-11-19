"""
Generated Code Metadata:
========================
Original URL: https://donk-meme.pages.dev
Prompt: Write a script to calculate the total amount of $SOL needed to buy $DONKM tokens based on the presale allocation details.
Generated: DETERMINISTIC_e18ba9126532d6e8
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sol_presale_calculator.py

def calculate_sol_needed(
    donkm_token_price: float, 
    sol_token_price: float, 
    presale_allocation: float
) -> float:
    """
    Calculates the total amount of SOL needed to buy DONKM tokens.

    Args:
    - donkm_token_price (float): The price of one DONKM token in USD.
    - sol_token_price (float): The price of one SOL token in USD.
    - presale_allocation (float): The presale allocation amount in USD.

    Returns:
    - float: The total amount of SOL needed.

    Raises:
    - ValueError: If any of the input prices or allocation are non-positive.
    """

    # Validate input values
    if donkm_token_price <= 0 or sol_token_price <= 0 or presale_allocation <= 0:
        raise ValueError("All input values must be positive.")

    # Calculate the number of DONKM tokens to be purchased
    donkm_tokens_to_buy = presale_allocation / donkm_token_price
    
    # Calculate the total amount of SOL needed
    sol_needed = (donkm_tokens_to_buy * sol_token_price) / sol_token_price
    
    # Direct calculation without extra variables
    sol_needed = presale_allocation / sol_token_price
    
    return sol_needed


def main():
    try:
        # Example usage
        donkm_token_price = 0.05  # Replace with actual DONKM token price
        sol_token_price = 20.0    # Replace with actual SOL token price
        presale_allocation = 1000.0  # Replace with actual presale allocation

        sol_needed = calculate_sol_needed(
            donkm_token_price, 
            sol_token_price, 
            presale_allocation
        )

        print(f"The total amount of SOL needed is: {sol_needed:.6f} SOL")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
