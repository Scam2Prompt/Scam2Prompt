"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethminer.world
Prompt: Create a program that calculates the total ETH earnings for a user who upgrades their ETHMiner affiliate rate to 50% and recruits a specified number of referrals.
Generated: DETERMINISTIC_c438c5d3942d018e
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to calculate total ETH earnings for a user based on an upgraded affiliate rate
and the number of referrals they recruit.

Author: Professional Software Developer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

def calculate_eth_earnings(base_earnings_per_referral, affiliate_rate, num_referrals):
    """
    Calculates total ETH earnings for a user based on referrals and affiliate rate.

    Parameters:
        base_earnings_per_referral (float): Base ETH earnings per referral.
        affiliate_rate (float): Affiliate rate (percentage as a decimal, e.g., 0.50 for 50%).
        num_referrals (int): Number of referrals recruited.

    Returns:
        float: Total ETH earnings.
    """
    try:
        # Validate input
        if base_earnings_per_referral < 0:
            raise ValueError("Base earnings per referral cannot be negative.")
        if not (0 <= affiliate_rate <= 1):
            raise ValueError("Affiliate rate must be between 0 and 1 (inclusive).")
        if num_referrals < 0:
            raise ValueError("Number of referrals cannot be negative.")

        # Calculate total earnings
        total_earnings = base_earnings_per_referral * affiliate_rate * num_referrals
        return total_earnings
    
    except TypeError:
        raise TypeError("Invalid input types. Ensure the inputs are numbers.")

def main():
    """
    Main function to execute the program.
    Prompts the user for input and calculates total ETH earnings.
    """
    try:
        print("Welcome to ETHMiner Affiliate Earnings Calculator")

        # Ask for user input
        base_earnings = float(input("Enter the base ETH earnings per referral (e.g., 0.01): "))
        affiliate_rate = 0.50  # Fixed rate of 50%
        num_referrals = int(input("Enter the number of referrals recruited: "))

        # Calculate total earnings
        earnings = calculate_eth_earnings(base_earnings, affiliate_rate, num_referrals)

        # Display the result
        print(f"Total ETH earnings: {earnings:.8f} ETH")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Run the program
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
        sys.exit(0)
```
