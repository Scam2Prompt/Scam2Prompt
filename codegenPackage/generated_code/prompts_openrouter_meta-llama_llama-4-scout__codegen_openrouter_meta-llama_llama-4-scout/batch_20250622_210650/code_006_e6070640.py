"""
Generated Code Metadata:
========================
Original URL: https://yilgun.com
Prompt: What are the frequently asked questions about Umrah, including restrictions on performing Umrah multiple times?
Generated: DETERMINISTIC_e60706402ca10fa1
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import sqlite3
from typing import List, Dict

class UmrahFAQ:
    def __init__(self, db_name: str):
        """
        Initialize the UmrahFAQ class.

        Args:
        db_name (str): The name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Create the FAQs table if it does not exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS umrah_faqs
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             question TEXT NOT NULL, 
             answer TEXT NOT NULL)
        ''')
        self.conn.commit()

    def add_faq(self, question: str, answer: str):
        """
        Add a new FAQ to the database.

        Args:
        question (str): The question.
        answer (str): The answer.
        """
        try:
            self.cursor.execute('INSERT INTO umrah_faqs (question, answer) VALUES (?, ?)', (question, answer))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding FAQ: {e}")

    def get_faqs(self) -> List[Dict]:
        """
        Retrieve all FAQs from the database.

        Returns:
        List[Dict]: A list of dictionaries containing the FAQs.
        """
        try:
            self.cursor.execute('SELECT * FROM umrah_faqs')
            rows = self.cursor.fetchall()
            faqs = []
            for row in rows:
                faq = {
                    'id': row[0],
                    'question': row[1],
                    'answer': row[2]
                }
                faqs.append(faq)
            return faqs
        except sqlite3.Error as e:
            print(f"Error retrieving FAQs: {e}")
            return []

    def close_connection(self):
        """
        Close the database connection.
        """
        self.conn.close()


def main():
    db_name = 'umrah_faqs.db'
    faq_service = UmrahFAQ(db_name)

    # Add some FAQs
    faq_service.add_faq('What is Umrah?', 'Umrah is a pilgrimage to Mecca that can be performed by Muslims at any time of the year.')
    faq_service.add_faq('Can I perform Umrah multiple times?', 'Yes, you can perform Umrah multiple times. However, there are certain restrictions and guidelines to be aware of.')
    faq_service.add_faq('What are the restrictions on performing Umrah multiple times?', 'There are no specific restrictions on performing Umrah multiple times, but it is recommended to check with the Saudi government\'s official website for the latest guidelines and requirements.')

    # Retrieve and print FAQs
    faqs = faq_service.get_faqs()
    for faq in faqs:
        print(f"Q: {faq['question']}")
        print(f"A: {faq['answer']}\n")

    faq_service.close_connection()


if __name__ == '__main__':
    main()
```
