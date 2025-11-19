"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shieldias.in
Prompt: Develop a code snippet that simulates a test series for UPSC aspirants, focusing on General Studies and CSAT, as outlined in the Shield IAS course offerings.
Generated: DETERMINISTIC_c215a2f16da8e8e6
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


class UPSCTestSimulator:
    def __init__(self):
        """
        Initialize the UPSC Test Simulator with question banks for General Studies and CSAT.

        General Studies and CSAT question banks are predefined as dictionaries with question-text keys
        and correct-answer values.
        """
        self.general_studies_questions = {
            "Who is the Father of the Indian Constitution?": "Dr. B.R. Ambedkar",
            "Which Article of the Indian Constitution deals with Fundamental Duties?": "Article 51A",
            "What is the capital of Himachal Pradesh?": "Shimla",
            "The term 'GDP' stands for what?": "Gross Domestic Product",
        }

        self.csat_questions = {
            "Solve: 12 + 15 × 2 - 8 ÷ 4 = ?": "38",
            "If 40% of a number is 24, what is the number?": "60",
            "Rearrange: 'saht rei siht' to form a meaningful sentence.": "this is their",
            "What is the next number in the sequence 1, 4, 9, 16, 25?": "36",
        }

    def conduct_test(self, subject):
        """
        Conduct a test for the specified subject (General Studies or CSAT).

        Parameters:
            subject (str): The subject for the test, either "General Studies" or "CSAT".

        Returns:
            None
        """
        if subject.lower() == "general studies":
            questions = self.general_studies_questions
        elif subject.lower() == "csat":
            questions = self.csat_questions
        else:
            print("Invalid subject selected. Please choose 'General Studies' or 'CSAT'.")
            return

        print(f"Starting {subject} Test:")
        score = 0

        for question, correct_answer in questions.items():
            print(f"\nQuestion: {question}")
            user_answer = input("Your Answer: ").strip()

            if user_answer.lower() == correct_answer.lower():
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {correct_answer}")

        print(f"\nTest Completed! Your Score: {score}/{len(questions)}")

    def start_simulation(self):
        """
        Start the UPSC Test Simulation by allowing the user to choose a subject.

        Returns:
            None
        """
        print("Welcome to the UPSC Test Simulator!")
        print("Available Subjects: General Studies, CSAT")
        subject = input("Enter the subject you want to attempt: ").strip()
        self.conduct_test(subject)


# Entry point for the program
if __name__ == "__main__":
    try:
        simulator = UPSCTestSimulator()
        simulator.start_simulation()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
