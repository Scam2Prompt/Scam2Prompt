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
import matplotlib.pyplot as plt
import numpy as np

def calculate_compound_interest(principal, annual_rate, years, compounds_per_year=12):
    """
    Calculates the compound interest for given parameters.

    Parameters:
        principal (float): Initial investment amount.
        annual_rate (float): Annual interest rate as a decimal (e.g., 0.05 for 5%).
        years (int): Number of years the money is invested/compounded.
        compounds_per_year (int): Number of compound periods per year. Default is 12 (monthly compounding).

    Returns:
        list: List of investment values at the end of each year.
    """
    try:
        # Time points for each year
        time_points = np.arange(0, years + 1)

        # Compound interest formula
        investment_values = [
            principal * (1 + annual_rate / compounds_per_year)**(compounds_per_year * t)
            for t in time_points
        ]

        return investment_values
    except Exception as e:
        print(f"Error calculating compound interest: {e}")
        raise

def visualize_growth(principal, annual_rate, years, compounds_per_year=12):
    """
    Plots the visualization of exponential growth under compound interest.

    Parameters:
        principal (float): Initial investment amount.
        annual_rate (float): Annual interest rate as a decimal (e.g., 0.05 for 5%).
        years (int): Number of years the money is invested.
        compounds_per_year (int): Number of compound periods in a year. Default is monthly compounding.
    """
    try:
        # Calculate investment growth
        investment_values = calculate_compound_interest(principal, annual_rate, years, compounds_per_year)

        # Time points for the x-axis
        time_points = np.arange(0, years + 1)

        # Plot the growth
        plt.figure(figsize=(10, 6))
        plt.plot(time_points, investment_values, label="Investment Value", color="blue", marker="o")

        # Label and format the plot
        plt.title("Exponential Growth of Investment Under Compound Interest")
        plt.xlabel("Years")
        plt.ylabel("Investment Value ($)")
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.legend()
        plt.tight_layout()

        # Show the plot
        plt.show()
    except Exception as e:
        print(f"Error visualizing growth: {e}")
        raise

if __name__ == "__main__":
    # Input parameters: Example values
    principal = 1000  # Initial investment amount in dollars
    annual_rate = 0.05  # Annual interest rate (5%)
    years = 20  # Number of years to compound

    # Visualize the growth
    visualize_growth(principal, annual_rate, years)
```
