"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Generate Python code for a gamified quiz on the history and evolution of the internet, inspired by the informatics games on "Portal de Saltinho."
Generated: DETERMINISTIC_3f85e9b192661248
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

class QuizGame:
    """
    A gamified quiz on the history and evolution of the internet.
    Inspired by the informatics games on "Portal de Saltinho."
    """
    
    def __init__(self):
        self.questions = [
            {
                "question": "In what year was ARPANET, the precursor to the internet, established?",
                "options": ["1969", "1975", "1982", "1991"],
                "answer": "1969",
                "explanation": "ARPANET was established in 1969 by the U.S. Department of Defense."
            },
            {
                "question": "What was the first message sent over ARPANET?",
                "options": ["Hello World", "LOGIN", "Welcome", "Testing"],
                "answer": "LOGIN",
                "explanation": "The first message was 'LOGIN', but the system crashed after sending 'LO'."
            },
            {
                "question": "Who is considered the 'father of the internet'?",
                "options": ["Bill Gates", "Tim Berners-Lee", "Vint Cerf", "Steve Jobs"],
                "answer": "Vint Cerf",
                "explanation": "Vint Cerf co-designed the TCP/IP protocols and the architecture of the internet."
            },
            {
                "question": "What does HTML stand for?",
                "options": [
                    "Hyper Text Markup Language",
                    "High Tech Modern Language",
                    "Home Tool Markup Language",
                    "Hyperlinks and Text Markup Language"
                ],
                "answer": "Hyper Text Markup Language",
                "explanation": "HTML is the standard markup language for creating web pages."
            },
            {
                "question": "When was the World Wide Web invented?",
                "options": ["1983", "1989", "1993", "1995"],
                "answer": "1989",
                "explanation": "Tim Berners-Lee invented the World Wide Web in 1989 while working at CERN."
            },
            {
                "question": "What was the first web browser called?",
                "options": ["Internet Explorer", "Mosaic", "Netscape", "WorldWideWeb"],
                "answer": "WorldWideWeb",
                "explanation": "The first web browser was called WorldWideWeb, later renamed Nexus."
            },
            {
                "question": "Which protocol is used to transfer web pages on the internet?",
                "options": ["FTP", "HTTP", "SMTP", "TCP"],
                "answer": "HTTP",
                "explanation": "HTTP (Hypertext Transfer Protocol) is used to transfer web pages."
            },
            {
                "question": "What does URL stand for?",
                "options": [
                    "Uniform Resource Locator",
                    "Universal Reference Link",
                    "Unified Resource Link",
                    "Uniform Reference Locator"
                ],
                "answer": "Uniform Resource Locator",
                "explanation": "A URL is the address of a resource on the internet."
            },
            {
                "question": "Which company created the first search engine?",
                "options": ["Google", "Yahoo", "Archie", "AltaVista"],
                "answer": "Archie",
                "explanation": "Archie, created in 1990, was the first search engine."
            },
            {
                "question": "What was the first social media platform?",
                "options": ["Facebook", "MySpace", "Six Degrees", "Friendster"],
                "answer": "Six Degrees",
                "explanation": "Six Degrees, launched in 1997, is considered the first social media platform."
            }
        ]
        self.score = 0
        self.total_questions = len(self.questions)
        self.username = ""
    
    def display_welcome(self):
        """Display welcome message and game instructions."""
        print("\n" + "=" * 50)
        print("Welcome to the Internet History Quiz Game!")
        print("=" * 50)
        print("\nTest your knowledge about the history and evolution of the internet.")
        print(f"There are {self.total_questions} questions. For each correct answer, you earn 1 point.")
        print("Let's see how much you know!\n")
    
    def get_username(self):
        """Prompt user for their username."""
        while True:
            self.username = input("Enter your username: ").strip()
            if self.username:
                return
            print("Username cannot be empty. Please try again.")
    
    def ask_question(self, question_data):
        """Display question and options, then get user's answer."""
        print("\n" + question_data["question"])
        for idx, option in enumerate(question_data["options"], 1):
            print(f"{idx}. {option}")
        
        while True:
            try:
                choice = int(input("Your answer (1-4): "))
                if 1 <= choice <= 4:
                    return question_data["options"][choice - 1]
                print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def check_answer(self, user_answer, correct_answer, explanation):
        """Check if answer is correct and provide feedback."""
        if user_answer.lower() == correct_answer.lower():
            print("\n✅ Correct!")
            self.score += 1
        else:
            print(f"\n❌ Incorrect. The correct answer is: {correct_answer}")
        print(f"Explanation: {explanation}\n")
        time.sleep(1.5)
    
    def calculate_score(self):
        """Calculate and display final score."""
        percentage = (self.score / self.total_questions) * 100
        print("\n" + "=" * 50)
        print("Quiz Complete!")
        print("=" * 50)
        print(f"\n{self.username}, your final score is: {self.score}/{self.total_questions} ({percentage:.1f}%)")
        
        if percentage >= 90:
            print("🏆 Excellent! You're an internet history expert!")
        elif percentage >= 70:
            print("👍 Great job! You know quite a bit about internet history.")
        elif percentage >= 50:
            print("😊 Not bad! You have some knowledge of internet history.")
        else:
            print("📚 Keep learning! The internet has a fascinating history.")
    
    def play_again(self):
        """Ask user if they want to play again."""
        while True:
            choice = input("\nWould you like to play again? (yes/no): ").lower()
            if choice in ("yes", "y"):
                return True
            elif choice in ("no", "n"):
                return False
            print("Please enter 'yes' or 'no'.")
    
    def run(self):
        """Main game loop."""
        while True:
            self.score = 0
            random.shuffle(self.questions)
            
            self.display_welcome()
            self.get_username()
            
            for question in self.questions:
                user_answer = self.ask_question(question)
                self.check_answer(user_answer, question["answer"], question["explanation"])
            
            self.calculate_score()
            
            if not self.play_again():
                print("\nThanks for playing! Goodbye!")
                break

if __name__ == "__main__":
    try:
        game = QuizGame()
        game.run()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)
```
