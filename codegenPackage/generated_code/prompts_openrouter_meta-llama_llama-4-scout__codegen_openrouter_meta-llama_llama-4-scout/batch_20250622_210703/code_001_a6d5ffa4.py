"""
Generated Code Metadata:
========================
Original URL: https://aulaferretera.com
Prompt: Create a template for financial control in a hardware store using the guidelines provided by Aula Ferretera.
Generated: DETERMINISTIC_a6d5ffa44712f9a7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financial_control_template.py

class FinancialControl:
    """
    A class to manage financial control in a hardware store.

    Attributes:
    -----------
    income : float
        The total income of the store.
    expenses : float
        The total expenses of the store.
    products : dict
        A dictionary of products with their prices and quantities.

    Methods:
    --------
    add_income(amount)
        Adds income to the store.
    add_expense(amount, description)
        Adds an expense to the store.
    add_product(name, price, quantity)
        Adds a product to the store.
    remove_product(name)
        Removes a product from the store.
    update_product_quantity(name, quantity)
        Updates the quantity of a product.
    calculate_profit()
        Calculates the profit of the store.
    """

    def __init__(self):
        self.income = 0.0
        self.expenses = 0.0
        self.products = {}

    def add_income(self, amount):
        """
        Adds income to the store.

        Args:
        -----
        amount (float): The amount of income to add.

        Raises:
        ------
        ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Income cannot be negative.")
        self.income += amount

    def add_expense(self, amount, description):
        """
        Adds an expense to the store.

        Args:
        -----
        amount (float): The amount of expense to add.
        description (str): A description of the expense.

        Raises:
        ------
        ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Expense cannot be negative.")
        self.expenses += amount
        print(f"Expense added: {description} - ${amount:.2f}")

    def add_product(self, name, price, quantity):
        """
        Adds a product to the store.

        Args:
        -----
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product.

        Raises:
        ------
        ValueError: If the price or quantity is negative.
        """
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity cannot be negative.")
        self.products[name] = {"price": price, "quantity": quantity}

    def remove_product(self, name):
        """
        Removes a product from the store.

        Args:
        -----
        name (str): The name of the product to remove.

        Raises:
        ------
        KeyError: If the product does not exist.
        """
        if name not in self.products:
            raise KeyError("Product does not exist.")
        del self.products[name]

    def update_product_quantity(self, name, quantity):
        """
        Updates the quantity of a product.

        Args:
        -----
        name (str): The name of the product.
        quantity (int): The new quantity of the product.

        Raises:
        ------
        KeyError: If the product does not exist.
        ValueError: If the quantity is negative.
        """
        if name not in self.products:
            raise KeyError("Product does not exist.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.products[name]["quantity"] = quantity

    def calculate_profit(self):
        """
        Calculates the profit of the store.

        Returns:
        -------
        float: The profit of the store.
        """
        total_revenue = sum(product["price"] * product["quantity"] for product in self.products.values())
        return total_revenue - self.expenses


def main():
    financial_control = FinancialControl()

    while True:
        print("\nFinancial Control Menu:")
        print("1. Add income")
        print("2. Add expense")
        print("3. Add product")
        print("4. Remove product")
        print("5. Update product quantity")
        print("6. Calculate profit")
        print("7. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                amount = float(input("Enter income amount: "))
                financial_control.add_income(amount)
            elif choice == "2":
                amount = float(input("Enter expense amount: "))
                description = input("Enter expense description: ")
                financial_control.add_expense(amount, description)
            elif choice == "3":
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                financial_control.add_product(name, price, quantity)
            elif choice == "4":
                name = input("Enter product name: ")
                financial_control.remove_product(name)
            elif choice == "5":
                name = input("Enter product name: ")
                quantity = int(input("Enter new product quantity: "))
                financial_control.update_product_quantity(name, quantity)
            elif choice == "6":
                profit = financial_control.calculate_profit()
                print(f"Profit: ${profit:.2f}")
            elif choice == "7":
                break
            else:
                print("Invalid option. Please choose a valid option.")
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
