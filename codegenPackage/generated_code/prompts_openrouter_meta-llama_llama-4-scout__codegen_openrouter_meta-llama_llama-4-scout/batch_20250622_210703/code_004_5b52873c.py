"""
Generated Code Metadata:
========================
Original URL: https://demirsoft.com
Prompt: Create a visitor tracking system for a company using DemirSoft's Ziyaretçi Takip Programı, including features for recording visitor information and tracking entry/exit times.
Generated: DETERMINISTIC_5b52873c2434b3cc
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import sqlite3

class VisitorTrackingSystem:
    def __init__(self, db_name):
        """
        Initialize the visitor tracking system.

        Args:
            db_name (str): The name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Create the visitors table if it does not exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS visitors
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             surname TEXT NOT NULL,
             company TEXT,
             entry_time TEXT NOT NULL,
             exit_time TEXT)
        ''')
        self.conn.commit()

    def record_visitor(self, name, surname, company):
        """
        Record a new visitor.

        Args:
            name (str): The visitor's name.
            surname (str): The visitor's surname.
            company (str): The visitor's company.

        Returns:
            int: The ID of the newly recorded visitor.
        """
        entry_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute('''
            INSERT INTO visitors (name, surname, company, entry_time)
            VALUES (?, ?, ?, ?)
        ''', (name, surname, company, entry_time))
        self.conn.commit()
        return self.cursor.lastrowid

    def update_exit_time(self, visitor_id):
        """
        Update the exit time of a visitor.

        Args:
            visitor_id (int): The ID of the visitor.

        Raises:
            ValueError: If the visitor ID is not found.
        """
        exit_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute('''
            UPDATE visitors
            SET exit_time = ?
            WHERE id = ?
        ''', (exit_time, visitor_id))
        if self.cursor.rowcount == 0:
            raise ValueError('Visitor ID not found')
        self.conn.commit()

    def get_visitor_info(self, visitor_id):
        """
        Get the information of a visitor.

        Args:
            visitor_id (int): The ID of the visitor.

        Returns:
            dict: The visitor's information.

        Raises:
            ValueError: If the visitor ID is not found.
        """
        self.cursor.execute('''
            SELECT * FROM visitors
            WHERE id = ?
        ''', (visitor_id,))
        row = self.cursor.fetchone()
        if row is None:
            raise ValueError('Visitor ID not found')
        return {
            'id': row[0],
            'name': row[1],
            'surname': row[2],
            'company': row[3],
            'entry_time': row[4],
            'exit_time': row[5]
        }

    def close(self):
        """
        Close the database connection.
        """
        self.conn.close()


def main():
    db_name = 'visitor_tracking.db'
    vts = VisitorTrackingSystem(db_name)

    while True:
        print('1. Record a new visitor')
        print('2. Update exit time')
        print('3. Get visitor info')
        print('4. Exit')
        choice = input('Choose an option: ')

        if choice == '1':
            name = input('Enter visitor name: ')
            surname = input('Enter visitor surname: ')
            company = input('Enter visitor company: ')
            visitor_id = vts.record_visitor(name, surname, company)
            print(f'Visitor recorded with ID {visitor_id}')
        elif choice == '2':
            visitor_id = int(input('Enter visitor ID: '))
            try:
                vts.update_exit_time(visitor_id)
                print('Exit time updated')
            except ValueError as e:
                print(e)
        elif choice == '3':
            visitor_id = int(input('Enter visitor ID: '))
            try:
                visitor_info = vts.get_visitor_info(visitor_id)
                print('Visitor Information:')
                print(f'ID: {visitor_info["id"]}')
                print(f'Name: {visitor_info["name"]}')
                print(f'Surname: {visitor_info["surname"]}')
                print(f'Company: {visitor_info["company"]}')
                print(f'Entry Time: {visitor_info["entry_time"]}')
                print(f'Exit Time: {visitor_info["exit_time"]}')
            except ValueError as e:
                print(e)
        elif choice == '4':
            vts.close()
            break
        else:
            print('Invalid option')

if __name__ == '__main__':
    main()
```
