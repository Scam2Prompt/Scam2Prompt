"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Write Python code for a game that helps students practice multiplication tables, inspired by the mathematics games on "Portal de Saltinho."
Generated: DETERMINISTIC_c377611b43e1c52f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def generate_question():
    """
    Generate a random multiplication question.
    Returns:
        tuple: A tuple containing two random numbers and their product.
    """
    num1 = random.randint(1, 12)  # Multiplicand (1-12 for standard tables)
    num2 = random.randint(1, 12)  # Multiplier (1-12 for standard tables)
    return num1, num2, num1 * num2

def ask_question(num1, num2, answer):
    """
    Ask the user the multiplication question and validate their response.
    Args:
        num1 (int): The first number in the multiplication.
        num2 (int): The second number in the multiplication.
        answer (int): The correct answer to the question.
    Returns:
        bool: True if the user answered correctly, False otherwise.
    """
    try:
        user_input = int(input(f"What is {num1} x {num2}? "))
        if user_input == answer:
            print("Correct! Well done!")
            return True
        else:
            print(f"Incorrect. The correct answer is {answer}.")
            return False
    except ValueError:
        print("Invalid input. Please enter a number.")
        return False

def multiplication_game():
    """
    Main function to run the multiplication game.
    """
    print("Welcome to the Multiplication Practice Game!")
    print("Try to answer as many multiplication questions as you can!")
    print("Type 'exit' anytime to quit.\n")
    
    score = 0  # Initialize the score
    
    while True:
        num1, num2, correct_answer = generate_question()
        
        user_input = input(f"What is {num1} x {num2}? (Type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print(f"Thanks for playing! Your final score is {score}.")
            break
        
        try:
            user_answer = int(user_input)
            if user_answer == correct_answer:
                print("Correct! Well done!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is {correct_answer}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
        print(f"Your current score is: {score}\n")

if __name__ == "__main__":
    # Entry point of the program
    multiplication_game()
```
