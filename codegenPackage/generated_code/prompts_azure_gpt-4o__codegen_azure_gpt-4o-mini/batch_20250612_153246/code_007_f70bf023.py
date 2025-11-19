"""
Generated Code Metadata:
========================
Original URL: https://lenderlibrary.ca
Prompt: Write a program to convert Dominion Lending's mortgage documentation into a searchable database, categorizing data by property type, income type, and lender accreditation.
Generated: DETERMINISTIC_f70bf02315661101
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
import csv
import os

# Define the database schema
DB_NAME = 'mortgage_documents.db'

def create_database():
    """Create a SQLite database and the necessary tables."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Create a table for mortgage documents
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mortgage_documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            property_type TEXT NOT NULL,
            income_type TEXT NOT NULL,
            lender_accreditation TEXT NOT NULL,
            document_path TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def insert_document(property_type, income_type, lender_accreditation, document_path):
    """Insert a new mortgage document into the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            INSERT INTO mortgage_documents (property_type, income_type, lender_accreditation, document_path)
            VALUES (?, ?, ?, ?)
        ''', (property_type, income_type, lender_accreditation, document_path))
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting document: {e}")
    finally:
        conn.close()

def load_documents_from_csv(csv_file_path):
    """Load mortgage documents from a CSV file into the database."""
    if not os.path.exists(csv_file_path):
        print(f"CSV file not found: {csv_file_path}")
        return
    
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            try:
                property_type = row['property_type']
                income_type = row['income_type']
                lender_accreditation = row['lender_accreditation']
                document_path = row['document_path']
                
                insert_document(property_type, income_type, lender_accreditation, document_path)
            except KeyError as e:
                print(f"Missing expected column in CSV: {e}")
            except Exception as e:
                print(f"Error processing row {row}: {e}")

def search_documents(property_type=None, income_type=None, lender_accreditation=None):
    """Search for mortgage documents based on specified criteria."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    query = 'SELECT * FROM mortgage_documents WHERE 1=1'
    params = []
    
    if property_type:
        query += ' AND property_type = ?'
        params.append(property_type)
    if income_type:
        query += ' AND income_type = ?'
        params.append(income_type)
    if lender_accreditation:
        query += ' AND lender_accreditation = ?'
        params.append(lender_accreditation)
    
    cursor.execute(query, params)
    results = cursor.fetchall()
    
    conn.close()
    return results

if __name__ == '__main__':
    # Create the database and tables
    create_database()
    
    # Load documents from a CSV file (update the path as necessary)
    load_documents_from_csv('mortgage_documents.csv')
    
    # Example search (modify parameters as needed)
    results = search_documents(property_type='Residential', income_type='Verified', lender_accreditation='Approved')
    
    # Print search results
    for result in results:
        print(result)
```
