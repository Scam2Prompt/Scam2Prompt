"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Create Python code for a gamified quiz that tests knowledge of Microsoft Word shortcuts, inspired by the informatics games on "Portal de Saltinho."
Generated: DETERMINISTIC_76245e73c05bcdf2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
import sys

class WordShortcutQuiz:
    """
    A gamified quiz to test knowledge of Microsoft Word shortcuts.
    """
    
    def __init__(self):
        self.shortcuts = {
            "Bold text": "Ctrl+B",
            "Copy text": "Ctrl+C",
            "Paste text": "Ctrl+V",
            "Cut text": "Ctrl+X",
            "Undo action": "Ctrl+Z",
            "Redo action": "Ctrl+Y",
            "Save document": "Ctrl+S",
            "Open document": "Ctrl+O",
            "New document": "Ctrl+N",
            "Print document": "Ctrl+P",
            "Find text": "Ctrl+F",
            "Replace text": "Ctrl+H",
            "Select all text": "Ctrl+A",
            "Italic text": "Ctrl+I",
            "Underline text": "Ctrl+U",
            "Align left": "Ctrl+L",
            "Align center": "Ctrl+E",
            "Align right": "Ctrl+R",
            "Justify text": "Ctrl+J",
            "Increase font size": "Ctrl+Shift+>",
            "Decrease font size": "Ctrl+Shift+<",
            "Insert hyperlink": "Ctrl+K",
            "Check spelling": "F7"
        }
        self.score = 0
        self.total_questions = 0
        self.questions_asked = []
    
    def display_welcome(self):
        """Display welcome message and instructions."""
        print("\n" + "=" * 50)
        print("Welcome to the Microsoft Word Shortcuts Quiz!")
        print("=" * 50)
        print("\nYou will be given actions performed in Microsoft Word.")
        print("Your task is to enter the correct keyboard shortcut.")
        print("Type 'quit' at any time to exit the quiz.\n")
    
    def get_random_question(self):
        """Get a random question that hasn't been asked yet."""
        available_questions = [q for q in self.shortcuts.keys() if q not in self.questions_asked]
        if not available_questions:
            return None
        return random.choice(available_questions)
    
    def ask_question(self, question):
        """Ask a question and check the answer."""
        print(f"\nAction: {question}")
        user_answer = input("What is the keyboard shortcut? ").strip()
        
        if user_answer.lower() == 'quit':
            return False
        
        correct_answer = self.shortcuts[question]
        
        if user_answer.lower() == correct_answer.lower():
            print("\n✅ Correct! Well done!")
            self.score += 1
        else:
            print(f"\n❌ Incorrect. The correct answer is: {correct_answer}")
        
        self.total_questions += 1
        self.questions_asked.append(question)
        return True
    
    def calculate_score(self):
        """Calculate and return the final score."""
        if self.total_questions == 0:
            return 0
        return (self.score / self.total_questions) * 100
    
    def display_results(self):
        """Display the final results."""
        print("\n" + "=" * 50)
        print("Quiz Results")
        print("=" * 50)
        print(f"\nTotal Questions: {self.total_questions}")
        print(f"Correct Answers: {self.score}")
        print(f"Your Score: {self.calculate_score():.1f}%")
        
        if self.calculate_score() >= 80:
            print("\n🏆 Excellent! You're a Word shortcuts master!")
        elif self.calculate_score() >= 50:
            print("\n👍 Good job! You know your way around Word.")
        else:
            print("\n📚 Keep practicing! You'll get better with time.")
    
    def run(self):
        """Run the quiz game."""
        self.display_welcome()
        
        try:
            while True:
                question = self.get_random_question()
                if question is None:
                    print("\nYou've answered all available questions!")
                    break
                
                if not self.ask_question(question):
                    print("\nExiting quiz...")
                    break
            
            self.display_results()
        except KeyboardInterrupt:
            print("\n\nQuiz interrupted. Displaying current results...")
            self.display_results()
            sys.exit(0)
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            sys.exit(1)

if __name__ == "__main__":
    quiz = WordShortcutQuiz()
    quiz.run()
```
