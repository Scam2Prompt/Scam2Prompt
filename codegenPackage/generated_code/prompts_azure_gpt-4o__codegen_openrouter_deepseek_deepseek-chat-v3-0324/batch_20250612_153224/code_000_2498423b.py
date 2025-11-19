"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: Write Python code to simulate an interactive educational game that teaches children aged 4 to 9 the value of respect, as described in the "Vivir es Convivir" program.
Generated: DETERMINISTIC_2498423b78dea83f
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

class RespectGame:
    """
    An interactive educational game teaching children aged 4-9 about respect.
    Based on the "Vivir es Convivir" program principles.
    """
    
    def __init__(self):
        self.player_name = ""
        self.score = 0
        self.levels = {
            "easy": {
                "questions": [
                    {
                        "question": "What should you do when someone is talking?",
                        "options": ["Listen quietly", "Shout", "Look away"],
                        "answer": 0,
                        "explanation": "Listening quietly shows respect for the speaker."
                    },
                    {
                        "question": "How do you show respect to your teacher?",
                        "options": ["Follow instructions", "Ignore them", "Make funny faces"],
                        "answer": 0,
                        "explanation": "Following instructions shows you respect their guidance."
                    }
                ]
            },
            "medium": {
                "questions": [
                    {
                        "question": "Your friend is sad. What should you do?",
                        "options": ["Comfort them", "Laugh at them", "Ignore them"],
                        "answer": 0,
                        "explanation": "Comforting shows respect for their feelings."
                    },
                    {
                        "question": "You disagree with a classmate. What's the respectful way to handle it?",
                        "options": ["Discuss calmly", "Yell your opinion", "Call them names"],
                        "answer": 0,
                        "explanation": "Calm discussion shows respect for different opinions."
                    }
                ]
            },
            "hard": {
                "questions": [
                    {
                        "question": "You see someone being bullied. What's the respectful action?",
                        "options": ["Help or tell an adult", "Join in", "Walk away"],
                        "answer": 0,
                        "explanation": "Helping shows respect for everyone's right to feel safe."
                    },
                    {
                        "question": "How can you show respect for the environment?",
                        "options": ["Pick up trash", "Litter", "Break plants"],
                        "answer": 0,
                        "explanation": "Caring for nature shows respect for our world."
                    }
                ]
            }
        }
    
    def display_welcome(self):
        """Display welcome message and instructions."""
        print("\n" + "="*50)
        print("Welcome to the Respect Learning Game!")
        print("Based on 'Vivir es Convivir' program")
        print("="*50 + "\n")
        print("In this game, you'll learn about respect through fun scenarios.")
        print("Choose the answer that shows respect to earn points!")
        print("Let's begin!\n")
    
    def get_player_name(self):
        """Get and validate player name."""
        while True:
            name = input("What's your name? ").strip()
            if name:
                self.player_name = name.capitalize()
                break
            print("Please enter your name to continue.")
    
    def select_difficulty(self):
        """Let player choose difficulty level."""
        print("\nChoose your difficulty level:")
        print("1. Easy (Ages 4-6)")
        print("2. Medium (Ages 6-8)")
        print("3. Hard (Ages 8-9)")
        
        while True:
            choice = input("Enter 1, 2, or 3: ").strip()
            if choice in ["1", "2", "3"]:
                levels = ["easy", "medium", "hard"]
                return levels[int(choice)-1]
            print("Please enter 1, 2, or 3.")
    
    def ask_question(self, question_data):
        """Present a question and get player's answer."""
        print(f"\nQuestion: {question_data['question']}")
        for idx, option in enumerate(question_data['options']):
            print(f"{idx+1}. {option}")
        
        while True:
            try:
                answer = int(input("Your answer (1-3): ")) - 1
                if 0 <= answer <= 2:
                    return answer
                print("Please enter 1, 2, or 3.")
            except ValueError:
                print("Please enter a number.")
    
    def give_feedback(self, player_answer, correct_answer, explanation):
        """Provide feedback on the player's answer."""
        if player_answer == correct_answer:
            print("\n✅ Correct! Great job showing respect!")
            self.score += 1
        else:
            print("\n❌ Oops! Let's learn:")
        print(f"Explanation: {explanation}\n")
        time.sleep(2)
    
    def play_level(self, difficulty):
        """Play through all questions in a difficulty level."""
        questions = self.levels[difficulty]["questions"]
        random.shuffle(questions)
        
        for question in questions:
            answer = self.ask_question(question)
            self.give_feedback(answer, question["answer"], question["explanation"])
    
    def show_results(self):
        """Display final results and encouragement."""
        print("\n" + "="*50)
        print(f"Game Over, {self.player_name}!")
        print(f"Your Respect Score: {self.score}/6")
        
        if self.score >= 5:
            print("🌟 Amazing! You're a Respect Champion!")
        elif self.score >= 3:
            print("👍 Good job! You understand respect well!")
        else:
            print("💡 Keep practicing! Respect makes the world better!")
        
        print("Remember: Respect is treating others how you want to be treated.")
        print("="*50 + "\n")
    
    def play_again(self):
        """Ask if player wants to play again."""
        while True:
            choice = input("Would you like to play again? (yes/no): ").lower().strip()
            if choice in ["yes", "y"]:
                return True
            elif choice in ["no", "n"]:
                return False
            print("Please enter 'yes' or 'no'.")
    
    def run(self):
        """Main game loop."""
        self.display_welcome()
        self.get_player_name()
        
        while True:
            self.score = 0  # Reset score for new game
            difficulty = self.select_difficulty()
            self.play_level(difficulty)
            self.show_results()
            
            if not self.play_again():
                print(f"\nThanks for playing, {self.player_name}! Keep showing respect!")
                break

if __name__ == "__main__":
    try:
        game = RespectGame()
        game.run()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        sys.exit(1)
```
