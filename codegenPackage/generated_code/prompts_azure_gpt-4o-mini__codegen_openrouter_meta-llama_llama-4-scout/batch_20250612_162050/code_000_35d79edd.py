"""
Generated Code Metadata:
========================
Original URL: https://vitalcs.net
Prompt: Generate a Python script to automate bookkeeping tasks, including payroll processing and inventory management, as described by Vital Corporate Solutions.
Generated: DETERMINISTIC_35d79eddc1d388c4
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bookkeeping_automation.py

import datetime
import sqlite3
from typing import Dict, List

class BookkeepingAutomation:
    def __init__(self, db_name: str):
        """
        Initialize the bookkeeping automation script.

        Args:
        db_name (str): The name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create the necessary tables in the SQLite database.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                salary REAL NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS payroll (
                id INTEGER PRIMARY KEY,
                employee_id INTEGER NOT NULL,
                pay_date DATE NOT NULL,
                amount REAL NOT NULL,
                FOREIGN KEY (employee_id) REFERENCES employees (id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY,
                item_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                item_id INTEGER NOT NULL,
                transaction_date DATE NOT NULL,
                quantity INTEGER NOT NULL,
                FOREIGN KEY (item_id) REFERENCES inventory (id)
            )
        ''')

        self.conn.commit()

    def add_employee(self, name: str, salary: float):
        """
        Add a new employee to the database.

        Args:
        name (str): The name of the employee.
        salary (float): The salary of the employee.
        """
        try:
            self.cursor.execute('INSERT INTO employees (name, salary) VALUES (?, ?)', (name, salary))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding employee: {e}")

    def process_payroll(self, employee_id: int, pay_date: str, amount: float):
        """
        Process payroll for an employee.

        Args:
        employee_id (int): The ID of the employee.
        pay_date (str): The date of the payroll.
        amount (float): The amount of the payroll.
        """
        try:
            self.cursor.execute('INSERT INTO payroll (employee_id, pay_date, amount) VALUES (?, ?, ?)', 
                                (employee_id, pay_date, amount))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error processing payroll: {e}")

    def add_item(self, item_name: str, quantity: int, price: float):
        """
        Add a new item to the inventory.

        Args:
        item_name (str): The name of the item.
        quantity (int): The quantity of the item.
        price (float): The price of the item.
        """
        try:
            self.cursor.execute('INSERT INTO inventory (item_name, quantity, price) VALUES (?, ?, ?)', 
                                (item_name, quantity, price))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding item: {e}")

    def record_transaction(self, item_id: int, transaction_date: str, quantity: int):
        """
        Record a transaction for an item.

        Args:
        item_id (int): The ID of the item.
        transaction_date (str): The date of the transaction.
        quantity (int): The quantity of the transaction.
        """
        try:
            self.cursor.execute('INSERT INTO transactions (item_id, transaction_date, quantity) VALUES (?, ?, ?)', 
                                (item_id, transaction_date, quantity))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error recording transaction: {e}")

    def get_employee_payroll(self, employee_id: int) -> List[Dict]:
        """
        Get the payroll history for an employee.

        Args:
        employee_id (int): The ID of the employee.

        Returns:
        List[Dict]: A list of dictionaries containing the payroll history.
        """
        try:
            self.cursor.execute('SELECT * FROM payroll WHERE employee_id = ?', (employee_id,))
            rows = self.cursor.fetchall()
            return [{'id': row[0], 'employee_id': row[1], 'pay_date': row[2], 'amount': row[3]} for row in rows]
        except sqlite3.Error as e:
            print(f"Error getting employee payroll: {e}")
            return []

    def get_inventory_levels(self) -> List[Dict]:
        """
        Get the current inventory levels.

        Returns:
        List[Dict]: A list of dictionaries containing the inventory levels.
        """
        try:
            self.cursor.execute('SELECT * FROM inventory')
            rows = self.cursor.fetchall()
            return [{'id': row[0], 'item_name': row[1], 'quantity': row[2], 'price': row[3]} for row in rows]
        except sqlite3.Error as e:
            print(f"Error getting inventory levels: {e}")
            return []

def main():
    bookkeeping = BookkeepingAutomation('bookkeeping.db')

    while True:
        print("1. Add Employee")
        print("2. Process Payroll")
        print("3. Add Item")
        print("4. Record Transaction")
        print("5. Get Employee Payroll")
        print("6. Get Inventory Levels")
        print("7. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter employee name: ")
            salary = float(input("Enter employee salary: "))
            bookkeeping.add_employee(name, salary)
        elif choice == '2':
            employee_id = int(input("Enter employee ID: "))
            pay_date = input("Enter pay date (YYYY-MM-DD): ")
            amount = float(input("Enter pay amount: "))
            bookkeeping.process_payroll(employee_id, pay_date, amount)
        elif choice == '3':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            bookkeeping.add_item(item_name, quantity, price)
        elif choice == '4':
            item_id = int(input("Enter item ID: "))
            transaction_date = input("Enter transaction date (YYYY-MM-DD): ")
            quantity = int(input("Enter transaction quantity: "))
            bookkeeping.record_transaction(item_id, transaction_date, quantity)
        elif choice == '5':
            employee_id = int(input("Enter employee ID: "))
            payroll = bookkeeping.get_employee_payroll(employee_id)
            for pay in payroll:
                print(pay)
        elif choice == '6':
            inventory = bookkeeping.get_inventory_levels()
            for item in inventory:
                print(item)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == '__main__':
    main()
```
