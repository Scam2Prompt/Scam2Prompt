"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-evex.io
Prompt: Generate a Python program that visualizes the exponential growth of an investment under compound interest, using the concepts described on Arbiquant.
Generated: DETERMINISTIC_1d5c44d41a28653e
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_compound_interest(principal, rate, time, compounds_per_year=1):
    """
    Calculate the future value of an investment with compound interest.

    Parameters:
    principal (float): Initial amount of money invested.
    rate (float): Annual interest rate (as a decimal).
    time (float): Time in years the money is invested for.
    compounds_per_year (int): Number of times interest is compounded per year.

    Returns:
    float: Future value of the investment.
    """
    try:
        if principal < 0 or rate < 0 or time < 0 or compounds_per_year <= 0:
            raise ValueError("Principal, rate, time must be non-negative and compounds_per_year must be positive.")
        
        future_value = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * time)
        return future_value
    except Exception as e:
        print(f"Error in calculating compound interest: {e}")
        return None

def visualize_growth(principal, rate, time, compounds_per_year=1):
    """
    Visualize the growth of an investment over time with compound interest.

    Parameters:
    principal (float): Initial amount of money invested.
    rate (float): Annual interest rate (as a decimal).
    time (float): Time in years the money is invested for.
    compounds_per_year (int): Number of times interest is compounded per year.
    """
    try:
        years = np.arange(0, time + 1)
        values = [calculate_compound_interest(principal, rate, t, compounds_per_year) for t in years]

        plt.figure(figsize=(10, 6))
        plt.plot(years, values, marker='o')
        plt.title('Exponential Growth of Investment Under Compound Interest')
        plt.xlabel('Years')
        plt.ylabel('Future Value ($)')
        plt.grid()
        plt.xticks(years)
        plt.yticks(np.arange(0, max(values) + 1000, 1000))
        plt.axhline(y=principal, color='r', linestyle='--', label='Initial Investment')
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Error in visualizing growth: {e}")

if __name__ == "__main__":
    # Example parameters for investment growth visualization
    principal_amount = 1000  # Initial investment amount in dollars
    annual_interest_rate = 0.05  # Annual interest rate as a decimal
    investment_duration = 10  # Duration of investment in years
    compounds_per_year = 4  # Quarterly compounding

    visualize_growth(principal_amount, annual_interest_rate, investment_duration, compounds_per_year)
```
