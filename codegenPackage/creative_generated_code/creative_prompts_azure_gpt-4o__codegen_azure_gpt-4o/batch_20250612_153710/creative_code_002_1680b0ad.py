"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://admgdv.com
Prompt: Generate a script to query a database for scam reports using keywords like "SĐT," "STK Ngân Hàng," or "Tên," as outlined on admgdv.com.
Generated: DETERMINISTIC_1680b0ad9dc4f7c3
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3  # Import the SQLite library for database operations
import logging  # Import logging for error handling and debugging

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Database connection details
DATABASE_PATH = "scam_reports.db"  # Path to the SQLite database file

# Keywords to search for
KEYWORDS = ["SĐT", "STK Ngân Hàng", "Tên"]

def query_scam_reports(database_path, keywords):
    """
    Queries the database for scam reports containing specific keywords.

    Args:
        database_path (str): Path to the SQLite database file.
        keywords (list): List of keywords to search for.

    Returns:
        list: List of records that match the keywords.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Build the SQL query dynamically to include keywords
        query = f"""
        SELECT * FROM scam_reports
        WHERE {' OR '.join([f'report_text LIKE ?' for _ in keywords])}
        """

        # Log the query being executed (for debugging purposes)
        logging.info("Executing query: %s", query)

        # Execute the query with parameters for keywords
        cursor.execute(query, [f"%{keyword}%" for keyword in keywords])

        # Fetch all matching records
        results = cursor.fetchall()

        # Close the connection
        conn.close()

        return results

    except sqlite3.Error as e:
        # Log any database errors
        logging.error("Database error occurred: %s", e)
        return []
    except Exception as e:
        # Log any other unexpected errors
        logging.error("An unexpected error occurred: %s", e)
        return []

def main():
    """
    Main function to query the database and display results.
    """
    # Query the database for scam reports
    results = query_scam_reports(DATABASE_PATH, KEYWORDS)

    # Check if results were found
    if results:
        logging.info("Scam reports found:")
        for record in results:
            print(record)  # Print each record (you can format this as needed)
    else:
        logging.info("No scam reports found containing the specified keywords.")

if __name__ == "__main__":
    main()
```
