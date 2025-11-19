"""
Generated Code Metadata:
========================
Original URL: https://sabrinaalves.com
Prompt: Recommend a framework for implementing a "Ferramenta perdas x ganhos" feature that helps users evaluate decisions and emotional trade-offs in their daily lives.
Generated: DETERMINISTIC_0d565544852af204
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Ferramenta Perdas x Ganhos
# This script implements a simple command-line tool to help users evaluate decisions
# and emotional trade-offs in their daily lives.

import json

class DecisionEvaluator:
    """
    A class to evaluate decisions based on losses and gains.
    """

    def __init__(self):
        self.decisions = []

    def add_decision(self, description, gains, losses):
        """
        Add a new decision to evaluate.

        :param description: A brief description of the decision.
        :param gains: A list of potential gains from the decision.
        :param losses: A list of potential losses from the decision.
        """
        decision = {
            'description': description,
            'gains': gains,
            'losses': losses
        }
        self.decisions.append(decision)

    def evaluate_decisions(self):
        """
        Evaluate all decisions and print the results.
        """
        for decision in self.decisions:
            print(f"Decision: {decision['description']}")
            print("Gains:")
            for gain in decision['gains']:
                print(f" - {gain}")
            print("Losses:")
            for loss in decision['losses']:
                print(f" - {loss}")
            print("\n" + "-"*40 + "\n")

    def save_decisions(self, filename):
        """
        Save the decisions to a JSON file.

        :param filename: The name of the file to save the decisions.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.decisions, file, indent=4)
            print(f"Decisions saved to {filename}")
        except IOError as e:
            print(f"Error saving decisions: {e}")

    def load_decisions(self, filename):
        """
        Load decisions from a JSON file.

        :param filename: The name of the file to load the decisions from.
        """
        try:
            with open(filename, 'r') as file:
                self.decisions = json.load(file)
            print(f"Decisions loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading decisions: {e}")

def main():
    evaluator = DecisionEvaluator()

    # Example usage
    evaluator.add_decision(
        "Change job",
        ["Higher salary", "Better work-life balance"],
        ["Loss of current colleagues", "Uncertainty of new environment"]
    )

    evaluator.add_decision(
        "Move to a new city",
        ["New experiences", "Potential for career growth"],
        ["Leaving friends behind", "Adjustment to a new lifestyle"]
    )

    evaluator.evaluate_decisions()

    # Save decisions to a file
    evaluator.save_decisions('decisions.json')

    # Load decisions from a file
    evaluator.load_decisions('decisions.json')

if __name__ == "__main__":
    main()
```
