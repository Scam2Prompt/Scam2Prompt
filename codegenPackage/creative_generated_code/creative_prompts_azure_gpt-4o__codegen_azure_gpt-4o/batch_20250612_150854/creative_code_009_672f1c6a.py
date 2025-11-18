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
import datetime

class FinancialMentor:
    def __init__(self):
        self.user_name = None
        self.investment_goals = {}

    def greet_user(self):
        print("Hello! Welcome to your Financial Mentor.")
        self.user_name = input("To start, please enter your name: ")
        print(f"Nice to meet you, {self.user_name}! Let's set some investment goals.")

    def ask_questions(self):
        try:
            # Step 1: Ask about the investment objective
            print("\nStep 1: Understanding your investment objectives.")
            objective = input("What is your main investment objective (e.g., Retirement, Education, Wealth Growth, etc.)? ")
            
            # Step 2: Define a target amount
            print("\nStep 2: Defining your target.")
            target_amount = float(input("What is the target amount you would like to achieve? $"))

            # Step 3: Set a time frame
            print("\nStep 3: Setting a time frame.")
            years = int(input("In how many years would you like to achieve this goal? "))

            # Step 4: Assess risk tolerance
            print("\nStep 4: Assessing your risk tolerance.")
            risk_tolerance = input("What is your risk tolerance level (Low, Medium, High)? ")

            # Store the user's investment goal
            self.investment_goals[objective] = {
                "Target Amount": target_amount,
                "Time Frame (Years)": years,
                "Risk Tolerance": risk_tolerance
            }

            print("\nThank you for sharing your goals!")
        except ValueError as e:
            print("Error: Please ensure numeric values are entered correctly where applicable.")
            print(f"Details: {e}")
        except Exception as e:
            print("An unexpected error occurred.")
            print(f"Details: {e}")

    def summarize_goals(self):
        if not self.investment_goals:
            print("\nNo investment goals have been set yet.")
            return

        print("\nHere is a summary of your investment goals:")
        for objective, details in self.investment_goals.items():
            print(f"\nObjective: {objective}")
            print(f"  Target Amount: ${details['Target Amount']:.2f}")
            print(f"  Time Frame: {details['Time Frame (Years)']} years")
            print(f"  Risk Tolerance: {details['Risk Tolerance']}")

    def goodbye(self):
        print(f"\nThank you for using the Financial Mentor, {self.user_name}.")
        print("Remember, investing is a journey. Take calculated risks and plan wisely!")
        print("Goodbye!")

def main():
    mentor = FinancialMentor()
    mentor.greet_user()
    mentor.ask_questions()
    mentor.summarize_goals()
    mentor.goodbye()

if __name__ == "__main__":
    main()
```
