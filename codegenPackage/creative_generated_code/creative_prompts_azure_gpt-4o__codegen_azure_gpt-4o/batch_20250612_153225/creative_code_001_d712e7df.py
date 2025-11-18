"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kimiyashimi.com
Prompt: Generate a script that uses the SDS (Safety Data Sheet) information to create a database for tracking chemical properties, hazards, and storage guidelines, referencing Kimia Shimi's emphasis on SDS documentation.
Generated: DETERMINISTIC_d712e7dfc4e9b97f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

# Define the database schema
DATABASE_NAME = "chemical_safety.db"

def initialize_database():
    """
    Initializes the SQLite database and creates necessary tables if they don't exist.
    """
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Create the chemicals table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chemicals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        cas_number TEXT NOT NULL UNIQUE,
        molecular_formula TEXT,
        hazards TEXT,
        storage_guidelines TEXT,
        first_aid_measures TEXT,
        date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    connection.commit()
    connection.close()

def add_chemical(name, cas_number, molecular_formula, hazards, storage_guidelines, first_aid_measures):
    """
    Adds a chemical entry to the database.
    :param name: Name of the chemical
    :param cas_number: CAS number for the chemical (unique identifier)
    :param molecular_formula: Molecular formula for the chemical
    :param hazards: Hazard information (e.g., flammable, toxic)
    :param storage_guidelines: Storage guidelines for the chemical
    :param first_aid_measures: Relevant first aid measures in case of exposure
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO chemicals (name, cas_number, molecular_formula, hazards, storage_guidelines, first_aid_measures)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (name, cas_number, molecular_formula, hazards, storage_guidelines, first_aid_measures))

        connection.commit()
        connection.close()
        print(f"Chemical '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: A chemical with CAS number '{cas_number}' already exists in the database.")
    except Exception as e:
        print(f"An error occurred: {e}")

def query_chemicals():
    """
    Queries and retrieves all chemical entries from the database.
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM chemicals")
        results = cursor.fetchall()

        connection.close()

        return results
    except Exception as e:
        print(f"An error occurred while querying the database: {e}")
        return []

if __name__ == "__main__":
    # Initialize database and create table if it doesn't exist
    initialize_database()

    # Example usage: Adding chemicals to the database
    add_chemical(
        name="Sulfuric Acid",
        cas_number="7664-93-9",
        molecular_formula="H2SO4",
        hazards="Corrosive, harmful if inhaled",
        storage_guidelines="Store in a cool, dry, well-ventilated area away from incompatible substances.",
        first_aid_measures="Flush skin thoroughly with water, seek medical attention for severe exposure."
    )

    add_chemical(
        name="Acetone",
        cas_number="67-64-1",
        molecular_formula="C3H6O",
        hazards="Highly flammable, irritant",
        storage_guidelines="Store in tightly closed containers away from heat, sparks, and open flames.",
        first_aid_measures="Move to fresh air if inhaled, wash affected skin with soap and water."
    )

    # Query and display chemicals
    chemicals = query_chemicals()
    for chemical in chemicals:
        print(chemical)
```
