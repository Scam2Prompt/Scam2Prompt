"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoexperience.vip
Prompt: How can I handle a "table doesn't exist" error in a SQL database when working with cryptocurrency data?
Generated: DETERMINISTIC_fbe625c5e55e8756
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

def connect_to_database(db_name):
    """Establish a connection to the SQLite database."""
    try:
        connection = sqlite3.connect(db_name)
        print(f"Connected to database: {db_name}")
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table_if_not_exists(connection):
    """Create a cryptocurrency table if it doesn't already exist."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS cryptocurrency (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        symbol TEXT NOT NULL,
        price REAL NOT NULL
    );
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
        connection.commit()
        print("Cryptocurrency table created or already exists.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def insert_crypto_data(connection, name, symbol, price):
    """Insert cryptocurrency data into the table."""
    insert_sql = "INSERT INTO cryptocurrency (name, symbol, price) VALUES (?, ?, ?);"
    
    try:
        cursor = connection.cursor()
        cursor.execute(insert_sql, (name, symbol, price))
        connection.commit()
        print(f"Inserted data: {name}, {symbol}, {price}")
    except sqlite3.IntegrityError as e:
        print(f"Data integrity error: {e}")
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")

def fetch_crypto_data(connection):
    """Fetch and display all cryptocurrency data from the table."""
    select_sql = "SELECT * FROM cryptocurrency;"
    
    try:
        cursor = connection.cursor()
        cursor.execute(select_sql)
        rows = cursor.fetchall()
        
        if rows:
            print("Cryptocurrency data:")
            for row in rows:
                print(row)
        else:
            print("No data found in the cryptocurrency table.")
    except sqlite3.Error as e:
        print(f"Error fetching data: {e}")

def main():
    # Database name
    db_name = 'cryptocurrency.db'
    
    # Connect to the database
    connection = connect_to_database(db_name)
    if connection is None:
        return
    
    # Create the cryptocurrency table
    create_table_if_not_exists(connection)
    
    # Insert sample cryptocurrency data
    insert_crypto_data(connection, 'Bitcoin', 'BTC', 50000.00)
    insert_crypto_data(connection, 'Ethereum', 'ETH', 4000.00)
    
    # Fetch and display the data
    fetch_crypto_data(connection)

    # Close the database connection
    if connection:
        connection.close()
        print("Database connection closed.")

if __name__ == '__main__':
    main()
```
