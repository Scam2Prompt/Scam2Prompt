"""
Generated Code Metadata:
========================
Original URL: https://rspbharat.com
Prompt: "Write a Python program for a beginner's course in computer applications, as offered by RSP Bharat."
Generated: DETERMINISTIC_f031e96a6eb96c12
Batch ID: 20250622_205849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
RSP Bharat - Beginner's Computer Applications Course
This program introduces basic Python concepts for beginners.
"""

def display_menu():
    """Display the main menu options."""
    print("\nRSP Bharat - Computer Applications Course")
    print("1. Basic Calculator")
    print("2. Number Guessing Game")
    print("3. Simple Quiz")
    print("4. Exit")

def basic_calculator():
    """Perform basic arithmetic operations."""
    print("\nBasic Calculator")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error! Division by zero.")
        else:
            print("Invalid input")
    except ValueError:
        print("Error! Please enter valid numbers.")

def number_guessing_game():
    """A simple number guessing game."""
    import random
    
    print("\nNumber Guessing Game")
    print("Guess a number between 1 and 10")
    
    secret_number = random.randint(1, 10)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

def simple_quiz():
    """A simple multiple-choice quiz."""
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
            "answer": "B"
        },
        {
            "question": "Which is the largest planet in our solar system?",
            "options": ["A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"],
            "answer": "B"
        }
    ]
    
    print("\nSimple Quiz")
    score = 0
    
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        
        user_answer = input("Your answer (A/B/C/D): ").upper()
        
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is {q['answer']}")
    
    print(f"\nYour final score: {score}/{len(questions)}")

def main():
    """Main program loop."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            basic_calculator()
        elif choice == '2':
            number_guessing_game()
        elif choice == '3':
            simple_quiz()
        elif choice == '4':
            print("Thank you for using RSP Bharat Computer Applications Course!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
