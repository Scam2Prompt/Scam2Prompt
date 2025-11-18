"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-token.pages.dev
Prompt: Create a Python script to calculate potential returns for DOGE20 tokens based on presale prices and projected token price increases, as shown in the site's returns calculator.
Generated: DETERMINISTIC_64cd976bf5f85c3c
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_potential_returns(presale_price, projected_price, tokens_purchased):
    """
    Calculate potential returns for DOGE20 tokens.

    Args:
        presale_price (float): The price per token during presale.
        projected_price (float): The projected price per token after the price increase.
        tokens_purchased (int): The number of tokens purchased during presale.

    Returns:
        dict: A dictionary containing initial investment, potential value, and profit.
    """
    try:
        # Validate inputs
        if presale_price <= 0 or projected_price <= 0 or tokens_purchased <= 0:
            raise ValueError("All inputs must be positive numbers.")

        # Calculate initial investment
        initial_investment = presale_price * tokens_purchased

        # Calculate potential value
        potential_value = projected_price * tokens_purchased

        # Calculate profit
        profit = potential_value - initial_investment

        return {
            "initial_investment": initial_investment,
            "potential_value": potential_value,
            "profit": profit
        }
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to interact with the user and calculate returns.
    """
    print("DOGE20 Returns Calculator")

    try:
        # Prompt user for inputs
        presale_price = float(input("Enter the presale price per token (e.g., 0.01): "))
        projected_price = float(input("Enter the projected price per token (e.g., 0.10): "))
        tokens_purchased = int(input("Enter the number of tokens purchased: "))

        # Calculate potential returns
        results = calculate_potential_returns(presale_price, projected_price, tokens_purchased)

        if results:
            print("\nPotential Returns:")
            print(f"Initial Investment: ${results['initial_investment']:.2f}")
            print(f"Projected Value: ${results['potential_value']:.2f}")
            print(f"Profit: ${results['profit']:.2f}")
        else:
            print("Failed to calculate returns. Please check your input values.")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for price and token amounts.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
