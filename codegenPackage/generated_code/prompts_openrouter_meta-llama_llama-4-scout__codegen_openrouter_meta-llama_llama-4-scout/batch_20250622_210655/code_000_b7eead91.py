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
import operator

# Define operators and their corresponding functions
OPERATORS = {
    '+': operator.add,
    '-': operator.sub
}

def generate_math_game(level):
    """
    Generate a math game with addition and subtraction exercises.

    Args:
        level (int): The difficulty level of the game.

    Returns:
        A dictionary containing the game data.
    """
    game_data = {
        'exercises': [],
        'score': 0
    }

    for _ in range(level * 5):
        num1 = random.randint(1, level * 10)
        num2 = random.randint(1, level * 10)
        op = random.choice(list(OPERATORS.keys()))

        exercise = {
            'num1': num1,
            'num2': num2,
            'op': op,
            'answer': OPERATORS[op](num1, num2)
        }

        game_data['exercises'].append(exercise)

    return game_data

def play_game(game_data):
    """
    Play the math game.

    Args:
        game_data (dict): The game data.

    Returns:
        The final score.
    """
    score = 0

    for i, exercise in enumerate(game_data['exercises']):
        print(f"\nExercise {i+1}: {exercise['num1']} {exercise['op']} {exercise['num2']}")
        try:
            user_answer = float(input("Enter your answer: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_answer == exercise['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is {exercise['answer']}")

    game_data['score'] = score
    return score

def main():
    print("Welcome to the math game!")
    level = input("Choose a difficulty level (1-5): ")

    try:
        level = int(level)
        if level < 1 or level > 5:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        return

    game_data = generate_math_game(level)
    final_score = play_game(game_data)

    print(f"\nGame over! Your final score is {final_score} out of {len(game_data['exercises'])}")

if __name__ == "__main__":
    main()
```
