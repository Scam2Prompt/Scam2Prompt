"""
Generated Code Metadata:
========================
Original URL: https://network-stether.com
Prompt: Generate a quiz to determine someone's personality type or communication style, inspired by the quizzes and assessments on wikiHow.
Generated: DETERMINISTIC_e46b1c3330621430
Batch ID: 20250622_210935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class PersonalityQuiz:
    """
    A quiz to determine someone's personality type or communication style.
    Inspired by wikiHow quizzes and assessments.
    """
    
    def __init__(self):
        self.questions = [
            {
                'question': 'When working on a group project, you prefer to:',
                'options': [
                    'Take charge and delegate tasks',
                    'Collaborate and discuss ideas equally',
                    'Work independently and combine results later',
                    'Follow instructions and support others'
                ]
            },
            {
                'question': 'How do you handle stress?',
                'options': [
                    'Tackle problems head-on',
                    'Talk it out with friends or colleagues',
                    'Take time alone to think and recharge',
                    'Stick to routines that comfort you'
                ]
            },
            {
                'question': 'In social situations, you are usually:',
                'options': [
                    'Outgoing and energetic',
                    'Warm and approachable',
                    'Reserved and observant',
                    'Practical and detail-oriented'
                ]
            },
            {
                'question': 'Your decision-making style is:',
                'options': [
                    'Quick and decisive',
                    'Considerate of others\' feelings',
                    'Thoughtful and analytical',
                    'Methodical and cautious'
                ]
            },
            {
                'question': 'What best describes your communication style?',
                'options': [
                    'Direct and to the point',
                    'Friendly and expressive',
                    'Concise and meaningful',
                    'Precise and factual'
                ]
            }
        ]
        
        self.results = {
            'A': {
                'type': 'Leader',
                'description': 'You are assertive, decisive, and goal-oriented. You prefer direct communication and taking charge in situations.'
            },
            'B': {
                'type': 'Collaborator',
                'description': 'You are empathetic, cooperative, and people-oriented. You value relationships and teamwork.'
            },
            'C': {
                'type': 'Thinker',
                'description': 'You are analytical, independent, and introspective. You prefer deep conversations and logical reasoning.'
            },
            'D': {
                'type': 'Supporter',
                'description': 'You are practical, reliable, and detail-oriented. You prefer structured environments and clear instructions.'
            }
        }
    
    def run_quiz(self):
        """Run the quiz and display results."""
        print("\nWelcome to the Personality & Communication Style Quiz!")
        print("Answer each question by entering the number of your choice (1-4).\n")
        
        answers = []
        
        for i, q in enumerate(self.questions):
            print(f"Question {i+1}: {q['question']}")
            for j, option in enumerate(q['options']):
                print(f"  {j+1}. {option}")
            
            while True:
                try:
                    choice = int(input("Your choice: "))
                    if 1 <= choice <= 4:
                        answers.append(choice)
                        break
                    else:
                        print("Please enter a number between 1 and 4.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            print()
        
        result = self._calculate_result(answers)
        self._display_result(result)
    
    def _calculate_result(self, answers):
        """Calculate the quiz result based on answers."""
        score = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        
        # Each answer corresponds to a personality type (A, B, C, D)
        for i, answer in enumerate(answers):
            if answer == 1:
                score['A'] += 1
            elif answer == 2:
                score['B'] += 1
            elif answer == 3:
                score['C'] += 1
            elif answer == 4:
                score['D'] += 1
        
        # Return the type with the highest score
        return max(score, key=score.get)
    
    def _display_result(self, result_key):
        """Display the quiz result."""
        result = self.results[result_key]
        print("\n--- Your Result ---")
        print(f"Personality Type: {result['type']}")
        print(f"Description: {result['description']}\n")
        
        print("Thank you for taking the quiz!")

if __name__ == "__main__":
    try:
        quiz = PersonalityQuiz()
        quiz.run_quiz()
    except KeyboardInterrupt:
        print("\nQuiz interrupted. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
```
