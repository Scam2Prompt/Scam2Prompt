"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binotradefx.com
Prompt: Write a program to calculate weekly, daily, or unlimited withdrawal amounts based on user-selected investment packages (Silver, Gold, Platinum) as described on BinoTrade Fx.
Generated: DETERMINISTIC_a14385a454427cb1
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate weekly, daily, or unlimited withdrawal amounts 
# based on user-selected investment packages on BinoTrade Fx.

# Import required modules
import sys

def main():
    """
    Main function to handle user input and calculate withdrawals
    based on investment packages.
    """
    print("Welcome to BinoTrade Fx Withdrawal Calculator")
    print("Select an investment package:")
    print("1. Silver")
    print("2. Gold")
    print("3. Platinum")

    try:
        package_choice = int(input("Enter the number corresponding to your package: "))
        if package_choice not in [1, 2, 3]:
            print("Invalid package option selected.")
            sys.exit(1)

        print("\nSelect withdrawal option:")
        print("1. Weekly Withdrawal")
        print("2. Daily Withdrawal")
        print("3. Unlimited Withdrawal")
        
        withdrawal_choice = int(input("Enter the number corresponding to your withdrawal option: "))
        if withdrawal_choice not in [1, 2, 3]:
            print("Invalid withdrawal option selected.")
            sys.exit(1)

        # Determine package limits
        if package_choice == 1:  # Silver Package
            limits = {"weekly": 500, "daily": 100, "unlimited": 2000}
        elif package_choice == 2:  # Gold Package
            limits = {"weekly": 1000, "daily": 200, "unlimited": 5000}
        elif package_choice == 3:  # Platinum Package
            limits = {"weekly": 2000, "daily": 500, "unlimited": 10000}

        # Calculate withdrawal amounts based on user choice
        if withdrawal_choice == 1:
            withdrawal_amount = limits["weekly"]
            print(f"\nYour weekly withdrawal limit is: ${withdrawal_amount}")
        elif withdrawal_choice == 2:
            withdrawal_amount = limits["daily"]
            print(f"\nYour daily withdrawal limit is: ${withdrawal_amount}")
        elif withdrawal_choice == 3:
            withdrawal_amount = limits["unlimited"]
            print(f"\nYour unlimited withdrawal limit is: ${withdrawal_amount}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Thank you for using BinoTrade Fx Withdrawal Calculator.")

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
```
