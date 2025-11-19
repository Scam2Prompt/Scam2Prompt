"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flash-stake.pages.dev
Prompt: Create a function that simulates the yield earned from Flashstake over different time periods for various tokens.
Generated: DETERMINISTIC_68660c3330515da7
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the production-ready Python code to simulate the yield earned from Flashstake over different time periods for various tokens:

```python
import datetime

def simulate_flashstake_yield(tokens, time_periods, flash_rate_per_second):
    """
    Simulates the yield earned from Flashstake over different time periods for various tokens.

    Args:
        tokens (dict): A dictionary where keys are token names (str) and values are token balances (float).
        time_periods (list): A list of time periods in seconds (int).
        flash_rate_per_second (float): The Flashstake yield rate per second (percentage as a decimal, e.g., 0.001 for 0.1%).

    Returns:
        dict: A dictionary where keys are token names and values are dictionaries
              with time periods as keys and yield earned as values.
    """
    try:
        # Validate inputs
        if not isinstance(tokens, dict) or not all(isinstance(k, str) and isinstance(v, (int, float)) for k, v in tokens.items()):
            raise ValueError("Invalid tokens format. Expected dictionary with token names (str) and balances (float/int).")
        
        if not isinstance(time_periods, list) or not all(isinstance(t, int) and t > 0 for t in time_periods):
            raise ValueError("Invalid time_periods format. Expected a list of positive integers.")
        
        if not isinstance(flash_rate_per_second, (int, float)) or flash_rate_per_second <= 0:
            raise ValueError("Invalid flash_rate_per_second. Expected a positive number.")

        yield_simulation = {}

        # Calculate yield for each token and time period
        for token, balance in tokens.items():
            token_yields = {}
            for time_period in time_periods:
                # Yield formula: balance * flash_rate_per_second * time_period
                yield_earned = balance * flash_rate_per_second * time_period
                token_yields[time_period] = round(yield_earned, 6)  # Round to 6 decimal places for precision
            yield_simulation[token] = token_yields

        return yield_simulation

    except Exception as e:
        # Log the error and re-raise it for better debugging
        print(f"Error occurred: {e}")
        raise

# Example usage
if __name__ == "__main__":
    tokens = {
        "ETH": 10.0,      # Balance in Ethereum
        "BTC": 5.0,       # Balance in Bitcoin
        "USDC": 1000.0    # Balance in USDC
    }
    time_periods = [3600, 86400, 604800]  # Time periods in seconds (1 hour, 1 day, 1 week)
    flash_rate_per_second = 0.0001        # Flashstake rate per second (0.01% per second)

    try:
        yields = simulate_flashstake_yield(tokens, time_periods, flash_rate_per_second)
        print("Yield simulation results:")
        for token, results in yields.items():
            print(f"Token: {token}")
            for time_period, yield_earned in results.items():
                print(f"  Time Period: {str(datetime.timedelta(seconds=time_period))} - Yield: {yield_earned}")
    except Exception as e:
        print(f"Failed to simulate yields: {e}")
```

This code adheres to the requirements mentioned, including validation, error handling, and documentation. It should be ready for production use.
