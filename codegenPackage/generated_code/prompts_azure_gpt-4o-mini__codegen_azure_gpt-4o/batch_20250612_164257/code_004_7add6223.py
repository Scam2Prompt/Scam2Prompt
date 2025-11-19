"""
Generated Code Metadata:
========================
Original URL: https://stewartpayroll.com
Prompt: Create a function that retrieves a user's Company ID using their last name and last four digits of their SSN as described in the Paylocity login help section.
Generated: DETERMINISTIC_7add62231ff27348
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3

def get_company_id(last_name: str, ssn_last4: str) -> str:
    """
    Retrieves a user's Company ID using their last name and the last four digits of their SSN.

    Args:
        last_name (str): The user's last name.
        ssn_last4 (str): The last four digits of the user's SSN.

    Returns:
        str: The Company ID if found, or an appropriate error message.
    """
    # Validate input parameters
    if not last_name or not ssn_last4:
        raise ValueError("Both last_name and ssn_last4 must be provided.")
    if not ssn_last4.isdigit() or len(ssn_last4) != 4:
        raise ValueError("SSN last four digits must be a 4-digit numeric string.")

    # Connect to the database (replace 'database.db' with your actual database file)
    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
    except sqlite3.Error as e:
        raise ConnectionError(f"Failed to connect to the database: {e}")

    try:
        # Query the database for the Company ID
        query = """
        SELECT company_id
        FROM users
        WHERE last_name = ? AND ssn_last4 = ?
        """
        cursor.execute(query, (last_name, ssn_last4))
        result = cursor.fetchone()

        # Check if a result was found
        if result:
            return result[0]  # Return the Company ID
        else:
            return "No matching user found for the provided last name and SSN last four digits."
    except sqlite3.Error as e:
        raise RuntimeError(f"An error occurred while querying the database: {e}")
    finally:
        # Ensure the database connection is closed
        connection.close()
```
