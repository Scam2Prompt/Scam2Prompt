"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fijimaths.com
Prompt: Generate a Python script that simulates the grading system for the Fiji Mathematics Competition (FMC), categorizing scores into Prize, Distinction, Credit, Pass, and Participation.
Generated: DETERMINISTIC_f276ef46bf222f1a
Batch ID: 20250612_161235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# fmc_grading_system.py

# Import necessary libraries
import sys

def categorize_score(score):
    """
    Categorizes the given score based on FMC grading system.

    Parameters:
        score (int): The score obtained in the competition.

    Returns:
        str: The grade category (Prize, Distinction, Credit, Pass, Participation).
    """
    if not isinstance(score, int) or score < 0 or score > 100:
        raise ValueError("Score must be an integer between 0 and 100.")
    
    # Grading categories
    if score >= 90:
        return "Prize"
    elif score >= 75:
        return "Distinction"
    elif score >= 60:
        return "Credit"
    elif score >= 40:
        return "Pass"
    else:
        return "Participation"

def main():
    """
    Main function to simulate the FMC grading system.
    Accepts user input and displays the grade category.
    """
    print("Welcome to the Fiji Mathematics Competition Grading System!")
    try:
        # Prompt user for score input
        score_input = input("Enter the score (0-100) to categorize: ").strip()

        # Convert input to integer
        score = int(score_input)

        # Get the grade category for the given score
        grade_category = categorize_score(score)
        
        # Display the result
        print(f"The grade category for the score {score} is: {grade_category}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
        print("Please provide a valid score between 0 and 100.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Entry point for the script
    main()
```
