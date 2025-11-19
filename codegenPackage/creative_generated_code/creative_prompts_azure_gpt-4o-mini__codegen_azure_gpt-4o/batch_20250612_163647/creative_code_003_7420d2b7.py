"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pipelinefinanceconseil.com
Prompt: Develop a script that models the impact of quarterly withdrawals on a savings plan with a variable average rate of 9.24%, reflecting the features of Pipeline Finance Conseil.
Generated: DETERMINISTIC_7420d2b7251b9fb9
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def simulate_savings_plan(initial_balance, quarterly_withdrawal, annual_rate, quarters):
    """
    Simulates the impact of quarterly withdrawals on a savings plan.
    
    Parameters:
        initial_balance (float): Initial savings balance.
        quarterly_withdrawal (float): Amount withdrawn at the end of each quarter.
        annual_rate (float): Average annual interest rate (as a percentage).
        quarters (int): Total number of quarters to simulate.
    
    Returns:
        dict: A dictionary containing the savings balance per quarter and total interest earned.
    """
    # Validate input parameters
    if initial_balance < 0:
        raise ValueError("Initial balance must be non-negative.")
    if quarterly_withdrawal < 0:
        raise ValueError("Quarterly withdrawal must be non-negative.")
    if annual_rate < 0:
        raise ValueError("Annual rate must be non-negative.")
    if quarters < 0:
        raise ValueError("Number of quarters must be non-negative.")

    # Convert the annual rate to quarterly rate (dividing by 4)
    quarterly_rate = annual_rate / 4 / 100  # Convert percentage to decimal

    # Initialize variables
    balance = initial_balance
    total_interest_earned = 0
    quarterly_balances = []

    # Simulate savings plan
    for quarter in range(1, quarters + 1):
        # Calculate interest for the quarter
        interest = balance * quarterly_rate
        
        # Update total interest earned
        total_interest_earned += interest
        
        # Apply interest to balance
        balance += interest

        # Process quarterly withdrawal
        if balance >= quarterly_withdrawal:
            balance -= quarterly_withdrawal
        else:
            # If withdrawal exceeds current balance, set balance to zero
            balance = 0

        # Record the balance at the end of the quarter
        quarterly_balances.append({
            'Quarter': quarter,
            'Balance': round(balance, 2),
            'Interest Earned': round(interest, 2),
        })

    return {
        'Quarterly Balances': quarterly_balances,
        'Total Interest Earned': round(total_interest_earned, 2),
    }

# Example usage
if __name__ == "__main__":
    try:
        # Model a savings plan with the following parameters
        initial_balance = 10000  # Starting with $10,000
        quarterly_withdrawal = 500  # $500 withdrawn every quarter
        annual_rate = 9.24  # Average annual interest rate of 9.24%
        quarters = 12  # Simulate for 12 quarters (3 years)

        result = simulate_savings_plan(initial_balance, quarterly_withdrawal, annual_rate, quarters)
        
        # Display the results
        print("Savings Plan Simulation:")
        for entry in result['Quarterly Balances']:
            print(f"Quarter {entry['Quarter']}: Balance = ${entry['Balance']}, Interest Earned = ${entry['Interest Earned']}")
        print(f"\nTotal Interest Earned: ${result['Total Interest Earned']}")
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
