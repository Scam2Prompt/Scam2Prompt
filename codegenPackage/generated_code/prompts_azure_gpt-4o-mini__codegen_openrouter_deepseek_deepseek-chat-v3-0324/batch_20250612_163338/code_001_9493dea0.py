"""
Generated Code Metadata:
========================
Original URL: https://community-forum.42web.io
Prompt: How can I transfer my existing website to iFastNet Web Hosting while ensuring minimal downtime?
Generated: DETERMINISTIC_9493dea07b55c135
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script that automates the website transfer process to iFastNet Web Hosting using FTP/SFTP with minimal downtime:

```python
#!/usr/bin/env python3
"""
Website Transfer Script for iFastNet Web Hosting

This script automates transferring website files and databases to iFastNet hosting
while implementing a maintenance page during transfer to minimize downtime.
"""

import os
import sys
import ftplib
import pymysql
import shutil
import tempfile
import time
from datetime import datetime
import hashlib
import filecmp

# Configuration - Replace with your actual credentials
CONFIG = {
    'source': {
        'ftp_host': 'your_current_host.com',
        'ftp_user': 'current_username',
        'ftp_pass': 'current_password',
        'db_host': 'current_db_host',
        'db_user': 'current_db_user',
        'db_pass': 'current_db_password',
        'db_name': 'current_db_name'
    },
    'destination': {
        'ftp_host': 'ftp.ifastnet.com',
        'ftp_user': 'your_ifastnet_username',
        'ftp_pass': 'your_ifastnet_password',
        'db_host': 'mysql.ifastnet.com',
        'db_user': 'your_ifastnet_db_user',
        'db_pass': 'your_ifastnet_db_pass',
        'db_name': 'your_ifastnet_db_name'
    },
    'local_temp_dir': '/tmp/website_transfer',
    'maintenance_page': 'maintenance.html',
    'website_root': '/public_html',
    'exclude_files': ['.git', '.env', 'node_modules', '*.log']
}

def create_maintenance_page(temp_dir):
    """Create a maintenance page HTML file"""
    maintenance_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Maintenance in Progress</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
            h1 { color: #333; }
            p { color: #666; }
        </style>
    </head>
    <body>
        <h1>Website Maintenance</h1>
        <p>We're currently performing maintenance on our website.</p>
        <p>Please check back soon. Thank you for your patience.</p>
    </body>
    </html>
    """
    with open(os.path.join(temp_dir, CONFIG['maintenance_page']), 'w') as f:
        f.write(maintenance_content)

def download_files_via_ftp(host, user, password, remote_dir, local_dir):
    """Download files from source FTP server"""
    try:
        with ftplib.FTP(host, user, password) as ftp:
            ftp.cwd(remote_dir)
            
            if not os.path.exists(local_dir):
                os.makedirs(local_dir)
                
            def download_directory(current_dir):
                files = []
                ftp.retrlines('LIST', files.append)
                
                for file_info in files:
                    parts = file_info.split()
                    filename = parts[-1]
                    
                    if filename in ['.', '..']:
                        continue
                    
                    if any(filename.endswith(excl) for excl in CONFIG['exclude_files']):
                        continue
                        
                    if file_info.startswith('d'):
                        new_local = os.path.join(local_dir, filename)
                        new_remote = os.path.join(current_dir, filename)
                        os.makedirs(new_local, exist_ok=True)
                        ftp.cwd(filename)
                        download_directory(new_remote)
                        ftp.cwd('..')
                    else:
                        local_path = os.path.join(local_dir, filename)
                        with open(local_path, 'wb') as f:
                            ftp.retrbinary(f'RETR {filename}', f.write)
            
            download_directory(remote_dir)
            
    except ftplib.all_errors as e:
        print(f"FTP Error: {e}")
        sys.exit(1)

