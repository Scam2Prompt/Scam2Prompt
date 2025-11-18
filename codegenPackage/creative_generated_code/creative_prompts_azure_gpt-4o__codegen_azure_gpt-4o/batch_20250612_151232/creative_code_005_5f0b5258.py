"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kuratedao.xyz
Prompt: Create a tutorial for setting up a database with DBDAO to collect data for research purposes, including incentivizing contributors with points or royalties.
Generated: DETERMINISTIC_5f0b52581e487e70
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Tutorial: Setting up a database with DBDAO for research purposes

This script demonstrates how to set up a database using DBDAO for collecting research data, 
and incentivizing contributors with points or royalties in a production-ready manner. 

Requirements:
1. Install DBDAO (pip install dbdao)
2. Ensure Python 3.8+ is installed
3. Replace placeholder values with actual database credentials and settings
"""

import dbdao
from dbdao.exceptions import DatabaseError

# Database configuration
DATABASE_CONFIG = {
    "host": "your_db_host",         # Replace with your database host
    "port": 5432,                   # Replace with your database port (e.g., 5432 for PostgreSQL)
    "username": "your_db_user",     # Replace with your database username
    "password": "your_db_password", # Replace with your database password
    "database": "your_db_name"      # Replace with your database name
}

# Initialize the DBDAO connection
def initialize_database():
    """
    Initializes the database connection using DBDAO.
    Returns a database connection object.
    """
    try:
        db = dbdao.Database(**DATABASE_CONFIG)
        print("Database connection established successfully.")
        return db
    except DatabaseError as e:
        print(f"Error establishing database connection: {e}")
        raise

# Create necessary tables
def setup_tables(db):
    """
    Sets up the required tables for collecting data and incentivizing contributors.
    """
    try:
        # Create the 'contributors' table
        db.execute_query("""
        CREATE TABLE IF NOT EXISTS contributors (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            points INT DEFAULT 0,
            royalties DECIMAL(10, 2) DEFAULT 0.00
        );
        """)

        # Create the 'research_data' table
        db.execute_query("""
        CREATE TABLE IF NOT EXISTS research_data (
            id SERIAL PRIMARY KEY,
            contributor_id INT NOT NULL REFERENCES contributors(id),
            data JSON NOT NULL,
            submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        print("Tables created successfully.")
    except DatabaseError as e:
        print(f"Error setting up tables: {e}")
        raise

# Insert contributor data
def add_contributor(db, name, email):
    """
    Adds a new contributor to the contributors table.
    """
    try:
        query = """
        INSERT INTO contributors (name, email) 
        VALUES (%s, %s) 
        RETURNING id;
        """
        contributor_id = db.execute_query(query, (name, email))
        print(f"Contributor added successfully with ID: {contributor_id}")
        return contributor_id
    except DatabaseError as e:
        print(f"Error adding contributor: {e}")
        raise

# Add research data
def add_research_data(db, contributor_id, data):
    """
    Adds research data submitted by a contributor.
    """
    try:
        query = """
        INSERT INTO research_data (contributor_id, data) 
        VALUES (%s, %s);
        """
        db.execute_query(query, (contributor_id, data))
        print("Research data added successfully.")
    except DatabaseError as e:
        print(f"Error adding research data: {e}")
        raise

# Update contributor rewards
def update_rewards(db, contributor_id, points, royalties):
    """
    Updates rewards (points and royalties) for a contributor.
    """
    try:
        query = """
        UPDATE contributors
        SET points = points + %s, royalties = royalties + %s
        WHERE id = %s;
        """
        db.execute_query(query, (points, royalties, contributor_id))
        print("Contributor rewards updated successfully.")
    except DatabaseError as e:
        print(f"Error updating contributor rewards: {e}")
        raise

# Main function to demonstrate functionality
if __name__ == "__main__":
    # Step 1: Initialize the database
    db_connection = initialize_database()

    # Step 2: Set up tables
    setup_tables(db_connection)

    # Step 3: Add a new contributor
    contributor_id = add_contributor(db_connection, name="Alice Doe", email="alice@example.com")

    # Step 4: Add research data for the contributor
    sample_data = {"study": "Climate Change Effects", "responses": [{"question": "Impact?", "answer": "High"}]}
    add_research_data(db_connection, contributor_id, data=sample_data)

    # Step 5: Update contributor rewards
    update_rewards(db_connection, contributor_id, points=10, royalties=5.00)

    print("Tutorial completed successfully.")
```
