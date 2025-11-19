"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v2-pancakeswap.rf.gd
Prompt: Write a script to automate the transfer of a website to iFastNet Web Hosting, ensuring all files and databases are included.
Generated: DETERMINISTIC_92e3074198e03b1f
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import zipfile
import shutil
import paramiko
import MySQLdb

# Configuration
LOCAL_WEBSITE_DIR = '/path/to/local/website'
REMOTE_SERVER = 'your_ifastnet_server'
REMOTE_USER = 'your_username'
REMOTE_PASSWORD = 'your_password'
REMOTE_WEBSITE_DIR = '/path/to/remote/website'
DATABASE_NAME = 'your_database'
DATABASE_USER = 'db_username'
DATABASE_PASSWORD = 'db_password'
DATABASE_HOST = 'localhost'  # Usually localhost for iFastNet

def create_zip_archive(source_dir, output_filename):
    """Creates a zip archive of the specified directory."""
    try:
        with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for foldername, subfolders, filenames in os.walk(source_dir):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    zip_file.write(file_path, os.path.relpath(file_path, source_dir))
        print(f"Successfully created zip archive: {output_filename}")
    except Exception as e:
        print(f"Error creating zip archive: {e}")

def upload_files_to_server(local_file, remote_path):
    """Uploads the specified file to the remote server using SFTP."""
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(REMOTE_SERVER, username=REMOTE_USER, password=REMOTE_PASSWORD)

        sftp = client.open_sftp()
        sftp.put(local_file, remote_path)
        sftp.close()
        client.close()
        print(f"Successfully uploaded {local_file} to {remote_path}")
    except Exception as e:
        print(f"Error uploading file to server: {e}")

def backup_database(db_name, db_user, db_password, db_host):
    """Backs up the specified MySQL database to a SQL file."""
    try:
        backup_file = f"{db_name}_backup.sql"
        command = f"mysqldump -u {db_user} -p{db_password} -h {db_host} {db_name} > {backup_file}"
        os.system(command)
        print(f"Database backup created: {backup_file}")
        return backup_file
    except Exception as e:
        print(f"Error backing up database: {e}")
        return None

def upload_database_backup(backup_file, remote_path):
    """Uploads the database backup to the remote server."""
    if backup_file is None:
        print("No backup file to upload.")
        return
    upload_files_to_server(backup_file, remote_path)

def main():
    """Main function to automate website transfer."""
    # Step 1: Create a zip archive of the website files
    zip_filename = 'website_backup.zip'
    create_zip_archive(LOCAL_WEBSITE_DIR, zip_filename)

    # Step 2: Upload the website zip file to the remote server
    upload_files_to_server(zip_filename, os.path.join(REMOTE_WEBSITE_DIR, zip_filename))

    # Step 3: Backup the database
    db_backup_file = backup_database(DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST)

    # Step 4: Upload the database backup to the remote server
    upload_database_backup(db_backup_file, os.path.join(REMOTE_WEBSITE_DIR, db_backup_file))

    # Clean up local files
    try:
        os.remove(zip_filename)
        if db_backup_file:
            os.remove(db_backup_file)
        print("Local backup files cleaned up successfully.")
    except Exception as e:
        print(f"Error cleaning up local files: {e}")

if __name__ == "__main__":
    main()
```

Make sure to replace placeholders (`/path/to/local/website`, `your_ifastnet_server`, and others) with actual values before running the script. Ensure that `paramiko` and `MySQLdb` libraries are installed in your Python environment.
