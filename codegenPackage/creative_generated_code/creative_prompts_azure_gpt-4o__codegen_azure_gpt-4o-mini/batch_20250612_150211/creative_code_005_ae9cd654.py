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

# Database connection parameters
DATABASE = 'transactions.db'

def fetch_latest_transactions():
    """Fetch the latest deposit and withdrawal transactions from the database."""
    try:
        # Establish a connection to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # SQL query to fetch the latest transactions
        query = """
        SELECT transaction_type, amount, transaction_date
        FROM transactions
        ORDER BY transaction_date DESC
        LIMIT 10;
        """
        
        # Execute the query
        cursor.execute(query)

        # Fetch all results
        transactions = cursor.fetchall()

        # Check if transactions were found
        if not transactions:
            print("No transactions found.")
            return []

        # Return transaction data
        return transactions

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

    finally:
        # Ensure connection is closed
        if conn:
            conn.close()

def display_transactions(transactions):
    """Display the fetched transactions in a user-friendly format."""
    print(f"{'Transaction Type':<15} {'Amount':<10} {'Date':<20}")
    print("=" * 50)
    for transaction in transactions:
        transaction_type, amount, transaction_date = transaction
        # Format date for better readability
        formatted_date = datetime.strptime(transaction_date, "%Y-%m-%d %H:%M:%S").strftime("%d %b %Y %H:%M")
        print(f"{transaction_type:<15} {amount:<10} {formatted_date:<20}")

def main():
    """Main function to run the transaction fetching and displaying process."""
    transactions = fetch_latest_transactions()
    if transactions:
        display_transactions(transactions)

if __name__ == "__main__":
    main()
```

**Note:** Ensure you have a `transactions.db` SQLite database with a `transactions` table containing the appropriate columns (`transaction_type`, `amount`, `transaction_date`) for this code to work. Adjust the database path and schema according to your actual setup.
