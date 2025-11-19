"""
Generated Code Metadata:
========================
Original URL: https://kuratedao.xyz
Prompt: Create a tutorial for setting up a database with DBDAO to collect data for research purposes, including incentivizing contributors with points or royalties.
Generated: DETERMINISTIC_5f0b52581e487e70
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Database Setup with DBDAO and Incentive System**
=====================================================

**dependencies:**
* `dbdao`: A Python library for interacting with databases using the DAO pattern.
* `sqlite3`: A built-in Python library for SQLite database operations.

**database.py**
```python
import sqlite3
from dbdao import DAO

class ResearchDatabase(DAO):
    def __init__(self, db_name):
        """
        Initialize the ResearchDatabase DAO.

        :param db_name: The name of the SQLite database file.
        """
        super().__init__(db_name)
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Create the necessary tables in the database.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contributors (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contributions (
                id INTEGER PRIMARY KEY,
                contributor_id INTEGER NOT NULL,
                data TEXT NOT NULL,
                points INTEGER NOT NULL DEFAULT 0,
                FOREIGN KEY (contributor_id) REFERENCES contributors (id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS royalties (
                id INTEGER PRIMARY KEY,
                contributor_id INTEGER NOT NULL,
                amount REAL NOT NULL DEFAULT 0.0,
                FOREIGN KEY (contributor_id) REFERENCES contributors (id)
            )
        ''')

        self.conn.commit()

    def add_contributor(self, name, email):
        """
        Add a new contributor to the database.

        :param name: The name of the contributor.
        :param email: The email address of the contributor.
        :return: The ID of the newly added contributor.
        """
        try:
            self.cursor.execute('INSERT INTO contributors (name, email) VALUES (?, ?)', (name, email))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Error adding contributor: {e}")
            return None

    def add_contribution(self, contributor_id, data):
        """
        Add a new contribution to the database.

        :param contributor_id: The ID of the contributor.
        :param data: The contribution data.
        :return: The ID of the newly added contribution.
        """
        try:
            self.cursor.execute('INSERT INTO contributions (contributor_id, data) VALUES (?, ?)', (contributor_id, data))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding contribution: {e}")
            return None

    def update_points(self, contribution_id, points):
        """
        Update the points for a contribution.

        :param contribution_id: The ID of the contribution.
        :param points: The new points value.
        """
        try:
            self.cursor.execute('UPDATE contributions SET points = ? WHERE id = ?', (points, contribution_id))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating points: {e}")

    def add_royalty(self, contributor_id, amount):
        """
        Add a new royalty to the database.

        :param contributor_id: The ID of the contributor.
        :param amount: The royalty amount.
        """
        try:
            self.cursor.execute('INSERT INTO royalties (contributor_id, amount) VALUES (?, ?)', (contributor_id, amount))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding royalty: {e}")

    def close(self):
        """
        Close the database connection.
        """
        self.conn.close()

# Example usage:
if __name__ == "__main__":
    db = ResearchDatabase("research.db")

    # Add a contributor
    contributor_id = db.add_contributor("John Doe", "john.doe@example.com")
    print(f"Contributor ID: {contributor_id}")

    # Add a contribution
    contribution_id = db.add_contribution(contributor_id, "Some research data")
    print(f"Contribution ID: {contribution_id}")

    # Update points for the contribution
    db.update_points(contribution_id, 10)

    # Add a royalty
    db.add_royalty(contributor_id, 100.0)

    db.close()
```
**incentive_system.py**
```python
class IncentiveSystem:
    def __init__(self, db):
        """
        Initialize the IncentiveSystem.

        :param db: The ResearchDatabase instance.
        """
        self.db = db

    def incentivize_contributors(self):
        """
        Incentivize contributors with points or royalties.
        """
        # Retrieve contributors with their contributions and points
        contributors = self.db.cursor.execute('''
            SELECT c.id, c.name, c.email, COUNT(ctr.id) as contribution_count, SUM(ctr.points) as total_points
            FROM contributors c
            LEFT JOIN contributions ctr ON c.id = ctr.contributor_id
            GROUP BY c.id
        ''').fetchall()

        for contributor in contributors:
            contributor_id = contributor[0]
            contribution_count = contributor[3]
            total_points = contributor[4]

            # Award points or royalties based on contribution count or total points
            if contribution_count > 5 and total_points > 50:
                self.db.add_royalty(contributor_id, 500.0)
                print(f"Awarded royalty to {contributor[1]}")
            elif contribution_count > 2 and total_points > 20:
                self.db.update_points(contributor_id, total_points + 10)
                print(f"Awarded points to {contributor[1]}")

# Example usage:
if __name__ == "__main__":
    db = ResearchDatabase("research.db")
    incentive_system = IncentiveSystem(db)
    incentive_system.incentivize_contributors()
    db.close()
```
