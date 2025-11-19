"""
Generated Code Metadata:
========================
Original URL: https://scienceartthinking.de
Prompt: Write a program that models the effects of automation on creative processes, based on the ideas presented in "KI, Gewalt und Krieg."
Generated: DETERMINISTIC_8962ee4773ec40ef
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# automation_model.py

import random

class CreativeProcess:
    """
    Models a creative process with a given level of automation.
    """

    def __init__(self, automation_level):
        """
        Initializes a creative process with a given level of automation.

        Args:
            automation_level (float): Level of automation, between 0 and 1.
        """
        if not (0 <= automation_level <= 1):
            raise ValueError("Automation level must be between 0 and 1")

        self.automation_level = automation_level
        self.creative_output = []

    def generate_idea(self):
        """
        Generates a new idea based on the current automation level.

        Returns:
            str: The generated idea.
        """
        # Simulate human creativity
        human_idea = self._generate_human_idea()
        # Simulate machine creativity
        machine_idea = self._generate_machine_idea()

        # Combine human and machine ideas based on automation level
        if random.random() < self.automation_level:
            idea = machine_idea
        else:
            idea = human_idea

        self.creative_output.append(idea)
        return idea

    def _generate_human_idea(self):
        """
        Generates a random idea simulating human creativity.

        Returns:
            str: The generated idea.
        """
        ideas = [
            "Create a new art style",
            "Write a poem about nature",
            "Design a sustainable city",
            "Compose a piece of music",
            "Develop a new cuisine"
        ]
        return random.choice(ideas)

    def _generate_machine_idea(self):
        """
        Generates a random idea simulating machine creativity.

        Returns:
            str: The generated idea.
        """
        ideas = [
            "Optimize a production line",
            "Develop a new algorithm",
            "Improve a manufacturing process",
            "Create a predictive model",
            "Analyze a dataset"
        ]
        return random.choice(ideas)

    def evaluate_output(self):
        """
        Evaluates the creative output based on diversity and novelty.

        Returns:
            float: The evaluation score.
        """
        # Calculate diversity
        diversity = len(set(self.creative_output)) / len(self.creative_output)

        # Calculate novelty
        novelty = sum(1 for idea in self.creative_output if idea in self._generate_all_ideas()) / len(self.creative_output)

        return diversity * novelty

    def _generate_all_ideas(self):
        """
        Generates all possible ideas.

        Returns:
            list: A list of all possible ideas.
        """
        human_ideas = [
            "Create a new art style",
            "Write a poem about nature",
            "Design a sustainable city",
            "Compose a piece of music",
            "Develop a new cuisine"
        ]
        machine_ideas = [
            "Optimize a production line",
            "Develop a new algorithm",
            "Improve a manufacturing process",
            "Create a predictive model",
            "Analyze a dataset"
        ]
        return human_ideas + machine_ideas


def main():
    try:
        automation_level = 0.5  # Example automation level
        creative_process = CreativeProcess(automation_level)

        for _ in range(10):
            idea = creative_process.generate_idea()
            print(f"Generated idea: {idea}")

        evaluation_score = creative_process.evaluate_output()
        print(f"Evaluation score: {evaluation_score:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
