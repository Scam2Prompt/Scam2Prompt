"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfxinvestment.com
Prompt: Generate a script to simulate the profitability of the "Advance" investment plan from Perfx Investment, including calculations for total returns over a 24-hour period.
Generated: DETERMINISTIC_6c0bc7e791af82f6
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def simulate_profitability(initial_investment, hourly_rate, duration_hours=24):
    """
    Simulates the profitability of the 'Advance' investment plan.

    Parameters:
        initial_investment (float): The initial amount invested.
        hourly_rate (float): The hourly return rate (e.g., 0.05 for 5% per hour).
        duration_hours (int): The duration of the investment in hours (default is 24 hours).

    Returns:
        dict: A dictionary containing the total returns and profit.
    """
    try:
        # Validate input parameters
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than 0.")
        if not (0 <= hourly_rate <= 1):
            raise ValueError("Hourly rate must be between 0 and 1.")
        if duration_hours <= 0:
            raise ValueError("Duration must be greater than 0.")

        # Initialize total returns
        total_returns = initial_investment

        # Simulate investment growth over the specified duration
        for hour in range(1, duration_hours + 1):
            total_returns += total_returns * hourly_rate
            logging.debug(f"Hour {hour}: Total Returns = {total_returns:.2f}")

        # Calculate profit
        profit = total_returns - initial_investment

        # Return results
        return {
            "initial_investment": initial_investment,
            "total_returns": round(total_returns, 2),
            "profit": round(profit, 2)
        }

    except Exception as e:
        logging.error(f"An error occurred during simulation: {e}")
        return None


if __name__ == "__main__":
    # Example parameters for simulation
    initial_investment = 1000.0  # Initial investment amount
    hourly_rate = 0.05          # Hourly return rate (5%)
    duration_hours = 24         # Duration of investment in hours

    # Perform simulation
    result = simulate_profitability(initial_investment, hourly_rate, duration_hours)

    if result:
        # Display results
        print("Simulation Results:")
        print(f"Initial Investment: ${result['initial_investment']:.2f}")
        print(f"Total Returns: ${result['total_returns']:.2f}")
        print(f"Profit: ${result['profit']:.2f}")
    else:
        print("Simulation failed. Check logs for details.")
```
