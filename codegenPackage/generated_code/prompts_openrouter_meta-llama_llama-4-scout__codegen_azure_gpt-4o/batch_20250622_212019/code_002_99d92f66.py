"""
Generated Code Metadata:
========================
Original URL: https://job4chat.crediblejobs.in
Prompt: Generate a Python script to automate the process of checking eligibility criteria for the Chat Service Representative job, including age, education, and typing speed requirements.
Generated: DETERMINISTIC_99d92f66b459cd5c
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def check_eligibility(age, education, typing_speed):
    """
    Function to check eligibility for the Chat Service Representative job.
    
    Parameters:
        age (int): Age of the candidate.
        education (str): Education level of the candidate (e.g., "High School", "Bachelor's").
        typing_speed (float): Typing speed of the candidate in words per minute (WPM).
    
    Returns:
        str: Eligibility status message.
    """
    try:
        # Validate age criteria
        if age < 18:
            return "Ineligible: Candidate must be at least 18 years old."
        
        # Validate education criteria
        if education.lower() not in ["high school", "bachelor's", "master's", "phd"]:
            return "Ineligible: Candidate must have at least a High School diploma."
        
        # Validate typing speed criteria
        if typing_speed < 40.0:
            return "Ineligible: Candidate must have a typing speed of at least 40 WPM."
        
        # If all criteria are met
        return "Eligible: Candidate meets all the criteria for the Chat Service Representative job."
    
    except Exception as e:
        return f"Error: An unexpected issue occurred - {str(e)}"


def main():
    """
    Main function to interact with the user and check eligibility.
    """
    try:
        print("Welcome to the Chat Service Representative Eligibility Checker!")
        
        # Get user input for age
        age = int(input("Enter your age: "))
        
        # Get user input for education level
        education = input("Enter your highest level of education (e.g., High School, Bachelor's): ")
        
        # Get user input for typing speed
        typing_speed = float(input("Enter your typing speed in words per minute (WPM): "))
        
        # Check eligibility
        result = check_eligibility(age, education, typing_speed)
        print(result)
    
    except ValueError:
        print("Error: Invalid input. Please ensure age is an integer and typing speed is a number.")
    except Exception as e:
        print(f"Error: An unexpected issue occurred - {str(e)}")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
