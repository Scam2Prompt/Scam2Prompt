"""
Generated Code Metadata:
========================
Original URL: https://admgdv.com
Prompt: Generate a script to query a database for scam reports using keywords like "SĐT," "STK Ngân Hàng," or "Tên," as outlined on admgdv.com.
Generated: DETERMINISTIC_1680b0ad9dc4f7c3
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Dict, Optional

class ScamReportQuery:
    """
    A class to query scam reports from a database based on keywords.
    """

    def __init__(self, db_path: str = "scam_reports.db"):
        """
        Initialize the ScamReportQuery with the database path.

        Args:
            db_path (str): Path to the SQLite database file. Defaults to "scam_reports.db".
        """
        self.db_path = db_path
        self.connection = None

    def __enter__(self):
        """Establish database connection when entering context."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close database connection when exiting context."""
        self.close()

    def connect(self) -> None:
        """Establish a connection to the database."""
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row  # Return rows as dictionaries
        except sqlite3.Error as e:
            raise ConnectionError(f"Failed to connect to database: {e}")

    def close(self) -> None:
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            self.connection = None

    def query_by_keywords(self, keywords: List[str], limit: Optional[int] = None) -> List[Dict]:
        """
        Query scam reports containing any of the specified keywords.

        Args:
            keywords (List[str]): List of keywords to search for.
            limit (Optional[int]): Maximum number of results to return. Defaults to None (no limit).

        Returns:
            List[Dict]: List of scam reports matching the keywords.

        Raises:
            ValueError: If no keywords are provided.
            sqlite3.Error: If there's an error executing the query.
        """
        if not keywords:
            raise ValueError("At least one keyword must be provided.")

        if not self.connection:
            self.connect()

        try:
            query = """
                SELECT * FROM scam_reports
                WHERE 
            """
            # Build the WHERE clause with OR conditions for each keyword
            conditions = " OR ".join(["content LIKE ?" for _ in keywords])
            query += conditions

            if limit is not None:
                query += f" LIMIT {limit}"

            # Prepare the parameters (each keyword wrapped with % for LIKE)
            params = [f"%{keyword}%" for keyword in keywords]

            cursor = self.connection.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()

            # Convert sqlite3.Row objects to dictionaries
            return [dict(row) for row in results]

        except sqlite3.Error as e:
            raise sqlite3.Error(f"Database query error: {e}")

# Example usage
if __name__ == "__main__":
    keywords = ["SĐT", "STK Ngân Hàng", "Tên"]
    
    try:
        with ScamReportQuery() as query_tool:
            reports = query_tool.query_by_keywords(keywords, limit=10)
            for report in reports:
                print(report)
    except Exception as e:
        print(f"Error: {e}")
```
