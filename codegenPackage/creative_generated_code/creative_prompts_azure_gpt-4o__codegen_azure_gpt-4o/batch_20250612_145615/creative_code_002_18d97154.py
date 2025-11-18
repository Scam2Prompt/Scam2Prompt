"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://l2lusty.site
Prompt: Create a Python script to calculate the expected Adena earnings for a player based on the drop rate (x20) and spoil rate (x20) provided on the L2Lusty server.
Generated: DETERMINISTIC_18d97154a30fd164
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_adena_earnings(drop_rate, spoil_rate, base_drop, base_spoil):
    """
    Calculate the expected Adena earnings for a player.

    Parameters:
    - drop_rate (float): The multiplier for the drop rate (e.g., x20).
    - spoil_rate (float): The multiplier for the spoil rate (e.g., x20).
    - base_drop (int): The base amount of Adena dropped by mobs.
    - base_spoil (int): The base amount of Adena obtained from spoiling mobs.

    Returns:
    - float: The total expected Adena earnings.
    """
    try:
        # Ensure all values are non-negative
        if drop_rate < 0 or spoil_rate < 0 or base_drop < 0 or base_spoil < 0:
            raise ValueError("All input values must be non-negative.")

        # Calculate earnings from drop and spoil separately
        total_from_drops = drop_rate * base_drop
        total_from_spoils = spoil_rate * base_spoil

        # Total expected Adena earnings
        total_earnings = total_from_drops + total_from_spoils
        return total_earnings

    except TypeError:
        raise ValueError("All inputs must be numbers (int or float).")
    except Exception as e:
        raise RuntimeError(f"An error occurred during calculation: {e}")

def main():
    """
    Main function to handle user input and calculate Adena earnings.
    """
    try:
        print("L2Lusty Adena Earnings Calculator")
        
        # Gather input with appropriate validation
        drop_rate = float(input("Enter the drop rate multiplier (e.g., 20 for x20): "))
        spoil_rate = float(input("Enter the spoil rate multiplier (e.g., 20 for x20): "))
        base_drop = int(input("Enter the base Adena dropped per mob: "))
        base_spoil = int(input("Enter the base Adena spoiled per mob: "))

        # Calculate Adena earnings
        total_earnings = calculate_adena_earnings(drop_rate, spoil_rate, base_drop, base_spoil)

        # Display the result
        print(f"\nExpected Adena Earnings: {total_earnings:.2f}")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Entry point for the script
    main()
```
