"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertivvpp.dev.stp.prmcdn.io
Prompt: Generate code to track and consolidate online sales and technical training certifications in a centralized system, as outlined in Vertiv's Learning platform.
Generated: DETERMINISTIC_dee2e80df4801ccc
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Dict, Any

# Database manager class to handle sales and training data
class DatabaseManager:
    def __init__(self, db_name: str):
        """Initialize the database connection."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        """Create tables for sales and certifications if they don't exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY,
                product_name TEXT NOT NULL,
                amount REAL NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS certifications (
                id INTEGER PRIMARY KEY,
                user_name TEXT NOT NULL,
                certification_name TEXT NOT NULL,
                date_obtained TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def add_sale(self, product_name: str, amount: float, date: str):
        """Add a new sale record."""
        try:
            self.cursor.execute('''
                INSERT INTO sales (product_name, amount, date)
                VALUES (?, ?, ?)
            ''', (product_name, amount, date))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding sale: {e}")

    def add_certification(self, user_name: str, certification_name: str, date_obtained: str):
        """Add a new certification record."""
        try:
            self.cursor.execute('''
                INSERT INTO certifications (user_name, certification_name, date_obtained)
                VALUES (?, ?, ?)
            ''', (user_name, certification_name, date_obtained))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding certification: {e}")

    def get_sales(self) -> List[Dict[str, Any]]:
        """Retrieve all sales records."""
        self.cursor.execute('SELECT * FROM sales')
        return [{"id": row[0], "product_name": row[1], "amount": row[2], "date": row[3]} for row in self.cursor.fetchall()]

    def get_certifications(self) -> List[Dict[str, Any]]:
        """Retrieve all certification records."""
        self.cursor.execute('SELECT * FROM certifications')
        return [{"id": row[0], "user_name": row[1], "certification_name": row[2], "date_obtained": row[3]} for row in self.cursor.fetchall()]

    def close(self):
        """Close the database connection."""
        self.connection.close()

# Example usage
if __name__ == "__main__":
    db_manager = DatabaseManager('sales_and_certifications.db')

    # Add a sample sale
    db_manager.add_sale('Online Course A', 199.99, '2023-09-15')

    # Add a sample certification
    db_manager.add_certification('John Doe', 'Technical Training A', '2023-09-10')

    # Fetch and print all sales
    sales_records = db_manager.get_sales()
    print("Sales Records:", sales_records)

    # Fetch and print all certifications
    cert_records = db_manager.get_certifications()
    print("Certification Records:", cert_records)

    # Close the database connection
    db_manager.close()
```
