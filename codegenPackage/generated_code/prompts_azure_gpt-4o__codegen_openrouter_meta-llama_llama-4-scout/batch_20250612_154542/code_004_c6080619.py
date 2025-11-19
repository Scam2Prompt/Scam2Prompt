"""
Generated Code Metadata:
========================
Original URL: https://mcoinners.com
Prompt: Create a Python script to simulate the hourly or daily growth of capital in a cryptocurrency account, as described in the "WATCH YOUR CAPITAL GROW" section of mcoinners.com.
Generated: DETERMINISTIC_c60806194057eb79
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import argparse
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_growth(principal, rate, time, compound_frequency):
    """
    Calculate the future value of an investment using compound interest formula.

    Args:
    - principal (float): Initial investment amount
    - rate (float): Growth rate per period (in decimal)
    - time (int): Number of periods
    - compound_frequency (int): Number of times interest is compounded per period

    Returns:
    - float: Future value of the investment
    """
    return principal * (1 + rate / compound_frequency) ** (compound_frequency * time)

def simulate_growth(principal, rate, time, compound_frequency, verbose=False):
    """
    Simulate the growth of capital over time.

    Args:
    - principal (float): Initial investment amount
    - rate (float): Growth rate per period (in decimal)
    - time (int): Number of periods
    - compound_frequency (int): Number of times interest is compounded per period
    - verbose (bool): Print detailed simulation output

    Returns:
    - list: List of tuples containing period, balance, and growth rate
    """
    growth_simulation = []
    balance = principal

    for period in range(1, time + 1):
        previous_balance = balance
        balance = calculate_growth(principal, rate, period, compound_frequency)
        growth_rate = (balance - previous_balance) / previous_balance * 100 if period > 1 else 0

        growth_simulation.append((period, balance, growth_rate))

        if verbose:
            logging.info(f"Period {period}: Balance = {balance:.2f}, Growth Rate = {growth_rate:.2f}%")

    return growth_simulation

def main():
    parser = argparse.ArgumentParser(description="Simulate cryptocurrency capital growth")
    parser.add_argument("-p", "--principal", type=float, required=True, help="Initial investment amount")
    parser.add_argument("-r", "--rate", type=float, required=True, help="Hourly or daily growth rate (in percent)")
    parser.add_argument("-t", "--time", type=int, required=True, help="Number of hours or days to simulate")
    parser.add_argument("-f", "--frequency", type=str, choices=["hourly", "daily"], default="daily", help="Compound frequency")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print detailed simulation output")

    args = parser.parse_args()

    rate = args.rate / 100  # Convert rate from percent to decimal
    compound_frequency = 1  # Default compound frequency is 1 (daily or hourly)

    if args.frequency == "hourly":
        compound_frequency = 1
    elif args.frequency == "daily":
        compound_frequency = 1

    try:
        growth_simulation = simulate_growth(args.principal, rate, args.time, compound_frequency, args.verbose)

        logging.info("Growth Simulation Results:")
        for period, balance, growth_rate in growth_simulation:
            logging.info(f"Period {period}: Balance = {balance:.2f}, Growth Rate = {growth_rate:.2f}%")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
