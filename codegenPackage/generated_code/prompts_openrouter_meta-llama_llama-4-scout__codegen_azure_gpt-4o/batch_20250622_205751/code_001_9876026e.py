"""
Generated Code Metadata:
========================
Original URL: https://askcardiologist.in
Prompt: Generate a code for a simple heart health assessment tool that considers Life’s Essential Eight factors.
Generated: DETERMINISTIC_9876026e58409fcf
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def get_user_input(prompt, valid_range):
    """
    Get validated user input within a specified range.

    Args:
        prompt (str): The prompt to display to the user.
        valid_range (tuple): A tuple specifying the valid range (min, max).

    Returns:
        float: The validated user input.
    """
    while True:
        try:
            value = float(input(prompt))
            if valid_range[0] <= value <= valid_range[1]:
                return value
            else:
                print(f"Please enter a value between {valid_range[0]} and {valid_range[1]}.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def assess_heart_health():
    """
    Assess heart health based on Life's Essential Eight factors.

    Returns:
        str: A summary of the user's heart health assessment.
    """
    print("Welcome to the Heart Health Assessment Tool!")
    print("Please provide the following information:")

    # Collect data for Life's Essential Eight factors
    age = get_user_input("Enter your age (years): ", (0, 120))
    systolic_bp = get_user_input("Enter your systolic blood pressure (mmHg): ", (50, 250))
    diastolic_bp = get_user_input("Enter your diastolic blood pressure (mmHg): ", (30, 150))
    cholesterol = get_user_input("Enter your total cholesterol level (mg/dL): ", (100, 400))
    blood_glucose = get_user_input("Enter your fasting blood glucose level (mg/dL): ", (50, 300))
    bmi = get_user_input("Enter your Body Mass Index (BMI): ", (10, 50))
    physical_activity = get_user_input("Enter your weekly physical activity (minutes): ", (0, 1000))
    smoking_status = input("Do you currently smoke? (yes/no): ").strip().lower()

    # Validate smoking status input
    while smoking_status not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
        smoking_status = input("Do you currently smoke? (yes/no): ").strip().lower()

    # Assess heart health based on collected data
    health_score = 0

    # Age factor
    if age < 45:
        health_score += 2
    elif 45 <= age <= 65:
        health_score += 1

    # Blood pressure factor
    if systolic_bp < 120 and diastolic_bp < 80:
        health_score += 2
    elif 120 <= systolic_bp <= 139 or 80 <= diastolic_bp <= 89:
        health_score += 1

    # Cholesterol factor
    if cholesterol < 200:
        health_score += 2
    elif 200 <= cholesterol <= 239:
        health_score += 1

    # Blood glucose factor
    if blood_glucose < 100:
        health_score += 2
    elif 100 <= blood_glucose <= 125:
        health_score += 1

    # BMI factor
    if 18.5 <= bmi <= 24.9:
        health_score += 2
    elif 25 <= bmi <= 29.9:
        health_score += 1

    # Physical activity factor
    if physical_activity >= 150:
        health_score += 2
    elif 75 <= physical_activity < 150:
        health_score += 1

    # Smoking status factor
    if smoking_status == "no":
        health_score += 2

    # Provide assessment summary
    print("\nHeart Health Assessment Summary:")
    if health_score >= 12:
        return "Excellent heart health! Keep up the good work."
    elif 8 <= health_score < 12:
        return "Good heart health, but there is room for improvement."
    else:
        return "Poor heart health. Consider consulting a healthcare professional."

if __name__ == "__main__":
    try:
        result = assess_heart_health()
        print(result)
    except KeyboardInterrupt:
        print("\nAssessment interrupted. Exiting...")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
