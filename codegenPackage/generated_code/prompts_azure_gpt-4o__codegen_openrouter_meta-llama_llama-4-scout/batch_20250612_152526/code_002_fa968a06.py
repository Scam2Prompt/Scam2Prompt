"""
Generated Code Metadata:
========================
Original URL: https://thebookkeepingdiaries.com
Prompt: Create a program that implements a streamlined bookkeeping system, including features for payroll management and income tax preparation, inspired by "The Bookkeeping Diaries" services.
Generated: DETERMINISTIC_fa968a0637eb2f5d
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bookkeeping_system.py

import datetime
import sqlite3

class BookkeepingSystem:
    def __init__(self, db_name):
        """
        Initialize the bookkeeping system with a database connection.

        Args:
            db_name (str): The name of the database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create the necessary tables in the database.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                salary REAL NOT NULL,
                tax_rate REAL NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS payroll (
                id INTEGER PRIMARY KEY,
                employee_id INTEGER NOT NULL,
                pay_date DATE NOT NULL,
                gross_pay REAL NOT NULL,
                taxes REAL NOT NULL,
                net_pay REAL NOT NULL,
                FOREIGN KEY (employee_id) REFERENCES employees (id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS income_tax (
                id INTEGER PRIMARY KEY,
                tax_year INTEGER NOT NULL,
                tax_amount REAL NOT NULL
            )
        ''')

        self.conn.commit()

    def add_employee(self, name, salary, tax_rate):
        """
        Add a new employee to the system.

        Args:
            name (str): The employee's name.
            salary (float): The employee's salary.
            tax_rate (float): The employee's tax rate.

        Returns:
            int: The employee's ID.
        """
        try:
            self.cursor.execute('INSERT INTO employees (name, salary, tax_rate) VALUES (?, ?, ?)', (name, salary, tax_rate))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding employee: {e}")
            return None

    def calculate_payroll(self, employee_id, pay_date):
        """
        Calculate the payroll for an employee.

        Args:
            employee_id (int): The employee's ID.
            pay_date (str): The pay date in YYYY-MM-DD format.

        Returns:
            dict: The payroll details.
        """
        try:
            self.cursor.execute('SELECT * FROM employees WHERE id = ?', (employee_id,))
            employee = self.cursor.fetchone()
            if employee:
                gross_pay = employee[2]
                taxes = gross_pay * employee[3] / 100
                net_pay = gross_pay - taxes
                self.cursor.execute('INSERT INTO payroll (employee_id, pay_date, gross_pay, taxes, net_pay) VALUES (?, ?, ?, ?, ?)', (employee_id, pay_date, gross_pay, taxes, net_pay))
                self.conn.commit()
                return {
                    'gross_pay': gross_pay,
                    'taxes': taxes,
                    'net_pay': net_pay
                }
            else:
                print("Employee not found")
                return None
        except sqlite3.Error as e:
            print(f"Error calculating payroll: {e}")
            return None

    def prepare_income_tax(self, tax_year):
        """
        Prepare the income tax for a given year.

        Args:
            tax_year (int): The tax year.

        Returns:
            float: The total tax amount.
        """
        try:
            self.cursor.execute('SELECT SUM(taxes) FROM payroll WHERE strftime("%Y", pay_date) = ?', (str(tax_year),))
            total_taxes = self.cursor.fetchone()[0]
            if total_taxes:
                self.cursor.execute('INSERT INTO income_tax (tax_year, tax_amount) VALUES (?, ?)', (tax_year, total_taxes))
                self.conn.commit()
                return total_taxes
            else:
                print("No payroll data for the given year")
                return None
        except sqlite3.Error as e:
            print(f"Error preparing income tax: {e}")
            return None

    def close_connection(self):
        """
        Close the database connection.
        """
        self.conn.close()


def main():
    bookkeeping_system = BookkeepingSystem('bookkeeping.db')

    while True:
        print("\nBookkeeping System Menu:")
        print("1. Add Employee")
        print("2. Calculate Payroll")
        print("3. Prepare Income Tax")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter employee name: ")
            salary = float(input("Enter employee salary: "))
            tax_rate = float(input("Enter employee tax rate: "))
            employee_id = bookkeeping_system.add_employee(name, salary, tax_rate)
            print(f"Employee added with ID: {employee_id}")
        elif choice == '2':
            employee_id = int(input("Enter employee ID: "))
            pay_date = input("Enter pay date (YYYY-MM-DD): ")
            payroll = bookkeeping_system.calculate_payroll(employee_id, pay_date)
            if payroll:
                print("Payroll Details:")
                print(f"Gross Pay: {payroll['gross_pay']}")
                print(f"Taxes: {payroll['taxes']}")
                print(f"Net Pay: {payroll['net_pay']}")
        elif choice == '3':
            tax_year = int(input("Enter tax year: "))
            total_taxes = bookkeeping_system.prepare_income_tax(tax_year)
            if total_taxes:
                print(f"Total Taxes for {tax_year}: {total_taxes}")
        elif choice == '4':
            bookkeeping_system.close_connection()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
```
