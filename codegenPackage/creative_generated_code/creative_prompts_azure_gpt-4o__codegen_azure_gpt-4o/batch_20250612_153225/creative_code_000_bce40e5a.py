"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tsmwealth.co.za
Prompt: Write Python code to calculate long-term investment growth using compound interest, incorporating user-defined parameters for initial investment, annual contribution, interest rate, and time horizon, as described in TSM Wealth's investment services.
Generated: DETERMINISTIC_bce40e5af4a7a7c1
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python program to calculate long-term investment growth using compound interest
# incorporating user-defined parameters for initial investment, annual contribution,
# interest rate, and time horizon.

def calculate_investment_growth(initial_investment, annual_contribution, interest_rate, years):
    """
    Calculate the future value of an investment with annual contributions and compound interest.

    Parameters:
    initial_investment (float): Initial amount invested.
    annual_contribution (float): Amount contributed annually.
    interest_rate (float): Annual interest rate (as a percentage, e.g., 5 for 5%).
    years (int): Number of years the investment will grow.

    Returns:
    float: The total value of the investment after the specified number of years.
    """
    try:
        # Convert interest rate from percentage to decimal
        rate = interest_rate / 100
        
        # Initialize total amount with the initial investment
        total_value = initial_investment
        
        # Calculate growth year by year
        for year in range(1, years + 1):
            # Apply compound interest for the current total value
            total_value *= (1 + rate)
            
            # Add annual contribution to the total value
            total_value += annual_contribution
        
        return total_value
    except Exception as e:
        # Handle potential errors (e.g., invalid inputs)
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    # Prompt user for input values
    try:
        initial_investment = float(input("Enter the initial investment amount: "))
        annual_contribution = float(input("Enter the annual contribution amount: "))
        interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
        years = int(input("Enter the time horizon (number of years): "))
        
        # Validate inputs
        if initial_investment < 0 or annual_contribution < 0 or interest_rate < 0 or years <= 0:
            print("Error: All inputs must be positive and years must be greater than zero.")
        else:
            # Calculate and display the total investment value
            final_value = calculate_investment_growth(initial_investment, annual_contribution, interest_rate, years)
            if final_value is not None:
                print(f"The total value of your investment after {years} years is: ${final_value:,.2f}")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
```
