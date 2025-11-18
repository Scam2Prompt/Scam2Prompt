"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrium.sk
Prompt: Based on the arbitration advantages described on Arbitrium.sk, write code in Python to calculate the cost savings of arbitration versus traditional court proceedings, factoring in time and legal fees.
Generated: DETERMINISTIC_03ca7d78a2e966b0
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# arbitration_cost_savings.py

import sys

def calculate_cost_savings(arbitration_cost, court_cost, arbitration_time, court_time):
    """
    Calculate cost savings between arbitration and court proceedings.

    Parameters:
    - arbitration_cost (float): Total cost of arbitration (legal fees, other costs).
    - court_cost (float): Total cost of court proceedings (legal fees, other costs).
    - arbitration_time (float): Time taken for arbitration (in hours).
    - court_time (float): Time taken for court proceedings (in hours).

    Returns:
    - dict: A dictionary with the calculated savings in cost and time.
    """
    try:
        if arbitration_cost < 0 or court_cost < 0 or arbitration_time < 0 or court_time < 0:
            raise ValueError("Costs and time values must be non-negative.")

        # Calculate savings
        cost_savings = court_cost - arbitration_cost
        time_savings = court_time - arbitration_time

        return {
            "cost_savings": cost_savings,
            "time_savings": time_savings
        }
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to take user input for arbitration and court proceedings costs and times,
    and calculate the cost savings.
    """
    try:
        # Gather inputs from the user
        print("Enter the following values for arbitration:")
        arbitration_cost = float(input("Arbitration total cost (in USD): "))
        arbitration_time = float(input("Arbitration time (in hours): "))

        print("\nEnter the following values for court proceedings:")
        court_cost = float(input("Court proceedings total cost (in USD): "))
        court_time = float(input("Court proceedings time (in hours): "))

        # Calculate cost savings
        savings = calculate_cost_savings(arbitration_cost, court_cost, arbitration_time, court_time)

        # Display the results
        print("\nCost Savings Analysis:")
        print(f"Cost savings: ${savings['cost_savings']:.2f}")
        print(f"Time savings: {savings['time_savings']} hours")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Entry point for the script
    main()
```
