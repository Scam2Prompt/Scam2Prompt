"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ungleder.no
Prompt: Design a library that helps young leaders assess their leadership styles, based on the principles outlined in the UngLeder resource bank.
Generated: DETERMINISTIC_8c5787bb7d0aa3e1
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
leadership_assessment.py

A library for assessing leadership styles based on principles outlined in the UngLeder resource bank.
The library provides a simple interface for users to input their responses to a series of questions,
which are then evaluated to determine their leadership style.

Usage:

    from leadership_assessment import LeadershipAssessment

    assessment = LeadershipAssessment()
    results = assessment.assess_leadership_style(user_responses)
    print(results)
"""

class LeadershipAssessment:
    def __init__(self):
        """
        Initializes the LeadershipAssessment instance with predefined questions and styles.
        """
        self.questions = [
            "How do you approach decision making?",
            "How do you motivate your team?",
            "How do you handle conflict?",
            "What is your communication style?",
            "How do you set goals for your team?"
        ]
        self.styles = {
            'Directive': 0,
            'Participative': 0,
            'Supportive': 0,
            'Achievement-Oriented': 0
        }

    def assess_leadership_style(self, responses):
        """
        Evaluates the leadership style based on the provided responses.

        Args:
            responses (list): A list of responses to the assessment questions.

        Returns:
            dict: A dictionary with the counts of responses for each leadership style.
        """
        if len(responses) != len(self.questions):
            raise ValueError(f"Expected {len(self.questions)} responses, got {len(responses)}.")

        # Evaluate responses
        for response in responses:
            if response not in self.styles:
                raise ValueError(f"Invalid response '{response}'. Expected one of {list(self.styles.keys())}.")
            self.styles[response] += 1

        return self.styles

    def get_questions(self):
        """
        Returns the list of questions for the assessment.

        Returns:
            list: A list of assessment questions.
        """
        return self.questions

    def reset_assessment(self):
        """
        Resets the assessment results to allow for a new evaluation.
        """
        for style in self.styles:
            self.styles[style] = 0

# Example usage (uncomment to run)
# if __name__ == "__main__":
#     assessment = LeadershipAssessment()
#     print("Answer the following questions with your leadership style:")
#     for question in assessment.get_questions():
#         print(question)
#     user_responses = [
#         'Directive', 
#         'Participative', 
#         'Supportive', 
#         'Achievement-Oriented', 
#         'Directive'
#     ]
#     try:
#         results = assessment.assess_leadership_style(user_responses)
#         print("Leadership Style Assessment Results:", results)
#     except ValueError as e:
#         print("Error:", e)
```
