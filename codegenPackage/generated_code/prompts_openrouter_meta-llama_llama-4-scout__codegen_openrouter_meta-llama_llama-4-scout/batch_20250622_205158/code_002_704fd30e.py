"""
Generated Code Metadata:
========================
Original URL: https://d5crl8r4pqx.typeform.com
Prompt: "Design a Typeform survey to gather employee satisfaction data, including questions and logic for follow-up questions."
Generated: DETERMINISTIC_704fd30e9d62ce73
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json

# Define the survey structure
class Survey:
    def __init__(self):
        self.survey = {
            "title": "Employee Satisfaction Survey",
            "description": "A survey to gather employee satisfaction data",
            "questions": []
        }

    def add_question(self, question):
        self.survey["questions"].append(question)

    def get_survey(self):
        return self.survey


# Define a question structure
class Question:
    def __init__(self, id, type, ref, question, description, choices=None):
        self.question = {
            "id": id,
            "type": type,
            "ref": ref,
            "question": question,
            "description": description,
            "choices": choices if choices else []
        }

    def add_choice(self, choice):
        self.question["choices"].append(choice)

    def get_question(self):
        return self.question


# Create survey and questions
survey = Survey()

# Question 1: Overall satisfaction
q1 = Question(
    id="q1",
    type="multiple_choice",
    ref="overall_satisfaction",
    question="How satisfied are you with your job overall?",
    description="Please select one of the following options",
    choices=[
        {"label": "Very Satisfied", "value": "very_satisfied"},
        {"label": "Somewhat Satisfied", "value": "somewhat_satisfied"},
        {"label": "Neutral", "value": "neutral"},
        {"label": "Somewhat Dissatisfied", "value": "somewhat_dissatisfied"},
        {"label": "Very Dissatisfied", "value": "very_dissatisfied"}
    ]
)

# Question 2: Satisfaction with manager (only if somewhat or very dissatisfied with overall satisfaction)
q2 = Question(
    id="q2",
    type="multiple_choice",
    ref="satisfaction_with_manager",
    question="How satisfied are you with your manager?",
    description="Please select one of the following options",
    choices=[
        {"label": "Very Satisfied", "value": "very_satisfied"},
        {"label": "Somewhat Satisfied", "value": "somewhat_satisfied"},
        {"label": "Neutral", "value": "neutral"},
        {"label": "Somewhat Dissatisfied", "value": "somewhat_dissatisfied"},
        {"label": "Very Dissatisfied", "value": "very_dissatisfied"}
    ]
)

# Question 3: Suggestions for improvement (open-ended)
q3 = Question(
    id="q3",
    type="paragraph",
    ref="suggestions_for_improvement",
    question="Do you have any suggestions for improving employee satisfaction?",
    description="Please provide your suggestions"
)

# Add questions to survey
survey.add_question(q1.get_question())

# Add logic for follow-up questions
survey.survey["logic"] = [
    {
        "id": "logic_1",
        "type": "condition",
        "condition": {
            "ref": "q1",
            "value": ["somewhat_dissatisfied", "very_dissatisfied"]
        },
        "actions": [
            {
                "type": "show_question",
                "question_ref": "q2"
            }
        ]
    }
]

survey.add_question(q2.get_question())
survey.add_question(q3.get_question())

# Print survey structure
def print_survey(survey):
    try:
        print(json.dumps(survey.get_survey(), indent=4))
    except Exception as e:
        print(f"An error occurred: {e}")

print_survey(survey)
```
