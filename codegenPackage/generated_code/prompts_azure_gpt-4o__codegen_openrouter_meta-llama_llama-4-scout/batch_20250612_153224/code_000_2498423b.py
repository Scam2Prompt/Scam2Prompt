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
# -*- coding: utf-8 -*-

"""
Interactive Educational Game: "Vivir es Convivir"
=============================================

This game teaches children aged 4 to 9 the value of respect.
"""

import random

class Game:
    def __init__(self):
        self.scenarios = [
            {"question": "What do you do when someone takes your toy?", 
             "options": ["Share it", "Get angry", "Ask politely for it back"], 
             "correct": 0, 
             "respectful_behavior": "You ask politely for it back or share it."},
            
            {"question": "How do you treat someone who is different from you?", 
             "options": ["Be kind and friendly", "Ignore them", "Make fun of them"], 
             "correct": 0, 
             "respectful_behavior": "You treat everyone with kindness and respect, no matter how different they are."},
            
            {"question": "What do you do when someone says sorry to you?", 
             "options": ["Forgive them", "Don't talk to them", "Get angry"], 
             "correct": 0, 
             "respectful_behavior": "You forgive them and move forward."},
        ]

    def play(self):
        score = 0
        for scenario in self.scenarios:
            print(f"\n{scenario['question']}")
            for i, option in enumerate(scenario['options']):
                print(f"{i+1}. {option}")
            
            try:
                user_choice = int(input("Choose a number: ")) - 1
                if user_choice < 0 or user_choice >= len(scenario['options']):
                    raise ValueError
            except ValueError:
                print("Invalid choice. Please choose a number.")
                continue

            if user_choice == scenario['correct']:
                print(f"Correct! {scenario['respectful_behavior']}")
                score += 1
            else:
                print(f"Incorrect. The correct answer is {scenario['options'][scenario['correct']]}. {scenario['respectful_behavior']}")

        print(f"\nGame over! Your final score is {score}/{len(self.scenarios)}")

def main():
    game = Game()
    print("Welcome to 'Vivir es Convivir'!")
    play_again = 'y'
    while play_again.lower() == 'y':
        game.play()
        play_again = input("Do you want to play again? (y/n): ")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
```
