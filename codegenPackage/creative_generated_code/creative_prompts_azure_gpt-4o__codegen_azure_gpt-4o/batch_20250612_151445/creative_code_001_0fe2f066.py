"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demoablabs.com
Prompt: Write a script to calculate rush charges for environmental testing based on A & B Labs' turnaround time (TAT) policy, including surcharges for 1-day, 2-day, and 3-day testing.
Generated: DETERMINISTIC_0fe2f0665d1adb29
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_rush_charges(base_price, tat_days):
    """
    Calculate rush charges based on turnaround time (TAT) policy.

    Parameters:
        base_price (float): The base price for the environmental test.
        tat_days (int): The requested turnaround time in days (1, 2, or 3).

    Returns:
        float: The total price after applying rush charges.
    """
    # Define rush surcharge rates for 1-day, 2-day, and 3-day TAT
    surcharge_rates = {
        1: 0.50,  # 50% surcharge for 1-day TAT
        2: 0.30,  # 30% surcharge for 2-day TAT
        3: 0.10   # 10% surcharge for 3-day TAT
    }

    # Validate input
    if tat_days not in surcharge_rates:
        raise ValueError("Invalid TAT. Only 1-day, 2-day, or 3-day TAT is allowed.")
    if base_price <= 0:
        raise ValueError("Base price must be a positive value.")

    # Calculate rush charges
    surcharge = base_price * surcharge_rates[tat_days]
    total_price = base_price + surcharge

    return total_price

def main():
    """
    Main function to interact with the user and calculate rush charges.
    """
    print("Welcome to the Environmental Testing Rush Charge Calculator!")
    
    try:
        # Get base price from user
        base_price = float(input("Enter the base price of the test: "))
        
        # Get TAT from user
        tat_days = int(input("Enter the requested turnaround time (1, 2, or 3 days): "))
        
        # Calculate total charges
        total_price = calculate_rush_charges(base_price, tat_days)
        
        # Display the results
        print(f"The total price for a {tat_days}-day turnaround is: ${total_price:.2f}")
    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Rush Charge Calculator.")

if __name__ == "__main__":
    # Entry point for the script
    main()
```
