"""
Generated Code Metadata:
========================
Original URL: https://complyaml.com
Prompt: Generate a code snippet for an interactive training module that helps staff understand AML (FIC) obligations.
Generated: DETERMINISTIC_ed049d527735fdca
Batch ID: 20250612_135717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import random

class AMLTrainingModule:
    def __init__(self):
        self.aml_scenarios = {
            "customer_due_diligence": {
                "question": "What is the primary purpose of Customer Due Diligence (CDD) in AML?",
                "answers": [
                    {"text": "To verify customer's identity", "correct": True},
                    {"text": "To monitor customer's transactions", "correct": False},
                    {"text": "To report suspicious activities", "correct": False},
                    {"text": "To freeze customer's assets", "correct": False}
                ]
            },
            "suspicious_activity_reporting": {
                "question": "What should you do if you suspect a transaction is related to money laundering?",
                "answers": [
                    {"text": "Report it to the Financial Intelligence Unit (FIU)", "correct": True},
                    {"text": "Ignore it and continue with your work", "correct": False},
                    {"text": "Discuss it with your colleagues", "correct": False},
                    {"text": "Report it to the police", "correct": False}
                ]
            },
            "aml_policy": {
                "question": "What is the purpose of an AML policy in an organization?",
                "answers": [
                    {"text": "To outline procedures for detecting and reporting suspicious activities", "correct": True},
                    {"text": "To promote a culture of compliance", "correct": False},
                    {"text": "To train employees on AML regulations", "correct": False},
                    {"text": "To monitor employee performance", "correct": False}
                ]
            }
        }

    def run_training_module(self):
        score = 0
        for scenario, details in self.aml_scenarios.items():
            print(f"\nScenario: {scenario.replace('_', ' ').title()}")
            print(details["question"])
            for i, answer in enumerate(details["answers"]):
                print(f"{i+1}. {answer['text']}")
            try:
                user_answer = int(input("Choose the correct answer (enter the number): ")) - 1
                if user_answer >= 0 and user_answer < len(details["answers"]):
                    if details["answers"][user_answer]["correct"]:
                        print("Correct!")
                        score += 1
                    else:
                        print(f"Incorrect. The correct answer is {details['answers'][0]['text'] if details['answers'][0]['correct'] else details['answers'][1]['text']}")
                else:
                    print("Invalid choice. Please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        print(f"\nTraining completed. Your final score is {score}/{len(self.aml_scenarios)}")

if __name__ == "__main__":
    try:
        training_module = AMLTrainingModule()
        training_module.run_training_module()
    except Exception as e:
        print(f"An error occurred: {e}")
```
