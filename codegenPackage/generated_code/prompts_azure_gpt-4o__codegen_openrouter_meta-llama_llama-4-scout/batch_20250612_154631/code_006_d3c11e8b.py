"""
Generated Code Metadata:
========================
Original URL: https://financeinvestmentslimited.org
Prompt: Develop code to simulate a financial advisory chatbot that provides budget planning recommendations, based on the services described by Finance Investment Limited.
Generated: DETERMINISTIC_d3c11e8b29c437df
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financial_advisor.py

class FinancialAdvisor:
    """
    A chatbot that provides budget planning recommendations.
    """

    def __init__(self):
        self.income_tax_rate = 0.25  # default income tax rate
        self.expenses_categories = {
            "housing": 0.3,
            "transportation": 0.1,
            "food": 0.1,
            "entertainment": 0.05,
            "savings": 0.2,
            "emergency_fund": 0.1,
            "debt_repayment": 0.05,
        }

    def calculate_net_income(self, gross_income):
        """
        Calculate net income based on gross income and income tax rate.

        Args:
            gross_income (float): The user's gross income.

        Returns:
            float: The user's net income.
        """
        return gross_income * (1 - self.income_tax_rate)

    def calculate_expenses(self, net_income):
        """
        Calculate expenses based on net income and expenses categories.

        Args:
            net_income (float): The user's net income.

        Returns:
            dict: A dictionary of expenses categories and their corresponding amounts.
        """
        expenses = {}
        for category, percentage in self.expenses_categories.items():
            expenses[category] = net_income * percentage
        return expenses

    def provide_recommendations(self, gross_income):
        """
        Provide budget planning recommendations based on the user's gross income.

        Args:
            gross_income (float): The user's gross income.

        Returns:
            dict: A dictionary of budget planning recommendations.
        """
        try:
            net_income = self.calculate_net_income(gross_income)
            expenses = self.calculate_expenses(net_income)
            recommendations = {
                "net_income": net_income,
                "expenses": expenses,
                "savings": expenses["savings"],
                "emergency_fund": expenses["emergency_fund"],
                "debt_repayment": expenses["debt_repayment"],
            }
            return recommendations
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None


def main():
    advisor = FinancialAdvisor()
    gross_income = float(input("Enter your gross income: $"))
    recommendations = advisor.provide_recommendations(gross_income)

    if recommendations:
        print("\nBudget Planning Recommendations:")
        print("----------------------------------")
        print(f"Net Income: ${recommendations['net_income']:.2f}")
        print("Expenses:")
        for category, amount in recommendations["expenses"].items():
            print(f"  {category.capitalize()}: ${amount:.2f}")
        print(f"Savings: ${recommendations['savings']:.2f}")
        print(f"Emergency Fund: ${recommendations['emergency_fund']:.2f}")
        print(f"Debt Repayment: ${recommendations['debt_repayment']:.2f}")


if __name__ == "__main__":
    main()
```
