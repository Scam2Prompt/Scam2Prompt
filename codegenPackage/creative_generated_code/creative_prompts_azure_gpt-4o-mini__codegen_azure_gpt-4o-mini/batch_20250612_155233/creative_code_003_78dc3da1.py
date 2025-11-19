"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medium.byethost10.com
Prompt: Create a guide for transferring an existing website to iFastNet Web Hosting, including code for database migration.
Generated: DETERMINISTIC_78dc3da1ebaf4c15
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import mysql.connector
from mysql.connector import Error

def transfer_website(source_dir, destination_dir):
    """
    Transfer website files from source directory to destination directory.

    :param source_dir: str, path to the source directory containing website files
    :param destination_dir: str, path to the destination directory on iFastNet
    """
    try:
        # Ensure the destination directory exists
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
            print(f"Created directory: {destination_dir}")
        
        # Copy files from source to destination
        shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)
        print(f"Website files transferred from {source_dir} to {destination_dir}.")
    
    except Exception as e:
        print(f"Error during website transfer: {e}")

def migrate_database(source_db_config, destination_db_config, db_name):
    """
    Migrate database from source to destination MySQL databases.

    :param source_db_config: dict, configuration for source MySQL database
    :param destination_db_config: dict, configuration for destination MySQL database
    :param db_name: str, name of the database to be migrated
    """
    try:
        # Connect to the source database
        source_conn = mysql.connector.connect(**source_db_config)
        if source_conn.is_connected():
            print("Connected to the source database.")

        # Create destination database
        destination_conn = mysql.connector.connect(**destination_db_config)
        if destination_conn.is_connected():
            cursor = destination_conn.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
            destination_conn.commit()
            print(f"Database {db_name} created in the destination.")

        # Export data from source and import to destination
        export_and_import_data(source_conn, destination_conn, db_name)

    except Error as e:
        print(f"Error: {e}")

    finally:
        if source_conn.is_connected():
            source_conn.close()
            print("Source database connection closed.")
        if destination_conn.is_connected():
            destination_conn.close()
            print("Destination database connection closed.")

def export_and_import_data(source_conn, destination_conn, db_name):
    """
    Export data from the source database and import it into the destination database.

    :param source_conn: MySQLConnection, connection to the source MySQL database
    :param destination_conn: MySQLConnection, connection to the destination MySQL database
    :param db_name: str, name of the database being migrated
    """
    try:
        source_cursor = source_conn.cursor()
        destination_cursor = destination_conn.cursor()

        # Get all tables from the source database
        source_cursor.execute(f"SHOW TABLES IN {db_name};")
        tables = source_cursor.fetchall()

        for (table_name,) in tables:
            # Create table in destination database
            source_cursor.execute(f"SHOW CREATE TABLE {db_name}.{table_name};")
            create_table_query = source_cursor.fetchone()[1]
            destination_cursor.execute(f"USE {db_name}; {create_table_query};")
            destination_conn.commit()

            # Transfer data
            source_cursor.execute(f"SELECT * FROM {db_name}.{table_name};")
            rows = source_cursor.fetchall()
            for row in rows:
                placeholders = ', '.join(['%s'] * len(row))
                destination_cursor.execute(f"INSERT INTO {db_name}.{table_name} VALUES ({placeholders});", row)

            destination_conn.commit()
            print(f"Data from table {table_name} migrated successfully.")

    except Error as e:
        print(f"Error during data migration: {e}")

# Example usage
if __name__ == "__main__":
    # Define source and destination configurations
    source_directory = "/path/to/your/website/files"
    destination_directory = "/path/on/ifastnet/server"

    source_database_config = {
        'host': 'source_host',
        'user': 'source_user',
        'password': 'source_password',
        'database': 'source_database'
    }

    destination_database_config = {
        'host': 'destination_host',
        'user': 'destination_user',
        'password': 'destination_password',
        'database': 'destination_database'
    }

    # Transfer website files
    transfer_website(source_directory, destination_directory)

    # Migrate the database
    migrate_database(source_database_config, destination_database_config, 'database_name')
```
