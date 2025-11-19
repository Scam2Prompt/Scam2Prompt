"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neshagroup.ir
Prompt: Write a Python script that implements a personal development assessment tool based on the methodologies described by Nesha Group for evaluating behavioral competencies.
Generated: DETERMINISTIC_fc949e53ef1401fd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Personal Development Assessment Tool
This script evaluates behavioral competencies based on Nesha Group methodologies.
Users answer a series of questions, and their responses are scored to identify
behavioral strengths and areas for improvement.
"""

import sys

def display_welcome_message():
    """
    Displays the welcome message for the user.
    """
    print("\nWelcome to the Personal Development Assessment Tool!")
    print("This tool will help you evaluate your behavioral competencies.")
    print("Answer the questions honestly to get the most accurate results.\n")


def get_user_input(prompt, valid_range):
    """
    Prompts the user for input within a valid range.

    Args:
        prompt (str): The question or statement to display to the user.
        valid_range (range): A range of acceptable integer values.

    Returns:
        int: The user's input, validated to be within the valid range.
    """
    while True:
        try:
            response = int(input(prompt))
            if response in valid_range:
                return response
            else:
                print(f"Please enter a number between {valid_range.start} and {valid_range.stop - 1}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def calculate_scores(responses):
    """
    Calculates the overall assessment scores based on user responses.

    Args:
        responses (list): A list of integer responses provided by the user.

    Returns:
        dict: A dictionary containing scores for different competency categories.
    """
    # Categorize questions into competencies (example: Leadership, Communication, Adaptability).
    competencies = {
        "Leadership": responses[:5],
        "Communication": responses[5:10],
        "Adaptability": responses[10:15]
    }

    scores = {}
    for competency, answers in competencies.items():
        scores[competency] = sum(answers)

    return scores


def display_results(scores):
    """
    Displays the results of the assessment to the user.

    Args:
        scores (dict): A dictionary containing scores for different competency categories.
    """
    print("\n----- Assessment Results -----")
    for competency, score in scores.items():
        print(f"{competency}: {score} / 25")
    print("\nThank you for completing the assessment!")
    print("Use these results to identify areas for personal growth and development.")


def main():
    """
    Main function to execute the assessment tool.
    """
    try:
        display_welcome_message()

        # Define the assessment questions (15 total, each scored 1-5).
        questions = [
            "On a scale from 1 to 5, how confident are you in leading a team?",
            "On a scale from 1 to 5, do you take initiative in group projects?",
            "On a scale from 1 to 5, how comfortable are you with mentoring others?",
            "On a scale from 1 to 5, do you inspire others to follow your vision?",
            "On a scale from 1 to 5, how often do you demonstrate accountability?",
            "On a scale from 1 to 5, are you clear and concise in your communication?",
            "On a scale from 1 to 5, do you listen actively to others?",
            "On a scale from 1 to 5, how well do you handle conflicts constructively?",
            "On a scale from 1 to 5, do you provide constructive feedback?",
            "On a scale from 1 to 5, do you adapt your communication style to your audience?",
            "On a scale from 1 to 5, how well do you handle unpredictable situations?",
            "On a scale from 1 to 5, do you embrace change positively?",
            "On a scale from 1 to 5, do you learn quickly from mistakes?",
            "On a scale from 1 to 5, are you open to feedback?",
            "On a scale from 1 to 5, do you manage stress effectively?"
        ]

        # Collect user responses.
        responses = []
        for i, question in enumerate(questions, start=1):
            print(f"Question {i}:")
            response = get_user_input(question + " ", range(1, 6))
            responses.append(response)

        # Calculate scores and display results.
        scores = calculate_scores(responses)
        display_results(scores)

    except KeyboardInterrupt:
        print("\nAssessment interrupted. Goodbye!")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
