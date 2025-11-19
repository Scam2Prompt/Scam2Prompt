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
import json

class ProblemSolver:
    """
    A simple problem-solving tool for educational settings.
    This class allows users to input a problem and receive a solution.
    """

    def __init__(self):
        self.problems = {}

    def add_problem(self, problem_id, problem_description, solution):
        """
        Adds a problem and its solution to the tool.

        :param problem_id: Unique identifier for the problem
        :param problem_description: Description of the problem
        :param solution: Solution to the problem
        """
        if problem_id in self.problems:
            raise ValueError(f"Problem ID '{problem_id}' already exists.")
        self.problems[problem_id] = {
            "description": problem_description,
            "solution": solution
        }

    def get_solution(self, problem_id):
        """
        Retrieves the solution for a given problem ID.

        :param problem_id: Unique identifier for the problem
        :return: Solution to the problem
        :raises KeyError: If the problem ID does not exist
        """
        try:
            return self.problems[problem_id]["solution"]
        except KeyError:
            raise KeyError(f"Problem ID '{problem_id}' not found.")

    def list_problems(self):
        """
        Lists all problems and their descriptions.

        :return: A list of tuples containing problem IDs and descriptions
        """
        return [(pid, details["description"]) for pid, details in self.problems.items()]

    def save_to_file(self, filename):
        """
        Saves the current problems and solutions to a JSON file.

        :param filename: The name of the file to save the data
        :raises IOError: If there is an issue writing to the file
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.problems, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving to file '{filename}': {e}")

    def load_from_file(self, filename):
        """
        Loads problems and solutions from a JSON file.

        :param filename: The name of the file to load the data from
        :raises IOError: If there is an issue reading the file
        :raises json.JSONDecodeError: If the file content is not valid JSON
        """
        try:
            with open(filename, 'r') as file:
                self.problems = json.load(file)
        except IOError as e:
            raise IOError(f"Error loading from file '{filename}': {e}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Error decoding JSON from file '{filename}': {e}")

# Example usage
if __name__ == "__main__":
    solver = ProblemSolver()
    solver.add_problem("1", "What is 2 + 2?", "4")
    solver.add_problem("2", "What is the capital of France?", "Paris")

    print("Available Problems:")
    for pid, desc in solver.list_problems():
        print(f"{pid}: {desc}")

    try:
        print("Solution to Problem 1:", solver.get_solution("1"))
    except KeyError as e:
        print(e)

    # Save problems to a file
    solver.save_to_file("problems.json")

    # Load problems from a file
    solver.load_from_file("problems.json")
```
