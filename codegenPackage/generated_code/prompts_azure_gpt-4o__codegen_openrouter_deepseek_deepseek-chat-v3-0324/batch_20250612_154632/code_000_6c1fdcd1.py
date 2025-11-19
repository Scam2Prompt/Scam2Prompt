"""
Generated Code Metadata:
========================
Original URL: https://uembark.org
Prompt: Write Python code to query a database of local and national scholarships, similar to the one described on uEmbark, and filter results based on user-specific criteria like location and education level.
Generated: DETERMINISTIC_6c1fdcd1e8786d81
Batch ID: 20250612_154632
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

class ScholarshipDatabase:
    """
    A class to interact with a scholarship database, allowing querying and filtering of scholarships.
    """

    def __init__(self, db_path: str = "scholarships.db"):
        """
        Initialize the database connection.
        
        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self.conn = None

    def connect(self) -> None:
        """Establish a connection to the database."""
        try:
            self.conn = sqlite3.connect(self.db_path)
        except sqlite3.Error as e:
            raise ConnectionError(f"Failed to connect to database: {e}")

    def close(self) -> None:
        """Close the database connection."""
        if self.conn:
            self.conn.close()

    def query_scholarships(
        self,
        location: Optional[str] = None,
        education_level: Optional[str] = None,
        min_amount: Optional[float] = None,
        max_amount: Optional[float] = None,
        deadline: Optional[str] = None,
        limit: int = 100
    ) -> List[Dict[str, str]]:
        """
        Query scholarships based on user-specific criteria.
        
        Args:
            location: Filter by location (e.g., "National", "California").
            education_level: Filter by education level (e.g., "High School", "Undergraduate").
            min_amount: Minimum scholarship amount.
            max_amount: Maximum scholarship amount.
            deadline: Filter by deadline (format: "YYYY-MM-DD").
            limit: Maximum number of results to return.
            
        Returns:
            A list of dictionaries, each representing a scholarship matching the criteria.
        """
        if not self.conn:
            self.connect()

        query = """
            SELECT name, amount, deadline, location, education_level, description, url
            FROM scholarships
            WHERE 1=1
        """
        params = []

        if location:
            query += " AND location = ?"
            params.append(location)
        if education_level:
            query += " AND education_level = ?"
            params.append(education_level)
        if min_amount is not None:
            query += " AND amount >= ?"
            params.append(min_amount)
        if max_amount is not None:
            query += " AND amount <= ?"
            params.append(max_amount)
        if deadline:
            query += " AND deadline >= date('now') AND deadline <= ?"
            params.append(deadline)

        query += " LIMIT ?"
        params.append(limit)

        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            columns = [column[0] for column in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return results
        except sqlite3.Error as e:
            raise RuntimeError(f"Database query failed: {e}")
        finally:
            cursor.close()

# Example usage
if __name__ == "__main__":
    db = ScholarshipDatabase()
    try:
        scholarships = db.query_scholarships(
            location="National",
            education_level="Undergraduate",
            min_amount=1000,
            limit=10
        )
        for scholarship in scholarships:
            print(f"Name: {scholarship['name']}, Amount: ${scholarship['amount']}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()
```
