"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assettrackr.app
Prompt: What are the key considerations for developing a retirement planning tool that reflects the principles of integrity and transparency highlighted by Grade World Investment Limited?
Generated: DETERMINISTIC_5c7ee75c14b26070
Batch ID: 20250612_155144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# retirement_planner.py
"""
Retirement Planning Tool by Grade World Investment Limited.
This tool is designed to reflect integrity and transparency principles,
helping users make informed decisions about retirement savings and planning.
"""

import sys

def validate_input(prompt, validator):
    """
    Validate user input based on a provided validator function.
    
    Args:
        prompt (str): The input prompt shown to the user.
        validator (function): A function to validate the input.
        
    Returns:
        value: The validated input value.
    """
    while True:
        try:
            user_input = input(prompt)
            value = validator(user_input)
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def get_float_input(prompt):
    """
    Get a float input from the user.
    
    Args:
        prompt (str): The input prompt shown to the user.
        
    Returns:
        float: The validated float value.
    """
    return validate_input(prompt, lambda x: float(x))

def get_int_input(prompt):
    """
    Get an integer input from the user.
    
    Args:
        prompt (str): The input prompt shown to the user.
        
    Returns:
        int: The validated integer value.
    """
    return validate_input(prompt, lambda x: int(x))

def calculate_retirement_savings(current_age, retirement_age, annual_savings, annual_growth_rate):
    """
    Calculate the estimated retirement savings.
    
    Args:
        current_age (int): The user's current age.
        retirement_age (int): The age at which the user plans to retire.
        annual_savings (float): Amount saved annually for retirement.
        annual_growth_rate (float): Estimated annual growth rate of savings (in percentage).
        
    Returns:
        float: The estimated total retirement savings.
    """
    years_to_save = retirement_age - current_age
    if years_to_save <= 0:
        raise ValueError("Retirement age must be greater than current age.")
    
    total_savings = 0.0
    for year in range(years_to_save):
        total_savings = (total_savings + annual_savings) * (1 + annual_growth_rate / 100.0)
    return total_savings

def main():
    """
    Main function to run the retirement planning tool.
    """
    print("Welcome to the Retirement Planning Tool")
    print("Please provide the following information:")
    
    try:
        # Get user inputs
        current_age = get_int_input("Enter your current age: ")
        retirement_age = get_int_input("Enter your desired retirement age: ")
        annual_savings = get_float_input("Enter your annual savings amount (in dollars): ")
        annual_growth_rate = get_float_input("Enter the expected annual growth rate of savings (in percentage): ")
        
        # Calculate and display the estimated savings
        estimated_savings = calculate_retirement_savings(
            current_age, retirement_age, annual_savings, annual_growth_rate
        )
        print(f"\nBased on the provided information, your estimated retirement savings will be "
              f"${estimated_savings:,.2f} by the time you retire.")
        print("Thank you for using the Retirement Planning Tool!")
    
    except ValueError as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Exiting the tool. Have a great day!")

# Entry point for the script
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
        sys.exit(0)
```
