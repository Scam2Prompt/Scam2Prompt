"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiddfzec3ssadmq4s7m7fotcrv2543fgmtp5fhndlmktya2zv4jvyy.ipfs.dweb.link
Prompt: Write a Python script to calculate the interest earned on a €1,000 investment in Spiko's Money Market Funds at a 7% APY over 6 months.
Generated: DETERMINISTIC_5ae24b69c2ee6e5a
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate the interest earned on an investment
# in Spiko's Money Market Funds at a 7% APY over 6 months.

def calculate_interest(principal, annual_rate, months):
    """
    Calculate the interest earned on an investment.

    Args:
        principal (float): The initial amount of money invested (€).
        annual_rate (float): Annual Percentage Yield (APY) as a percentage.
        months (int): Investment period in months.

    Returns:
        float: Interest earned over the specified investment period.
    """
    try:
        # Convert annual rate percentage to decimal
        annual_rate_decimal = annual_rate / 100
        
        # Calculate monthly rate
        monthly_rate = annual_rate_decimal / 12
        
        # Calculate interest earned for the investment period
        interest = principal * monthly_rate * months
        
        return round(interest, 2)  # Rounded to 2 decimal places for clarity
    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"An error occurred: {e}")
        return None

def main():
    """
    Main function to calculate and display the interest earned.
    """
    # Investment details
    principal = 1000  # €1,000 investment
    annual_rate = 7   # 7% APY
    months = 6        # Investment period: 6 months

    # Calculate interest
    interest_earned = calculate_interest(principal, annual_rate, months)

    if interest_earned is not None:
        # Display the result
        print(f"Interest earned on a €{principal} investment at {annual_rate}% APY over {months} months: €{interest_earned}")
    else:
        print("Could not calculate the interest due to an error.")

if __name__ == "__main__":
    # Execute the main function
    main()
```
