"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://houdiniswapstaking.pages.dev
Prompt: Generate code to calculate the annual percentage yield (APY) for the Houdini Swap staking pool based on the provided +31% APY value.
Generated: DETERMINISTIC_06665eadcc2426c7
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate the Annual Percentage Yield (APY)
# based on a provided rate for the Houdini Swap staking pool (+31% APY)

def calculate_apy(principal, rate, compounding_frequency, time_in_years=1):
    """
    Calculate the Annual Percentage Yield (APY) using the formula:
    APY = (1 + r/n)^(n*t) - 1
    
    Args:
        principal (float): The initial amount of money invested/staked.
        rate (float): The annual interest rate (in decimal form, e.g., 0.31 for 31%).
        compounding_frequency (int): The number of compounding periods per year.
        time_in_years (float): The time for investment in years (default is 1 year).

    Returns:
        float: The calculated APY value as a decimal.
    """
    try:
        # Ensure valid inputs
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if rate <= 0 or rate > 1:
            raise ValueError("Rate must be greater than zero and less than or equal to 1.")
        if compounding_frequency <= 0:
            raise ValueError("Compounding frequency must be a positive integer.")
        if time_in_years <= 0:
            raise ValueError("Time in years must be greater than zero.")

        # APY formula
        apy = (1 + rate / compounding_frequency) ** (compounding_frequency * time_in_years) - 1
        return apy
    except Exception as e:
        # Handle errors gracefully
        print(f"Error calculating APY: {e}")
        return None

def main():
    """
    Main function to demonstrate the calculation of APY for
    the Houdini Swap staking pool with a +31% annual rate.
    """
    # Parameters
    principal = 1000  # Example principal amount in dollars
    rate = 0.31       # +31% annual rate (converted to decimal)
    compounding_frequency = 12  # Monthly compounding (12 compounding periods per year)
    time_in_years = 1  # Investment duration in years

    # Calculate APY
    apy = calculate_apy(principal, rate, compounding_frequency, time_in_years)

    if apy is not None:
        # Display results
        print(f"Principal: ${principal:,.2f}")
        print(f"Annual Rate: {rate * 100:.2f}%")
        print(f"Compounding Frequency: {compounding_frequency} times per year")
        print(f"APY: {apy * 100:.2f}%")
    else:
        print("Failed to calculate APY.")

# Entry point for the script
if __name__ == "__main__":
    main()
```
