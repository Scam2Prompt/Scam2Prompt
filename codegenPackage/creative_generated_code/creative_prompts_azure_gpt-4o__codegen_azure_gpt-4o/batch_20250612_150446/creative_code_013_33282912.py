"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitalwealthtraders.com
Prompt: Develop a tool to calculate the profitability of different investment plans based on fixed hourly interest rates and durations, as outlined on Digitalwealthtraders.
Generated: DETERMINISTIC_33282912a2481d13
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_profit(principal, hourly_rate, duration_hours):
    """
    Calculate the profit of an investment plan.
    
    :param principal: Initial investment amount (float)
    :param hourly_rate: Hourly interest rate as a percentage (float)
    :param duration_hours: Duration of the investment in hours (int)
    :return: Total profit (float)
    """
    try:
        # Validate inputs
        if principal <= 0:
            raise ValueError("Principal amount must be greater than 0.")
        if hourly_rate <= 0:
            raise ValueError("Hourly interest rate must be greater than 0.")
        if duration_hours <= 0:
            raise ValueError("Duration in hours must be greater than 0.")
        
        # Calculate profit
        total_profit = principal * (hourly_rate / 100) * duration_hours
        return total_profit
    except ValueError as e:
        print(f"Input error: {e}")
        sys.exit(1)

def main():
    """
    Main function to execute the investment profitability calculator.
    """
    print("Welcome to the Investment Profitability Calculator!")
    
    try:
        # Gather user inputs
        principal = float(input("Enter the principal amount (e.g., 1000.00): "))
        hourly_rate = float(input("Enter the hourly interest rate (in %, e.g., 1.5): "))
        duration_hours = int(input("Enter the duration in hours (e.g., 24): "))
        
        # Calculate and display the profit
        profit = calculate_profit(principal, hourly_rate, duration_hours)
        print(f"\nInvestment Details:")
        print(f"Principal: ${principal:.2f}")
        print(f"Hourly Interest Rate: {hourly_rate}%")
        print(f"Duration: {duration_hours} hours")
        print(f"Total Profit: ${profit:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values where applicable.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation canceled by the user.")
        sys.exit(1)

if __name__ == "__main__":
    # Entry point of the script
    main()
```
