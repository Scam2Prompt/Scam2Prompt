"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smart-appbasicguardversepro.com
Prompt: Write a script to automate website migration to Hostinger using FTP and database import/export.
Generated: DETERMINISTIC_04c513e7f4979a55
Batch ID: 20250612_150644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import ftplib
import MySQLdb
import tarfile
from contextlib import closing

# Configuration variables
FTP_HOST = 'ftp.yourhostinger.com'
FTP_USER = 'your_ftp_username'
FTP_PASS = 'your_ftp_password'
DB_HOST = 'localhost'
DB_USER = 'your_db_username'
DB_PASS = 'your_db_password'
DB_NAME = 'your_db_name'
LOCAL_BACKUP_DIR = '/path/to/local/backup/'
REMOTE_BACKUP_DIR = '/path/to/remote/backup/'
DB_DUMP_FILE = 'database_backup.sql'
TAR_FILE = 'website_backup.tar.gz'

def ftp_upload(local_file, remote_file):
    """Uploads a file to the FTP server."""
    with closing(ftplib.FTP(FTP_HOST)) as ftp:
        try:
            ftp.login(FTP_USER, FTP_PASS)
            with open(local_file, 'rb') as file:
                ftp.storbinary(f'STOR {remote_file}', file)
            print(f'Successfully uploaded {local_file} to {remote_file}')
        except ftplib.all_errors as e:
            print(f'FTP error: {e}')

def db_backup(db_name, dump_file):
    """Creates a database backup and saves it to a specified file."""
    try:
        db = MySQLdb.connect(DB_HOST, DB_USER, DB_PASS, db_name)
        cursor = db.cursor()
        with open(dump_file, 'w') as f:
            cursor.execute(f'SHOW TABLES')
            tables = cursor.fetchall()
            for table in tables:
                table_name = table[0]
                cursor.execute(f'SELECT * FROM {table_name}')
                rows = cursor.fetchall()
                # Write table creation statement
                cursor.execute(f'SHOW CREATE TABLE {table_name}')
                create_table_stmt = cursor.fetchone()[1]
                f.write(f'{create_table_stmt};\n')
                # Write insert statements
                for row in rows:
                    values = ', '.join(f"'{str(v).replace('\'', '\\\'')}'" for v in row)
                    f.write(f'INSERT INTO {table_name} VALUES ({values});\n')
        print(f'Database backup successfully created: {dump_file}')
    except MySQLdb.Error as e:
        print(f'Database error: {e}')
    finally:
        if 'db' in locals():
            db.close()

def create_tarball(source_dir, tar_file):
    """Creates a tar.gz archive of the specified directory."""
    with tarfile.open(tar_file, 'w:gz') as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
    print(f'Tarball created: {tar_file}')

def migrate_website():
    """Main function to handle the website migration process."""
    # Step 1: Backup database
    db_backup(DB_NAME, DB_DUMP_FILE)

    # Step 2: Create a tarball of the website files
    create_tarball(LOCAL_BACKUP_DIR, TAR_FILE)

    # Step 3: Upload database dump to FTP
    ftp_upload(DB_DUMP_FILE, f'{REMOTE_BACKUP_DIR}/{DB_DUMP_FILE}')

    # Step 4: Upload website tarball to FTP
    ftp_upload(TAR_FILE, f'{REMOTE_BACKUP_DIR}/{TAR_FILE}')

if __name__ == '__main__':
    try:
        migrate_website()
    except Exception as e:
        print(f'An error occurred: {e}')
```

Make sure to replace the configuration variables with appropriate values before running the code. Also, ensure you have the necessary permissions for the database and FTP server.
