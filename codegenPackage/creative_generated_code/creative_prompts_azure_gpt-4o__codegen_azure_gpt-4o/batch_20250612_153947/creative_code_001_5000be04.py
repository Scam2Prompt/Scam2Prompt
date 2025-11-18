"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tunfush-airdrop.pages.dev
Prompt: Generate code to calculate and display the bonding curve progress for the Tanfush (Tan) token, which starts at 1% and graduates to Raydium at a $76,869 market cap.
Generated: DETERMINISTIC_5000be040092932a
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# bonding_curve_calculator.py
# Script to calculate and display the bonding curve progress for the Tanfush (Tan) token.

def calculate_bonding_curve_progress(current_market_cap, start_percent=1, goal_market_cap=76869):
    """
    Calculate the bonding curve progress percentage for Tan token.

    Args:
        current_market_cap (float): The current market capitalization of the token.
        start_percent (float): The starting bonding percentage (default is 1%).
        goal_market_cap (float): The target market capitalization for full bonding (default is $76,869).

    Returns:
        float: The bonding curve progress percentage.
    """
    if current_market_cap < 0:
        raise ValueError("Market cap cannot be negative.")
    if current_market_cap > goal_market_cap:
        return 100.0  # cap at 100% progress
    progress = ((current_market_cap / goal_market_cap) * (100 - start_percent)) + start_percent
    return progress


def display_bonding_curve_progress(current_market_cap):
    """
    Display the bonding curve progress for Tan token.

    Args:
        current_market_cap (float): The current market capitalization of the token.
    """
    try:
        progress = calculate_bonding_curve_progress(current_market_cap)
        print(f"Current Market Cap: ${current_market_cap:,.2f}")
        print(f"Bonding Curve Progress: {progress:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Example usage: Replace this with actual market cap values in production.
    try:
        current_market_cap = float(input("Enter the current market cap of the Tan token ($): "))
        display_bonding_curve_progress(current_market_cap)
    except ValueError:
        print("Invalid input. Please enter a valid numerical value for the market cap.")
```
