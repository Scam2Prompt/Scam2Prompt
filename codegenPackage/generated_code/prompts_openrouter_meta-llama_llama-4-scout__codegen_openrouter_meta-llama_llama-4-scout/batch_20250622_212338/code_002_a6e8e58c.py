"""
Generated Code Metadata:
========================
Original URL: https://lethmixedslowpitch.com
Prompt: Create a comprehensive budget for a slo-pitch softball tournament using a budget generator tool and provide a detailed breakdown of estimated costs.
Generated: DETERMINISTIC_a6e8e58cb4e71c85
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# budget_generator.py

class BudgetGenerator:
    def __init__(self, tournament_name, num_teams, num_games, team_registration_fee, 
                 equipment_cost, facility_rental_cost, umpire_fee, insurance_cost, 
                 marketing_cost, food_beverage_cost, contingency_fund_percentage):
        """
        Initialize the budget generator with tournament details.

        Args:
            tournament_name (str): Name of the tournament.
            num_teams (int): Number of teams participating.
            num_games (int): Number of games in the tournament.
            team_registration_fee (float): Registration fee per team.
            equipment_cost (float): Cost of equipment rental/purchase.
            facility_rental_cost (float): Cost of facility rental.
            umpire_fee (float): Umpire fee per game.
            insurance_cost (float): Cost of insurance.
            marketing_cost (float): Cost of marketing and promotion.
            food_beverage_cost (float): Cost of food and beverages.
            contingency_fund_percentage (float): Percentage of total costs for contingency fund.
        """
        self.tournament_name = tournament_name
        self.num_teams = num_teams
        self.num_games = num_games
        self.team_registration_fee = team_registration_fee
        self.equipment_cost = equipment_cost
        self.facility_rental_cost = facility_rental_cost
        self.umpire_fee = umpire_fee
        self.insurance_cost = insurance_cost
        self.marketing_cost = marketing_cost
        self.food_beverage_cost = food_beverage_cost
        self.contingency_fund_percentage = contingency_fund_percentage

    def calculate_revenue(self):
        """
        Calculate total revenue from team registration fees.

        Returns:
            float: Total revenue.
        """
        return self.num_teams * self.team_registration_fee

    def calculate_expenses(self):
        """
        Calculate total expenses.

        Returns:
            dict: Dictionary of expenses with descriptions.
        """
        expenses = {
            "Equipment": self.equipment_cost,
            "Facility Rental": self.facility_rental_cost,
            "Umpire Fees": self.num_games * self.umpire_fee,
            "Insurance": self.insurance_cost,
            "Marketing": self.marketing_cost,
            "Food and Beverages": self.food_beverage_cost
        }
        return expenses

    def calculate_total_expenses(self, expenses):
        """
        Calculate total expenses.

        Args:
            expenses (dict): Dictionary of expenses.

        Returns:
            float: Total expenses.
        """
        return sum(expenses.values())

    def calculate_contingency_fund(self, total_expenses):
        """
        Calculate contingency fund amount.

        Args:
            total_expenses (float): Total expenses.

        Returns:
            float: Contingency fund amount.
        """
        return total_expenses * (self.contingency_fund_percentage / 100)

    def generate_budget(self):
        """
        Generate a comprehensive budget for the tournament.

        Returns:
            dict: Dictionary containing revenue, expenses, and contingency fund information.
        """
        revenue = self.calculate_revenue()
        expenses = self.calculate_expenses()
        total_expenses = self.calculate_total_expenses(expenses)
        contingency_fund = self.calculate_contingency_fund(total_expenses)

        budget = {
            "Tournament Name": self.tournament_name,
            "Revenue": f"${revenue:,.2f}",
            "Expenses": expenses,
            "Total Expenses": f"${total_expenses:,.2f}",
            "Contingency Fund": f"${contingency_fund:,.2f}",
            "Net Profit/Loss": f"${revenue - total_expenses - contingency_fund:,.2f}"
        }
        return budget


def main():
    try:
        tournament_name = "Slo-Pitch Softball Tournament"
        num_teams = 10
        num_games = 20
        team_registration_fee = 500.0
        equipment_cost = 1000.0
        facility_rental_cost = 2000.0
        umpire_fee = 100.0
        insurance_cost = 500.0
        marketing_cost = 1500.0
        food_beverage_cost = 2000.0
        contingency_fund_percentage = 10.0

        budget_generator = BudgetGenerator(tournament_name, num_teams, num_games, 
                                          team_registration_fee, equipment_cost, 
                                          facility_rental_cost, umpire_fee, 
                                          insurance_cost, marketing_cost, 
                                          food_beverage_cost, contingency_fund_percentage)

        budget = budget_generator.generate_budget()

        print("# Budget Breakdown")
        print(f"## {budget['Tournament Name']}")
        print(f"### Revenue: {budget['Revenue']}")
        print("### Expenses:")
        for expense, cost in budget["Expenses"].items():
            print(f"* {expense}: ${cost:,.2f}")
        print(f"### Total Expenses: {budget['Total Expenses']}")
        print(f"### Contingency Fund: {budget['Contingency Fund']}")
        print(f"### Net Profit/Loss: {budget['Net Profit/Loss']}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
