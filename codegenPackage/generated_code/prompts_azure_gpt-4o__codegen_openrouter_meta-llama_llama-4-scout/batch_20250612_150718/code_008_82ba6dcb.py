"""
Generated Code Metadata:
========================
Original URL: https://consultech.ci
Prompt: Provide an example of integrating Microsoft and Oracle technologies for enterprise resource planning, as highlighted by ConsulTech's expertise.
Generated: DETERMINISTIC_82ba6dcba77763b3
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Microsoft and Oracle Integration for ERP**
=============================================

### Prerequisites

* Python 3.8+
* `pyodbc` library for Oracle database connection
* `pymssql` library for Microsoft SQL Server connection
* `xml.etree.ElementTree` for XML parsing

### Code

```python
import pyodbc
import pymssql
import xml.etree.ElementTree as ET
from datetime import datetime

# Oracle Database Connection Settings
ORACLE_DB_HOST = 'oracle-host'
ORACLE_DB_NAME = 'oracle-db'
ORACLE_DB_USER = 'oracle-user'
ORACLE_DB_PASSWORD = 'oracle-password'

# Microsoft SQL Server Connection Settings
MSSQL_DB_HOST = 'mssql-host'
MSSQL_DB_NAME = 'mssql-db'
MSSQL_DB_USER = 'mssql-user'
MSSQL_DB_PASSWORD = 'mssql-password'

def connect_oracle_db():
    """Establish a connection to the Oracle database"""
    try:
        oracle_conn = pyodbc.connect(f"DRIVER={{Oracle ODBC Driver - ODBC Driver 21 for Oracle}};SERVER={ORACLE_DB_HOST};DATABASE={ORACLE_DB_NAME};UID={ORACLE_DB_USER};PWD={ORACLE_DB_PASSWORD}")
        return oracle_conn
    except pyodbc.Error as e:
        print(f"Oracle DB connection error: {e}")
        return None

def connect_mssql_db():
    """Establish a connection to the Microsoft SQL Server database"""
    try:
        mssql_conn = pymssql.connect(server=MSSQL_DB_HOST, user=MSSQL_DB_USER, password=MSSQL_DB_PASSWORD, database=MSSQL_DB_NAME)
        return mssql_conn
    except pymssql.Error as e:
        print(f"MS SQL Server DB connection error: {e}")
        return None

def sync_data(oracle_conn, mssql_conn):
    """Synchronize data between Oracle and MS SQL Server databases"""
    try:
        # Retrieve data from Oracle database
        oracle_cursor = oracle_conn.cursor()
        oracle_cursor.execute("SELECT * FROM customers")
        oracle_data = oracle_cursor.fetchall()

        # Insert data into MS SQL Server database
        mssql_cursor = mssql_conn.cursor()
        for row in oracle_data:
            mssql_cursor.execute("INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)", row)

        # Commit changes and close cursors
        mssql_conn.commit()
        oracle_cursor.close()
        mssql_cursor.close()
    except (pyodbc.Error, pymssql.Error) as e:
        print(f"Data synchronization error: {e}")

def generate_xml_report(mssql_conn):
    """Generate an XML report from MS SQL Server database data"""
    try:
        # Retrieve data from MS SQL Server database
        mssql_cursor = mssql_conn.cursor()
        mssql_cursor.execute("SELECT * FROM customers")
        mssql_data = mssql_cursor.fetchall()

        # Create an XML report
        root = ET.Element("customers")
        for row in mssql_data:
            customer = ET.SubElement(root, "customer")
            ET.SubElement(customer, "name").text = row[0]
            ET.SubElement(customer, "email").text = row[1]
            ET.SubElement(customer, "phone").text = row[2]

        # Save the XML report to a file
        tree = ET.ElementTree(root)
        tree.write("customers_report.xml", encoding="utf-8")
    except (pyodbc.Error, pymssql.Error) as e:
        print(f"XML report generation error: {e}")

def main():
    oracle_conn = connect_oracle_db()
    mssql_conn = connect_mssql_db()

    if oracle_conn and mssql_conn:
        sync_data(oracle_conn, mssql_conn)
        generate_xml_report(mssql_conn)

    if oracle_conn:
        oracle_conn.close()
    if mssql_conn:
        mssql_conn.close()

if __name__ == "__main__":
    start_time = datetime.now()
    main()
    print(f"Execution time: {datetime.now() - start_time}")
```

### Example Usage

Run the script using Python:
```bash
python microsoft_oracle_integration.py
```
This will establish connections to the Oracle and MS SQL Server databases, synchronize data between them, and generate an XML report from the MS SQL Server database data. The execution time will be printed to the console.
