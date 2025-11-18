"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimhenlo.com
Prompt: Write code to calculate the difference between Henlo Crew points and the amount of $oHENLO received, as explained in the FAQ section of the HENLO Airdrop page.
Generated: DETERMINISTIC_9d75317d2fce69f0
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: henlo_points_difference.py
# Description: This script calculates the difference between Henlo Crew points and the amount of $oHENLO received.

# Import necessary libraries
import sys

def calculate_difference(henlo_points, ohenlo_received):
    """
    Calculate the difference between Henlo Crew points and $oHENLO received.

    Parameters:
        henlo_points (float): Total points earned in Henlo Crew.
        ohenlo_received (float): Amount of $oHENLO tokens received.

    Returns:
        float: The difference between Henlo Crew points and $oHENLO.
    """
    try:
        # Ensure inputs are valid numbers
        henlo_points = float(henlo_points)
        ohenlo_received = float(ohenlo_received)
    except ValueError:
        raise ValueError("Both Henlo Crew points and $oHENLO received must be numbers.")

    # Calculate the difference
    difference = henlo_points - ohenlo_received

    return difference

if __name__ == "__main__":
    # Command-line interface for user input
    try:
        # Take input from the user
        henlo_points = input("Enter Henlo Crew points: ")
        ohenlo_received = input("Enter $oHENLO received: ")

        # Calculate the difference
        difference = calculate_difference(henlo_points, ohenlo_received)

        # Display the result
        print(f"The difference between Henlo Crew points and $oHENLO received is: {difference:.2f}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
```
