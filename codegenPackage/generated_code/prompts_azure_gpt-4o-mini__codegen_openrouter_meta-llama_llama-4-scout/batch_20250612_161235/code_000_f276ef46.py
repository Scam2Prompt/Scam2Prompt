"""
Generated Code Metadata:
========================
Original URL: https://fijimaths.com
Prompt: Generate a Python script that simulates the grading system for the Fiji Mathematics Competition (FMC), categorizing scores into Prize, Distinction, Credit, Pass, and Participation.
Generated: DETERMINISTIC_f276ef46bf222f1a
Batch ID: 20250612_161235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Fiji Mathematics Competition (FMC) Grading System Simulator

This script simulates the grading system for the Fiji Mathematics Competition (FMC),
categorizing scores into Prize, Distinction, Credit, Pass, and Participation.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_grade(score):
    """
    Calculate the grade based on the score.

    Args:
        score (int): The score obtained by the participant.

    Returns:
        str: The grade corresponding to the score.

    Raises:
        ValueError: If the score is not within the valid range (0-100).
    """
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100")

    if score >= 90:
        return "Prize"
    elif score >= 80:
        return "Distinction"
    elif score >= 70:
        return "Credit"
    elif score >= 50:
        return "Pass"
    else:
        return "Participation"


def main():
    try:
        # Example usage
        scores = [95, 85, 75, 45, 30]

        for score in scores:
            grade = calculate_grade(score)
            print(f"Score: {score}, Grade: {grade}")

        # Get user input
        while True:
            try:
                user_score = int(input("Enter a score (0-100): "))
                grade = calculate_grade(user_score)
                print(f"Score: {user_score}, Grade: {grade}")
                cont = input("Do you want to continue? (y/n): ")
                if cont.lower() != 'y':
                    break
            except ValueError as e:
                print(f"Invalid input: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
