"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitplusinvestment.com
Prompt: Write a Python script to calculate the ROI for the "Basic Plan" offered by Bitplus Investment, which provides a 10% return on investment after 1 day for amounts between $100 and $1,000. Include input validation for the investment amount.
Generated: DETERMINISTIC_e71285c43b7e4313
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_roi(investment_amount):
    """
    Calculate the return on investment (ROI) for the Basic Plan of Bitplus Investment.

    Args:
        investment_amount (float): The amount of money to invest.

    Returns:
        float: The total amount returned after 1 day, including the original investment.

    Raises:
        ValueError: If the investment amount is not within the allowed range or is not a number.
    """
    # Define the return rate and the valid range for investment
    return_rate = 0.10  # 10% return
    min_investment = 100.0
    max_investment = 1000.0

    # Input validation
    if not isinstance(investment_amount, (int, float)):
        raise ValueError("Investment amount must be a number.")

    if investment_amount < min_investment or investment_amount > max_investment:
        raise ValueError(f"Investment amount must be between ${min_investment} and ${max_investment}.")

    # Calculate the total return
    total_return = investment_amount + (investment_amount * return_rate)
    return total_return


def main():
    """
    Main function to execute the ROI calculation.

    It prompts the user for the investment amount, validates the input,
    calculates the ROI, and prints the result.
    """
    try:
        # Prompt user for investment amount
        investment_input = input("Enter your investment amount for the Basic Plan ($100 - $1000): ")

        # Convert input to float
        investment_amount = float(investment_input)

        # Calculate ROI
        total_return = calculate_roi(investment_amount)

        # Display the result
        print(f"Total return after 1 day: ${total_return:.2f}")

    except ValueError as e:
        # Handle input validation errors
        print(f"Error: {e}")

    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
