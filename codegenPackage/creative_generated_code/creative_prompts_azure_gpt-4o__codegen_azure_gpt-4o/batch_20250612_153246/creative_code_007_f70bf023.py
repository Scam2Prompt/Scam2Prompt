"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lenderlibrary.ca
Prompt: Write a program to convert Dominion Lending's mortgage documentation into a searchable database, categorizing data by property type, income type, and lender accreditation.
Generated: DETERMINISTIC_f70bf02315661101
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import json

# Define database schema
DB_SCHEMA = """
CREATE TABLE IF NOT EXISTS mortgage_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_type TEXT NOT NULL,
    income_type TEXT NOT NULL,
    lender_accreditation TEXT NOT NULL,
    document_content TEXT NOT NULL
);
"""

def create_database(db_name="mortgage_data.db"):
    """Creates a SQLite database with the required schema."""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute(DB_SCHEMA)  # Create table if not exists
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error creating database:", e)

def insert_data(db_name, property_type, income_type, lender_accreditation, document_content):
    """
    Inserts a single record into the mortgage_data table.
    
    :param db_name: Name of the SQLite database file
    :param property_type: Type of property (e.g., Residential, Commercial)
    :param income_type: Type of income (e.g., Salaried, Self-employed)
    :param lender_accreditation: Accreditation of the lender
    :param document_content: Full content of the mortgage document
    """
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO mortgage_data (property_type, income_type, lender_accreditation, document_content) 
            VALUES (?, ?, ?, ?)
        """, (property_type, income_type, lender_accreditation, document_content))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error inserting data:", e)

def search_data(db_name, property_type=None, income_type=None, lender_accreditation=None):
    """
    Searches the database for records matching the given criteria.
    
    :param db_name: Name of the SQLite database file
    :param property_type: Filter by property type (optional)
    :param income_type: Filter by income type (optional)
    :param lender_accreditation: Filter by lender accreditation (optional)
    :return: List of matching records
    """
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        # Build query dynamically based on filters
        query = "SELECT * FROM mortgage_data WHERE 1=1"
        params = []
        if property_type:
            query += " AND property_type = ?"
            params.append(property_type)
        if income_type:
            query += " AND income_type = ?"
            params.append(income_type)
        if lender_accreditation:
            query += " AND lender_accreditation = ?"
            params.append(lender_accreditation)
        
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()
        return results
    except sqlite3.Error as e:
        print("Error searching data:", e)
        return []

def load_documentation(file_path):
    """
    Loads mortgage documentation from a JSON file.
    
    :param file_path: Path to the JSON file containing documentation
    :return: List of mortgage records
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print("Error loading documentation:", e)
        return []

# Example usage
if __name__ == "__main__":
    db_name = "mortgage_data.db"
    
    # Step 1: Create database
    create_database(db_name)
    
    # Step 2: Load documentation from a JSON file
    documentation = load_documentation("documentation.json")
    
    # Step 3: Insert loaded documentation into the database
    for record in documentation:
        insert_data(
            db_name=db_name,
            property_type=record.get("property_type", "Unknown"),
            income_type=record.get("income_type", "Unknown"),
            lender_accreditation=record.get("lender_accreditation", "Unknown"),
            document_content=record.get("document_content", "")
        )
    
    # Step 4: Search database for specific records
    search_results = search_data(db_name, property_type="Residential")
    for result in search_results:
        print(result)
```
