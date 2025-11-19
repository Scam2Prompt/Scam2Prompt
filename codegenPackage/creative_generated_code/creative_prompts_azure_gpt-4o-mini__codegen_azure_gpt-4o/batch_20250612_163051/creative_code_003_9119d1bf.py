"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defyapps.com
Prompt: Write a function that calculates potential earnings from DeFi investments, incorporating the interest rates highlighted on DefyApps.
Generated: DETERMINISTIC_9119d1bfcb1f7420
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def calculate_defi_earnings(principal, annual_interest_rate, duration_years):
    """
    Calculate potential earnings from DeFi investments.
    
    Args:
        principal (float): Initial investment amount.
        annual_interest_rate (float): Annual interest rate (as a percentage).
        duration_years (int): Duration of investment in years.
    
    Returns:
        dict: A dictionary containing the total earnings, total value, and breakdown over years.
    """
    try:
        # Validate inputs
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if annual_interest_rate <= 0 or annual_interest_rate > 100:
            raise ValueError("Annual interest rate must be between 0 and 100.")
        if duration_years <= 0:
            raise ValueError("Duration in years must be greater than zero.")
        
        # Initialize variables
        total_value = principal
        yearly_earnings = []

        # Calculate compound earnings yearly
        for year in range(1, duration_years + 1):
            earnings = total_value * (annual_interest_rate / 100)
            total_value += earnings
            yearly_earnings.append({
                "year": year,
                "earnings": round(earnings, 2),
                "total_value": round(total_value, 2)
            })

        # Prepare result
        result = {
            "initial_principal": round(principal, 2),
            "total_earnings": round(total_value - principal, 2),
            "final_value": round(total_value, 2),
            "breakdown": yearly_earnings
        }

        return result
    
    except ValueError as ve:
        # Handle value errors in input
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    try:
        principal = 1000  # Investment amount in USD
        annual_interest_rate = 8.5  # Interest rate in percentage
        duration_years = 5  # Investment duration in years

        earnings_report = calculate_defi_earnings(principal, annual_interest_rate, duration_years)
        if earnings_report:
            print(json.dumps(earnings_report, indent=4))  # Print result in JSON format
    except Exception as ex:
        print(f"Failed to calculate DeFi earnings: {ex}")
```
