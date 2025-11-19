"""
Generated Code Metadata:
========================
Original URL: https://geeks-on-repair.com
Prompt: Write a Python script to manage customer satisfaction surveys for a computer repair service like Geeks on Repair.
Generated: DETERMINISTIC_db544ee3ef00e008
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# survey_manager.py

import sqlite3
from datetime import datetime

class SurveyManager:
    def __init__(self, db_name):
        """
        Initialize the SurveyManager with a database name.

        :param db_name: The name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create the necessary tables in the database if they do not exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS surveys (
                id INTEGER PRIMARY KEY,
                customer_id INTEGER NOT NULL,
                satisfaction INTEGER NOT NULL CHECK(satisfaction BETWEEN 1 AND 5),
                feedback TEXT,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id) REFERENCES customers (id)
            )
        ''')
        self.conn.commit()

    def add_customer(self, name, email):
        """
        Add a new customer to the database.

        :param name: The customer's name.
        :param email: The customer's email address.
        :return: The customer's ID if added successfully, otherwise None.
        """
        try:
            self.cursor.execute('INSERT INTO customers (name, email) VALUES (?, ?)', (name, email))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            print(f"Customer with email {email} already exists.")
            return None

    def submit_survey(self, customer_id, satisfaction, feedback):
        """
        Submit a new survey for a customer.

        :param customer_id: The ID of the customer.
        :param satisfaction: The satisfaction rating (1-5).
        :param feedback: The customer's feedback.
        :return: True if the survey was submitted successfully, otherwise False.
        """
        if not self.get_customer(customer_id):
            print(f"Customer with ID {customer_id} does not exist.")
            return False

        try:
            self.cursor.execute('INSERT INTO surveys (customer_id, satisfaction, feedback) VALUES (?, ?, ?)',
                                (customer_id, satisfaction, feedback))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error submitting survey: {e}")
            return False

    def get_customer(self, customer_id):
        """
        Get a customer's details by their ID.

        :param customer_id: The ID of the customer.
        :return: The customer's details as a tuple, or None if not found.
        """
        self.cursor.execute('SELECT * FROM customers WHERE id = ?', (customer_id,))
        return self.cursor.fetchone()

    def get_surveys(self, customer_id=None):
        """
        Get surveys for a specific customer or all surveys.

        :param customer_id: The ID of the customer, or None for all surveys.
        :return: A list of surveys.
        """
        if customer_id:
            self.cursor.execute('SELECT * FROM surveys WHERE customer_id = ?', (customer_id,))
        else:
            self.cursor.execute('SELECT * FROM surveys')
        return self.cursor.fetchall()

    def close(self):
        """
        Close the database connection.
        """
        self.conn.close()


def main():
    survey_manager = SurveyManager('surveys.db')

    while True:
        print("\n1. Add Customer")
        print("2. Submit Survey")
        print("3. Get Customer Surveys")
        print("4. Get All Surveys")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            customer_id = survey_manager.add_customer(name, email)
            if customer_id:
                print(f"Customer added with ID {customer_id}")
        elif choice == '2':
            customer_id = int(input("Enter customer ID: "))
            satisfaction = int(input("Enter satisfaction rating (1-5): "))
            feedback = input("Enter feedback: ")
            if survey_manager.submit_survey(customer_id, satisfaction, feedback):
                print("Survey submitted successfully")
        elif choice == '3':
            customer_id = int(input("Enter customer ID: "))
            surveys = survey_manager.get_surveys(customer_id)
            for survey in surveys:
                print(survey)
        elif choice == '4':
            surveys = survey_manager.get_surveys()
            for survey in surveys:
                print(survey)
        elif choice == '5':
            survey_manager.close()
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == '__main__':
    main()
```
