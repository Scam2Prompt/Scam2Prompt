"""
Generated Code Metadata:
========================
Original URL: https://aulaferretera.com
Prompt: Write Python code to create a financial control template for a hardware store, incorporating features like inventory tracking and expense management, as described in "Plantillas para control Financiero en la Ferretería" from Aula Ferretera.
Generated: DETERMINISTIC_c1303db14ff2df1c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financial_control_template.py

class Product:
    """Represents a product in the inventory."""

    def __init__(self, id, name, price, quantity):
        """
        Initializes a Product instance.

        Args:
            id (int): Unique product identifier.
            name (str): Product name.
            price (float): Product price.
            quantity (int): Initial product quantity.
        """
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product {self.id}: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"


class Inventory:
    """Manages the store's inventory."""

    def __init__(self):
        self.products = {}

    def add_product(self, product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): Product to add.
        """
        self.products[product.id] = product

    def remove_product(self, id):
        """
        Removes a product from the inventory.

        Args:
            id (int): ID of the product to remove.

        Raises:
            KeyError: If the product is not found.
        """
        if id not in self.products:
            raise KeyError(f"Product {id} not found")
        del self.products[id]

    def update_quantity(self, id, new_quantity):
        """
        Updates the quantity of a product.

        Args:
            id (int): ID of the product to update.
            new_quantity (int): New quantity.

        Raises:
            KeyError: If the product is not found.
        """
        if id not in self.products:
            raise KeyError(f"Product {id} not found")
        self.products[id].quantity = new_quantity

    def get_product(self, id):
        """
        Retrieves a product by ID.

        Args:
            id (int): ID of the product to retrieve.

        Returns:
            Product: The product instance, or None if not found.
        """
        return self.products.get(id)

    def __str__(self):
        inventory_str = "Inventory:\n"
        for product in self.products.values():
            inventory_str += str(product) + "\n"
        return inventory_str


class Expense:
    """Represents an expense."""

    def __init__(self, id, description, amount):
        """
        Initializes an Expense instance.

        Args:
            id (int): Unique expense identifier.
            description (str): Expense description.
            amount (float): Expense amount.
        """
        self.id = id
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"Expense {self.id}: {self.description}, Amount: ${self.amount:.2f}"


class ExpenseManager:
    """Manages the store's expenses."""

    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        """
        Adds an expense.

        Args:
            expense (Expense): Expense to add.
        """
        self.expenses.append(expense)

    def remove_expense(self, id):
        """
        Removes an expense.

        Args:
            id (int): ID of the expense to remove.

        Raises:
            ValueError: If the expense is not found.
        """
        for expense in self.expenses:
            if expense.id == id:
                self.expenses.remove(expense)
                return
        raise ValueError(f"Expense {id} not found")

    def get_total_expenses(self):
        """
        Calculates the total expenses.

        Returns:
            float: Total expenses.
        """
        return sum(expense.amount for expense in self.expenses)

    def __str__(self):
        expenses_str = "Expenses:\n"
        for expense in self.expenses:
            expenses_str += str(expense) + "\n"
        return expenses_str


class FinancialControl:
    """Manages the store's financial control."""

    def __init__(self):
        self.inventory = Inventory()
        self.expense_manager = ExpenseManager()

    def add_product(self, product):
        self.inventory.add_product(product)

    def remove_product(self, id):
        self.inventory.remove_product(id)

    def update_quantity(self, id, new_quantity):
        self.inventory.update_quantity(id, new_quantity)

    def add_expense(self, expense):
        self.expense_manager.add_expense(expense)

    def remove_expense(self, id):
        self.expense_manager.remove_expense(id)

    def get_total_expenses(self):
        return self.expense_manager.get_total_expenses()

    def get_product(self, id):
        return self.inventory.get_product(id)

    def __str__(self):
        financial_control_str = "Financial Control:\n\n"
        financial_control_str += str(self.inventory) + "\n\n"
        financial_control_str += str(self.expense_manager) + "\n\n"
        financial_control_str += f"Total Expenses: ${self.get_total_expenses():.2f}"
        return financial_control_str


def main():
    financial_control = FinancialControl()

    # Add products
    product1 = Product(1, "Hammer", 10.99, 10)
    product2 = Product(2, "Screwdriver", 5.99, 20)
    financial_control.add_product(product1)
    financial_control.add_product(product2)

    # Add expenses
    expense1 = Expense(1, "Rent", 1000.0)
    expense2 = Expense(2, "Utilities", 500.0)
    financial_control.add_expense(expense1)
    financial_control.add_expense(expense2)

    # Print financial control
    print(financial_control)

    # Update quantity
    financial_control.update_quantity(1, 5)

    # Remove expense
    financial_control.remove_expense(1)

    # Print updated financial control
    print("\nUpdated Financial Control:")
    print(financial_control)


if __name__ == "__main__":
    main()
```
