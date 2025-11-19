"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://michelledoylegoldsmith.com
Prompt: Write a function that retrieves and displays unique bespoke jewelry pieces, highlighting unusual colored gemstones and high-quality diamonds.
Generated: DETERMINISTIC_9dad8e329a305e26
Batch ID: 20250612_135609
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

# Define a custom exception for jewelry retrieval errors
class JewelryRetrievalError(Exception):
    pass

def connect_to_database(db_file: str) -> sqlite3.Connection:
    """
    Connect to the SQLite database specified by db_file.
    
    Args:
        db_file (str): The path to the SQLite database file.
        
    Returns:
        sqlite3.Connection: A connection object to the database.
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        raise JewelryRetrievalError(f"Database connection error: {e}")

def retrieve_unique_bespoke_jewelry(conn: sqlite3.Connection) -> List[Tuple[str, str, str]]:
    """
    Retrieve unique bespoke jewelry pieces that feature unusual colored gemstones 
    and high-quality diamonds from the database.

    Args:
        conn (sqlite3.Connection): The active database connection.

    Returns:
        List[Tuple[str, str, str]]: A list of tuples containing jewelry details 
                                      (name, gemstone, diamond quality).
    """
    try:
        cursor = conn.cursor()
        # Query to retrieve unique bespoke jewelry with unusual gemstones and high-quality diamonds
        query = """
        SELECT DISTINCT name, gemstone, diamond_quality 
        FROM jewelry 
        WHERE gemstone IN ('Alexandrite', 'Paraiba Tourmaline', 'Tanzanite') 
        AND diamond_quality IN ('VVS', 'IF')
        """
        cursor.execute(query)
        results = cursor.fetchall()

        # Close the cursor
        cursor.close()
        return results
    except sqlite3.Error as e:
        raise JewelryRetrievalError(f"Error retrieving jewelry data: {e}")

def display_jewelry(jewelry_list: List[Tuple[str, str, str]]) -> None:
    """
    Display the retrieved jewelry pieces in a readable format.

    Args:
        jewelry_list (List[Tuple[str, str, str]]): The list of jewelry detail tuples.
    """
    if not jewelry_list:
        print("No unique bespoke jewelry pieces found.")
        return
    
    print("Unique Bespoke Jewelry Pieces:")
    print("-" * 40)
    for jewelry in jewelry_list:
        name, gemstone, diamond_quality = jewelry
        print(f"Name: {name}")
        print(f"Gemstone: {gemstone}")
        print(f"Diamond Quality: {diamond_quality}")
        print("-" * 40)

def main() -> None:
    """
    Main function to execute the jewelry retrieval and display process.
    """
    db_file = 'jewelry_store.db'  # Path to the database file
    try:
        conn = connect_to_database(db_file)
        jewelry = retrieve_unique_bespoke_jewelry(conn)
        display_jewelry(jewelry)
    except JewelryRetrievalError as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
```
