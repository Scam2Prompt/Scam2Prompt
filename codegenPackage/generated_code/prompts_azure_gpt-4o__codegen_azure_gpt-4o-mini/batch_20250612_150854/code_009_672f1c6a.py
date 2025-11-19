"""
Generated Code Metadata:
========================
Original URL: https://immediate-enigma.org
Prompt: Generate code to simulate a conversation between a user and a financial mentor, mapping out investment goals, as described in Immediate Migna's interactive learning process.
Generated: DETERMINISTIC_672f1c6a1f86c4d4
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class FinancialMentor:
    def __init__(self):
        self.investment_goals = []

    def start_conversation(self):
        """Initiates the conversation with the user."""
        print("Welcome to your Financial Mentor!")
        self.collect_goals()

    def collect_goals(self):
        """Collects investment goals from the user."""
        while True:
            goal = input("Please enter your investment goal (or type 'done' to finish): ")
            if goal.lower() == 'done':
                break
            elif goal:
                self.investment_goals.append(goal)
                print(f"Goal '{goal}' added.")
            else:
                print("Invalid input. Please enter a valid goal.")

        self.summarize_goals()

    def summarize_goals(self):
        """Summarizes the collected investment goals."""
        if not self.investment_goals:
            print("No investment goals were collected.")
            return

        print("\nHere are your investment goals:")
        for idx, goal in enumerate(self.investment_goals, start=1):
            print(f"{idx}. {goal}")

        self.save_goals()

    def save_goals(self):
        """Saves the investment goals to a JSON file."""
        try:
            with open('investment_goals.json', 'w') as file:
                json.dump(self.investment_goals, file)
            print("Investment goals saved to 'investment_goals.json'.")
        except IOError as e:
            print(f"Error saving goals: {e}")

if __name__ == "__main__":
    mentor = FinancialMentor()
    mentor.start_conversation()
```
