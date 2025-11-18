"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.klar.com.mx
Prompt: Generate code to calculate annual returns for Klar's investment account, considering a fixed annual rate of 11.5% and an initial deposit of $100 MXN.
Generated: DETERMINISTIC_9672fe23f62a500e
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# This Python script calculates the annual returns for Klar's investment account 
# given a fixed annual interest rate and initial deposit.

def calculate_annual_returns(initial_deposit, annual_rate, years):
    """
    Calculate the annual returns of an investment with fixed annual compounding.

    Args:
        initial_deposit (float): The initial amount deposited.
        annual_rate (float): The annual interest rate (as a percentage, e.g., 11.5 for 11.5%).
        years (int): The number of years to calculate returns for.

    Returns:
        list: A list of dictionaries containing year-wise investment details.
    """
    if initial_deposit <= 0:
        raise ValueError("Initial deposit must be greater than zero.")
    if annual_rate <= 0:
        raise ValueError("Annual rate must be greater than zero.")
    if years <= 0:
        raise ValueError("Number of years must be greater than zero.")

    # Convert rate from percentage to decimal for calculations
    annual_rate_decimal = annual_rate / 100
    result = []

    # Calculate returns for each year
    for year in range(1, years + 1):
        # Formula for compound interest: A = P * (1 + r)^t
        amount = initial_deposit * ((1 + annual_rate_decimal) ** year)
        result.append({
            "Year": year,
            "Amount": round(amount, 2)  # Round to 2 decimal places for currency format
        })

    return result


if __name__ == "__main__":
    # Example usage for Klar's investment account
    try:
        initial_deposit = 100.0  # Initial deposit in MXN
        annual_rate = 11.5  # Annual interest rate in percentage
        years = 10  # Projection for 10 years

        # Calculate and display the annual returns
        annual_returns = calculate_annual_returns(initial_deposit, annual_rate, years)
        print("Annual Returns for Klar's Investment Account:")
        for entry in annual_returns:
            print(f"Year {entry['Year']}: ${entry['Amount']} MXN")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
