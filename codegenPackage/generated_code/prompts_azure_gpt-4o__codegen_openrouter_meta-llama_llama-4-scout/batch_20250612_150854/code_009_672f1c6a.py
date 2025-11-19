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
# investment_goals.py

class FinancialMentor:
    def __init__(self):
        self.investment_goals = {}

    def start_conversation(self):
        print("Welcome to the investment goal simulator!")
        self.get_investor_info()

    def get_investor_info(self):
        # Get investor's name and current financial situation
        name = input("Please enter your name: ")
        income = self.get_positive_float("What is your annual income? $")
        savings = self.get_positive_float("How much do you have in savings? $")

        self.investment_goals[name] = {"income": income, "savings": savings}

        self.determine_investment_goals(name)

    def determine_investment_goals(self, name):
        print(f"\nHello {name}, let's discuss your investment goals.")
        goal_amount = self.get_positive_float("How much do you want to invest? $")
        goal_timeframe = self.get_timeframe("What is your investment timeframe (short-term, medium-term, long-term)? ")

        self.investment_goals[name]["goal_amount"] = goal_amount
        self.investment_goals[name]["goal_timeframe"] = goal_timeframe

        self.suggest_investment_strategies(name)

    def suggest_investment_strategies(self, name):
        goal_amount = self.investment_goals[name]["goal_amount"]
        goal_timeframe = self.investment_goals[name]["goal_timeframe"]
        income = self.investment_goals[name]["income"]
        savings = self.investment_goals[name]["savings"]

        if goal_timeframe == "short-term":
            print(f"\nFor a {goal_timeframe} goal of ${goal_amount:.2f}, we suggest a high-yield savings account or a short-term CD.")
        elif goal_timeframe == "medium-term":
            print(f"\nFor a {goal_timeframe} goal of ${goal_amount:.2f}, we suggest a diversified portfolio of stocks and bonds.")
        elif goal_timeframe == "long-term":
            print(f"\nFor a {goal_timeframe} goal of ${goal_amount:.2f}, we suggest a more aggressive portfolio with a higher stock allocation.")

        self.risk_tolerance_assessment(name)

    def risk_tolerance_assessment(self, name):
        print(f"\n{ name}, let's assess your risk tolerance.")
        risk_tolerance = input("Are you comfortable with high-risk, high-reward investments? (yes/no): ")

        if risk_tolerance.lower() == "yes":
            print(f"\nBased on your risk tolerance, we suggest a more aggressive investment strategy.")
        else:
            print(f"\nBased on your risk tolerance, we suggest a more conservative investment strategy.")

        self.investment_summary(name)

    def investment_summary(self, name):
        print(f"\nInvestment Summary for {name}:")
        print(f"Income: ${self.investment_goals[name]['income']:.2f}")
        print(f"Savings: ${self.investment_goals[name]['savings']:.2f}")
        print(f"Goal Amount: ${self.investment_goals[name]['goal_amount']:.2f}")
        print(f"Goal Timeframe: {self.investment_goals[name]['goal_timeframe']}")

    @staticmethod
    def get_positive_float(prompt):
        while True:
            try:
                value = float(input(prompt))
                if value > 0:
                    return value
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    @staticmethod
    def get_timeframe(prompt):
        while True:
            timeframe = input(prompt).lower()
            if timeframe in ["short-term", "medium-term", "long-term"]:
                return timeframe
            else:
                print("Invalid input. Please enter short-term, medium-term, or long-term.")

def main():
    mentor = FinancialMentor()
    mentor.start_conversation()

if __name__ == "__main__":
    main()
```
