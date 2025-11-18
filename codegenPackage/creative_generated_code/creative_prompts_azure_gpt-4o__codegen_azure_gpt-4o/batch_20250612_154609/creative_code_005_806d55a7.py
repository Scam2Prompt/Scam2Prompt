"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welforcevestcapital.com
Prompt: Create a Python program to simulate the investment plan selection process on Welforcevest Capital, allowing users to choose plans like Starter, Standard, Advanced, Pro, or Enterprise and calculate the expected profit.
Generated: DETERMINISTIC_806d55a7a5c61f53
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
import sys

def display_menu():
    """
    Display the investment plans menu to the user.
    """
    print("\nWelcome to Welforcevest Capital Investment Plans!")
    print("Please choose an investment plan:")
    print("1. Starter Plan    - $1,000 investment, 5% monthly profit")
    print("2. Standard Plan   - $5,000 investment, 6% monthly profit")
    print("3. Advanced Plan   - $10,000 investment, 7% monthly profit")
    print("4. Pro Plan        - $50,000 investment, 8% monthly profit")
    print("5. Enterprise Plan - $100,000 investment, 10% monthly profit")
    print("6. Exit")

def calculate_profit(investment, rate, months):
    """
    Calculate the expected profit for a given investment, rate, and duration.

    Parameters:
    investment (float): Initial investment amount.
    rate (float): Monthly profit rate in percentage.
    months (int): Duration of the investment in months.

    Returns:
    float: Expected profit over the investment period.
    """
    return investment * (rate / 100) * months

def get_user_input(prompt, valid_options=None):
    """
    Get validated input from the user.

    Parameters:
    prompt (str): Input prompt for the user.
    valid_options (list): List of valid options (optional).

    Returns:
    str: Validated user input.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if valid_options and user_input not in valid_options:
                raise ValueError("Invalid option. Please try again.")
            return user_input
        except ValueError as e:
            print(e)

def main():
    """
    Main function to simulate the investment plan selection process.
    """
    plans = {
        "1": {"name": "Starter Plan", "investment": 1000, "rate": 5},
        "2": {"name": "Standard Plan", "investment": 5000, "rate": 6},
        "3": {"name": "Advanced Plan", "investment": 10000, "rate": 7},
        "4": {"name": "Pro Plan", "investment": 50000, "rate": 8},
        "5": {"name": "Enterprise Plan", "investment": 100000, "rate": 10},
    }

    while True:
        # Display menu to the user
        display_menu()

        # Get user's choice of investment plan
        user_choice = get_user_input("Enter the number corresponding to your choice: ", valid_options=list(plans.keys()) + ["6"])

        if user_choice == "6":
            print("Thank you for using Welforcevest Capital. Goodbye!")
            sys.exit()

        # Get the plan details based on the user's choice
        chosen_plan = plans[user_choice]
        print(f"\nYou selected {chosen_plan['name']}!")

        # Get the investment duration in months
        while True:
            try:
                months = int(get_user_input("Enter the number of months you want to invest for: "))
                if months <= 0:
                    raise ValueError("Investment duration must be a positive integer.")
                break
            except ValueError as e:
                print(e)

        # Calculate the expected profit
        profit = calculate_profit(chosen_plan["investment"], chosen_plan["rate"], months)
        print(f"\nInvestment Summary:")
        print(f"Plan: {chosen_plan['name']}")
        print(f"Initial Investment: ${chosen_plan['investment']}")
        print(f"Monthly Profit Rate: {chosen_plan['rate']}%")
        print(f"Duration: {months} months")
        print(f"Expected Profit: ${profit:.2f}")

if __name__ == "__main__":
    # Run the program
    main()
```
