"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://truflation-governance.com
Prompt: What specific configurations are needed for a successful website migration to Hostinger?
Generated: DETERMINISTIC_6f7eec0fe1962b97
Batch ID: 20250612_155332
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
import subprocess

class WebsiteMigrator:
    """
    A class to handle the migration of a website to Hostinger.
    """

    def __init__(self, source_directory, destination_directory, database_config):
        """
        Initializes the WebsiteMigrator with source and destination directories and database configuration.

        :param source_directory: str - Path to the source website files
        :param destination_directory: str - Path to the destination directory on Hostinger
        :param database_config: dict - Dictionary containing database configuration (host, user, password, db_name)
        """
        self.source_directory = source_directory
        self.destination_directory = destination_directory
        self.database_config = database_config

    def transfer_files(self):
        """
        Transfers files from the source directory to the destination directory.

        Raises:
            Exception: If the transfer fails
        """
        try:
            shutil.copytree(self.source_directory, self.destination_directory)
            print(f"Successfully transferred files from {self.source_directory} to {self.destination_directory}")
        except Exception as e:
            raise Exception(f"Error during file transfer: {e}")

    def export_database(self):
        """
        Exports the database from the source configuration.

        Raises:
            Exception: If the export fails
        """
        try:
            export_command = (
                f"mysqldump -h {self.database_config['host']} "
                f"-u {self.database_config['user']} "
                f"-p{self.database_config['password']} "
                f"{self.database_config['db_name']} > {self.database_config['db_name']}.sql"
            )
            subprocess.run(export_command, shell=True, check=True)
            print("Database export successful.")
        except subprocess.CalledProcessError as e:
            raise Exception(f"Database export failed: {e}")

    def import_database(self):
        """
        Imports the database to the Hostinger environment.

        Raises:
            Exception: If the import fails
        """
        try:
            import_command = (
                f"mysql -h {self.database_config['host']} "
                f"-u {self.database_config['user']} "
                f"-p{self.database_config['password']} "
                f"{self.database_config['db_name']} < {self.database_config['db_name']}.sql"
            )
            subprocess.run(import_command, shell=True, check=True)
            print("Database import successful.")
        except subprocess.CalledProcessError as e:
            raise Exception(f"Database import failed: {e}")

    def run_migration(self):
        """
        Executes the full migration process.
        """
        try:
            self.transfer_files()
            self.export_database()
            self.import_database()
            print("Migration completed successfully.")
        except Exception as e:
            print(f"Migration failed: {e}")

if __name__ == "__main__":
    # Configuration
    source_dir = "/path/to/source/website"
    dest_dir = "/path/to/hostinger/destination"
    db_config = {
        "host": "localhost",
        "user": "db_user",
        "password": "db_password",
        "db_name": "db_name"
    }

    # Create an instance of the migrator and run the migration
    migrator = WebsiteMigrator(source_dir, dest_dir, db_config)
    migrator.run_migration()
```
