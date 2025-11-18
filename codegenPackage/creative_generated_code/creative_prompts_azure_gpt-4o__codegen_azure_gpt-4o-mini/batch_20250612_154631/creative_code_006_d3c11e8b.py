"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeinvestmentslimited.org
Prompt: Develop code to simulate a financial advisory chatbot that provides budget planning recommendations, based on the services described by Finance Investment Limited.
Generated: DETERMINISTIC_d3c11e8b29c437df
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class FinancialAdvisoryChatbot:
    """
    A simple financial advisory chatbot that provides budget planning recommendations.
    """

    def __init__(self):
        # Initialize the chatbot with default services and user data
        self.services = {
            "basic_budgeting": "A basic service to track your income and expenses.",
            "investment_advice": "Personalized investment advice based on your risk profile.",
            "retirement_planning": "Guidance on how to save for retirement based on your goals.",
            "debt_management": "Strategies to manage and reduce your debts effectively."
        }
        self.user_data = {}

    def greet_user(self):
        """Greets the user and presents available services."""
        print("Welcome to Finance Investment Limited Chatbot!")
        print("Here are the services we offer:")
        for service in self.services:
            print(f"- {service}: {self.services[service]}")
    
    def get_user_budget(self):
        """Prompts user to input their budget details and stores them."""
        try:
            income = float(input("Please enter your monthly income: "))
            expenses = float(input("Please enter your monthly expenses: "))
            self.user_data['income'] = income
            self.user_data['expenses'] = expenses
        except ValueError:
            print("Invalid input. Please enter numeric values for income and expenses.")
            return self.get_user_budget()  # Retry getting input

    def analyze_budget(self):
        """Analyzes the user's budget and provides recommendations."""
        income = self.user_data.get('income', 0)
        expenses = self.user_data.get('expenses', 0)

        if income <= 0:
            print("Income must be greater than zero to provide recommendations.")
            return

        savings = income - expenses
        if savings < 0:
            print("You are currently overspending. Consider reducing your expenses.")
        elif savings < income * 0.2:
            print("You are saving less than 20% of your income. Aim to save more.")
        else:
            print("Great job! You are saving a healthy portion of your income.")

        self.suggest_services()

    def suggest_services(self):
        """Suggests relevant services based on user's budget analysis."""
        print("Based on your budget, we recommend the following services:")
        if self.user_data['expenses'] > self.user_data['income']:
            print("- Debt Management: To help you manage overspending.")
        elif self.user_data['income'] * 0.2 > self.user_data['expenses']:
            print("- Basic Budgeting: To maintain your financial health.")
        else:
            print("- Investment Advice: To help maximize your savings.")

    def run_chatbot(self):
        """Runs the chatbot interaction loop."""
        self.greet_user()
        self.get_user_budget()
        self.analyze_budget()


if __name__ == "__main__":
    try:
        chatbot = FinancialAdvisoryChatbot()
        chatbot.run_chatbot()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
