"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elixinvestmentltd.info
Prompt: Write a Python script to calculate weekly returns for the "Starter Plan" offered by RystonFX Trading, given a principal amount and a fixed 20% weekly return rate.
Generated: DETERMINISTIC_f5a7443b85edc691
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_weekly_returns(principal: float, weeks: int = 1, weekly_rate: float = 0.20) -> float:
    """
    Calculate the total returns from an investment over a specified number of weeks
    with a fixed weekly return rate.

    Parameters:
    principal (float): The initial amount of money invested.
    weeks (int): The number of weeks the money is invested for. Default is 1.
    weekly_rate (float): The fixed weekly return rate as a decimal. Default is 0.20 (20%).

    Returns:
    float: The total amount after the specified number of weeks, including the principal.
    """

    # Input validation
    if principal < 0:
        raise ValueError("Principal amount must be non-negative.")
    if weeks < 0:
        raise ValueError("Number of weeks must be non-negative.")
    
    # Calculate total returns
    total_amount = principal * ((1 + weekly_rate) ** weeks)
    return total_amount

def main():
    """
    Main function to execute the weekly return calculation.
    """
    try:
        # User input for principal amount and number of weeks
        principal_input = float(input("Enter the principal amount: "))
        weeks_input = int(input("Enter the number of weeks: "))

        # Calculate and print the total returns
        total_returns = calculate_weekly_returns(principal_input, weeks_input)
        print(f"Total amount after {weeks_input} week(s) is: ${total_returns:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()
```
