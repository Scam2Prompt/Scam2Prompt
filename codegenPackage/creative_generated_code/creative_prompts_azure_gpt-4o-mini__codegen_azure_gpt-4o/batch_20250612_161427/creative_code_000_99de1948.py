"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jesse-9y3.pages.dev
Prompt: Generate a code snippet to calculate the conversion rate from BASE to JESSE tokens based on a presale cap of 1000 BASE.
Generated: DETERMINISTIC_99de1948face5ced
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Token Conversion Rate Calculator
# This script calculates the conversion rate from BASE tokens to JESSE tokens
# based on a presale cap of 1000 BASE tokens.

# Constants
PRESALE_CAP = 1000  # Maximum number of BASE tokens for the presale
JESSE_PER_BASE = 10  # Conversion rate: 1 BASE token equals 10 JESSE tokens

def calculate_conversion(base_tokens):
    """
    Calculate the equivalent JESSE tokens for a given BASE token amount.

    Parameters:
        base_tokens (float): Number of BASE tokens to be converted.

    Returns:
        float: Equivalent JESSE token amount.
    """
    if base_tokens < 0:
        raise ValueError("BASE token amount cannot be negative.")
    if base_tokens > PRESALE_CAP:
        raise ValueError(f"BASE token amount exceeds presale cap of {PRESALE_CAP}.")

    # Conversion calculation
    return base_tokens * JESSE_PER_BASE

def main():
    """
    Main function to demonstrate the conversion rate calculation.
    """
    try:
        # Example Usage: Prompt user for BASE token input
        base_tokens = float(input("Enter the number of BASE tokens: "))
        jesse_tokens = calculate_conversion(base_tokens)
        print(f"{base_tokens} BASE tokens are equivalent to {jesse_tokens} JESSE tokens.")
    except ValueError as e:
        # Handle invalid inputs or amount exceeding the presale cap
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
