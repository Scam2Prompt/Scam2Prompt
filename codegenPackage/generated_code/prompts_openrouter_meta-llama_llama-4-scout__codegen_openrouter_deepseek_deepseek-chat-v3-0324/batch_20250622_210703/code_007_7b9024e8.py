"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: "Write a code snippet to implement a simulated exam feature for ENEM preparation, similar to the ones offered by Maratona do ENEM, using a programming language of your choice."
Generated: DETERMINISTIC_7b9024e82cdd22c4
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
import json
import time
from typing import List, Dict, Optional

class Question:
    def __init__(self, id: int, text: str, options: List[str], correct_answer: int, subject: str):
        self.id = id
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
        self.subject = subject

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'text': self.text,
            'options': self.options,
            'correct_answer': self.correct_answer,
            'subject': self.subject
        }

class ExamSimulator:
    def __init__(self):
        self.questions: List[Question] = []
        self.load_questions()
        self.user_answers: Dict[int, int] = {}
        self.start_time: Optional[float] = None
        self.end_time: Optional[float] = None

    def load_questions(self) -> None:
        """Load questions from a JSON file or create sample questions if file doesn't exist"""
        try:
            with open('enem_questions.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.questions = [Question(**q) for q in data]
        except FileNotFoundError:
            self._create_sample_questions()
            self._save_questions_to_file()

    def _create_sample_questions(self) -> None:
        """Create sample questions for demonstration purposes"""
        subjects = ['Math', 'Portuguese', 'History', 'Geography', 'Biology']
        for i in range(1, 21):
            subject = random.choice(subjects)
            self.questions.append(
                Question(
                    id=i,
                    text=f"Sample question {i} about {subject}",
                    options=[f"Option {j}" for j in range(1, 5)],
                    correct_answer=random.randint(0, 3),
                    subject=subject
                )
            )

    def _save_questions_to_file(self) -> None:
        """Save questions to a JSON file"""
        with open('enem_questions.json', 'w', encoding='utf-8') as f:
            json.dump([q.to_dict() for q in self.questions], f, indent=2, ensure_ascii=False)

    def start_exam(self) -> None:
        """Start the exam timer"""
        self.start_time = time.time()
        print("ENEM Simulator started. Good luck!\n")

    def display_question(self, question: Question) -> None:
        """Display a question to the user"""
        print(f"\nQuestion {question.id} ({question.subject}):")
        print(question.text)
        for i, option in enumerate(question.options):
            print(f"{i + 1}. {option}")

    def record_answer(self, question_id: int, answer: int) -> None:
        """Record user's answer"""
        if answer < 1 or answer > 4:
            raise ValueError("Answer must be between 1 and 4")
        self.user_answers[question_id] = answer - 1  # Convert to 0-based index

    def end_exam(self) -> Dict[str, float]:
        """End the exam and calculate results"""
        if not self.start_time:
            raise RuntimeError("Exam hasn't been started")
            
        self.end_time = time.time()
        duration = self.end_time - self.start_time
        
        score = self.calculate_score()
        return {
            'score': score,
            'duration': duration,
            'correct_answers': score,
            'total_questions': len(self.questions)
        }

    def calculate_score(self) -> int:
        """Calculate the user's score"""
        correct = 0
        for question in self.questions:
            if question.id in self.user_answers and self.user_answers[question.id] == question.correct_answer:
                correct += 1
        return correct

    def run_interactive_exam(self) -> None:
        """Run the exam in interactive mode"""
        self.start_exam()
        
        for question in self.questions:
            self.display_question(question)
            while True:
                try:
                    answer = int(input("Your answer (1-4): "))
                    self.record_answer(question.id, answer)
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}. Please enter a number between 1 and 4.")
        
        results = self.end_exam()
        print("\nExam completed!")
        print(f"Your score: {results['correct_answers']}/{results['total_questions']}")
        print(f"Time taken: {results['duration']:.2f} seconds")

if __name__ == "__main__":
    simulator = ExamSimulator()
    simulator.run_interactive_exam()
```
