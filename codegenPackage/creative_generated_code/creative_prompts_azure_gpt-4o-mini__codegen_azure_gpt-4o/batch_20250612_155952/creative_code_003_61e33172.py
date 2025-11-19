"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maiv-whitelist.pages.dev
Prompt: Generate a Python script that assesses investment preferences based on varying returns and durations offered by MAIV.
Generated: DETERMINISTIC_61e3317265bafda2
Batch ID: 20250612_155952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Investment Preferences Assessment Script
This script evaluates investment preferences based on varying returns and durations
offered by MAIV (My Awesome Investment Venture). Users are prompted to input their
preferred minimum return and maximum duration for investment, and the script assesses
available options based on their preferences.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import sys

# Sample investment options offered by MAIV
INVESTMENT_OPTIONS = [
    {"id": 1, "name": "High Yield Bond", "return": 8.5, "duration_months": 24},
    {"id": 2, "name": "Stock Portfolio", "return": 12.0, "duration_months": 36},
    {"id": 3, "name": "Real Estate Fund", "return": 10.0, "duration_months": 60},
    {"id": 4, "name": "Savings Account", "return": 3.0, "duration_months": 12},
    {"id": 5, "name": "Growth ETF", "return": 15.0, "duration_months": 48}
]

def get_user_preferences():
    """
    Prompts the user to input their investment preferences.
    :return: A tuple containing minimum return and maximum duration as floats and integers.
    """
    try:
        min_return = float(input("Enter your preferred minimum return percentage (e.g., 7.5): "))
        max_duration = int(input("Enter your preferred maximum duration in months: "))
        return min_return, max_duration
    except ValueError:
        print("Invalid input. Please enter a numeric value for return and an integer for duration.")
        sys.exit(1)

def filter_investment_options(min_return, max_duration):
    """
    Filters the investment options based on user preferences.
    :param min_return: Minimum return percentage desired by the user.
    :param max_duration: Maximum duration in months acceptable to the user.
    :return: A list of investment options matching the criteria.
    """
    return [
        option for option in INVESTMENT_OPTIONS
        if option["return"] >= min_return and option["duration_months"] <= max_duration
    ]

def display_results(filtered_options):
    """
    Displays the filtered investment options to the user.
    :param filtered_options: List of investment options matching the user's criteria.
    """
    if filtered_options:
        print("\nBased on your preferences, the following investment options are available:")
        for option in filtered_options:
            print(f"- {option['name']} (Return: {option['return']}%, Duration: {option['duration_months']} months)")
    else:
        print("\nNo investment options match your preferences. Please adjust your criteria.")

def main():
    """
    Main function to run the assessment script.
    """
    print("Welcome to the MAIV Investment Preferences Assessment Tool!")
    
    # Get the user's preferences
    min_return, max_duration = get_user_preferences()
    
    # Filter investment options based on preferences
    filtered_options = filter_investment_options(min_return, max_duration)
    
    # Display the results
    display_results(filtered_options)
    print("\nThank you for using the MAIV Investment Preferences Assessment Tool!")

if __name__ == "__main__":
    main()
```
