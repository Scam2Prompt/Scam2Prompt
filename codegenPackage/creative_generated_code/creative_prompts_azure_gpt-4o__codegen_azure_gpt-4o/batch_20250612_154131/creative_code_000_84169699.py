"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkventure.net
Prompt: Write Python code to calculate the quarterly redemption amount for an investor in the ARK Venture Fund, given their total investment and the fund's 5% liquidity policy.
Generated: DETERMINISTIC_84169699605cdb2e
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate the quarterly redemption amount for an investor
# in the ARK Venture Fund based on a 5% liquidity policy.

# Import required modules
def calculate_quarterly_redemption(total_investment):
    """
    Calculate the quarterly redemption amount for an investor based on the fund's liquidity policy.

    Parameters:
        total_investment (float): The total investment amount by the investor in USD.

    Returns:
        float: Quarterly redemption amount as per the fund's 5% liquidity policy.
    """
    try:
        # Validate input
        if total_investment < 0:
            raise ValueError("Total investment must be a non-negative number.")

        # ARK Venture Fund's liquidity policy: 5% of the total investment per quarter
        liquidity_percentage = 0.05  # 5% expressed as a decimal

        # Calculate quarterly redemption amount
        quarterly_redemption = total_investment * liquidity_percentage

        return quarterly_redemption

    except TypeError:
        raise TypeError("Total investment must be a numeric value.")
    except ValueError as ve:
        raise ve


# Example usage:
if __name__ == "__main__":
    try:
        # Prompt the user to input their total investment amount
        total_investment = float(input("Enter your total investment amount in USD: "))

        # Calculate and display the quarterly redemption amount
        redemption_amount = calculate_quarterly_redemption(total_investment)
        print(f"Your quarterly redemption amount is: ${redemption_amount:.2f}")

    except ValueError:
        print("Invalid input. Please enter a valid numeric investment amount.")
```
tion as e:
        print(f"An unexpected error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
