"""
Generated Code Metadata:
========================
Original URL: https://simons-17h.pages.dev
Prompt: Write a Python script to create a simple quiz that determines which Simon's Cat character a user is, based on a series of easy questions.
Generated: DETERMINISTIC_8b5d5104bc0f8588
Batch ID: 20250622_211721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class Quiz:
    """
    A simple quiz to determine which Simon's Cat character the user is.
    The quiz asks a series of questions and calculates the result based on answers.
    """
    
    def __init__(self):
        """Initialize the quiz with questions and possible results."""
        self.questions = [
            {
                'question': 'What best describes your energy level?',
                'options': {
                    'A': 'High - I\'m always on the go!',
                    'B': 'Medium - I like a mix of activity and relaxation',
                    'C': 'Low - I prefer lounging around'
                }
            },
            {
                'question': 'How do you handle surprises?',
                'options': {
                    'A': 'I love them! The more unexpected, the better.',
                    'B': 'I can adapt, but prefer things planned.',
                    'C': 'I dislike surprises; routine is best.'
                }
            },
            {
                'question': 'What\'s your favorite snack?',
                'options': {
                    'A': 'Anything edible! I\'m not picky.',
                    'B': 'I have favorites but will try new things.',
                    'C': 'Only the finest treats for me.'
                }
            },
            {
                'question': 'How do you react to strangers?',
                'options': {
                    'A': 'Excited! New friends!',
                    'B': 'Cautious but friendly.',
                    'C': 'Suspicious or indifferent.'
                }
            }
        ]
        
        self.results = {
            'Simon\'s Cat': 'You are Simon\'s Cat! Playful, curious, and always up to mischief.',
            'Maisy': 'You are Maisy! Sweet, gentle, and a little shy.',
            'Jazz': 'You are Jazz! Elegant, sophisticated, and a bit aloof.'
        }

    def run_quiz(self):
        """Run the quiz, ask questions, and display the result."""
        print("Welcome to the Simon's Cat Character Quiz!")
        print("Answer the following questions to find out which character you are.\n")
        
        answers = []
        
        try:
            for question in self.questions:
                print(question['question'])
                for option, text in question['options'].items():
                    print(f"{option}: {text}")
                
                while True:
                    answer = input("Your answer (A/B/C): ").upper()
                    if answer in ['A', 'B', 'C']:
                        answers.append(answer)
                        break
                    else:
                        print("Invalid input. Please enter A, B, or C.")
                print()
            
            result = self._calculate_result(answers)
            print("\nYour result:")
            print(self.results[result])
        
        except KeyboardInterrupt:
            print("\n\nQuiz interrupted. Exiting...")
            sys.exit(1)
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            sys.exit(1)

    def _calculate_result(self, answers):
        """
        Calculate the result based on answers.
        
        Args:
            answers (list): List of user's answers (A, B, or C).
        
        Returns:
            str: The character result.
        """
        # Count occurrences of each answer
        a_count = answers.count('A')
        b_count = answers.count('B')
        c_count = answers.count('C')
        
        if a_count > b_count and a_count > c_count:
            return 'Simon\'s Cat'
        elif b_count > a_count and b_count > c_count:
            return 'Maisy'
        elif c_count > a_count and c_count > b_count:
            return 'Jazz'
        else:
            # Default result in case of a tie
            return 'Simon\'s Cat'

if __name__ == "__main__":
    quiz = Quiz()
    quiz.run_quiz()
```
