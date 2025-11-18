"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v1-fixedflolat.com
Prompt: Write code to calculate and display FixedFloat's transaction fees for both fixed and floating rate swaps, based on user input for cryptocurrency pair and amount.
Generated: DETERMINISTIC_f79d5dad9a8bd77f
Batch ID: 20250612_154842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_fixed_rate_fee(amount):
    """
    Calculate the transaction fee for fixed rate swaps.
    Fixed rate swaps have a flat fee of 1% of the transaction amount.
    """
    try:
        fee = amount * 0.01  # Fixed rate fee is 1%
        return round(fee, 8)  # Round to 8 decimal places for precision
    except Exception as e:
        raise ValueError(f"Error calculating fixed rate fee: {e}")

def calculate_floating_rate_fee(amount):
    """
    Calculate the transaction fee for floating rate swaps.
    Floating rate swaps have a fee of 0.5% of the transaction amount.
    """
    try:
        fee = amount * 0.005  # Floating rate fee is 0.5%
        return round(fee, 8)  # Round to 8 decimal places for precision
    except Exception as e:
        raise ValueError(f"Error calculating floating rate fee: {e}")

def main():
    """
    Main function to take user input, calculate fees, and display results.
    """
    try:
        print("Welcome to FixedFloat Fee Calculator!")
        
        # Prompt user for cryptocurrency pair
        crypto_pair = input("Enter the cryptocurrency pair (e.g., BTC-ETH): ").strip()
        if not crypto_pair:
            raise ValueError("Cryptocurrency pair cannot be empty.")
        
        # Prompt user for transaction amount
        try:
            amount = float(input("Enter the transaction amount (in crypto units): ").strip())
            if amount <= 0:
                raise ValueError("Transaction amount must be positive.")
        except ValueError:
            raise ValueError("Invalid transaction amount. Please enter a valid number.")
        
        # Calculate fees for fixed and floating rate swaps
        fixed_fee = calculate_fixed_rate_fee(amount)
        floating_fee = calculate_floating_rate_fee(amount)
        
        # Display the results
        print("\nTransaction Fee Details:")
        print(f"Cryptocurrency Pair: {crypto_pair}")
        print(f"Transaction Amount: {amount:.8f}")
        print(f"Fixed Rate Swap Fee (1%): {fixed_fee:.8f}")
        print(f"Floating Rate Swap Fee (0.5%): {floating_fee:.8f}")
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
