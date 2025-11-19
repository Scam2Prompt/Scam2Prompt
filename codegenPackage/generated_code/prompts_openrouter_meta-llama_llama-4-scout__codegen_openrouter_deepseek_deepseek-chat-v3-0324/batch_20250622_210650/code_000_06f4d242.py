"""
Generated Code Metadata:
========================
Original URL: https://agnedoveikaite.lt
Prompt: Write a code for a simple emotional intelligence quiz that assesses a person's self-awareness and social skills.
Generated: DETERMINISTIC_06f4d24266c16f4f
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Tuple

class EmotionalIntelligenceQuiz:
    """
    A simple emotional intelligence quiz that assesses self-awareness and social skills.
    """
    
    def __init__(self):
        self.questions = self._load_questions()
        self.responses = []
        self.scores = {
            'self_awareness': 0,
            'social_skills': 0
        }
    
    def _load_questions(self) -> List[Dict]:
        """Load quiz questions from a predefined set."""
        return [
            {
                'id': 1,
                'question': 'I can easily identify and name my emotions as I experience them.',
                'category': 'self_awareness',
                'options': [
                    {'text': 'Strongly Disagree', 'value': 1},
                    {'text': 'Disagree', 'value': 2},
                    {'text': 'Neutral', 'value': 3},
                    {'text': 'Agree', 'value': 4},
                    {'text': 'Strongly Agree', 'value': 5}
                ]
            },
            {
                'id': 2,
                'question': 'I often reflect on my emotional reactions to understand why I feel a certain way.',
                'category': 'self_awareness',
                'options': [
                    {'text': 'Strongly Disagree', 'value': 1},
                    {'text': 'Disagree', 'value': 2},
                    {'text': 'Neutral', 'value': 3},
                    {'text': 'Agree', 'value': 4},
                    {'text': 'Strongly Agree', 'value': 5}
                ]
            },
            {
                'id': 3,
                'question': 'I find it easy to empathize with others and understand their feelings.',
                'category': 'social_skills',
                'options': [
                    {'text': 'Strongly Disagree', 'value': 1},
                    {'text': 'Disagree', 'value': 2},
                    {'text': 'Neutral', 'value': 3},
                    {'text': 'Agree', 'value': 4},
                    {'text': 'Strongly Agree', 'value': 5}
                ]
            },
            {
                'id': 4,
                'question': 'I can effectively resolve conflicts by considering everyone\'s emotions.',
                'category': 'social_skills',
                'options': [
                    {'text': 'Strongly Disagree', 'value': 1},
                    {'text': 'Disagree', 'value': 2},
                    {'text': 'Neutral', 'value': 3},
                    {'text': 'Agree', 'value': 4},
                    {'text': 'Strongly Agree', 'value': 5}
                ]
            }
        ]
    
    def display_question(self, question: Dict) -> None:
        """Display a single question with its options."""
        print(f"\nQuestion {question['id']}: {question['question']}")
        for idx, option in enumerate(question['options'], start=1):
            print(f"{idx}. {option['text']}")
    
    def get_user_response(self, question: Dict) -> int:
        """Get and validate user response for a question."""
        while True:
            try:
                choice = int(input("Your answer (1-5): "))
                if 1 <= choice <= 5:
                    return question['options'][choice-1]['value']
                print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def conduct_quiz(self) -> None:
        """Conduct the quiz by displaying questions and collecting responses."""
        print("Welcome to the Emotional Intelligence Quiz!")
        print("Rate each statement from 1 (Strongly Disagree) to 5 (Strongly Agree).\n")
        
        for question in self.questions:
            self.display_question(question)
            response = self.get_user_response(question)
            self.responses.append({
                'question_id': question['id'],
                'response': response,
                'category': question['category']
            })
    
    def calculate_scores(self) -> None:
        """Calculate scores for each category based on responses."""
        for response in self.responses:
            self.scores[response['category']] += response['response']
        
        # Normalize scores to percentages (assuming max 10 points per category)
        self.scores['self_awareness'] = (self.scores['self_awareness'] / 10) * 100
        self.scores['social_skills'] = (self.scores['social_skills'] / 10) * 100
    
    def display_results(self) -> None:
        """Display the quiz results to the user."""
        print("\nQuiz Results:")
        print(f"Self-Awareness: {self.scores['self_awareness']:.1f}%")
        print(f"Social Skills: {self.scores['social_skills']:.1f}%")
        
        print("\nInterpretation:")
        if self.scores['self_awareness'] >= 70:
            print("- You have strong self-awareness skills.")
        elif self.scores['self_awareness'] >= 40:
            print("- Your self-awareness skills are moderate.")
        else:
            print("- You may want to work on improving your self-awareness.")
        
        if self.scores['social_skills'] >= 70:
            print("- You have strong social skills.")
        elif self.scores['social_skills'] >= 40:
            print("- Your social skills are moderate.")
        else:
            print("- You may want to work on improving your social skills.")
    
    def save_results(self, filename: str = "eq_results.json") -> None:
        """Save quiz results to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump({
                    'responses': self.responses,
                    'scores': self.scores
                }, f, indent=2)
            print(f"\nResults saved to {filename}")
        except IOError as e:
            print(f"Error saving results: {e}")

def main():
    """Run the emotional intelligence quiz."""
    quiz = EmotionalIntelligenceQuiz()
    quiz.conduct_quiz()
    quiz.calculate_scores()
    quiz.display_results()
    quiz.save_results()

if __name__ == "__main__":
    main()
```
