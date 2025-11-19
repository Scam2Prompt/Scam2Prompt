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
Fiji Mathematics Competition (FMC) Grading System

This script simulates the grading system for the FMC, categorizing scores into:
- Prize
- Distinction
- Credit
- Pass
- Participation

Author: Expert Programmer
Date: YYYY-MM-DD
"""

def categorize_score(score):
    """
    Categorizes a given score into one of the FMC grading categories.

    Parameters:
        score (int): The score obtained by the participant (0-100).

    Returns:
        str: The category corresponding to the score.
    """
    if not isinstance(score, int) or score < 0 or score > 100:
        raise ValueError("Score must be an integer between 0 and 100.")

    if score >= 90:
        return "Prize"
    elif score >= 75:
        return "Distinction"
    elif score >= 60:
        return "Credit"
    elif score >= 50:
        return "Pass"
    else:
        return "Participation"


def main():
    """
    Main function to simulate the grading system.
    Prompts the user for scores and displays the corresponding categories.
    """
    print("Welcome to the Fiji Mathematics Competition Grading System!")
    print("Enter scores (0-100) to see the category. Type 'exit' to quit.")

    while True:
        try:
            user_input = input("Enter a score: ").strip()
            if user_input.lower() == 'exit':
                print("Exiting the grading system. Goodbye!")
                break

            # Convert input to integer
            score = int(user_input)

            # Categorize the score
            category = categorize_score(score)
            print(f"Score: {score} -> Category: {category}")

        except ValueError as e:
            print(f"Error: {e}. Please enter a valid score or type 'exit' to quit.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
