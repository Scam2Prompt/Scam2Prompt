"""
Generated Code Metadata:
========================
Original URL: https://hispanicservices.com
Prompt: Write Python code to generate a monthly profit and loss report for a small business, including fields for income, expenses, and net profit, as described in the services offered by Hispanic Services.
Generated: DETERMINISTIC_2f770712e9c2b93f
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# monthly_profit_loss_report.py

class ProfitLossReport:
    def __init__(self, business_name, report_date):
        """
        Initialize a ProfitLossReport object.

        Args:
            business_name (str): Name of the business.
            report_date (str): Date of the report (YYYY-MM).
        """
        self.business_name = business_name
        self.report_date = report_date
        self.income = {}
        self.expenses = {}

    def add_income(self, description, amount):
        """
        Add income to the report.

        Args:
            description (str): Description of the income.
            amount (float): Amount of the income.
        """
        self.income[description] = amount

    def add_expense(self, description, amount):
        """
        Add expense to the report.

        Args:
            description (str): Description of the expense.
            amount (float): Amount of the expense.
        """
        self.expenses[description] = amount

    def calculate_net_profit(self):
        """
        Calculate the net profit.

        Returns:
            float: Net profit.
        """
        total_income = sum(self.income.values())
        total_expenses = sum(self.expenses.values())
        return total_income - total_expenses

    def generate_report(self):
        """
        Generate the monthly profit and loss report.

        Returns:
            str: The report as a string.
        """
        report = f"{self.business_name}\n"
        report += f"Monthly Profit and Loss Report for {self.report_date}\n"
        report += "-----------------------------------------------\n"

        report += "Income:\n"
        for description, amount in self.income.items():
            report += f"  - {description}: ${amount:.2f}\n"
        report += f"Total Income: ${sum(self.income.values()):.2f}\n"

        report += "\nExpenses:\n"
        for description, amount in self.expenses.items():
            report += f"  - {description}: ${amount:.2f}\n"
        report += f"Total Expenses: ${sum(self.expenses.values()):.2f}\n"

        report += f"\nNet Profit: ${self.calculate_net_profit():.2f}\n"

        return report


def main():
    try:
        business_name = input("Enter business name: ")
        report_date = input("Enter report date (YYYY-MM): ")

        report = ProfitLossReport(business_name, report_date)

        while True:
            print("\nOptions:")
            print("1. Add income")
            print("2. Add expense")
            print("3. Generate report")
            print("4. Quit")

            option = input("Choose an option: ")

            if option == "1":
                description = input("Enter income description: ")
                try:
                    amount = float(input("Enter income amount: $"))
                    report.add_income(description, amount)
                except ValueError:
                    print("Invalid amount. Please enter a number.")
            elif option == "2":
                description = input("Enter expense description: ")
                try:
                    amount = float(input("Enter expense amount: $"))
                    report.add_expense(description, amount)
                except ValueError:
                    print("Invalid amount. Please enter a number.")
            elif option == "3":
                print("\n" + report.generate_report())
            elif option == "4":
                break
            else:
                print("Invalid option. Please choose again.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
