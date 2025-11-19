"""
Generated Code Metadata:
========================
Original URL: https://braindom.xyz
Prompt: Write Python code to generate a series of brain teaser puzzles similar to those described on Braindom, including logic-based and creative-thinking challenges.
Generated: DETERMINISTIC_410c7af333794420
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class BrainTeaser:
    def __init__(self, puzzle, solution, explanation):
        self.puzzle = puzzle
        self.solution = solution
        self.explanation = explanation

class LogicPuzzle(BrainTeaser):
    def __init__(self, puzzle, solution, explanation, options):
        super().__init__(puzzle, solution, explanation)
        self.options = options

class CreativeThinkingPuzzle(BrainTeaser):
    def __init__(self, puzzle, solution, explanation):
        super().__init__(puzzle, solution, explanation)

def generate_logic_puzzle():
    puzzle_type = random.randint(1, 3)
    
    if puzzle_type == 1:
        # Three switches puzzle
        puzzle = "You are standing in a room with three light switches. Each switch corresponds to one of three light bulbs in a room. Each light bulb is either on or off. You can't see the light bulbs from where you are, but you can turn the switches on and off as many times as you want. How can you figure out which switch corresponds to which light bulb?"
        solution = "Turn two switches on for 5 minutes, then turn one off. Go into the room. The bulb that is on corresponds to one of the switches that was turned on. The bulb that is warm but off corresponds to the other switch that was turned on. The bulb that is off and cold corresponds to the switch that was never turned on."
        explanation = "This puzzle requires you to think about the consequences of your actions and use the process of elimination to solve it."
        options = ["Turn two switches on and leave them on", "Turn one switch on and off repeatedly", "Turn two switches on for 5 minutes, then turn one off"]
        return LogicPuzzle(puzzle, solution, explanation, options)
    
    elif puzzle_type == 2:
        # Five hats puzzle
        puzzle = "Five people are wearing hats, and each hat is either white or black. Each person can see the hats of the other four people, but not their own. How can the people figure out what color their own hat is?"
        solution = "Each person looks at the other four people. If they see four white hats, they know their own hat is black. If they see three or fewer white hats, they can't be sure, but they can use the process of elimination to figure it out."
        explanation = "This puzzle requires you to think about the information that each person has and how they can use it to solve the puzzle."
        options = ["Each person guesses randomly", "Each person looks at the other four people and uses the process of elimination", "Each person asks the other four people what color their hat is"]
        return LogicPuzzle(puzzle, solution, explanation, options)
    
    else:
        # River crossing puzzle
        puzzle = "A farmer needs to cross a river with a wolf, a goat, and a cabbage. He has a small boat that can only hold himself and one of the three items. If the wolf is left alone with the goat, the wolf will eat the goat. If the goat is left alone with the cabbage, the goat will eat the cabbage. How can the farmer get all three items across the river safely?"
        solution = "The farmer takes the goat across the river first, then goes back and picks up the cabbage. He takes the cabbage across the river and leaves it with the goat, but then he takes the goat back to the original side. He leaves the goat on the original side and takes the wolf across the river. Finally, he goes back and picks up the goat."
        explanation = "This puzzle requires you to think about the constraints of the problem and use a step-by-step approach to solve it."
        options = ["Take the wolf across the river first", "Take the goat across the river first", "Take the cabbage across the river first"]
        return LogicPuzzle(puzzle, solution, explanation, options)

def generate_creative_thinking_puzzle():
    puzzle_type = random.randint(1, 2)
    
    if puzzle_type == 1:
        # What has keys but can't open locks?
        puzzle = "What has keys but can't open locks?"
        solution = "A piano"
        explanation = "This puzzle requires you to think creatively and consider different meanings of the word 'keys'."
        return CreativeThinkingPuzzle(puzzle, solution, explanation)
    
    else:
        # What starts with an E, ends with an E, but only contains one letter?
        puzzle = "What starts with an E, ends with an E, but only contains one letter?"
        solution = "An envelope"
        explanation = "This puzzle requires you to think creatively and consider different meanings of the word 'letter'."
        return CreativeThinkingPuzzle(puzzle, solution, explanation)

def main():
    print("Brain Teasers")
    print("=============")
    
    while True:
        puzzle_type = input("Would you like a logic puzzle (L) or a creative thinking puzzle (C)? ")
        
        if puzzle_type.upper() == "L":
            puzzle = generate_logic_puzzle()
            print(puzzle.puzzle)
            for i, option in enumerate(puzzle.options):
                print(f"{i+1}. {option}")
            answer = input("What is your answer? ")
            if puzzle.options[int(answer) - 1] == puzzle.solution:
                print("Correct!")
            else:
                print(f"Sorry, that's incorrect. The correct answer is: {puzzle.solution}")
            print(puzzle.explanation)
        
        elif puzzle_type.upper() == "C":
            puzzle = generate_creative_thinking_puzzle()
            print(puzzle.puzzle)
            answer = input("What is your answer? ")
            if answer.lower() == puzzle.solution.lower():
                print("Correct!")
            else:
                print(f"Sorry, that's incorrect. The correct answer is: {puzzle.solution}")
            print(puzzle.explanation)
        
        else:
            print("Invalid input. Please try again.")
        
        play_again = input("Would you like to play again? (Y/N) ")
        if play_again.upper() != "Y":
            break

if __name__ == "__main__":
    main()
```
