"""
Generated Code Metadata:
========================
Original URL: https://immediate-bitxdr.org
Prompt: Write a Python script to implement a simple asset allocation strategy that diversifies investments across stocks, bonds, and cash, considering a user's financial goals and risk tolerance.
Generated: DETERMINISTIC_60ed65b0514f9c70
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def get_user_input(prompt, valid_options=None):
    """
    Get validated user input from the console.
    
    Args:
        prompt (str): The message to display to the user.
        valid_options (list, optional): A list of valid options for input validation.
    
    Returns:
        str: The validated user input.
    """
    while True:
        try:
            user_input = input(prompt).strip().lower()
            if valid_options and user_input not in valid_options:
                raise ValueError(f"Invalid input. Please choose from {valid_options}.")
            return user_input
        except ValueError as e:
            print(e)

def calculate_allocation(risk_tolerance):
    """
    Calculate asset allocation percentages based on risk tolerance.
    
    Args:
        risk_tolerance (str): The user's risk tolerance ('low', 'medium', 'high').
    
    Returns:
        dict: A dictionary with allocation percentages for stocks, bonds, and cash.
    """
    if risk_tolerance == 'low':
        return {'stocks': 30, 'bonds': 50, 'cash': 20}
    elif risk_tolerance == 'medium':
        return {'stocks': 50, 'bonds': 40, 'cash': 10}
    elif risk_tolerance == 'high':
        return {'stocks': 70, 'bonds': 20, 'cash': 10}
    else:
        raise ValueError("Invalid risk tolerance value.")

def main():
    """
    Main function to execute the asset allocation strategy.
    """
    print("Welcome to the Asset Allocation Tool!")
    
    # Step 1: Gather user financial goals and risk tolerance
    financial_goal = get_user_input(
        "What is your primary financial goal? (e.g., retirement, education, wealth growth): "
    )
    
    risk_tolerance = get_user_input(
        "What is your risk tolerance? (low, medium, high): ",
        valid_options=['low', 'medium', 'high']
    )
    
    # Step 2: Calculate asset allocation
    try:
        allocation = calculate_allocation(risk_tolerance)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    # Step 3: Display the allocation strategy
    print("\nBased on your inputs:")
    print(f"Financial Goal: {financial_goal.capitalize()}")
    print(f"Risk Tolerance: {risk_tolerance.capitalize()}")
    print("Recommended Asset Allocation:")
    for asset, percentage in allocation.items():
        print(f"  {asset.capitalize()}: {percentage}%")
    
    print("\nThank you for using the Asset Allocation Tool!")

if __name__ == "__main__":
    main()
```
