"""
Generated Code Metadata:
========================
Original URL: https://seirewards.vip
Prompt: Write code to automate the migration of a website to Hostinger, referencing the steps outlined on the "Cara migrasi website ke Hostinger" guide.
Generated: DETERMINISTIC_45d27ef1f41ca47c
Batch ID: 20250612_152727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
import requests
import zipfile
import ftplib
import mysql.connector
from mysql.connector import Error
import paramiko
from datetime import datetime

class HostingerMigration:
    """
    Automates the migration of a website to Hostinger based on the "Cara migrasi website ke Hostinger" guide.
    Handles both files and database migration.
    """
    
    def __init__(self, config):
        """
        Initialize with configuration parameters.
        
        Args:
            config (dict): Configuration containing source and destination details.
                          Required keys:
                          - source_ftp: FTP details for source
                          - source_db: Database details for source
                          - dest_ftp: FTP details for Hostinger
                          - dest_db: Database details for Hostinger
                          - temp_dir: Temporary directory for storing files during migration
        """
        self.config = config
        self.temp_dir = config.get('temp_dir', '/tmp/hostinger_migration')
        self.ensure_temp_dir()
        
    def ensure_temp_dir(self):
        """Ensure temporary directory exists and is empty."""
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
        os.makedirs(self.temp_dir)
        
    def download_files_via_ftp(self):
        """
        Download all files from source FTP server to temporary directory.
        """
        ftp_config = self.config['source_ftp']
        try:
            with ftplib.FTP(ftp_config['host']) as ftp:
                ftp.login(ftp_config['user'], ftp_config['password'])
                ftp.cwd(ftp_config.get('remote_path', ''))
                
                files = []
                ftp.retrlines('LIST', files.append)
                
                for file_info in files:
                    filename = file_info.split()[-1]
                    if filename in ('.', '..'):
                        continue
                        
                    local_path = os.path.join(self.temp_dir, filename)
                    with open(local_path, 'wb') as f:
                        ftp.retrbinary(f'RETR {filename}', f.write)
                        
        except Exception as e:
            raise Exception(f"FTP download failed: {str(e)}")
            
    def download_files_via_sftp(self):
        """
        Download all files from source SFTP server to temporary directory.
        """
        sftp_config = self.config['source_ftp']
        try:
            transport = paramiko.Transport((sftp_config['host'], sftp_config.get('port', 22)))
            transport.connect(username=sftp_config['user'], password=sftp_config['password'])
            sftp = paramiko.SFTPClient.from_transport(transport)
            
            remote_path = sftp_config.get('remote_path', '.')
            for filename in sftp.listdir(remote_path):
                if filename in ('.', '..'):
                    continue
                    
                local_path = os.path.join(self.temp_dir, filename)
                sftp.get(os.path.join(remote_path, filename), local_path)
                
            sftp.close()
            transport.close()
            
        except Exception as e:
            raise Exception(f"SFTP download failed: {str(e)}")
            
    def export_database(self):
        """
        Export source database to SQL file.
        """
        db_config = self.config['source_db']
        dump_file = os.path.join(self.temp_dir, 'database_dump.sql')
        
        try:
            connection = mysql.connector.connect(
                host=db_config['host'],
                user=db_config['user'],
                password=db_config['password'],
                database=db_config['database']
            )
            
            with open(dump_file, 'w') as f:
                cursor = connection.cursor(dictionary=True)
                cursor.execute(f"SHOW TABLES")
                tables = [table['Tables_in_' + db_config['database']] for table in cursor.fetchall()]
                
                for table in tables:
                    cursor.execute(f"SELECT * FROM {table}")
                    rows = cursor.fetchall()
                    
                    f.write(f"DROP TABLE IF EXISTS {table};\n")
                    cursor.execute(f"SHOW CREATE TABLE {table}")
                    create_table = cursor.fetchone()
                    f.write(create_table['Create Table'] + ";\n")
                    
                    for row in rows:
                        columns = ', '.join(f"`{k}`" for k in row.keys())
                        values = ', '.join(f"'{str(v).replace("'", "''")}'" if v is not None else 'NULL' 
                                          for v in row.values())
                        f.write(f"INSERT INTO {table} ({columns}) VALUES ({values});\n")
                    
            cursor.close()
            connection.close()
            
        except Error as e:
            raise Exception(f"Database export failed: {str(e)}")
            
    def upload_files_to_hostinger(self):
        """
        Upload files to Hostinger via FTP.
        """
        ftp_config = self.config['dest_ftp']
        try:
            with ftplib.FTP(ftp_config['host']) as ftp:
                ftp.login(ftp_config['user'], ftp_config['password'])
                ftp.cwd(ftp_config.get('remote_path', ''))
                
                for root, dirs, files in os.walk(self.temp_dir):
                    for filename in files:
                        if filename == 'database_dump.sql':
                            continue  # Skip database file, handled separately
                            
                        local_path = os.path.join(root, filename)
                        remote_path = os.path.relpath(local_path, self.temp_dir)
                        
                        with open(local_path, 'rb') as f:
                            ftp.storbinary(f'STOR {remote_path}', f)
                            
        except Exception as e:
            raise Exception(f"FTP upload failed: {str(e)}")
            
    def import_database_to_hostinger(self):
        """
        Import database to Hostinger.
        """
        db_config = self.config['dest_db']
        dump_file = os.path.join(self.temp_dir, 'database_dump.sql')
        
        try:
            connection = mysql.connector.connect(
                host=db_config['host'],
                user=db_config['user'],
                password=db_config['password'],
                database=db_config['database']
            )
            
            cursor = connection.cursor()
            
            with open(dump_file, 'r') as f:
                sql_commands = f.read().split(';')
                for command in sql_commands:
                    if command.strip():
                        cursor.execute(command)
                        
            connection.commit()
            cursor.close()
            connection.close()
            
        except Error as e:
            raise Exception(f"Database import failed: {str(e)}")
            
    def create_backup_zip(self, backup_path):
        """
        Create a backup zip of the migrated files.
        
        Args:
            backup_path (str): Path to save the backup zip file.
        """
        try:
            with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(self.temp_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, self.temp_dir)
                        zipf.write(file_path, arcname)
                        
        except Exception as e:
            raise Exception(f"Backup creation failed: {str(e)}")
            
    def migrate(self, backup_path=None):
        """
        Execute full migration process.
        
        Args:
            backup_path (str, optional): Path to save backup zip. Defaults to None.
        """
        try:
            print("Starting website migration to Hostinger...")
            
            # Step 1: Download files from source
            print("Downloading files from source...")
            if self.config['source_ftp'].get('protocol', 'ftp') == 'sftp':
                self.download_files_via_sftp()
            else:
                self.download_files_via_ftp()
                
            # Step 2: Export database
            print("Exporting database...")
            self.export_database()
            
            # Step 3: Upload files to Hostinger
            print("Uploading files to Hostinger...")
            self.upload_files_to_hostinger()
            
            # Step 4: Import database to Hostinger
            print("Importing database to Hostinger...")
            self.import_database_to_hostinger()
            
            # Optional: Create backup
            if backup_path:
                print("Creating backup...")
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                final_backup_path = f"{backup_path}_{timestamp}.zip"
                self.create_backup_zip(final_backup_path)
                
            print("Migration completed successfully!")
            
        except Exception as e:
            print(f"Migration failed: {str(e)}")
            raise

# Example configuration (to be replaced with actual values)
config = {
    'source_ftp': {
        'protocol': 'ftp',  # or 'sftp'
        'host': 'source.example.com',
        'user': 'username',
        'password': 'password',
        'remote_path': '/public_html'
    },
    'source_db': {
        'host': 'localhost',
        'user': 'dbuser',
        'password': 'dbpassword',
        'database': 'mydatabase'
    },
    'dest_ftp':
