"""
Generated Code Metadata:
========================
Original URL: https://financestargate.com
Prompt: Write a Python function that demonstrates the common mistakes to avoid when using SQL stored procedures as discussed in Finance StarGate's article.
Generated: DETERMINISTIC_5eda68c8f8e5bb0b
Batch ID: 20250612_164213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import Optional, List, Dict, Any

def demonstrate_sql_stored_procedure_mistakes(db_path: str = ":memory:") -> None:
    """
    Demonstrates common mistakes to avoid when using SQL stored procedures.
    Based on Finance StarGate's article, this function shows anti-patterns and their corrections.
    
    Args:
        db_path (str): Path to SQLite database file. Uses in-memory DB by default.
    
    Raises:
        sqlite3.Error: If any SQLite operation fails.
    """

    # Anti-pattern 1: Not using parameterized queries (SQL injection vulnerability)
    def anti_pattern_1_sql_injection(conn: sqlite3.Connection, user_input: str) -> None:
        try:
            cursor = conn.cursor()
            # UNSAFE: Direct string concatenation
            cursor.execute(f"SELECT * FROM users WHERE username = '{user_input}'")
            results = cursor.fetchall()
            print(f"Anti-pattern 1 results: {results}")
        except sqlite3.Error as e:
            print(f"Anti-pattern 1 error: {e}")

    # Correction for Anti-pattern 1
    def correction_1_parameterized(conn: sqlite3.Connection, user_input: str) -> None:
        try:
            cursor = conn.cursor()
            # SAFE: Parameterized query
            cursor.execute("SELECT * FROM users WHERE username = ?", (user_input,))
            results = cursor.fetchall()
            print(f"Correction 1 results: {results}")
        except sqlite3.Error as e:
            print(f"Correction 1 error: {e}")

    # Anti-pattern 2: Not handling transactions properly
    def anti_pattern_2_no_transaction(conn: sqlite3.Connection, data: Dict[str, Any]) -> None:
        try:
            cursor = conn.cursor()
            # UNSAFE: No transaction handling
            cursor.execute("INSERT INTO accounts (user_id, balance) VALUES (?, ?)", 
                          (data['user_id'], data['balance']))
            # Some other operation that might fail
            cursor.execute("UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE id = ?", 
                          (data['user_id'],))
            # No commit or rollback
            print("Anti-pattern 2: Operations executed without transaction")
        except sqlite3.Error as e:
            print(f"Anti-pattern 2 error: {e}")

    # Correction for Anti-pattern 2
    def correction_2_with_transaction(conn: sqlite3.Connection, data: Dict[str, Any]) -> None:
        try:
            cursor = conn.cursor()
            # SAFE: Proper transaction handling
            conn.execute("BEGIN TRANSACTION")
            cursor.execute("INSERT INTO accounts (user_id, balance) VALUES (?, ?)", 
                          (data['user_id'], data['balance']))
            cursor.execute("UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE id = ?", 
                          (data['user_id'],))
            conn.commit()
            print("Correction 2: Operations executed within transaction")
        except sqlite3.Error as e:
            conn.rollback()
            print(f"Correction 2 error: {e}. Transaction rolled back.")

    # Anti-pattern 3: Not setting proper isolation levels
    def anti_pattern_3_isolation(conn: sqlite3.Connection) -> None:
        try:
            # UNSAFE: Default isolation level may lead to concurrency issues
            cursor = conn.cursor()
            cursor.execute("SELECT balance FROM accounts WHERE user_id = 1")
            balance = cursor.fetchone()[0]
            # No proper isolation between read and write
            cursor.execute("UPDATE accounts SET balance = ? WHERE user_id = 1", (balance + 100,))
            conn.commit()
            print("Anti-pattern 3: Balance updated without proper isolation")
        except sqlite3.Error as e:
            print(f"Anti-pattern 3 error: {e}")

    # Correction for Anti-pattern 3
    def correction_3_proper_isolation(conn: sqlite3.Connection) -> None:
        try:
            # SAFE: Set proper isolation level
            conn.isolation_level = "IMMEDIATE"  # or "EXCLUSIVE" depending on needs
            cursor = conn.cursor()
            cursor.execute("BEGIN TRANSACTION")
            cursor.execute("SELECT balance FROM accounts WHERE user_id = 1")
            balance = cursor.fetchone()[0]
            cursor.execute("UPDATE accounts SET balance = ? WHERE user_id = 1", (balance + 100,))
            conn.commit()
            print("Correction 3: Balance updated with proper isolation")
        except sqlite3.Error as e:
            conn.rollback()
            print(f"Correction 3 error: {e}. Transaction rolled back.")
        finally:
            conn.isolation_level = None  # Reset to default

    # Anti-pattern 4: Not handling NULL values properly
    def anti_pattern_4_null_handling(conn: sqlite3.Connection, user_id: int) -> None:
        try:
            cursor = conn.cursor()
            # UNSAFE: No NULL handling
            cursor.execute("SELECT last_login FROM users WHERE id = ?", (user_id,))
            last_login = cursor.fetchone()[0]  # Could be None
            print(f"Anti-pattern 4 last login: {last_login.strftime('%Y-%m-%d')}")  # Potential AttributeError
        except (sqlite3.Error, AttributeError) as e:
            print(f"Anti-pattern 4 error: {e}")

    # Correction for Anti-pattern 4
    def correction_4_null_handling(conn: sqlite3.Connection, user_id: int) -> None:
        try:
            cursor = conn.cursor()
            # SAFE: Proper NULL handling
            cursor.execute("SELECT last_login FROM users WHERE id = ?", (user_id,))
            result = cursor.fetchone()
            if result and result[0]:
                print(f"Correction 4 last login: {result[0].strftime('%Y-%m-%d')}")
            else:
                print("Correction 4: No login record found")
        except sqlite3.Error as e:
            print(f"Correction 4 error: {e}")

    # Setup test database
    try:
        with sqlite3.connect(db_path) as conn:
            # Create test tables
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    last_login TIMESTAMP
                )
            """)
            
            conn.execute("""
                CREATE TABLE IF NOT EXISTS accounts (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    balance DECIMAL(10, 2) NOT NULL,
                    FOREIGN KEY(user_id) REFERENCES users(id)
                )
            """)
            
            # Insert test data
            conn.execute("INSERT INTO users (id, username) VALUES (1, 'testuser')")
            conn.execute("INSERT INTO accounts (user_id, balance) VALUES (1, 1000.00)")
            conn.commit()

            # Demonstrate anti-patterns and corrections
            malicious_input = "testuser' OR '1'='1"
            anti_pattern_1_sql_injection(conn, malicious_input)
            correction_1_parameterized(conn, "testuser")
            
            test_data = {'user_id': 1, 'balance': 500.00}
            anti_pattern_2_no_transaction(conn, test_data)
            correction_2_with_transaction(conn, test_data)
            
            anti_pattern_3_isolation(conn)
            correction_3_proper_isolation(conn)
            
            anti_pattern_4_null_handling(conn, 1)
            correction_4_null_handling(conn, 1)
            
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        raise

# Example usage
if __name__ == "__main__":
    demonstrate_sql_stored_procedure_mistakes()
```
