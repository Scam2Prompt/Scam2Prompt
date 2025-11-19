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
"""
Guide: Transfer an existing website to iFastNet Web Hosting including database migration.
This script automates the process of migrating a database from a local server to remote iFastNet hosting.

Prerequisites:
- Have access to both the local database and remote database credentials.
- Install Python and MySQL connector library (`pip install mysql-connector-python`).

IMPORTANT: Ensure to back up your data before running this script.
"""

import mysql.connector
from mysql.connector import Error


def backup_database(local_db_config, backup_file_path):
    """
    Creates a backup of the local database by exporting its contents to a file.
    
    :param local_db_config: Dictionary containing local database connection details.
    :param backup_file_path: Path to save the backup file.
    """
    try:
        # Connect to the local database
        connection = mysql.connector.connect(**local_db_config)
        cursor = connection.cursor()

        # Query to get all tables
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        # Open the backup file to write data
        with open(backup_file_path, 'w', encoding='utf-8') as backup_file:
            for (table_name,) in tables:
                # Export table structure
                cursor.execute(f"SHOW CREATE TABLE {table_name}")
                create_table_query = cursor.fetchone()[1]
                backup_file.write(f"{create_table_query};\n\n")

                # Export table data
                cursor.execute(f"SELECT * FROM {table_name}")
                rows = cursor.fetchall()
                for row in rows:
                    values = ', '.join([f"'{str(value)}'" if value is not None else 'NULL'
                                        for value in row])
                    insert_query = f"INSERT INTO {table_name} VALUES ({values});\n"
                    backup_file.write(insert_query)

                backup_file.write("\n\n")

        print(f"Database successfully backed up to {backup_file_path}")

    except Error as e:
        print(f"Error while backing up database: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def restore_database(remote_db_config, backup_file_path):
    """
    Restores the database backup to the remote server.
    
    :param remote_db_config: Dictionary containing remote database connection details.
    :param backup_file_path: Path to the backup file to restore.
    """
    try:
        # Connect to the remote database
        connection = mysql.connector.connect(**remote_db_config)
        cursor = connection.cursor()

        # Read backup file and execute queries
        with open(backup_file_path, 'r', encoding='utf-8') as backup_file:
            sql_commands = backup_file.read().split(';')

            for command in sql_commands:
                if command.strip():  # Skip empty lines
                    cursor.execute(command)

        connection.commit()
        print("Database successfully restored to remote server.")

    except Error as e:
        print(f"Error while restoring database: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


if __name__ == "__main__":
    # Local database connection details
    local_database_config = {
        'host': 'localhost',
        'user': 'your_local_db_user',
        'password': 'your_local_db_password',
        'database': 'your_local_db_name'
    }

    # Remote database connection details
    remote_database_config = {
        'host': 'your_ifastnet_host',
        'user': 'your_ifastnet_user',
        'password': 'your_ifastnet_password',
        'database': 'your_ifastnet_db_name'
    }

    # File path for backup
    backup_file = "database_backup.sql"

    # Step 1: Backup local database
    backup_database(local_database_config, backup_file)

    # Step 2: Restore backup to remote database
    restore_database(remote_database_config, backup_file)
```
