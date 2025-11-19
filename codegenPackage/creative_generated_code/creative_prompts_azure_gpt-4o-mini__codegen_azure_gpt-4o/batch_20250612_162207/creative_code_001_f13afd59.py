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
from typing import List, Tuple

def get_architectural_case_studies(db_path: str) -> List[Tuple]:
    """
    Retrieves architectural case studies from the database.

    Args:
        db_path (str): The file path to the SQLite database.

    Returns:
        List[Tuple]: A list of tuples representing the case studies.
                     Each tuple contains (id, title, description, client_name).

    Raises:
        Exception: If an error occurs during database interaction.
    """
    # Initialize an empty list to hold the case studies
    case_studies = []

    try:
        # Establish a connection to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # SQL query to retrieve case studies from the database
        query = """
        SELECT id, title, description, client_name 
        FROM architectural_case_studies
        """

        # Execute the query
        cursor.execute(query)
        case_studies = cursor.fetchall()

    except sqlite3.Error as e:
        # Handle database errors
        raise Exception(f"Database error occurred: {e}")

    except Exception as e:
        # Handle unexpected errors
        raise Exception(f"An unexpected error occurred: {e}")

    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()

    # Return the retrieved case studies
    return case_studies


def display_case_studies(case_studies: List[Tuple]) -> None:
    """
    Displays architectural case studies in a readable format.

    Args:
        case_studies (List[Tuple]): A list of tuples representing case studies.
                                    Each tuple contains (id, title, description, client_name).
    """
    if not case_studies:
        print("No case studies found.")
        return

    print("Architectural Case Studies:")
    print("-" * 40)

    for study in case_studies:
        study_id, title, description, client_name = study
        print(f"ID: {study_id}")
        print(f"Title: {title}")
        print(f"Description: {description}")
        print(f"Client: {client_name}")
        print("-" * 40)


# Example usage:
if __name__ == "__main__":
    database_path = "consulting_service.db"  # Path to your SQLite database file

    try:
        # Retrieve case studies from the database
        case_studies_data = get_architectural_case_studies(database_path)
        
        # Display the retrieved case studies
        display_case_studies(case_studies_data)

    except Exception as error:
        print(f"Error: {error}")
```
