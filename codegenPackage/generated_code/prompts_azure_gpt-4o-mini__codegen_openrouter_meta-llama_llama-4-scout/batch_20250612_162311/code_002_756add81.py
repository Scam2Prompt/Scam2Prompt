"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.web.app
Prompt: Create a sample application questionnaire for the Sui Foundation's Developer Grants Program, ensuring it emphasizes the project's impact on decentralization.
Generated: DETERMINISTIC_756add81d3aca771
Batch ID: 20250612_162311
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# application_questionnaire.py

class ApplicationQuestionnaire:
    def __init__(self):
        self.questions = {
            "project_description": "",
            "decentralization_impact": "",
            "team_description": "",
            "technical_details": "",
            "timeline": "",
            "budget": "",
        }

    def ask_questions(self):
        for question, answer in self.questions.items():
            if question == "project_description":
                self.questions[question] = input("1. Please provide a brief description of your project: ")
            elif question == "decentralization_impact":
                self.questions[question] = input("2. How does your project contribute to decentralization on the Sui network? ")
            elif question == "team_description":
                self.questions[question] = input("3. Please describe your team's experience and qualifications: ")
            elif question == "technical_details":
                self.questions[question] = input("4. Provide technical details about your project, including any relevant code repositories: ")
            elif question == "timeline":
                self.questions[question] = input("5. What is your project's timeline, including key milestones? ")
            elif question == "budget":
                while True:
                    try:
                        budget = float(input("6. What is your project's budget, and how will funds be used? $"))
                        if budget < 0:
                            print("Budget cannot be negative.")
                        else:
                            self.questions[question] = f"${budget:.2f}"
                            break
                    except ValueError:
                        print("Invalid budget. Please enter a valid number.")

    def validate_answers(self):
        for question, answer in self.questions.items():
            if not answer.strip():
                print(f"Please answer question {self.get_question_number(question)}.")
                return False
        return True

    def get_question_number(self, question):
        question_numbers = {
            "project_description": "1",
            "decentralization_impact": "2",
            "team_description": "3",
            "technical_details": "4",
            "timeline": "5",
            "budget": "6",
        }
        return question_numbers[question]

    def save_application(self):
        try:
            with open("application.txt", "w") as file:
                file.write("Sui Foundation Developer Grants Program Application\n\n")
                for question, answer in self.questions.items():
                    if question == "project_description":
                        file.write(f"1. Project Description:\n{answer}\n\n")
                    elif question == "decentralization_impact":
                        file.write(f"2. Decentralization Impact:\n{answer}\n\n")
                    elif question == "team_description":
                        file.write(f"3. Team Description:\n{answer}\n\n")
                    elif question == "technical_details":
                        file.write(f"4. Technical Details:\n{answer}\n\n")
                    elif question == "timeline":
                        file.write(f"5. Timeline:\n{answer}\n\n")
                    elif question == "budget":
                        file.write(f"6. Budget:\n{answer}\n\n")
            print("Application saved to application.txt")
        except Exception as e:
            print(f"Failed to save application: {str(e)}")

def main():
    questionnaire = ApplicationQuestionnaire()
    questionnaire.ask_questions()
    if questionnaire.validate_answers():
        questionnaire.save_application()

if __name__ == "__main__":
    main()
```
