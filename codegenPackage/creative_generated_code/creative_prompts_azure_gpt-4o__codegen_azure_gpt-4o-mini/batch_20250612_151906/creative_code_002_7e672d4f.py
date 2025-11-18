"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrium.io
Prompt: Generate code to simulate decision-making workflows using Arbitrium's management control system principles.
Generated: DETERMINISTIC_7e672d4f85b3cf78
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DecisionNode:
    """
    A class representing a decision node in the workflow.
    Each node can have multiple child nodes based on the decisions made.
    """

    def __init__(self, question, yes_node=None, no_node=None):
        """
        Initializes a DecisionNode with a question and optional child nodes.

        :param question: The question to be asked at this node.
        :param yes_node: The next DecisionNode if the answer is yes.
        :param no_node: The next DecisionNode if the answer is no.
        """
        self.question = question
        self.yes_node = yes_node
        self.no_node = no_node

    def make_decision(self, answer):
        """
        Processes the decision based on the given answer.

        :param answer: The user's answer (True for yes, False for no).
        :return: Result of the workflow based on the answer.
        """
        if answer:
            if self.yes_node:
                return self.yes_node.make_decision(self.yes_node.ask_question())
            else:
                return "End of workflow: Yes path chosen."
        else:
            if self.no_node:
                return self.no_node.make_decision(self.no_node.ask_question())
            else:
                return "End of workflow: No path chosen."

    def ask_question(self):
        """
        Asks the question at this node and returns the user's answer.

        :return: User's answer as a boolean.
        """
        while True:
            try:
                response = input(f"{self.question} (yes/no): ").strip().lower()
                if response not in ('yes', 'no'):
                    raise ValueError("Invalid input. Please answer with 'yes' or 'no'.")
                return response == 'yes'
            except ValueError as e:
                print(e)


def main():
    """
    Main function to set up the decision workflow and start the process.
    """
    # Define the workflow structure using DecisionNodes
    node3 = DecisionNode("Is the project aligned with company goals?")
    node2 = DecisionNode("Is the budget sufficient?", yes_node=node3)
    root = DecisionNode("Is the project viable?", yes_node=node2)

    print("Starting Decision Workflow")
    
    # Start the decision-making process
    result = root.make_decision(root.ask_question())
    print(result)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
