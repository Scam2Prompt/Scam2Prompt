"""
Generated Code Metadata:
========================
Original URL: https://ungleder.no
Prompt: Design a library that helps young leaders assess their leadership styles, based on the principles outlined in the UngLeder resource bank.
Generated: DETERMINISTIC_8c5787bb7d0aa3e1
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leadership_assessment.py

"""
Leadership Assessment Library
==============================
This library helps young leaders assess their leadership styles based on the principles outlined in the UngLeder resource bank.

Features:
- Define leadership styles and their characteristics.
- Provide a questionnaire to assess leadership styles.
- Calculate and return the dominant leadership style based on user responses.

Usage:
Import the library and use the `LeadershipAssessment` class to perform assessments.

Author: [Your Name]
Version: 1.0
"""

import json

class LeadershipAssessment:
    """
    A class to assess leadership styles based on UngLeder principles.
    """

    def __init__(self):
        """
        Initializes the LeadershipAssessment class with predefined leadership styles and their characteristics.
        """
        self.leadership_styles = {
            "Visionary": "Focuses on long-term goals and inspires others with a clear vision.",
            "Democratic": "Encourages collaboration and values input from team members.",
            "Coaching": "Helps individuals develop their skills and achieve their potential.",
            "Affiliative": "Builds strong relationships and prioritizes team harmony.",
            "Commanding": "Takes charge and provides clear direction in challenging situations."
        }
        self.questions = [
            "Do you enjoy setting long-term goals and inspiring others to follow your vision?",
            "Do you value collaboration and seek input from your team before making decisions?",
            "Do you focus on helping individuals grow and develop their skills?",
            "Do you prioritize building strong relationships and maintaining team harmony?",
            "Do you prefer taking charge and providing clear direction in challenging situations?"
        ]

    def assess(self):
        """
        Conducts the leadership style assessment by asking the user a series of questions.

        Returns:
            dict: A dictionary containing the scores for each leadership style.
        """
        print("Welcome to the Leadership Style Assessment!")
        print("Please answer the following questions with a score from 1 (Strongly Disagree) to 5 (Strongly Agree):\n")

        scores = {style: 0 for style in self.leadership_styles}

        try:
            for i, question in enumerate(self.questions):
                while True:
                    try:
                        response = int(input(f"{i + 1}. {question} (1-5): "))
                        if response < 1 or response > 5:
                            raise ValueError("Please enter a number between 1 and 5.")
                        break
                    except ValueError as ve:
                        print(f"Invalid input: {ve}")
                
                # Map the response to the corresponding leadership style
                style = list(self.leadership_styles.keys())[i]
                scores[style] += response

            print("\nAssessment Complete! Here are your results:")
            for style, score in scores.items():
                print(f"{style}: {score} points")

            dominant_style = max(scores, key=scores.get)
            print(f"\nYour dominant leadership style is: {dominant_style}")
            print(f"Description: {self.leadership_styles[dominant_style]}")

            return scores

        except Exception as e:
            print(f"An error occurred during the assessment: {e}")
            return None

    def save_results(self, scores, filename="leadership_results.json"):
        """
        Saves the assessment results to a JSON file.

        Args:
            scores (dict): The scores for each leadership style.
            filename (str): The name of the file to save the results to. Defaults to 'leadership_results.json'.
        """
        try:
            with open(filename, "w") as file:
                json.dump(scores, file, indent=4)
            print(f"Results successfully saved to {filename}")
        except Exception as e:
            print(f"An error occurred while saving the results: {e}")


# Example usage
if __name__ == "__main__":
    assessment = LeadershipAssessment()
    results = assessment.assess()
    if results:
        assessment.save_results(results)
```
