"""
Generated Code Metadata:
========================
Original URL: https://idealproblemsolver.net
Prompt: Generate code for a simple problem-solving tool that can be used in educational settings.
Generated: DETERMINISTIC_870414ef72683dc6
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simple Problem-Solving Tool for Educational Settings

This tool provides basic problem-solving functionalities including:
- Math problem solving (basic operations)
- Word problems (simple parsing and solving)
- Multiple-choice question handling
"""

import re
import random
from typing import Union, List, Dict, Optional

class ProblemSolver:
    """
    A simple problem-solving tool for educational purposes.
    """
    
    def __init__(self):
        self.math_patterns = {
            'addition': r'(\d+)\s*\+\s*(\d+)',
            'subtraction': r'(\d+)\s*\-\s*(\d+)',
            'multiplication': r'(\d+)\s*\*\s*(\d+)',
            'division': r'(\d+)\s*\/\s*(\d+)'
        }
        
    def solve_math_problem(self, problem: str) -> Union[float, str]:
        """
        Solves basic math problems with +, -, *, / operations.
        
        Args:
            problem: String containing the math problem (e.g., "2 + 2")
            
        Returns:
            Solution as float or error message if invalid
        """
        try:
            for operation, pattern in self.math_patterns.items():
                match = re.fullmatch(pattern, problem.strip())
                if match:
                    num1, num2 = map(float, match.groups())
                    if operation == 'addition':
                        return num1 + num2
                    elif operation == 'subtraction':
                        return num1 - num2
                    elif operation == 'multiplication':
                        return num1 * num2
                    elif operation == 'division':
                        if num2 == 0:
                            return "Error: Division by zero"
                        return num1 / num2
            return "Error: Invalid math problem format"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def solve_word_problem(self, problem: str) -> str:
        """
        Attempts to solve simple word problems.
        
        Args:
            problem: String containing the word problem
            
        Returns:
            Solution or explanation
        """
        try:
            problem = problem.lower()
            
            # Handle simple addition word problems
            if 'add' in problem or 'sum' in problem or 'total' in problem:
                numbers = [int(num) for num in re.findall(r'\d+', problem)]
                if len(numbers) >= 2:
                    return f"The sum is {sum(numbers)}"
            
            # Handle simple subtraction word problems
            elif 'difference' in problem or 'subtract' in problem or 'left' in problem:
                numbers = [int(num) for num in re.findall(r'\d+', problem)]
                if len(numbers) >= 2:
                    return f"The difference is {numbers[0] - numbers[1]}"
            
            return "I can only solve simple addition or subtraction word problems right now."
        except Exception as e:
            return f"Error processing word problem: {str(e)}"
    
    def generate_multiple_choice(self, question: str, options: List[str], correct_index: int) -> Dict:
        """
        Generates a multiple-choice question with feedback.
        
        Args:
            question: The question text
            options: List of possible answers
            correct_index: Index of the correct answer (0-based)
            
        Returns:
            Dictionary containing question, options, and feedback
        """
        if not (0 <= correct_index < len(options)):
            raise ValueError("Correct index must be within options range")
        
        return {
            'question': question,
            'options': options,
            'correct_index': correct_index,
            'feedback': {
                'correct': "Correct! Well done.",
                'incorrect': f"Incorrect. The correct answer is: {options[correct_index]}"
            }
        }
    
    def check_answer(self, question_data: Dict, user_answer: int) -> Dict:
        """
        Checks user's answer against the correct answer.
        
        Args:
            question_data: Dictionary from generate_multiple_choice
            user_answer: Index of user's answer (0-based)
            
        Returns:
            Dictionary with result and feedback
        """
        try:
            is_correct = user_answer == question_data['correct_index']
            feedback = question_data['feedback']['correct'] if is_correct else question_data['feedback']['incorrect']
            
            return {
                'is_correct': is_correct,
                'feedback': feedback,
                'correct_answer': question_data['correct_index']
            }
        except Exception as e:
            return {
                'is_correct': False,
                'feedback': f"Error checking answer: {str(e)}",
                'correct_answer': None
            }

def main():
    """Example usage of the ProblemSolver class."""
    solver = ProblemSolver()
    
    # Math problem examples
    math_problems = ["2 + 2", "5 - 3", "4 * 6", "10 / 2", "10 / 0"]
    for problem in math_problems:
        print(f"Problem: {problem} => Solution: {solver.solve_math_problem(problem)}")
    
    # Word problem examples
    word_problems = [
        "What is the sum of 5 and 3?",
        "Find the difference between 10 and 7",
        "How many apples are there?"
    ]
    for problem in word_problems:
        print(f"Problem: {problem} => Solution: {solver.solve_word_problem(problem)}")
    
    # Multiple choice example
    mcq = solver.generate_multiple_choice(
        "What is 2 + 2?",
        ["3", "4", "5", "6"],
        1
    )
    print("\nMultiple Choice Question:")
    print(f"Question: {mcq['question']}")
    for i, option in enumerate(mcq['options']):
        print(f"{i}. {option}")
    
    # Test correct and incorrect answers
    print("\nTesting answers:")
    for answer in [1, 2]:
        result = solver.check_answer(mcq, answer)
        print(f"Answer {answer}: {result['feedback']}")

if __name__ == "__main__":
    main()
```
