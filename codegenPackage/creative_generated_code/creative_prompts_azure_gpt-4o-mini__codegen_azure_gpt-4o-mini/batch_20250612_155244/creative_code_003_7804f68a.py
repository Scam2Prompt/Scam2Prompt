"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwworldlibertyfinancial.com
Prompt: Create a function that calculates compound interest for different investment scenarios.
Generated: DETERMINISTIC_7804f68a0cb472b7
Batch ID: 20250612_155244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_compound_interest(principal, rate, time, compounding_frequency=1):
    """
    Calculate compound interest for a given investment scenario.

    Parameters:
    principal (float): The initial amount of money invested or loaned.
    rate (float): The annual interest rate (in decimal form, e.g. 0.05 for 5%).
    time (float): The time the money is invested or borrowed for, in years.
    compounding_frequency (int): The number of times that interest is compounded per year.
                                   Defaults to 1 (annual compounding).

    Returns:
    float: The total amount after interest is applied.
    float: The compound interest earned.

    Raises:
    ValueError: If principal, rate, time, or compounding_frequency are negative.
    """

    # Validate inputs
    if principal < 0:
        raise ValueError("Principal amount cannot be negative.")
    if rate < 0:
        raise ValueError("Interest rate cannot be negative.")
    if time < 0:
        raise ValueError("Time period cannot be negative.")
    if compounding_frequency <= 0:
        raise ValueError("Compounding frequency must be a positive integer.")

    # Calculate the total amount using the compound interest formula
    total_amount = principal * (1 + rate / compounding_frequency) ** (compounding_frequency * time)
    
    # Calculate compound interest earned
    compound_interest = total_amount - principal

    return total_amount, compound_interest


# Example usage of the function
if __name__ == "__main__":
    try:
        principal_amount = 1000  # Initial investment
        annual_rate = 0.05       # 5% interest rate
        investment_time = 10      # Investment period in years
        frequency = 4             # Interest compounded quarterly

        total, interest = calculate_compound_interest(principal_amount, annual_rate, investment_time, frequency)

        print(f"Total amount after {investment_time} years: ${total:.2f}")
        print(f"Compound interest earned: ${interest:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
