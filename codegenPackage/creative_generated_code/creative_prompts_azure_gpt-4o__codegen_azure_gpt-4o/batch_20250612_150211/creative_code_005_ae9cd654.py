"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sup10xtrade.i.ng
Prompt: Create a script to fetch and display the latest deposit and withdrawal transactions from a database, similar to the "Latest Transactions" section on the 10x Investment website.
Generated: DETERMINISTIC_ae9cd654e7dd73b6
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime

# Configuration
DB_PATH = 'transactions.db'  # Path to your SQLite database
LATEST_TRANSACTIONS_LIMIT = 10  # Number of latest transactions to fetch

def fetch_latest_transactions(db_path, limit):
    """
    Fetch the latest deposit and withdrawal transactions from the database.

    Args:
    db_path (str): Path to the SQLite database.
    limit (int): Number of latest transactions to fetch.

    Returns:
    dict: A dictionary containing the latest deposits and withdrawals.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Query for the latest deposit transactions
        cursor.execute("""
            SELECT id, transaction_type, amount, timestamp 
            FROM transactions 
            WHERE transaction_type = 'deposit' 
            ORDER BY timestamp DESC 
            LIMIT ?
        """, (limit,))
        deposits = cursor.fetchall()

        # Query for the latest withdrawal transactions
        cursor.execute("""
            SELECT id, transaction_type, amount, timestamp 
            FROM transactions 
            WHERE transaction_type = 'withdrawal' 
            ORDER BY timestamp DESC 
            LIMIT ?
        """, (limit,))
        withdrawals = cursor.fetchall()

        # Close the database connection
        conn.close()

        # Format the results
        return {
            "deposits": [{"id": row[0], "type": row[1], "amount": row[2], "timestamp": row[3]} for row in deposits],
            "withdrawals": [{"id": row[0], "type": row[1], "amount": row[2], "timestamp": row[3]} for row in withdrawals]
        }

    except sqlite3.Error as e:
        print(f"[ERROR] Database error: {e}")
        return {"deposits": [], "withdrawals": []}
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        return {"deposits": [], "withdrawals": []}

def display_transactions(transactions):
    """
    Display the latest deposit and withdrawal transactions in a readable format.

    Args:
    transactions (dict): A dictionary containing deposit and withdrawal transactions.
    """
    print("\nLatest Deposit Transactions:")
    for transaction in transactions['deposits']:
        print(f"ID: {transaction['id']}, Type: {transaction['type']}, Amount: ${transaction['amount']}, Timestamp: {transaction['timestamp']}")

    print("\nLatest Withdrawal Transactions:")
    for transaction in transactions['withdrawals']:
        print(f"ID: {transaction['id']}, Type: {transaction['type']}, Amount: ${transaction['amount']}, Timestamp: {transaction['timestamp']}")

# Main script execution
if __name__ == "__main__":
    print("[INFO] Fetching latest transactions...")
    transactions = fetch_latest_transactions(DB_PATH, LATEST_TRANSACTIONS_LIMIT)
    display_transactions(transactions)
```

### Notes:
- Ensure that the database (`transactions.db`) and the table (`transactions`) exist before running the script. The table should have at least the columns: `id`, `transaction_type`, `amount`, and `timestamp`.
- Replace `DB_PATH` with the correct database path if necessary.
- Enhance security (e.g., parameterize queries) if the script is used in a web application to avoid SQL injection risks.
