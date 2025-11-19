"""
Generated Code Metadata:
========================
Original URL: https://presale-srunexyz.pages.dev
Prompt: Write a script in Python to calculate the amount of $SRUNE tokens received for a given amount of SOL based on the exchange rate provided on the $SRUNE pre-sale page (1 SOL = 99,500 $SRUNE).
Generated: DETERMINISTIC_5128c07e36ba045b
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_srune_tokens(sol_amount: float) -> float:
    """
    Calculate the amount of $SRUNE tokens received for a given amount of SOL.
    
    Args:
        sol_amount (float): Amount of SOL to be exchanged for $SRUNE tokens.
        
    Returns:
        float: Amount of $SRUNE tokens received.
        
    Raises:
        ValueError: If sol_amount is negative.
    """
    if sol_amount < 0:
        raise ValueError("SOL amount cannot be negative.")
    
    exchange_rate = 99500  # 1 SOL = 99,500 $SRUNE
    srune_amount = sol_amount * exchange_rate
    return srune_amount

def main():
    try:
        sol_amount = float(input("Enter the amount of SOL you want to exchange: "))
        srune_amount = calculate_srune_tokens(sol_amount)
        print(f"You will receive {srune_amount:,.0f} $SRUNE tokens for {sol_amount} SOL.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
