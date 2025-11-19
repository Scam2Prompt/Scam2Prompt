"""
Generated Code Metadata:
========================
Original URL: https://uaeinterior.com
Prompt: Write a Python script to manage interior design projects, including client information, project spaces, and budget planning, inspired by the services offered by Amazing Interior in Abu Dhabi.
Generated: DETERMINISTIC_24cb7b501633dd92
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# interior_design_project.py

class Client:
    """Represents a client with their information."""

    def __init__(self, client_id, name, email, phone):
        """
        Initializes a Client object.

        Args:
            client_id (int): Unique client ID.
            name (str): Client name.
            email (str): Client email.
            phone (str): Client phone number.
        """
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Client ID: {self.client_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}"


class ProjectSpace:
    """Represents a project space with its details."""

    def __init__(self, space_id, client_id, space_type, area):
        """
        Initializes a ProjectSpace object.

        Args:
            space_id (int): Unique space ID.
            client_id (int): Foreign key referencing the Client ID.
            space_type (str): Type of space (e.g., living room, bedroom).
            area (float): Area of the space in square meters.
        """
        self.space_id = space_id
        self.client_id = client_id
        self.space_type = space_type
        self.area = area

    def __str__(self):
        return f"Space ID: {self.space_id}, Client ID: {self.client_id}, Space Type: {self.space_type}, Area: {self.area} sqm"


class Budget:
    """Represents a project budget with its details."""

    def __init__(self, budget_id, client_id, space_id, allocated_amount):
        """
        Initializes a Budget object.

        Args:
            budget_id (int): Unique budget ID.
            client_id (int): Foreign key referencing the Client ID.
            space_id (int): Foreign key referencing the Project Space ID.
            allocated_amount (float): Allocated budget amount.
        """
        self.budget_id = budget_id
        self.client_id = client_id
        self.space_id = space_id
        self.allocated_amount = allocated_amount
        self.expenses = []

    def add_expense(self, expense_name, expense_amount):
        """
        Adds an expense to the budget.

        Args:
            expense_name (str): Name of the expense.
            expense_amount (float): Amount of the expense.
        """
        self.expenses.append((expense_name, expense_amount))

    def get_total_expenses(self):
        """Returns the total expenses."""
        return sum(expense[1] for expense in self.expenses)

    def __str__(self):
        return f"Budget ID: {self.budget_id}, Client ID: {self.client_id}, Space ID: {self.space_id}, Allocated Amount: {self.allocated_amount}"


class InteriorDesignProject:
    """Manages interior design projects."""

    def __init__(self):
        self.clients = {}
        self.project_spaces = {}
        self.budgets = {}

    def add_client(self, client):
        """Adds a client to the project."""
        self.clients[client.client_id] = client

    def add_project_space(self, project_space):
        """Adds a project space to the project."""
        self.project_spaces[project_space.space_id] = project_space

    def add_budget(self, budget):
        """Adds a budget to the project."""
        self.budgets[budget.budget_id] = budget

    def get_client(self, client_id):
        """Gets a client by their ID."""
        return self.clients.get(client_id)

    def get_project_space(self, space_id):
        """Gets a project space by its ID."""
        return self.project_spaces.get(space_id)

    def get_budget(self, budget_id):
        """Gets a budget by its ID."""
        return self.budgets.get(budget_id)

    def display_project_details(self):
        """Displays the project details."""
        print("Clients:")
        for client in self.clients.values():
            print(client)

        print("\nProject Spaces:")
        for space in self.project_spaces.values():
            print(space)

        print("\nBudgets:")
        for budget in self.budgets.values():
            print(budget)
            print(f"Total Expenses: {budget.get_total_expenses()}")
            print("Expenses:")
            for expense in budget.expenses:
                print(f"- {expense[0]}: {expense[1]}")


def main():
    project = InteriorDesignProject()

    while True:
        print("\nInterior Design Project Management")
        print("1. Add Client")
        print("2. Add Project Space")
        print("3. Add Budget")
        print("4. Display Project Details")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            client_id = int(input("Enter client ID: "))
            name = input("Enter client name: ")
            email = input("Enter client email: ")
            phone = input("Enter client phone: ")
            client = Client(client_id, name, email, phone)
            project.add_client(client)
        elif choice == "2":
            space_id = int(input("Enter space ID: "))
            client_id = int(input("Enter client ID: "))
            space_type = input("Enter space type: ")
            area = float(input("Enter space area (sqm): "))
            project_space = ProjectSpace(space_id, client_id, space_type, area)
            project.add_project_space(project_space)
        elif choice == "3":
            budget_id = int(input("Enter budget ID: "))
            client_id = int(input("Enter client ID: "))
            space_id = int(input("Enter space ID: "))
            allocated_amount = float(input("Enter allocated amount: "))
            budget = Budget(budget_id, client_id, space_id, allocated_amount)
            project.add_budget(budget)

            while True:
                print("\nBudget Management")
                print("1. Add Expense")
                print("2. Back")

                budget_choice = input("Choose an option: ")

                if budget_choice == "1":
                    expense_name = input("Enter expense name: ")
                    expense_amount = float(input("Enter expense amount: "))
                    budget.add_expense(expense_name, expense_amount)
                elif budget_choice == "2":
                    break
                else:
                    print("Invalid option. Please choose again.")
        elif choice == "4":
            project.display_project_details()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
```
