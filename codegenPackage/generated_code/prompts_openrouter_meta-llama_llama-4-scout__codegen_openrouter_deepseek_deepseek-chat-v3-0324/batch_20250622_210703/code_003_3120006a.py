"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: "Create a quiz on workplace safety regulations, specifically NR-10 and NR-34, for a course on electrical safety in industrial settings."
Generated: DETERMINISTIC_3120006a3f85109e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random

class WorkplaceSafetyQuiz:
    """
    A quiz application for workplace safety regulations NR-10 and NR-34.
    """
    
    def __init__(self):
        self.questions = self._load_questions()
        self.score = 0
        self.total_questions = len(self.questions)
    
    def _load_questions(self):
        """
        Load questions from a JSON file or return default questions if file not found.
        """
        try:
            with open('safety_questions.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return self._get_default_questions()
    
    def _get_default_questions(self):
        """
        Return default set of questions if JSON file is not available.
        """
        return [
            {
                "question": "What is the main purpose of NR-10?",
                "options": [
                    "Regulate electrical installations",
                    "Standardize workplace uniforms",
                    "Control chemical exposure",
                    "Manage ergonomic risks"
                ],
                "answer": 0,
                "regulation": "NR-10"
            },
            {
                "question": "According to NR-10, what is required before working on energized electrical systems?",
                "options": [
                    "Approval from HR",
                    "Proper training and authorization",
                    "Just a basic understanding",
                    "No specific requirements"
                ],
                "answer": 1,
                "regulation": "NR-10"
            },
            {
                "question": "What does NR-34 regulate?",
                "options": [
                    "Electrical safety in construction",
                    "Safety in shipbuilding and repair",
                    "Office ergonomics",
                    "Chemical handling procedures"
                ],
                "answer": 1,
                "regulation": "NR-34"
            },
            {
                "question": "Under NR-34, what must be done before hot work begins?",
                "options": [
                    "Inform the supervisor",
                    "Conduct a risk assessment",
                    "Wear proper PPE",
                    "All of the above"
                ],
                "answer": 3,
                "regulation": "NR-34"
            },
            {
                "question": "What is the minimum required training duration for NR-10 according to Brazilian regulations?",
                "options": [
                    "20 hours",
                    "40 hours",
                    "60 hours",
                    "80 hours"
                ],
                "answer": 1,
                "regulation": "NR-10"
            }
        ]
    
    def _display_question(self, question_data):
        """
        Display a single question and its options.
        """
        print(f"\nRegulation: {question_data['regulation']}")
        print(f"Question: {question_data['question']}")
        for i, option in enumerate(question_data['options']):
            print(f"{i}. {option}")
    
    def _get_user_answer(self, options_count):
        """
        Get and validate user's answer.
        """
        while True:
            try:
                answer = int(input("\nEnter your answer (0-3): "))
                if 0 <= answer < options_count:
                    return answer
                print(f"Please enter a number between 0 and {options_count-1}")
            except ValueError:
                print("Please enter a valid number.")
    
    def run_quiz(self):
        """
        Run the quiz by displaying questions and evaluating answers.
        """
        print("Workplace Safety Regulations Quiz (NR-10 and NR-34)")
        print(f"Total questions: {self.total_questions}\n")
        
        random.shuffle(self.questions)
        
        for question in self.questions:
            self._display_question(question)
            user_answer = self._get_user_answer(len(question['options']))
            
            if user_answer == question['answer']:
                print("Correct!")
                self.score += 1
            else:
                print(f"Incorrect. The correct answer is: {question['options'][question['answer']]}")
        
        self._display_results()
    
    def _display_results(self):
        """
        Display the final quiz results.
        """
        percentage = (self.score / self.total_questions) * 100
        print("\nQuiz Results:")
        print(f"Correct answers: {self.score}/{self.total_questions}")
        print(f"Score: {percentage:.2f}%")
        
        if percentage >= 80:
            print("Excellent! You have a strong understanding of NR-10 and NR-34.")
        elif percentage >= 60:
            print("Good job! You understand the basics of NR-10 and NR-34.")
        else:
            print("Consider reviewing NR-10 and NR-34 materials to improve your knowledge.")

if __name__ == "__main__":
    quiz = WorkplaceSafetyQuiz()
    quiz.run_quiz()
```
