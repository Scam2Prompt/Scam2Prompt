"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-pump.fun
Prompt: Create code to display dynamic pricing tiers (e.g., 1 SOL, 5 SOL, 10 SOL) for a token pre-sale, similar to the $PUMP pre-sale platform.
Generated: DETERMINISTIC_5a7797f59330bf3e
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sys

def display_pricing_tiers():
    """
    Function to display dynamic pricing tiers for a token pre-sale.
    Pricing tiers will be displayed in a human-readable format.
    """
    try:
        # Define the pricing tiers in SOL
        pricing_tiers = [
            {"tokens": 100, "price_per_token": 1},  # 1 SOL per token
            {"tokens": 500, "price_per_token": 0.95},  # 0.95 SOL per token
            {"tokens": 1000, "price_per_token": 0.90},  # 0.90 SOL per token
        ]

        # Header for display
        print("\nToken Pre-sale Pricing Tiers:")
        print("=" * 40)

        # Iterate over each tier and display details
        for tier in pricing_tiers:
            print(f"{tier['tokens']} Tokens - {tier['price_per_token']} SOL per token")

        print("=" * 40)
        print("Note: Larger purchases benefit from discounted rates.")
    
    except Exception as e:
        # Provide error handling for unexpected issues
        print(f"An error occurred while displaying pricing tiers: {e}", file=sys.stderr)

# Main function to encapsulate script execution
def main():
    """
    Main function to execute the display logic for token pre-sale pricing tiers.
    """
    try:
        # Call the function to display pricing tiers
        display_pricing_tiers()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
```
