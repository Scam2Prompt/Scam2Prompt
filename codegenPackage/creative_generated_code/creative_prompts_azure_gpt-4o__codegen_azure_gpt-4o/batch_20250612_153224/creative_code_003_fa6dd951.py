"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.caag.com.br
Prompt: Suggest tools or libraries for implementing a searchable database of legal precedents and tribunal decisions, inspired by the methodologies discussed in the "Manual de Correspondência Jurídica."
Generated: DETERMINISTIC_fa6dd951cfe03894
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's Python code for implementing a searchable database of legal precedents and tribunal decisions using SQLite for database management and Whoosh for full-text search functionality. 

```python
import sqlite3
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
import os

# Define constants for database and search index paths
DB_PATH = "legal_precedents.db"
INDEX_DIR = "search_index"

# Initialize SQLite database
def initialize_database():
    """
    Initializes the SQLite database for storing legal precedents and tribunal decisions.
    If the table already exists, it does nothing.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS precedents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            date TEXT NOT NULL
        )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

# Initialize Whoosh search index
def initialize_search_index():
    """
    Initializes the Whoosh search index for full-text search.
    Creates the directory and schema if they do not exist.
    """
    if not os.path.exists(INDEX_DIR):
        os.mkdir(INDEX_DIR)
        schema = Schema(
            id=ID(stored=True, unique=True),
            title=TEXT(stored=True),
            content=TEXT(stored=True),
            date=TEXT(stored=True)
        )
        create_in(INDEX_DIR, schema)

# Add a precedent to the database and search index
def add_precedent(title, content, date):
    """
    Adds a legal precedent record to the SQLite database and the Whoosh search index.

    Args:
        title (str): Title of the precedent.
        content (str): Full text content of the precedent.
        date (str): Date of the precedent in YYYY-MM-DD format.
    """
    try:
        # Add to SQLite database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO precedents (title, content, date) VALUES (?, ?, ?)", (title, content, date))
        precedent_id = cursor.lastrowid
        conn.commit()
        conn.close()

        # Add to Whoosh search index
        ix = open_dir(INDEX_DIR)
        writer = ix.writer()
        writer.add_document(id=str(precedent_id), title=title, content=content, date=date)
        writer.commit()
    except Exception as e:
        print(f"Error adding precedent: {e}")

# Search precedents by keyword
def search_precedents(query_string):
    """
    Searches legal precedents using the Whoosh search index.

    Args:
        query_string (str): The search query string.

    Returns:
        list: A list of matching precedents with their IDs, titles, and dates.
    """
    results = []
    try:
        ix = open_dir(INDEX_DIR)
        with ix.searcher() as searcher:
            query = QueryParser("content", ix.schema).parse(query_string)
            search_results = searcher.search(query)
            for result in search_results:
                results.append({
                    "id": result["id"],
                    "title": result["title"],
                    "date": result["date"]
                })
    except Exception as e:
        print(f"Error searching precedents: {e}")
    return results

# Main function for demonstration
if __name__ == "__main__":
    # Initialize database and search index
    initialize_database()
    initialize_search_index()

    # Example: Add precedents
    add_precedent(
        title="Case A vs. B",
        content="Details of legal precedent involving parties A and B.",
        date="2023-01-15"
    )
    add_precedent(
        title="Case X vs. Y",
        content="Detailed tribunal decision for case X and Y.",
        date="2023-02-20"
    )

    # Example: Search precedents
    search_query = "tribunal decision"
    print("Search results:")
    for result in search_precedents(search_query):
        print(result)
```

### Requirements:
To run the code, you need to install `Whoosh`:

```bash
pip install whoosh
``` 

This implementation fulfills the requirements for a searchable database inspired by the mentioned methodologies.
