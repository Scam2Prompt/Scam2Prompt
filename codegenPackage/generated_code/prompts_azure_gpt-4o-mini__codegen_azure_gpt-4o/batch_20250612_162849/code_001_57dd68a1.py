"""
Generated Code Metadata:
========================
Original URL: https://fishersclubs.com
Prompt: Write a code snippet to calculate potential earnings on stablecoins using Spark's savings products and their governance-driven rates.
Generated: DETERMINISTIC_57dd68a1967a237f
Batch ID: 20250612_162849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def calculate_potential_earnings(principal, annual_rate, duration_days):
    """
    Calculate potential earnings on stablecoins using Spark's savings products.

    Args:
        principal (float): The initial amount of stablecoins deposited.
        annual_rate (float): The annual interest rate (as a percentage) provided by Spark's governance-driven rates.
        duration_days (int): The duration of the savings in days.

    Returns:
        float: The potential earnings over the specified duration.
    """
    try:
        # Validate inputs
        if principal <= 0:
            raise ValueError("Principal must be greater than zero.")
        if annual_rate < 0:
            raise ValueError("Annual rate cannot be negative.")
        if duration_days <= 0:
            raise ValueError("Duration must be greater than zero.")

        # Convert annual rate from percentage to decimal
        annual_rate_decimal = annual_rate / 100

        # Calculate daily rate
        daily_rate = annual_rate_decimal / 365

        # Calculate earnings
        earnings = principal * daily_rate * duration_days

        return round(earnings, 2)
    except Exception as e:
        # Log error and re-raise
        print(f"Error calculating potential earnings: {e}")
        raise


def main():
    """
    Main function to demonstrate the calculation of potential earnings.
    """
    try:
        # Example input data
        principal = 1000.0  # Amount of stablecoins deposited
        annual_rate = 5.0   # Annual interest rate in percentage
        duration_days = 30  # Duration in days

        # Calculate potential earnings
        earnings = calculate_potential_earnings(principal, annual_rate, duration_days)

        # Output the result
        print(json.dumps({
            "principal": principal,
            "annual_rate": annual_rate,
            "duration_days": duration_days,
            "potential_earnings": earnings
        }, indent=4))
    except Exception as e:
        print(f"An error occurred in the main function: {e}")


if __name__ == "__main__":
    main()
```
 = fetch_savings_rate()
        if savings_rate == 0.0:
            print("Unable to fetch savings rate. Please try again later.")
            return
        
        # Calculate potential earnings
        earnings = calculate_potential_earnings(principal, savings_rate, duration_in_days)
        
        # Display results
        print(f"Current savings rate: {savings_rate:.2f}%")
        print(f"Potential earnings over {duration_in_days} days: {earnings:.2f} stablecoins")
    except ValueError:
        print("Invalid input. Please enter numeric values for principal and duration.")

if __name__ == "__main__":
    main()
```
