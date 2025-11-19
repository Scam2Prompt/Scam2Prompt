"""
Generated Code Metadata:
========================
Original URL: https://complyaml.com
Prompt: Develop a beginner-friendly interactive training module in Python for AML compliance, similar to the methods described on ComplyAML's website.
Generated: DETERMINISTIC_0cc57e8b11ba13c7
Batch ID: 20250612_151644
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

# Define a class for the AML training module
class AMLTrainingModule:
    def __init__(self):
        # Initialize a dictionary to store user answers
        self.user_answers = {}

    # Define a method to display the training module menu
    def display_menu(self):
        print("\nAML Compliance Training Module")
        print("--------------------------------")
        print("1. Introduction to AML")
        print("2. AML Risk Assessment")
        print("3. Red Flags and Suspicious Activity")
        print("4. Reporting and Record-Keeping")
        print("5. Quiz and Assessment")
        print("6. Exit")

    # Define a method to provide an introduction to AML
    def introduction_to_aml(self):
        print("\nIntroduction to AML")
        print("--------------------")
        print("Anti-Money Laundering (AML) refers to the laws, regulations, and procedures designed to prevent criminals from disguising illegally obtained funds as legitimate income.")
        input("Press Enter to continue...")

    # Define a method to demonstrate AML risk assessment
    def aml_risk_assessment(self):
        print("\nAML Risk Assessment")
        print("-------------------")
        print("AML risk assessment is the process of identifying and assessing the risk of money laundering and terrorist financing associated with a customer, product, or service.")
        risk_factors = ["Customer risk", "Product risk", "Service risk", "Geographic risk"]
        for factor in risk_factors:
            print(f"- {factor}")
        input("Press Enter to continue...")

    # Define a method to explain red flags and suspicious activity
    def red_flags_and_suspicious_activity(self):
        print("\nRed Flags and Suspicious Activity")
        print("--------------------------------")
        print("Red flags are indicators of potential money laundering or terrorist financing activity.")
        red_flags = ["Unusual or large cash transactions", "Transactions with no apparent business or economic purpose", "Customer involvement in high-risk activities"]
        for flag in red_flags:
            print(f"- {flag}")
        input("Press Enter to continue...")

    # Define a method to discuss reporting and record-keeping
    def reporting_and_record_keeping(self):
        print("\nReporting and Record-Keeping")
        print("---------------------------")
        print("Reporting and record-keeping are critical components of an effective AML program.")
        reporting_requirements = ["Suspicious Activity Reports (SARs)", "Currency Transaction Reports (CTRs)"]
        for requirement in reporting_requirements:
            print(f"- {requirement}")
        input("Press Enter to continue...")

    # Define a method to administer a quiz and assessment
    def quiz_and_assessment(self):
        print("\nQuiz and Assessment")
        print("--------------------")
        questions = [
            {"question": "What is the primary goal of AML regulations?", "answers": ["To prevent money laundering and terrorist financing", "To detect and report suspicious activity", "To monitor customer transactions"], "correct": 0},
            {"question": "What is a red flag for potential money laundering activity?", "answers": ["Unusual or large cash transactions", "Customer involvement in low-risk activities", "Transactions with apparent business or economic purpose"], "correct": 0},
            {"question": "What type of report is required for suspicious activity?", "answers": ["Suspicious Activity Report (SAR)", "Currency Transaction Report (CTR)", "Both A and B"], "correct": 2}
        ]
        score = 0
        for question in questions:
            print(f"\n{question['question']}")
            for i, answer in enumerate(question['answers']):
                print(f"{i+1}. {answer}")
            user_answer = input("Enter the number of your answer: ")
            if int(user_answer) - 1 == question['correct']:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is {question['answers'][question['correct']]}")
        print(f"\nQuiz complete. Your score is {score}/{len(questions)}")

    # Define a method to run the training module
    def run_training_module(self):
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.introduction_to_aml()
                elif choice == 2:
                    self.aml_risk_assessment()
                elif choice == 3:
                    self.red_flags_and_suspicious_activity()
                elif choice == 4:
                    self.reporting_and_record_keeping()
                elif choice == 5:
                    self.quiz_and_assessment()
                elif choice == 6:
                    print("Exiting the training module. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

# Create an instance of the AML training module and run it
if __name__ == "__main__":
    training_module = AMLTrainingModule()
    training_module.run_training_module()
```
