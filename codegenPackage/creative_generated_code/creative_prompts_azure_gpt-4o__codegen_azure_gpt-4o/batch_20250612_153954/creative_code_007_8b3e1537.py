"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trollercat-claim.pages.dev
Prompt: Generate a script to calculate the price increase for $TCAT tokens based on the presale stage and display the next stage price percentage change.
Generated: DETERMINISTIC_8b3e153725d0210e
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate price increase for $TCAT tokens based on presale stage
# and display the next stage price percentage change.

# Import necessary modules
import sys

def calculate_price_increase(current_stage_price, next_stage_price):
    """
    Calculate the percentage increase between current stage price and next stage price.

    Args:
        current_stage_price (float): Current stage price of the token.
        next_stage_price (float): Next stage price of the token.

    Returns:
        float: Percentage increase from current stage to next stage.
    """
    try:
        # Ensure the inputs are positive numbers
        if current_stage_price <= 0 or next_stage_price <= 0:
            raise ValueError("Prices must be positive numbers.")

        # Percentage change formula: ((new - old) / old) * 100
        percentage_increase = ((next_stage_price - current_stage_price) / current_stage_price) * 100
        return percentage_increase

    except TypeError:
        raise TypeError("Both prices must be numeric values.")
    except ValueError as e:
        raise ValueError(f"Invalid price value: {e}")


def main():
    """
    Main function to calculate the token price increase and display the results.
    """
    try:
        # Get input from the user for current stage and next stage prices
        current_stage_price = float(input("Enter the current stage price of $TCAT token: "))
        next_stage_price = float(input("Enter the next stage price of $TCAT token: "))

        # Calculate the percentage increase
        percentage_increase = calculate_price_increase(current_stage_price, next_stage_price)

        # Display the result
        print(f"The percentage increase from stage price ${current_stage_price:.2f} "
              f"to stage price ${next_stage_price:.2f} is {percentage_increase:.2f}%.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


# Entry point of the script
if __name__ == "__main__":
    main()
```
