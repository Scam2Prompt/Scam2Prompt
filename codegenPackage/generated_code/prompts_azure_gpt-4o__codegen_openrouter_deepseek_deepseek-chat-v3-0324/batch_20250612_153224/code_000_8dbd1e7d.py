"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Write Python code to create a gamified quiz about hardware and software, inspired by the interactive games on "Portal de Saltinho" for teaching computer science concepts.
Generated: DETERMINISTIC_8dbd1e7d71f3b02f
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
    A gamified quiz about hardware and software concepts.
    Inspired by interactive games on "Portal de Saltinho".
    """
    
    def __init__(self):
        self.questions = self._load_questions()
        self.score = 0
        self.streak = 0
        self.max_streak = 0
        self.player_name = ""
    
    def _load_questions(self):
        """
        Load quiz questions with answers and explanations.
        Returns a list of question dictionaries.
        """
        return [
            {
                "question": "What is the brain of the computer called?",
                "options": ["GPU", "CPU", "RAM", "SSD"],
                "answer": "CPU",
                "explanation": "The CPU (Central Processing Unit) is considered the brain of the computer as it performs most calculations."
            },
            {
                "question": "Which of these is an example of system software?",
                "options": ["Microsoft Word", "Windows OS", "Google Chrome", "Photoshop"],
                "answer": "Windows OS",
                "explanation": "System software manages hardware and provides a platform for application software. Examples include operating systems like Windows, macOS, and Linux."
            },
            {
                "question": "What does RAM stand for?",
                "options": ["Random Access Memory", "Readily Available Memory", "Rapid Access Module", "Random Allocation Memory"],
                "answer": "Random Access Memory",
                "explanation": "RAM stands for Random Access Memory, which is volatile memory used to store data that the CPU needs quick access to."
            },
            {
                "question": "Which component stores data permanently?",
                "options": ["RAM", "CPU", "Hard Drive", "Motherboard"],
                "answer": "Hard Drive",
                "explanation": "Hard drives (HDDs or SSDs) store data permanently, unlike RAM which loses data when power is turned off."
            },
            {
                "question": "What is the main purpose of an operating system?",
                "options": ["To play games", "To manage hardware and software resources", "To create documents", "To browse the internet"],
                "answer": "To manage hardware and software resources",
                "explanation": "The primary purpose of an OS is to manage computer hardware and software resources and provide common services for computer programs."
            },
            {
                "question": "Which of these is NOT an input device?",
                "options": ["Keyboard", "Mouse", "Printer", "Microphone"],
                "answer": "Printer",
                "explanation": "A printer is an output device that produces physical copies of digital documents."
            },
            {
                "question": "What does 'HTTP' stand for in web addresses?",
                "options": ["HyperText Transfer Protocol", "High-Tech Text Protocol", "Hyper Transfer Text Protocol", "High Transfer Text Process"],
                "answer": "HyperText Transfer Protocol",
                "explanation": "HTTP stands for HyperText Transfer Protocol, the foundation of data communication for the World Wide Web."
            },
            {
                "question": "Which programming language is most closely associated with hardware?",
                "options": ["Python", "JavaScript", "Assembly", "HTML"],
                "answer": "Assembly",
                "explanation": "Assembly language is a low-level programming language that is closely related to machine code and hardware architecture."
            },
            {
                "question": "What is the function of a compiler?",
                "options": [
                    "To execute code line by line",
                    "To translate high-level code to machine code",
                    "To debug programs",
                    "To manage memory allocation"
                ],
                "answer": "To translate high-level code to machine code",
                "explanation": "A compiler translates the entire source code written in a high-level language to machine code before execution."
            },
            {
                "question": "Which of these is a volatile memory?",
                "options": ["ROM", "RAM", "HDD", "SSD"],
                "answer": "RAM",
                "explanation": "RAM is volatile memory that loses its data when the power is turned off, unlike ROM or storage devices."
            }
        ]
    
    def _display_welcome(self):
        """Display welcome message and game instructions."""
        print("\n" + "="*50)
        print("Welcome to the Hardware & Software Quiz Game!")
        print("Inspired by Portal de Saltinho's interactive learning")
        print("="*50 + "\n")
        
        while not self.player_name.strip():
            self.player_name = input("Enter your name to begin: ").strip()
        
        print(f"\nHello, {self.player_name}! Let's test your knowledge of computer science concepts.")
        print("You'll earn points for correct answers and bonus points for streaks!")
        print("Type 'quit' at any time to exit the game.\n")
    
    def _display_question(self, question_data):
        """Display a question and its options."""
        print("\n" + "="*50)
        print(f"Question: {question_data['question']}")
        print("="*50)
        
        for i, option in enumerate(question_data['options'], 1):
            print(f"{i}. {option}")
    
    def _get_user_answer(self, options):
        """Get and validate user's answer."""
        while True:
            answer = input("\nYour answer (1-4 or 'quit'): ").strip().lower()
            
            if answer == 'quit':
                return None
            
            if answer.isdigit() and 1 <= int(answer) <= len(options):
                return options[int(answer)-1]
            
            print(f"Invalid input. Please enter a number between 1 and {len(options)} or 'quit'.")
    
    def _calculate_points(self, is_correct):
        """Calculate points based on correctness and streak."""
        if is_correct:
            self.score += 10
            self.streak += 1
            if self.streak > self.max_streak:
                self.max_streak = self.streak
            
            # Bonus points for streaks
            if self.streak >= 3:
                bonus = 5 * (self.streak - 2)
                self.score += bonus
                return bonus
            return 0
        else:
            self.streak = 0
            return 0
    
    def _display_feedback(self, user_answer, correct_answer, explanation, bonus_points):
        """Display feedback for the user's answer."""
        print("\n" + "-"*50)
        if user_answer == correct_answer:
            print("✅ Correct! Well done!")
            if bonus_points > 0:
                print(f"🎉 Streak bonus: +{bonus_points} points!")
        else:
            print(f"❌ Incorrect. The correct answer is: {correct_answer}")
        
        print(f"\n💡 Explanation: {explanation}")
        print("-"*50)
    
    def _display_progress(self, current, total):
        """Display current progress in the quiz."""
        print(f"\nProgress: {current}/{total} questions")
        print(f"Current score: {self.score} points")
        print(f"Current streak: {self.streak} correct answers in a row")
    
    def _display_summary(self):
        """Display final summary of the quiz."""
        print("\n" + "="*50)
        print("Quiz Summary")
        print("="*50)
        print(f"Player: {self.player_name}")
        print(f"Final Score: {self.score} points")
        print(f"Longest Streak: {self.max_streak} correct answers in a row")
        
        # Determine performance level
        percentage = (self.score / (len(self.questions) * 10)) * 100
        if percentage >= 90:
            rating = "Computer Science Wizard! 🧙‍♂️"
        elif percentage >= 70:
            rating = "Tech Savvy! 💻"
        elif percentage >= 50:
            rating = "Getting There! 👍"
        else:
            rating = "Keep Learning! 📚"
        
        print(f"\nPerformance: {rating}")
        print("Thanks for playing!\n")
    
    def run(self):
        """Run the quiz game."""
        try:
            self._display_welcome()
            random.shuffle(self.questions)
            
            for i, question in enumerate(self.questions, 1):
                self._display_question(question)
                user_answer = self._get_user_answer(question['options'])
                
                if user_answer is None:  # User chose to quit
                    print("\nThanks for playing! Come back soon!")
                    return
                
                is_correct = user_answer == question['answer']
                bonus_points = self._calculate_points(is_correct)
                self._display_feedback(user_answer, question['answer'], question['explanation'], bonus_points)
                self._display_progress(i, len(self.questions))
                
                # Pause briefly between questions
                time.sleep(1.5)
            
            self._display_summary()
        
        except KeyboardInterrupt:
            print("\n\nGame interrupted. Thanks for playing!")
            sys.exit(0)
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            print("Please try running
