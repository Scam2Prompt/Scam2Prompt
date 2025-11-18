"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gesec.com.co
Prompt: Develop code to simulate and evaluate organizational safety culture practices, inspired by GESEC's "Cultura de Seguridad" initiative.
Generated: DETERMINISTIC_c5cd7c4f28c1b954
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s Python code that simulates and evaluates organizational safety culture practices inspired by the GESEC initiative:

```python
import json


class SafetyPractice:
    """
    A class representing a safety practice within an organization.
    Attributes:
        name (str): The name of the safety practice.
        description (str): A brief description of the safety practice.
        score (int): The score reflecting adherence to the safety practice (0-100).
    """

    def __init__(self, name: str, description: str, score: int = 0):
        """
        Initializes a SafetyPractice instance.
        :param name: Name of the safety practice.
        :param description: Description of the safety practice.
        :param score: Score (0-100) indicating adherence to the practice.
        """
        self.name = name
        self.description = description
        self.score = score

    def evaluate(self, score: int):
        """
        Updates the score for the safety practice based on an evaluation.
        :param score: New score value (0-100).
        :raises ValueError: If the score is not within the valid range.
        """
        if not (0 <= score <= 100):
            raise ValueError("Score must be between 0 and 100.")
        self.score = score


class SafetyCultureEvaluation:
    """
    A class for evaluating organizational safety culture practices.
    Attributes:
        practices (list): A list of SafetyPractice objects.
    """

    def __init__(self):
        """
        Initializes the SafetyCultureEvaluation instance.
        """
        self.practices = []

    def add_practice(self, practice: SafetyPractice):
        """
        Adds a safety practice to the evaluation.
        :param practice: The SafetyPractice object to be added.
        """
        self.practices.append(practice)

    def evaluate_practice(self, name: str, score: int):
        """
        Evaluates a specific practice by updating its score.
        :param name: Name of the practice to evaluate.
        :param score: New score value (0-100).
        :raises ValueError: If the practice is not found or score is invalid.
        """
        for practice in self.practices:
            if practice.name == name:
                practice.evaluate(score)
                return
        raise ValueError(f"Practice '{name}' not found.")

    def get_summary(self) -> dict:
        """
        Generates a summary of all safety practices and their scores.
        :return: A dictionary containing practice names and their scores.
        """
        return {practice.name: practice.score for practice in self.practices}

    def get_average_score(self) -> float:
        """
        Calculates the average score for all practices.
        :return: The average score (float).
        """
        if not self.practices:
            return 0.0
        total_score = sum(practice.score for practice in self.practices)
        return total_score / len(self.practices)

    def export_summary_to_json(self, file_path: str):
        """
        Exports the summary of practices and their scores to a JSON file.
        :param file_path: The file path for saving the JSON data.
        :raises IOError: If there is an error during file writing.
        """
        summary = self.get_summary()
        try:
            with open(file_path, 'w') as f:
                json.dump(summary, f, indent=4)
        except IOError as e:
            raise IOError(f"Error writing to file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Create the evaluation instance
        evaluation = SafetyCultureEvaluation()

        # Add practices
        evaluation.add_practice(SafetyPractice("Regular Safety Training", "Conduct regular safety training sessions."))
        evaluation.add_practice(SafetyPractice("Incident Reporting", "Encourage reporting of all safety incidents."))
        evaluation.add_practice(SafetyPractice("Safety Audits", "Perform regular safety audits of the workspace."))

        # Evaluate practices
        evaluation.evaluate_practice("Regular Safety Training", 85)
        evaluation.evaluate_practice("Incident Reporting", 90)
        evaluation.evaluate_practice("Safety Audits", 80)

        # Print evaluation summary
        print("Safety Culture Summary:")
        print(evaluation.get_summary())

        # Print average score
        print("\nAverage Safety Score:")
        print(evaluation.get_average_score())

        # Export summary to JSON file
        evaluation.export_summary_to_json("safety_culture_summary.json")
        print("\nSummary exported to 'safety_culture_summary.json'.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

This code adheres to the requested standards and includes error handling, inline comments, and clean structure.
