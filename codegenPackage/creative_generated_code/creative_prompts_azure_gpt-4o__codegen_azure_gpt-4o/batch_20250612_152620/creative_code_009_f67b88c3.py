"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-en.web.app
Prompt: Generate code for a rewards calculator that takes the amount of DOGE20 purchased and predicts its future value based on token price appreciation scenarios.
Generated: DETERMINISTIC_f67b88c39212fd63
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def rewards_calculator(doge20_purchased, appreciation_rate):
    """
    Calculates the future value of purchased DOGE20 tokens based on an appreciation rate.

    Parameters:
    doge20_purchased (float): The amount of DOGE20 tokens purchased.
    appreciation_rate (float): The predicted appreciation rate (percentage increase as a decimal).

    Returns:
    float: The future value of the DOGE20 tokens.
    """
    try:
        # Validate inputs
        if doge20_purchased <= 0:
            raise ValueError("DOGE20 purchased must be greater than 0.")
        if appreciation_rate < 0:
            raise ValueError("Appreciation rate must not be negative.")

        # Calculate future value
        future_value = doge20_purchased * (1 + appreciation_rate)
        return future_value
    except ValueError as e:
        print(f"Input Error: {e}")
        sys.exit(1)


def main():
    """
    Main function to handle user input and calculate the rewards.
    """
    try:
        # Prompt user for input
        doge20_purchased = float(input("Enter the amount of DOGE20 tokens purchased: "))
        appreciation_rate = float(input("Enter the predicted appreciation rate (as a decimal, e.g., 0.25 for 25%): "))

        # Calculate and display the future value
        future_value = rewards_calculator(doge20_purchased, appreciation_rate)
        print(f"Based on an appreciation rate of {appreciation_rate * 100:.2f}%, "
              f"the future value of your DOGE20 tokens will be: {future_value:.2f}")
    except ValueError:
        print("Invalid input. Please ensure you enter numeric values for both fields.")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
