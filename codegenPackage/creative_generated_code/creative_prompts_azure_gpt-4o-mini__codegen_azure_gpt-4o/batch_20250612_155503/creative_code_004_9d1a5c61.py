"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://livesupportdesks.live
Prompt: How do I set up a knowledge base for a live support desk, inspired by the content on livesupportdesks.live?
Generated: DETERMINISTIC_9d1a5c61f89aae07
Batch ID: 20250612_155503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script sets up a basic knowledge base for a live support desk using Python and SQLite.
It provides functionality to add FAQs and query them based on user input.
"""

import sqlite3
import os

# Constants for database file
DB_FILE = "knowledge_base.db"

def initialize_database():
    """
    Initialize the SQLite database with a table for the knowledge base.
    If the table already exists, this function does nothing.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Create the table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS knowledge_base (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
        """)
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def add_faq(question, answer):
    """
    Add a frequently asked question (FAQ) to the knowledge base.
    :param question: The question to be added to the knowledge base.
    :param answer: The corresponding answer to the question.
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Insert the new FAQ into the knowledge_base table
        cursor.execute("INSERT INTO knowledge_base (question, answer) VALUES (?, ?)", (question, answer))
        
        conn.commit()
        print("FAQ added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding FAQ: {e}")
    finally:
        conn.close()

def query_faq(keyword):
    """
    Query the knowledge base for FAQs matching the provided keyword.
    :param keyword: The keyword to search for in the questions.
    :return: A list of matching FAQs (question-answer pairs).
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Search for FAQs containing the keyword
        cursor.execute("SELECT question, answer FROM knowledge_base WHERE question LIKE ?", ('%' + keyword + '%',))
        results = cursor.fetchall()

        return results
    except sqlite3.Error as e:
        print(f"Error querying FAQs: {e}")
        return []
    finally:
        conn.close()

def main():
    """
    Main function to demonstrate the functionality of the knowledge base.
    """
    # Initialize the database
    initialize_database()
    
    # Add some sample FAQs
    add_faq("What is the return policy?", "Our return policy is valid for 30 days.")
    add_faq("How do I reset my password?", "Use the 'Forgot Password' link on the login page.")
    
    # Query FAQs based on user input
    keyword = input("Enter a keyword to search for FAQs: ")
    results = query_faq(keyword)
    
    if results:
        print("\nMatching FAQs:")
        for question, answer in results:
            print(f"Q: {question}\nA: {answer}\n")
    else:
        print("No matching FAQs found.")

if __name__ == "__main__":
    main()
```
