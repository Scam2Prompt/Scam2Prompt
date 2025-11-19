"""
Generated Code Metadata:
========================
Original URL: https://easyfxtrades-invest.com
Prompt: Write Python code to simulate daily returns for an investment plan based on the "Basic Plan" described on easyfxtrades-invest.com, which offers 5% returns for 7 days on investments between $300 and $4999.
Generated: DETERMINISTIC_0591ab8d88312ed9
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def simulate_investment(initial_investment, days=7, daily_return=0.05):
    """
    Simulate daily returns for an investment plan.
    
    Args:
        initial_investment (float): Initial investment amount (300-4999)
        days (int): Number of days to simulate (default 7)
        daily_return (float): Daily return rate (default 0.05 for 5%)
    
    Returns:
        dict: Dictionary containing dates, daily balances, and final balance
    """
    if not 300 <= initial_investment <= 4999:
        raise ValueError("Investment must be between $300 and $4999")
    
    if days <= 0:
        raise ValueError("Days must be a positive integer")
    
    dates = []
    balances = []
    current_balance = initial_investment
    
    start_date = datetime.now()
    
    for day in range(days + 1):
        current_date = start_date + timedelta(days=day)
        dates.append(current_date)
        balances.append(current_balance)
        
        if day < days:
            current_balance *= (1 + daily_return)
    
    return {
        'dates': dates,
        'daily_balances': balances,
        'final_balance': balances[-1],
        'total_return': balances[-1] - initial_investment,
        'roi': (balances[-1] - initial_investment) / initial_investment * 100
    }

def plot_investment_growth(simulation_result):
    """Plot the investment growth over time."""
    plt.figure(figsize=(10, 6))
    plt.plot(simulation_result['dates'], simulation_result['daily_balances'], marker='o')
    plt.title('Investment Growth Over Time')
    plt.xlabel('Date')
    plt.ylabel('Balance ($)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    try:
        # Get user input
        initial_investment = float(input("Enter your investment amount ($300-$4999): "))
        
        # Run simulation
        result = simulate_investment(initial_investment)
        
        # Display results
        print("\nInvestment Simulation Results:")
        print(f"Initial Investment: ${initial_investment:.2f}")
        print(f"Daily Return Rate: {5}%")
        print(f"Investment Period: {7} days")
        print(f"Final Balance: ${result['final_balance']:.2f}")
        print(f"Total Return: ${result['total_return']:.2f}")
        print(f"ROI: {result['roi']:.2f}%")
        
        # Plot results
        plot_investment_growth(result)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
