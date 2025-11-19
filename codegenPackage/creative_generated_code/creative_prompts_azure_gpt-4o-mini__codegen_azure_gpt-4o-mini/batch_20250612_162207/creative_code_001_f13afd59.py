"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rdmerakyat.com
Prompt: Write a Python function that retrieves and displays architectural case studies from a database for a consulting service.
Generated: DETERMINISTIC_f13afd59b2c5f419
Batch ID: 20250612_162207
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

class DatabaseError(Exception):
    """Custom exception for database operations."""
    pass

def get_architectural_case_studies(db_path: str) -> List[Dict[str, Any]]:
    """
    Retrieve architectural case studies from the database.

    Args:
        db_path (str): The file path to the SQLite database.

    Returns:
        List[Dict[str, Any]]: A list of case study records where each record is a dictionary.

    Raises:
        DatabaseError: If there is an error connecting to the database or executing the query.
    """
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # Execute the SQL query to retrieve case studies
        query = "SELECT * FROM architectural_case_studies"
        cursor.execute(query)

        # Fetch all results
        case_studies = cursor.fetchall()

        # Get column names from the cursor description
        columns = [column[0] for column in cursor.description]

        # Convert fetched results into a list of dictionaries
        results = [dict(zip(columns, row)) for row in case_studies]

        return results

    except sqlite3.Error as e:
        # Raise custom database error with the error message
        raise DatabaseError(f"Database error occurred: {e}")

    finally:
        # Ensure the database connection is closed
        if connection:
            connection.close()

def display_case_studies(case_studies: List[Dict[str, Any]]) -> None:
    """
    Display architectural case studies in a readable format.

    Args:
        case_studies (List[Dict[str, Any]]): A list of case study records.
    """
    if not case_studies:
        print("No case studies found.")
        return

    for case_study in case_studies:
        print("Case Study:")
        for key, value in case_study.items():
            print(f"  {key}: {value}")
        print("\n" + "-" * 40 + "\n")

if __name__ == "__main__":
    # Path to the SQLite database
    database_path = "path/to/your/database.db"

    try:
        # Retrieve case studies from the database
        case_studies = get_architectural_case_studies(database_path)
        
        # Display the retrieved case studies
        display_case_studies(case_studies)

    except DatabaseError as e:
        print(f"Error: {e}")
```
