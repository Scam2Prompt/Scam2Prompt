"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-alpha.app
Prompt: Create a Python script to calculate risk tolerance based on Immediate Adipex's recommended parameters for crypto investments.
Generated: DETERMINISTIC_9c0dea3caf3c64b3
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate risk tolerance for crypto investments based on Immediate Adipex's recommended parameters.

The script calculates risk tolerance by analyzing user inputs such as age, income, investment knowledge, 
and willingness to take risks. It classifies the user into one of three categories: High, Medium, or Low tolerance.
"""

# Import necessary libraries
import sys

def get_user_input(prompt, input_type=str):
    """
    Safely gets input from the user and casts it to the specified type.

    Args:
        prompt (str): The message to display to the user.
        input_type (type): The type to cast the input to (default is str).

    Returns:
        value: The user's input cast to the specified type.

    Raises:
        ValueError: If the input cannot be cast to the specified type.
    """
    while True:
        try:
            value = input_type(input(prompt))
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

def calculate_risk_tolerance(age, annual_income, investment_knowledge, risk_willingness):
    """
    Calculates the risk tolerance based on user inputs.

    Args:
        age (int): The user's age.
        annual_income (float): The user's annual income.
        investment_knowledge (int): A score (1-5) representing the user's investment knowledge.
        risk_willingness (int): A score (1-5) representing the user's willingness to take risks.

    Returns:
        str: The risk tolerance category ('High', 'Medium', 'Low').
    """
    # Validate input ranges
    if not (1 <= investment_knowledge <= 5):
        raise ValueError("Investment knowledge must be between 1 and 5.")
    if not (1 <= risk_willingness <= 5):
        raise ValueError("Risk willingness must be between 1 and 5.")
    
    # Assign weights to parameters
    age_weight = (100 - age) / 100  # Younger individuals often have higher risk tolerance
    income_weight = annual_income / 100000  # Higher income may enable higher risk tolerance
    knowledge_weight = investment_knowledge / 5
    risk_weight = risk_willingness / 5

    # Compute overall risk tolerance score
    risk_score = (age_weight + income_weight + knowledge_weight + risk_weight) / 4

    # Classify risk tolerance
    if risk_score >= 0.7:
        return "High"
    elif risk_score >= 0.4:
        return "Medium"
    else:
        return "Low"

def main():
    """
    Main function to execute the risk tolerance calculator.
    """
    print("Welcome to the Crypto Investment Risk Tolerance Calculator!\n")
    
    # Gather user inputs
    try:
        age = get_user_input("Enter your age: ", int)
        annual_income = get_user_input("Enter your annual income (in USD): ", float)
        investment_knowledge = get_user_input(
            "Rate your investment knowledge (1-5, where 1 is beginner and 5 is expert): ", int
        )
        risk_willingness = get_user_input(
            "Rate your willingness to take risks (1-5, where 1 is very low and 5 is very high): ", int
        )
    
        # Calculate risk tolerance
        risk_tolerance = calculate_risk_tolerance(age, annual_income, investment_knowledge, risk_willingness)
        print(f"\nYour risk tolerance is classified as: {risk_tolerance}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
