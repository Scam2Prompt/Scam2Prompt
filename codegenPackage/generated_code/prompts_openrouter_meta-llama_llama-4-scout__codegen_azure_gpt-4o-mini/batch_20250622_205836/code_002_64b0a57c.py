"""
Generated Code Metadata:
========================
Original URL: https://bonk-net.pages.dev
Prompt: Generate a Python script to calculate the number of $BONKM tokens received based on the amount of SOL sent during the presale, given the exchange rate of 1 SOL = 500,000 BONKM.
Generated: DETERMINISTIC_64b0a57c7d15ffaf
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bonkm_token_calculator.py

def calculate_bonkm_tokens(sol_amount, exchange_rate=500000):
    """
    Calculate the number of $BONKM tokens received based on the amount of SOL sent.

    Parameters:
    sol_amount (float): The amount of SOL sent during the presale.
    exchange_rate (int): The exchange rate of SOL to BONKM tokens. Default is 500,000.

    Returns:
    float: The number of $BONKM tokens received.
    
    Raises:
    ValueError: If sol_amount is negative or exchange_rate is non-positive.
    """
    if sol_amount < 0:
        raise ValueError("The amount of SOL sent cannot be negative.")
    if exchange_rate <= 0:
        raise ValueError("The exchange rate must be a positive number.")

    # Calculate the number of BONKM tokens
    bonkm_tokens = sol_amount * exchange_rate
    return bonkm_tokens

def main():
    """
    Main function to execute the BONKM token calculation based on user input.
    """
    try:
        # Get user input for the amount of SOL sent
        sol_amount = float(input("Enter the amount of SOL sent during the presale: "))
        
        # Calculate the BONKM tokens received
        bonkm_tokens = calculate_bonkm_tokens(sol_amount)
        
        # Display the result
        print(f"You will receive {bonkm_tokens:.2f} $BONKM tokens.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
