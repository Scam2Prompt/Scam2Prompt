"""
Generated Code Metadata:
========================
Original URL: https://swapepoocoine.blogspot.com
Prompt: Write a SQL query to retrieve shoe information from a database, filtering by type (e.g., chuteira, tenis de esporte).
Generated: DETERMINISTIC_d68da98364afc82f
Batch ID: 20250622_212513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve shoe information from the database, filtering by type

-- Define the database schema for clarity
-- CREATE TABLE shoes (
--     id INT PRIMARY KEY,
--     name VARCHAR(255) NOT NULL,
--     type VARCHAR(255) NOT NULL,
--     size DECIMAL(3, 2) NOT NULL,
--     color VARCHAR(255) NOT NULL,
--     material VARCHAR(255) NOT NULL
-- );

-- SQL query to retrieve shoe information
SELECT 
    s.id,
    s.name,
    s.type,
    s.size,
    s.color,
    s.material
FROM 
    shoes s
WHERE 
    LOWER(s.type) IN (:type);

-- Example usage
-- Prepare the query with a parameter to prevent SQL injection
-- Replace ':type' with actual values or use a prepared statement

-- For chuteira
-- SELECT * FROM shoes WHERE LOWER(type) = 'chuteira';

-- For tenis de esporte
-- SELECT * FROM shoes WHERE LOWER(type) = 'tenis de esporte';

-- For multiple types
-- SELECT * FROM shoes WHERE LOWER(type) IN ('chuteira', 'tenis de esporte');
```

To execute this query securely with multiple types using a programming language (e.g., Python with psycopg2 for PostgreSQL):

```python
import psycopg2

def get_shoes_by_type(types):
    try:
        # Establish a connection to the database
        conn = psycopg2.connect(
            dbname="your_database",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        )
        
        # Create a cursor object
        cur = conn.cursor()
        
        # SQL query string
        query = """
            SELECT 
                s.id,
                s.name,
                s.type,
                s.size,
                s.color,
                s.material
            FROM 
                shoes s
            WHERE 
                LOWER(s.type) IN (%s);
        """
        
        # Execute the query with parameters
        cur.execute(query, (tuple(types),))
        
        # Fetch all rows
        rows = cur.fetchall()
        
        # Close the cursor and connection
        cur.close()
        conn.close()
        
        return rows
    
    except psycopg2.Error as e:
        print(f"Error: {e}")
        return []

# Example usage
types = ['chuteira', 'tenis de esporte']
shoes = get_shoes_by_type(types)
for shoe in shoes:
    print(shoe)
```
