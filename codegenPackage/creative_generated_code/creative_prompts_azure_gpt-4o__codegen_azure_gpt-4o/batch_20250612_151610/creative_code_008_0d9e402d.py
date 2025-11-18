"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apperley.ca
Prompt: Create a Python script to generate reports and statistics about family data stored in a genealogy database, including most common surnames and places.
Generated: DETERMINISTIC_0d9e402d9764f3d0
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from collections import Counter
from typing import List, Dict, Tuple

# Constants
DATABASE_PATH = 'genealogy.db'

def connect_to_database(db_path: str) -> sqlite3.Connection:
    """
    Establish a connection to the SQLite database.

    Args:
        db_path (str): Path to the SQLite database file.

    Returns:
        sqlite3.Connection: Connection object to interact with the database.
    """
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        raise RuntimeError(f"Failed to connect to the database: {e}")

def fetch_family_data(conn: sqlite3.Connection) -> List[Tuple[str, str]]:
    """
    Fetch family data containing surnames and places from the database.

    Args:
        conn (sqlite3.Connection): SQLite database connection object.

    Returns:
        List[Tuple[str, str]]: List of tuples containing surname and place.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT surname, place FROM family_data")
        return cursor.fetchall()
    except sqlite3.Error as e:
        raise RuntimeError(f"Failed to fetch family data: {e}")

def generate_statistics(data: List[Tuple[str, str]]) -> Dict[str, Dict[str, int]]:
    """
    Generate statistics for the most common surnames and places.

    Args:
        data (List[Tuple[str, str]]): List of tuples containing surname and place.

    Returns:
        Dict[str, Dict[str, int]]: A dictionary with statistics for surnames and places.
    """
    surnames = [entry[0] for entry in data]
    places = [entry[1] for entry in data]

    surname_counter = Counter(surnames)
    place_counter = Counter(places)

    return {
        "most_common_surnames": surname_counter.most_common(10),  # Top 10 surnames
        "most_common_places": place_counter.most_common(10)      # Top 10 places
    }

def generate_report(statistics: Dict[str, Dict[str, int]]) -> None:
    """
    Generate a human-readable report from the statistics.

    Args:
        statistics (Dict[str, Dict[str, int]]): Statistics dictionary.
    """
    print("===== Genealogy Report =====")
    print("\nMost Common Surnames:")
    for surname, count in statistics["most_common_surnames"]:
        print(f"{surname}: {count} occurrences")
    
    print("\nMost Common Places:")
    for place, count in statistics["most_common_places"]:
        print(f"{place}: {count} occurrences")
    print("============================")

def main():
    """
    Main function to orchestrate the report generation process.
    """
    try:
        # Connect to the database
        conn = connect_to_database(DATABASE_PATH)
        
        # Fetch family data from the database
        family_data = fetch_family_data(conn)
        
        # Generate statistics from the data
        statistics = generate_statistics(family_data)
        
        # Generate and display the report
        generate_report(statistics)
    except RuntimeError as e:
        print(f"Error: {e}")
    finally:
        # Ensure the database connection is closed
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    main()
```