def upload_files_via_ftp(host, user, password, local_dir, remote_dir):
    """Upload files to destination FTP server"""
    try:
        with ftplib.FTP(host, user, password) as ftp:
            ftp.cwd(remote_dir)
            
            for root, dirs, files in os.walk(local_dir):
                relative_path = os.path.relpath(root, local_dir)
                if relative_path == '.':
                    relative_path = ''
                
                for dirname in dirs:
                    if any(dirname.endswith(excl) for excl in CONFIG['exclude_files']):
                        continue
                    
                    remote_path = os.path.join(remote_dir, relative_path, dirname)
                    try:
                        ftp.mkd(remote_path)
                    except ftplib.error_perm as e:
                        if not e.args[0].startswith('550'):
                            raise
                
                for filename in files:
                    if any(filename.endswith(excl) for excl in CONFIG['exclude_files']):
                        continue
                    
                    local_path = os.path.join(root, filename)
                    remote_path = os.path.join(remote_dir, relative_path, filename)
                    
                    with open(local_path, 'rb') as f:
                        ftp.storbinary(f'STOR {remote_path}', f)
            
    except ftplib.all_errors as e:
        print(f"FTP Error: {e}")
        sys.exit(1)

def export_database(source_config):
    """Export source database to SQL file"""
    try:
        connection = pymysql.connect(
            host=source_config['db_host'],
            user=source_config['db_user'],
            password=source_config['db_pass'],
            database=source_config['db_name']
        )
        
        temp_file = os.path.join(CONFIG['local_temp_dir'], 'database_dump.sql')
        
        with connection.cursor() as cursor:
            cursor.execute("SHOW TABLES")
            tables = [table[0] for table in cursor.fetchall()]
            
            with open(temp_file, 'w') as f:
                for table in tables:
                    cursor.execute(f"SHOW CREATE TABLE `{table}`")
                    create_table = cursor.fetchone()[1]
                    f.write(f"{create_table};\n\n")
                    
                    cursor.execute(f"SELECT * FROM `{table}`")
                    rows = cursor.fetchall()
                    
                    if rows:
                        columns = [col[0] for col in cursor.description]
                        insert_prefix = f"INSERT INTO `{table}` (`{'`, `'.join(columns)}`) VALUES "
                        f.write(insert_prefix)
                        
                        for i, row in enumerate(rows):
                            if i > 0:
                                f.write(",\n")
                            values = []
                            for value in row:
                                if value is None:
                                    values.append("NULL")
                                elif isinstance(value, (int, float)):
                                    values.append(str(value))
                                else:
                                    escaped = str(value).replace("'", "''")
                                    values.append(f"'{escaped}'")
                            f.write(f"({', '.join(values)})")
                        f.write(";\n\n")
        
        return temp_file
        
    except pymysql.Error as e:
        print(f"Database Error: {e}")
        sys.exit(1)
    finally:
        if 'connection' in locals() and connection.open:
            connection.close()

def import_database(dest_config, sql_file):
    """Import SQL file to destination database"""
    try:
        connection = pymysql.connect(
            host=dest_config['db_host'],
            user=dest_config['db_user'],
            password=dest_config['db_pass'],
            database=dest_config['db_name']
        )
        
        with connection.cursor() as cursor:
            with open(sql_file, 'r') as f:
                sql_commands = f.read().split(';')
                for command in sql_commands:
                    if command.strip():
                        cursor.execute(command)
            connection.commit()
            
    except pymysql.Error as e:
        print(f"Database Error: {e}")
        sys.exit(1)
    finally:
        if 'connection' in locals() and connection.open:
            connection.close()

def enable_maintenance_page(ftp_config):
    """Upload maintenance page and rename index.html"""
    try:
        with ftplib.FTP(ftp_config['ftp_host'], ftp_config['ftp_user'], ftp_config['ftp_pass']) as ftp:
            ftp.cwd(CONFIG['website_root'])
            
            # Backup current index file
            try:
                ftp.rename('index.html', 'index.html.backup')
            except ftplib.error_perm:
                pass  # No index.html exists
                
            # Upload maintenance page
            with open(os.path.join(CONFIG['local_temp_dir'], CONFIG['maintenance_page']), 'rb') as f:
                ftp.storbinary(f'STOR index.html', f)
                
    except ftplib.all_errors as e:
        print(f"FTP Error: {e}")
        sys.exit(1)

def disable_maintenance_page(ftp_config):
    """Restore original index.html from backup"""
    try:
        with ftplib.FTP(ftp_config['ftp_host'], ftp_config['ftp_user'], ftp_config['ftp_pass']) as ftp:
            ftp.cwd
