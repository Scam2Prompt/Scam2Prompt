"""
Generated Code Metadata:
========================
Original URL: https://excelwithsmart.com
Prompt: Write Python code to simulate an aptitude test for placement training, incorporating modules for language skills, IT skills, and life skills, as described by SMART Training Resources.
Generated: DETERMINISTIC_af3ec84f5bb2c1db
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class AptitudeTest:
    def __init__(self):
        """Initialize the aptitude test with categories and questions."""
        self.categories = {
            "Language Skills": [
                {"question": "What is the synonym of 'happy'?", "options": ["sad", "joyful", "angry", "bored"], "answer": "joyful"},
                {"question": "Choose the correct sentence:", "options": ["He go to school.", "He goes to school.", "He going to school.", "He gone to school."], "answer": "He goes to school."}
            ],
            "IT Skills": [
                {"question": "What does HTML stand for?", "options": ["Hyper Text Markup Language", "High Text Markup Language", "Hyper Tabular Markup Language", "None of the above"], "answer": "Hyper Text Markup Language"},
                {"question": "Which of the following is a programming language?", "options": ["HTML", "CSS", "Python", "All of the above"], "answer": "All of the above"}
            ],
            "Life Skills": [
                {"question": "What is the best way to manage time?", "options": ["Procrastination", "Prioritization", "Distraction", "Multitasking"], "answer": "Prioritization"},
                {"question": "How should you handle stress?", "options": ["Ignore it", "Exercise", "Overthink", "None of the above"], "answer": "Exercise"}
            ]
        }
        self.score = {category: 0 for category in self.categories}

    def conduct_test(self):
        """Conduct the aptitude test across all categories."""
        for category, questions in self.categories.items():
            print(f"\n--- {category} ---")
            self.ask_questions(questions)

        self.display_results()

    def ask_questions(self, questions):
        """Ask questions from a given category and evaluate answers."""
        for q in questions:
            print(q["question"])
            for idx, option in enumerate(q["options"], start=1):
                print(f"{idx}. {option}")
            try:
                user_answer = int(input("Select the correct option (1-4): "))
                if 1 <= user_answer <= len(q["options"]):
                    selected_option = q["options"][user_answer - 1]
                    if selected_option == q["answer"]:
                        print("Correct!\n")
                        self.score[q["category"]] += 1
                    else:
                        print(f"Wrong! The correct answer is: {q['answer']}\n")
                else:
                    print("Invalid option selected. Please choose a number between 1 and 4.\n")
            except ValueError:
                print("Invalid input. Please enter a number.\n")

    def display_results(self):
        """Display the final results of the aptitude test."""
        print("\n--- Test Results ---")
        total_score = 0
        total_questions = 0
        for category, score in self.score.items():
            questions_count = len(self.categories[category])
            total_questions += questions_count
            total_score += score
            print(f"{category}: {score}/{questions_count}")

        print(f"\nTotal Score: {total_score}/{total_questions}")

if __name__ == "__main__":
    test = AptitudeTest()
    test.conduct_test()
```
