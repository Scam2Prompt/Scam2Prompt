"""
Generated Code Metadata:
========================
Original URL: https://kinikangg.pages.dev
Prompt: Create a code example for implementing a win rate calculator, like the "Spy Result" feature on AI Waifu, using inventory resources.
Generated: DETERMINISTIC_27753debd325e988
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# win_rate_calculator.py

# Import necessary modules
import sys

def calculate_win_rate(successful_attempts, total_attempts):
    """
    Calculate the win rate percentage based on successful attempts and total attempts.

    Args:
        successful_attempts (int): Number of successful attempts.
        total_attempts (int): Total number of attempts.

    Returns:
        float: Win rate percentage.
    """
    try:
        # Validate inputs
        if total_attempts <= 0:
            raise ValueError("Total attempts must be greater than zero.")
        if successful_attempts < 0 or successful_attempts > total_attempts:
            raise ValueError("Successful attempts must be between 0 and total attempts.")

        # Calculate win rate
        win_rate = (successful_attempts / total_attempts) * 100
        return round(win_rate, 2)
    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None

def main():
    """
    Main function to demonstrate the win rate calculator.
    """
    try:
        # Example inventory resources
        inventory = {
            "successful_attempts": 45,
            "total_attempts": 60
        }

        # Extract values from inventory
        successful_attempts = inventory.get("successful_attempts", 0)
        total_attempts = inventory.get("total_attempts", 0)

        # Calculate win rate
        win_rate = calculate_win_rate(successful_attempts, total_attempts)

        if win_rate is not None:
            print(f"Win Rate: {win_rate}%")
        else:
            print("Failed to calculate win rate due to input errors.")
    except Exception as e:
        print(f"Unexpected Error in main: {e}")
        sys.exit(1)

# Entry point for the script
if __name__ == "__main__":
    main()
```
