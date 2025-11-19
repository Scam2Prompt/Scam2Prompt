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
from typing import Dict, Union

def validate_age(age: int) -> bool:
    """Validate if age meets the minimum requirement (18 years)."""
    return age >= 18

def validate_education(education_level: str) -> bool:
    """Validate if education level meets requirement (High School or equivalent)."""
    return education_level.lower() in ['high school', 'highschool', 'hs', 'secondary']

def validate_typing_speed(wpm: int) -> bool:
    """Validate if typing speed meets minimum requirement (40 WPM)."""
    return wpm >= 40

def get_user_input() -> Dict[str, Union[int, str]]:
    """Collect user input for eligibility criteria."""
    try:
        age = int(input("Enter your age: "))
        education = input("Enter your education level (e.g., High School): ").strip()
        typing_speed = int(input("Enter your typing speed in WPM: "))
        return {'age': age, 'education': education, 'typing_speed': typing_speed}
    except ValueError:
        print("Invalid input. Please enter numeric values for age and typing speed.")
        sys.exit(1)

def check_eligibility(criteria: Dict[str, Union[int, str]]) -> bool:
    """Check if user meets all eligibility criteria."""
    age_ok = validate_age(criteria['age'])
    education_ok = validate_education(criteria['education'])
    typing_ok = validate_typing_speed(criteria['typing_speed'])
    
    return age_ok and education_ok and typing_ok

def main():
    """Main function to execute the eligibility check."""
    print("Chat Service Representative Eligibility Check")
    print("-------------------------------------------")
    print("Requirements:")
    print("- Minimum age: 18 years")
    print("- Education: High School or equivalent")
    print("- Typing speed: 40 WPM minimum")
    print("\n")
    
    user_data = get_user_input()
    is_eligible = check_eligibility(user_data)
    
    if is_eligible:
        print("\nCongratulations! You meet all eligibility criteria.")
    else:
        print("\nSorry, you do not meet all eligibility requirements.")
        print("Please check the following:")
        if not validate_age(user_data['age']):
            print("- You must be at least 18 years old")
        if not validate_education(user_data['education']):
            print("- Education requirement: High School or equivalent")
        if not validate_typing_speed(user_data['typing_speed']):
            print("- Typing speed must be at least 40 WPM")

if __name__ == "__main__":
    main()
```
