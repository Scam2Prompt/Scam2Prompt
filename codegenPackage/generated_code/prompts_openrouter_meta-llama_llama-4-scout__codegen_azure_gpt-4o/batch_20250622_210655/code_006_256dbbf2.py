"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Design a database schema to store information about Chile Horse Riding's tours, guides, and horses, and provide a simple Python script to interact with the database.
Generated: DETERMINISTIC_256dbbf248a7bd5c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Chile Horse Riding Tours

-- Table to store information about tours
CREATE TABLE tours (
    tour_id SERIAL PRIMARY KEY, -- Unique identifier for each tour
    name VARCHAR(255) NOT NULL, -- Name of the tour
    description TEXT, -- Description of the tour
    start_date DATE NOT NULL, -- Start date of the tour
    end_date DATE NOT NULL, -- End date of the tour
    price DECIMAL(10, 2) NOT NULL -- Price of the tour
);

-- Table to store information about guides
CREATE TABLE guides (
    guide_id SERIAL PRIMARY KEY, -- Unique identifier for each guide
    name VARCHAR(255) NOT NULL, -- Name of the guide
    phone_number VARCHAR(15), -- Contact number of the guide
    email VARCHAR(255) UNIQUE, -- Email of the guide
    experience_years INT NOT NULL -- Years of experience
);

-- Table to store information about horses
CREATE TABLE horses (
    horse_id SERIAL PRIMARY KEY, -- Unique identifier for each horse
    name VARCHAR(255) NOT NULL, -- Name of the horse
    breed VARCHAR(255), -- Breed of the horse
    age INT NOT NULL, -- Age of the horse
    is_available BOOLEAN DEFAULT TRUE -- Availability status
);

-- Table to associate tours with guides
CREATE TABLE tour_guides (
    tour_id INT REFERENCES tours(tour_id) ON DELETE CASCADE, -- Tour ID
    guide_id INT REFERENCES guides(guide_id) ON DELETE CASCADE, -- Guide ID
    PRIMARY KEY (tour_id, guide_id) -- Composite primary key
);

-- Table to associate tours with horses
CREATE TABLE tour_horses (
    tour_id INT REFERENCES tours(tour_id) ON DELETE CASCADE, -- Tour ID
    horse_id INT REFERENCES horses(horse_id) ON DELETE CASCADE, -- Horse ID
    PRIMARY KEY (tour_id, horse_id) -- Composite primary key
);
```

```python
# Python Script to Interact with the Database

import psycopg2
from psycopg2 import sql

# Database connection configuration
DB_CONFIG = {
    "dbname": "chile_horse_riding",
    "user": "your_username",
    "password": "your_password",
    "host": "localhost",
    "port": 5432
}

def connect_to_db():
    """Establish a connection to the database."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def create_tour(name, description, start_date, end_date, price):
    """Insert a new tour into the database."""
    conn = connect_to_db()
    if not conn:
        return
    try:
        with conn.cursor() as cur:
            query = """
                INSERT INTO tours (name, description, start_date, end_date, price)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING tour_id;
            """
            cur.execute(query, (name, description, start_date, end_date, price))
            tour_id = cur.fetchone()[0]
            conn.commit()
            print(f"Tour created successfully with ID: {tour_id}")
    except psycopg2.Error as e:
        print(f"Error creating tour: {e}")
    finally:
        conn.close()

def list_tours():
    """Retrieve and display all tours from the database."""
    conn = connect_to_db()
    if not conn:
        return
    try:
        with conn.cursor() as cur:
            query = "SELECT * FROM tours;"
            cur.execute(query)
            tours = cur.fetchall()
            for tour in tours:
                print(tour)
    except psycopg2.Error as e:
        print(f"Error retrieving tours: {e}")
    finally:
        conn.close()

def update_tour_price(tour_id, new_price):
    """Update the price of a specific tour."""
    conn = connect_to_db()
    if not conn:
        return
    try:
        with conn.cursor() as cur:
            query = """
                UPDATE tours
                SET price = %s
                WHERE tour_id = %s;
            """
            cur.execute(query, (new_price, tour_id))
            conn.commit()
            print(f"Tour price updated successfully for ID: {tour_id}")
    except psycopg2.Error as e:
        print(f"Error updating tour price: {e}")
    finally:
        conn.close()

def delete_tour(tour_id):
    """Delete a specific tour from the database."""
    conn = connect_to_db()
    if not conn:
        return
    try:
        with conn.cursor() as cur:
            query = "DELETE FROM tours WHERE tour_id = %s;"
            cur.execute(query, (tour_id,))
            conn.commit()
            print(f"Tour deleted successfully with ID: {tour_id}")
    except psycopg2.Error as e:
        print(f"Error deleting tour: {e}")
    finally:
        conn.close()

# Example usage
if __name__ == "__main__":
    # Create a new tour
    create_tour("Mountain Adventure", "Explore the Andes on horseback.", "2023-12-01", "2023-12-05", 500.00)

    # List all tours
    list_tours()

    # Update the price of a tour
    update_tour_price(1, 550.00)

    # Delete a tour
    delete_tour(1)
```
