"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tareekhsouria.com
Prompt: Develop a code snippet that retrieves and displays historical documents related to Syrian leaders from a database, focusing on figures like Hachem al-Atassi and Adeb al-Chichkli.
Generated: DETERMINISTIC_80df908a9f02ca77
Batch ID: 20250612_163454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Tuple

class HistoricalDocumentRetriever:
    def __init__(self, db_path: str):
        """
        Initializes the HistoricalDocumentRetriever with the specified database path.
        
        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path

    def connect_to_db(self):
        """
        Establishes a connection to the SQLite database.
        
        :return: SQLite connection object.
        """
        try:
            conn = sqlite3.connect(self.db_path)
            return conn
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            return None

    def fetch_documents(self, leaders: List[str]) -> List[Tuple[str, str]]:
        """
        Fetches historical documents related to specified Syrian leaders from the database.
        
        :param leaders: List of leader names to search for.
        :return: List of tuples containing document titles and contents.
        """
        documents = []
        
        # Connect to the database
        conn = self.connect_to_db()
        if conn is None:
            return documents
        
        try:
            cursor = conn.cursor()
            # Prepare SQL query using placeholders for security
            query = "SELECT title, content FROM documents WHERE leader_name IN ({})"
            placeholders = ', '.join('?' for _ in leaders)
            query = query.format(placeholders)
            
            # Execute the query with the leaders' names
            cursor.execute(query, leaders)
            documents = cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching documents: {e}")
        finally:
            conn.close()  # Ensure the connection is closed

        return documents

    def display_documents(self, documents: List[Tuple[str, str]]):
        """
        Displays the retrieved documents in a user-friendly format.
        
        :param documents: List of tuples containing document titles and contents.
        """
        if not documents:
            print("No documents found.")
            return
        
        for title, content in documents:
            print(f"Title: {title}\nContent: {content}\n{'-'*40}")

# Example usage
if __name__ == "__main__":
    # Path to the SQLite database
    DATABASE_PATH = "historical_documents.db"
    
    # Leaders to search for
    leaders_of_interest = ["Hachem al-Atassi", "Adeb al-Chichkli"]
    
    # Create an instance of the retriever
    retriever = HistoricalDocumentRetriever(DATABASE_PATH)
    
    # Fetch and display the documents
    historical_documents = retriever.fetch_documents(leaders_of_interest)
    retriever.display_documents(historical_documents)
```
