"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Write a Python script to analyze user input and suggest strategies for overcoming waning motivation, based on the tactics described in the "Action Acceleration" phase.
Generated: DETERMINISTIC_8fc42d465164b163
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# motivation_analyzer.py

class MotivationAnalyzer:
    """
    Analyzes user input and suggests strategies for overcoming waning motivation.
    """

    def __init__(self):
        # Define tactics for overcoming waning motivation
        self.tactics = {
            "break_down_goals": "Break down large goals into smaller, manageable tasks.",
            "create_schedule": "Create a schedule and stick to it.",
            "find_accountability": "Find an accountability partner or join a community.",
            "celebrate_progress": "Celebrate small wins to build momentum.",
            "identify_distractions": "Identify and eliminate distractions.",
            "reward_system": "Implement a reward system for achieving milestones.",
        }

    def analyze_input(self, user_input):
        """
        Analyze user input and suggest strategies.

        Args:
            user_input (str): User's description of their motivation struggles.

        Returns:
            list: Suggested strategies for overcoming waning motivation.
        """
        # Convert user input to lowercase for case-insensitive analysis
        user_input = user_input.lower()

        # Initialize list to store suggested strategies
        suggested_strategies = []

        # Check if user mentions feeling overwhelmed
        if "overwhelmed" in user_input or "stressed" in user_input:
            suggested_strategies.append(self.tactics["break_down_goals"])

        # Check if user mentions procrastination
        if "procrastinate" in user_input or "putting things off" in user_input:
            suggested_strategies.append(self.tactics["create_schedule"])
            suggested_strategies.append(self.tactics["identify_distractions"])

        # Check if user mentions lack of motivation
        if "unmotivated" in user_input or "lack of motivation" in user_input:
            suggested_strategies.append(self.tactics["find_accountability"])
            suggested_strategies.append(self.tactics["reward_system"])

        # Check if user mentions feeling stuck
        if "stuck" in user_input or "plateau" in user_input:
            suggested_strategies.append(self.tactics["celebrate_progress"])

        # If no specific struggles mentioned, provide general suggestions
        if not suggested_strategies:
            suggested_strategies = list(self.tactics.values())

        return suggested_strategies


def main():
    analyzer = MotivationAnalyzer()

    print("Motivation Analyzer")
    print("--------------------")

    while True:
        user_input = input("Please describe your motivation struggles (or 'quit' to exit): ")

        if user_input.lower() == "quit":
            break

        try:
            suggested_strategies = analyzer.analyze_input(user_input)

            print("\nSuggested Strategies:")
            for i, strategy in enumerate(suggested_strategies, start=1):
                print(f"{i}. {strategy}")

            print()
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
