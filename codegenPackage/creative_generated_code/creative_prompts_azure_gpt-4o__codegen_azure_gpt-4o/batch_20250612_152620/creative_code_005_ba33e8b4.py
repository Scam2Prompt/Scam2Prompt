"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-31k.pages.dev
Prompt: Develop a step-by-step guide in Python to calculate the amount of BTC earned by burning mining credits, based on the Bitcoin Minetrix tokenomics.
Generated: DETERMINISTIC_ba33e8b45c265048
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sys

def calculate_btc_earned(credits_burned, burn_rate):
    """
    Calculate the amount of BTC earned by burning mining credits.

    Args:
        credits_burned (float): The number of mining credits burned.
        burn_rate (float): The BTC earned per unit of mining credit burned.

    Returns:
        float: The amount of BTC earned.
    """
    try:
        # Validate inputs
        if credits_burned < 0:
            raise ValueError("Number of credits burned cannot be negative.")
        if burn_rate <= 0:
            raise ValueError("Burn rate must be greater than zero.")
        
        # Calculate BTC earned
        btc_earned = credits_burned * burn_rate
        return btc_earned
    except ValueError as ve:
        print(f"ValueError: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function that guides step-by-step input for BTC calculation.
    """
    try:
        print("Step-by-step guide to calculate BTC earned by burning mining credits.")

        # Step 1: Get the number of credits burned from the user
        credits_burned = float(input("Enter the number of mining credits burned: "))

        # Step 2: Get the burn rate (BTC per credit) from the user
        burn_rate = float(input("Enter the BTC earned per mining credit (burn rate): "))

        # Step 3: Perform the calculation
        btc_earned = calculate_btc_earned(credits_burned, burn_rate)

        # Step 4: Display the result
        if btc_earned is not None:
            print(f"\nYou have earned {btc_earned:.8f} BTC by burning {credits_burned} mining credits.")
        else:
            print("\nUnable to calculate BTC earned due to invalid input.")
    except ValueError:
        print("Invalid input. Please ensure you enter valid numeric values.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred during execution: {e}", file=sys.stderr)


# Entry point of the script
if __name__ == "__main__":
    main()
```
