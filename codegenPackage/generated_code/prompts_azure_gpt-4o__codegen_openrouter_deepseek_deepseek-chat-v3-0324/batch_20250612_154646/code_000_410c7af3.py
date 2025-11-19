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
from typing import List, Dict, Union, Optional

class BrainTeaserGenerator:
    """
    A class to generate various types of brain teaser puzzles.
    Supports logic puzzles, riddles, lateral thinking, and math challenges.
    """
    
    def __init__(self):
        self._load_puzzle_templates()
    
    def _load_puzzle_templates(self) -> None:
        """Initialize puzzle templates and data."""
        self.riddles = [
            {
                "question": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
                "answer": "echo",
                "hint": "You might hear me in a canyon"
            },
            {
                "question": "The more you take, the more you leave behind. What am I?",
                "answer": "footsteps",
                "hint": "Think about walking"
            },
            {
                "question": "What has keys but can't open locks?",
                "answer": "piano",
                "hint": "Musical instrument"
            }
        ]
        
        self.logic_puzzles = [
            {
                "question": "If all Bloops are Razzies and all Razzies are Lazzies, are all Bloops definitely Lazzies?",
                "answer": "yes",
                "hint": "Follow the chain of relationships"
            },
            {
                "question": "A man builds a house rectangular in shape. All sides have southern exposure. A bear walks by. What color is the bear?",
                "answer": "white",
                "hint": "Think about the location of the house"
            }
        ]
        
        self.lateral_thinking = [
            {
                "question": "A man lives on the 10th floor of a building. Every day he takes the elevator to go down to the ground floor to go to work. When he returns, he takes the elevator to the 7th floor and walks up the stairs to reach his apartment on the 10th floor. Why?",
                "answer": "He's too short to reach the button for the 10th floor",
                "hint": "Consider the man's height"
            },
            {
                "question": "A woman shoots her husband. Then she holds him underwater for five minutes. Finally, she hangs him. But five minutes later, they both go out together and enjoy a wonderful dinner together. How?",
                "answer": "She's a photographer",
                "hint": "Think about alternative meanings of the actions"
            }
        ]
        
        self.math_challenges = [
            {
                "question": "If 1=3, 2=3, 3=5, 4=4, 5=4, then what does 6=?",
                "answer": "3",
                "hint": "Count the letters in the number words"
            },
            {
                "question": "What is the next number in the sequence: 2, 10, 12, 16, 17, 18, 19, ___?",
                "answer": "200",
                "hint": "Think about numbers starting with the letter 'T'"
            }
        ]
    
    def generate_puzzle(self, category: Optional[str] = None) -> Dict[str, str]:
        """
        Generate a random brain teaser puzzle.
        
        Args:
            category: Optional filter for puzzle type ('riddle', 'logic', 'lateral', 'math')
            
        Returns:
            Dictionary containing question, answer, hint, and category
        """
        if category:
            category = category.lower()
            valid_categories = {
                'riddle': self.riddles,
                'logic': self.logic_puzzles,
                'lateral': self.lateral_thinking,
                'math': self.math_challenges
            }
            
            if category not in valid_categories:
                raise ValueError(f"Invalid category. Must be one of: {list(valid_categories.keys())}")
            
            puzzle = random.choice(valid_categories[category])
            puzzle['category'] = category
            return puzzle
        
        # If no category specified, choose from all puzzles
        all_puzzles = []
        categories = [
            ('riddle', self.riddles),
            ('logic', self.logic_puzzles),
            ('lateral', self.lateral_thinking),
            ('math', self.math_challenges)
        ]
        
        for cat, puzzles in categories:
            for p in puzzles:
                p_copy = p.copy()
                p_copy['category'] = cat
                all_puzzles.append(p_copy)
        
        return random.choice(all_puzzles)
    
    def generate_puzzle_set(self, count: int = 5, categories: Optional[List[str]] = None) -> List[Dict[str, str]]:
        """
        Generate multiple puzzles with optional category filtering.
        
        Args:
            count: Number of puzzles to generate
            categories: Optional list of categories to include
            
        Returns:
            List of puzzle dictionaries
        """
        if count <= 0:
            raise ValueError("Count must be a positive integer")
            
        puzzles = []
        available_puzzles = []
        
        if categories:
            categories = [c.lower() for c in categories]
            valid_categories = {'riddle', 'logic', 'lateral', 'math'}
            invalid_cats = set(categories) - valid_categories
            if invalid_cats:
                raise ValueError(f"Invalid categories: {invalid_cats}. Valid options: {valid_categories}")
            
            for cat in categories:
                if cat == 'riddle':
                    available_puzzles.extend([p.copy() for p in self.riddles])
                elif cat == 'logic':
                    available_puzzles.extend([p.copy() for p in self.logic_puzzles])
                elif cat == 'lateral':
                    available_puzzles.extend([p.copy() for p in self.lateral_thinking])
                elif cat == 'math':
                    available_puzzles.extend([p.copy() for p in self.math_challenges])
        else:
            available_puzzles = []
            for p in self.riddles + self.logic_puzzles + self.lateral_thinking + self.math_challenges:
                available_puzzles.append(p.copy())
        
        if count > len(available_puzzles):
            raise ValueError(f"Requested {count} puzzles but only {len(available_puzzles)} available with current filters")
        
        selected_indices = random.sample(range(len(available_puzzles)), min(count, len(available_puzzles)))
        
        for idx in selected_indices:
            puzzle = available_puzzles[idx]
            if 'category' not in puzzle:
                # Determine category for puzzles from the full set
                if puzzle in self.riddles:
                    puzzle['category'] = 'riddle'
                elif puzzle in self.logic_puzzles:
                    puzzle['category'] = 'logic'
                elif puzzle in self.lateral_thinking:
                    puzzle['category'] = 'lateral'
                elif puzzle in self.math_challenges:
                    puzzle['category'] = 'math'
            puzzles.append(puzzle)
        
        return puzzles

    def check_answer(self, puzzle: Dict[str, str], user_answer: str) -> bool:
        """
        Check if the user's answer matches the puzzle's solution.
        
        Args:
            puzzle: The puzzle dictionary
            user_answer: The user's answer to check
            
        Returns:
            True if answer is correct (with some flexibility), False otherwise
        """
        if not puzzle or 'answer' not in puzzle:
            raise ValueError("Invalid puzzle provided")
            
        if not user_answer:
            return False
            
        correct_answer = puzzle['answer'].lower().strip()
        user_answer = user_answer.lower().strip()
        
        # Allow for some answer flexibility
        return (user_answer == correct_answer or 
                user_answer in correct_answer or 
                correct_answer in user_answer)

# Example usage
if __name__ == "__main__":
    generator = BrainTeaserGenerator()
    
    # Generate a single random puzzle
    puzzle = generator.generate_puzzle()
    print("\nRandom Puzzle:")
    print(f"Category: {puzzle['category'].title()}")
    print(f"Question: {puzzle['question']}")
    print(f"Hint: {puzzle['hint']}")
    print(f"Answer: {puzzle['answer']}")
    
    # Generate a set of math puzzles
    print("\nMath Puzzles Set:")
    math_puzzles = generator.generate_puzzle_set(2, categories=['math'])
    for i, p in enumerate(math_puzzles, 1):
        print(f"\nPuzzle {i}:")
        print(f"Question: {p['question']}")
        print(f"Hint: {p['hint']}")
        print(f"Answer: {p['answer']}")
```
