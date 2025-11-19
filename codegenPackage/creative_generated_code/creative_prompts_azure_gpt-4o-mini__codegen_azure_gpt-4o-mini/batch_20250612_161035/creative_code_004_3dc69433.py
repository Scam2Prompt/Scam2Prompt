"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-hypeloot.com
Prompt: Write a script that calculates the potential earnings from staking $HPLT tokens based on the average APY of 322% mentioned in the Hypeloot documentation.
Generated: DETERMINISTIC_3dc6943358bf43d6
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to capture potential issues
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_staking_earnings(principal: float, apy: float, years: float) -> float:
    """
    Calculate the potential earnings from staking tokens based on the principal amount,
    annual percentage yield (APY), and the number of years.

    Parameters:
    principal (float): The initial amount of tokens staked.
    apy (float): The annual percentage yield (as a decimal).
    years (float): The number of years the tokens are staked.

    Returns:
    float: The total amount of tokens after staking period.
    """
    try:
        # Validate inputs
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        if apy < 0:
            raise ValueError("APY must be non-negative.")
        if years < 0:
            raise ValueError("Number of years must be non-negative.")

        # Calculate total amount using the formula for compound interest
        total_amount = principal * ((1 + apy) ** years)
        
        return total_amount

    except ValueError as e:
        logging.error(f"Input Error: {e}")
        return 0.0  # Return 0 if there's an input error

def main():
    # Example parameters for staking calculation
    principal_amount = 1000.0  # Amount in $HPLT tokens
    average_apy = 3.22         # APY as a decimal (322%)
    staking_years = 1          # Number of years to stake

    # Calculate potential earnings
    earnings = calculate_staking_earnings(principal_amount, average_apy, staking_years)

    # Display the results
    logging.info(f"Staking {principal_amount} $HPLT tokens at an average APY of {average_apy * 100}% for {staking_years} year(s) results in: {earnings:.2f} $HPLT tokens.")

if __name__ == "__main__":
    main()
```
