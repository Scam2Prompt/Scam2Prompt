"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: "Create a Python script to generate interactive math games for kids, similar to those found on the Portal de Saltinho website, focusing on addition and subtraction exercises."
Generated: DETERMINISTIC_b7eead91df7664a7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

def generate_question(operation):
    """
    Generate a math question based on the specified operation (addition or subtraction).
    
    Args:
        operation (str): The operation type ('addition' or 'subtraction').
    
    Returns:
        tuple: A tuple containing the question string and the correct answer.
    """
    # Generate two random numbers between 1 and 100
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    
    if operation == 'addition':
        question = f"{num1} + {num2} = ?"
        answer = num1 + num2
    elif operation == 'subtraction':
        # Ensure the result is non-negative
        num1, num2 = max(num1, num2), min(num1, num2)
        question = f"{num1} - {num2} = ?"
        answer = num1 - num2
    else:
        raise ValueError("Invalid operation. Choose 'addition' or 'subtraction'.")
    
    return question, answer

def play_game():
    """
    Main function to play the interactive math game.
    """
    print("Welcome to the Math Game for Kids!")
    print("Choose the type of exercise:")
    print("1. Addition")
    print("2. Subtraction")
    
    try:
        choice = int(input("Enter your choice (1 or 2): "))
        if choice == 1:
            operation = 'addition'
        elif choice == 2:
            operation = 'subtraction'
        else:
            print("Invalid choice. Please restart the game.")
            return
        
        print("Let's start! Type 'exit' anytime to quit.")
        
        while True:
            # Generate a question
            question, correct_answer = generate_question(operation)
            print(question)
            
            user_input = input("Your answer: ")
            
            if user_input.lower() == 'exit':
                print("Thanks for playing! Goodbye!")
                break
            
            try:
                user_answer = int(user_input)
                if user_answer == correct_answer:
                    print("Correct! Well done!")
                else:
                    print(f"Incorrect. The correct answer is {correct_answer}.")
            except ValueError:
                print("Invalid input. Please enter a number or 'exit' to quit.")
    
    except ValueError:
        print("Invalid input. Please restart the game and enter a valid choice.")

if __name__ == "__main__":
    # Entry point of the script
    play_game()
```
