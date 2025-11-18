"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chainairdrop.org
Prompt: Generate code to calculate the total USDT raised during Stage 1 of the NEX token sale and display the progress toward the $50,000 goal.
Generated: DETERMINISTIC_4407252feae4df6c
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Constants
GOAL_AMOUNT_USDT = 50000  # Goal for Stage 1 in USDT

# Sample data: Assume this is the JSON file containing contributions data
# Each entry represents a contribution with the amount in USDT
contributions_data = '''
[
    {"contributor": "Alice", "amount_usdt": 15000},
    {"contributor": "Bob", "amount_usdt": 20000},
    {"contributor": "Charlie", "amount_usdt": 5000},
    {"contributor": "Diana", "amount_usdt": 7500}
]
'''

def calculate_total_usdt(data):
    """
    Calculate the total USDT raised during Stage 1.

    Parameters:
    - data (list): A list of contributions with amounts in USDT.

    Returns:
    - float: Total USDT raised.
    """
    try:
        # Summing up the USDT contributions from all contributors
        total_usdt = sum(contribution["amount_usdt"] for contribution in data)
        return total_usdt
    except KeyError:
        raise ValueError("Invalid data format: Missing 'amount_usdt' key in some contributions.")
    except TypeError:
        raise ValueError("Invalid data format: 'data' should be a list of dictionaries.")

def display_progress(total_usdt, goal_usdt):
    """
    Display progress toward the goal.

    Parameters:
    - total_usdt (float): Total USDT raised during Stage 1.
    - goal_usdt (float): Goal USDT amount.

    Returns:
    - None
    """
    try:
        print(f"Total USDT Raised: ${total_usdt:,.2f}")
        print(f"Goal: ${goal_usdt:,.2f}")
        progress_percentage = (total_usdt / goal_usdt) * 100
        print(f"Progress: {progress_percentage:.2f}%")
    except ZeroDivisionError:
        print("Goal amount cannot be zero.")
    except Exception as e:
        print(f"An error occurred while displaying progress: {str(e)}")

def main():
    """
    Main function to calculate and display the progress of the NEX token sale Stage 1.

    Returns:
    - None
    """
    try:
        # Load contributions data
        contributions = json.loads(contributions_data)

        # Calculate total USDT raised
        total_usdt_raised = calculate_total_usdt(contributions)

        # Display the progress toward the goal
        display_progress(total_usdt_raised, GOAL_AMOUNT_USDT)
    except json.JSONDecodeError:
        print("Failed to load contributions data: Invalid JSON format.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Entry point
if __name__ == "__main__":
    main()
```
