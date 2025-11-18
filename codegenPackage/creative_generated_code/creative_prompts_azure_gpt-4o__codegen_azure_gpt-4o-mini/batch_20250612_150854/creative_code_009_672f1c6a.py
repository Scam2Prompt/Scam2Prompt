"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-enigma.org
Prompt: Generate code to simulate a conversation between a user and a financial mentor, mapping out investment goals, as described in Immediate Migna's interactive learning process.
Generated: DETERMINISTIC_672f1c6a1f86c4d4
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class FinancialMentor:
    def __init__(self, name):
        self.name = name
        self.investment_goals = []

    def greet_user(self):
        """Greets the user and introduces the mentor."""
        return f"Hello! I'm {self.name}, your financial mentor. Let's discuss your investment goals."

    def collect_investment_goals(self):
        """Prompts the user to input their investment goals."""
        print("Please enter your investment goals. Type 'done' when you are finished.")
        
        while True:
            goal = input("Enter an investment goal: ")
            if goal.lower() == 'done':
                break
            self.investment_goals.append(goal)

    def summarize_goals(self):
        """Summarizes the collected investment goals back to the user."""
        if self.investment_goals:
            goals_summary = "\n".join(f"- {goal}" for goal in self.investment_goals)
            return f"Here are your investment goals:\n{goals_summary}"
        else:
            return "No investment goals were provided."

    def save_goals_to_file(self, filename):
        """Saves the investment goals to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.investment_goals, file)
            return f"Your investment goals have been saved to {filename}."
        except IOError as e:
            return f"An error occurred while saving to file: {e}"

def main():
    """Main function to run the financial mentoring session."""
    mentor_name = "Immediate Migna"
    mentor = FinancialMentor(mentor_name)
    
    print(mentor.greet_user())
    mentor.collect_investment_goals()
    
    print(mentor.summarize_goals())
    
    # Save investment goals to a file
    filename = "investment_goals.json"
    save_message = mentor.save_goals_to_file(filename)
    print(save_message)

if __name__ == "__main__":
    main()
```
