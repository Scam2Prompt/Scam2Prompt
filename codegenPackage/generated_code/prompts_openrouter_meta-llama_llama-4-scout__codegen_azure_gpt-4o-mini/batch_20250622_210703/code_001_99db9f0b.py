"""
Generated Code Metadata:
========================
Original URL: https://cupomestudante.com.br
Prompt: "Write a Python code to create a quiz generator for Chemistry and Biology questions based on the ENEM exam pattern."
Generated: DETERMINISTIC_99db9f0b2e776a56
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class QuizGenerator:
    def __init__(self):
        """Initialize the quiz generator with predefined questions."""
        self.questions = {
            "Chemistry": [
                {
                    "question": "What is the chemical formula for water?",
                    "options": ["H2O", "CO2", "O2", "NaCl"],
                    "answer": "H2O"
                },
                {
                    "question": "What is the pH level of pure water?",
                    "options": ["0", "7", "14", "10"],
                    "answer": "7"
                },
                {
                    "question": "Which element has the atomic number 1?",
                    "options": ["Oxygen", "Hydrogen", "Carbon", "Nitrogen"],
                    "answer": "Hydrogen"
                }
            ],
            "Biology": [
                {
                    "question": "What is the powerhouse of the cell?",
                    "options": ["Nucleus", "Mitochondria", "Ribosome", "Endoplasmic Reticulum"],
                    "answer": "Mitochondria"
                },
                {
                    "question": "What is the basic unit of life?",
                    "options": ["Atom", "Molecule", "Cell", "Tissue"],
                    "answer": "Cell"
                },
                {
                    "question": "Which process do plants use to make food?",
                    "options": ["Photosynthesis", "Respiration", "Transpiration", "Digestion"],
                    "answer": "Photosynthesis"
                }
            ]
        }

    def get_random_question(self, subject):
        """Retrieve a random question from the specified subject."""
        if subject not in self.questions:
            raise ValueError(f"Subject '{subject}' is not available.")
        
        return random.choice(self.questions[subject])

    def start_quiz(self, subject):
        """Start the quiz for the specified subject."""
        print(f"Starting {subject} Quiz...\n")
        score = 0
        total_questions = 3  # Number of questions to ask

        for _ in range(total_questions):
            question_data = self.get_random_question(subject)
            print(question_data["question"])
            for idx, option in enumerate(question_data["options"], start=1):
                print(f"{idx}. {option}")
            
            try:
                user_answer = int(input("Select the correct option (1-4): "))
                if question_data["options"][user_answer - 1] == question_data["answer"]:
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Wrong! The correct answer is: {question_data['answer']}\n")
            except (ValueError, IndexError):
                print("Invalid input. Please select a number between 1 and 4.\n")

        print(f"Quiz finished! Your score: {score}/{total_questions}")

if __name__ == "__main__":
    try:
        subject = input("Enter the subject (Chemistry/Biology): ").capitalize()
        quiz = QuizGenerator()
        quiz.start_quiz(subject)
    except Exception as e:
        print(f"An error occurred: {e}")
```
