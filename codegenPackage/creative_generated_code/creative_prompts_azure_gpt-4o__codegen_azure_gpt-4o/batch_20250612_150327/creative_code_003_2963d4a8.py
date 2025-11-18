"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linearlive.co.uk
Prompt: Create a script to parse and store company registration details, such as those provided by Linear Live Limited, in a database.
Generated: DETERMINISTIC_2963d4a80bf9422b
Batch ID: 20250612_150327
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

# Database setup function
def setup_database():
    """
    Sets up the SQLite database and creates the required table if it doesn't exist.
    """
    try:
        # Connect to the SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect('company_data.db')
        cursor = conn.cursor()

        # Create the company registration table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS company_registration (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name TEXT NOT NULL,
                registration_number TEXT NOT NULL,
                address TEXT NOT NULL,
                country TEXT NOT NULL,
                status TEXT NOT NULL
            )
        """)

        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error setting up the database: {e}")

# Function to parse and store company registration details
def store_company_registration_details(data):
    """
    Stores company registration details in the database.

    Args:
        data (dict): A dictionary containing company registration details.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect('company_data.db')
        cursor = conn.cursor()

        # Insert data into the table
        cursor.execute("""
            INSERT INTO company_registration (company_name, registration_number, address, country, status)
            VALUES (:company_name, :registration_number, :address, :country, :status)
        """, {
            'company_name': data['company_name'],
            'registration_number': data['registration_number'],
            'address': data['address'],
            'country': data['country'],
            'status': data['status']
        })

        conn.commit()
        conn.close()
        print(f"Company registration details for '{data['company_name']}' have been saved.")
    except sqlite3.Error as e:
        print(f"Error storing company registration details: {e}")
    except KeyError as e:
        print(f"Missing required field in the input data: {e}")

# Function to parse JSON input
def parse_company_details(json_input):
    """
    Parses JSON input containing company registration details.

    Args:
        json_input (str): A JSON string containing company registration details.

    Returns:
        dict: A dictionary with parsed company details, or None if parsing fails.
    """
    try:
        data = json.loads(json_input)
        return data
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON input: {e}")
        return None

# Example Usage
if __name__ == "__main__":
    # Example JSON input for a company (can be replaced with dynamic user input)
    company_json = '''
    {
        "company_name": "Linear Live Limited",
        "registration_number": "12345678",
        "address": "123 Example Street, London, UK",
        "country": "United Kingdom",
        "status": "Active"
    }
    '''

    # Setup the database
    setup_database()

    # Parse the JSON input
    company_details = parse_company_details(company_json)

    # Store the parsed details in the database
    if company_details:
        store_company_registration_details(company_details)
```
