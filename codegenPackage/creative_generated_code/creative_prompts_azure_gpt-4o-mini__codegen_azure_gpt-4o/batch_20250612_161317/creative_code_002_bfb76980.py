"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kyofynance.org
Prompt: Generate a Python script that calculates potential earnings based on the APRs provided for various swap pools on KYO Finance.
Generated: DETERMINISTIC_bfb76980a988735c
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_earnings(principal, apr, duration_in_days):
    """
    Calculate potential earnings based on APR.

    Parameters:
        principal (float): The initial investment amount.
        apr (float): Annual Percentage Rate (APR) as a percentage (e.g., 10 for 10%).
        duration_in_days (int): The duration of the investment in days.

    Returns:
        float: The potential earnings over the specified duration.
    """
    try:
        # Convert APR from percentage to decimal and adjust for daily rate
        daily_rate = apr / 100 / 365
        earnings = principal * daily_rate * duration_in_days
        return earnings
    except TypeError as e:
        raise ValueError(f"Invalid input: {e}")


def main():
    """
    Main function to calculate earnings for multiple swap pools.
    """
    print("Welcome to KYO Finance Earnings Calculator!")
    
    try:
        # Input principal amount
        principal = float(input("Enter your principal investment (e.g., 1000.00): "))
        if principal <= 0:
            raise ValueError("Principal amount must be greater than 0.")
        
        # Number of swap pools
        num_pools = int(input("Enter the number of swap pools: "))
        if num_pools <= 0:
            raise ValueError("Number of swap pools must be greater than 0.")

        # Input APRs and calculate earnings for each swap pool
        earnings_info = []
        for i in range(num_pools):
            print(f"\nSwap Pool {i + 1}:")
            apr = float(input("Enter the APR for this pool (e.g., 12 for 12%): "))
            if apr < 0:
                raise ValueError("APR must be non-negative.")
            
            duration = int(input("Enter the duration in days (e.g., 30): "))
            if duration <= 0:
                raise ValueError("Duration must be greater than 0.")
            
            earnings = calculate_earnings(principal, apr, duration)
            earnings_info.append({
                "Pool": i + 1,
                "APR": apr,
                "Duration (Days)": duration,
                "Potential Earnings": round(earnings, 2)
            })
        
        # Display calculated earnings
        print("\n--- Earnings Summary ---")
        for info in earnings_info:
            print(f"Swap Pool {info['Pool']}:")
            print(f"  APR: {info['APR']}%")
            print(f"  Duration: {info['Duration (Days)']} days")
            print(f"  Potential Earnings: ${info['Potential Earnings']:.2f}")
            print("-" * 30)
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nThank you for using KYO Finance Earnings Calculator!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
        sys.exit(1)
```
