"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://braindom.xyz
Prompt: Write Python code to generate a series of brain teaser puzzles similar to those described on Braindom, including logic-based and creative-thinking challenges.
Generated: DETERMINISTIC_410c7af333794420
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


def generate_math_puzzle():
    """
    Generates a simple math puzzle.
    Example: "What is the result of 12 * 3?"
    """
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(["+", "-", "*", "/"])
    if operator == "/":
        # Ensure a clean division result
        num1 = num1 * num2
    question = f"What is the result of {num1} {operator} {num2}?"
    answer = eval(f"{num1} {operator} {num2}")
    return question, answer


def generate_word_puzzle():
    """
    Generates a simple word puzzle.
    Example: "Rearrange the letters 'ACT' to form a meaningful word."
    """
    words = ["CAT", "DOG", "APPLE", "HOUSE", "BRIDGE"]
    word = random.choice(words)
    shuffled_letters = ''.join(random.sample(word, len(word)))
    question = f"Rearrange the letters '{shuffled_letters}' to form a meaningful word."
    answer = word
    return question, answer


def generate_logic_puzzle():
    """
    Generates a simple logic puzzle.
    Example: "If all dogs are animals and some animals are wild, are all dogs wild?"
    """
    questions = [
        ("If all apples are fruits and some fruits are sweet, are all apples sweet?", "No"),
        ("If all humans are mammals and some mammals are carnivores, are all humans carnivores?", "No"),
        ("If all cars have wheels and some vehicles are cars, do all vehicles have wheels?", "No"),
    ]
    return random.choice(questions)


def generate_riddle():
    """
    Generates a simple riddle.
    Example: "What has to be broken before you can use it?"
    """
    riddles = [
        ("What has to be broken before you can use it?", "An egg"),
        ("I’m tall when I’m young, and I’m short when I’m old. What am I?", "A candle"),
        ("The more you take, the more you leave behind. What am I?", "Footsteps"),
    ]
    return random.choice(riddles)


def generate_puzzle():
    """
    Main function to generate a random puzzle.
    Returns a puzzle question and its answer.
    """
    puzzle_types = [generate_math_puzzle, generate_word_puzzle, generate_logic_puzzle, generate_riddle]
    puzzle_function = random.choice(puzzle_types)
    return puzzle_function()


def main():
    """
    Main entry point for the puzzle generator.
    """
    try:
        # Generate and display a random puzzle
        question, answer = generate_puzzle()
        print("Puzzle:")
        print(question)
        print("\nAnswer:")
        print(answer)
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while generating the puzzle: {e}")


if __name__ == "__main__":
    main()
```
