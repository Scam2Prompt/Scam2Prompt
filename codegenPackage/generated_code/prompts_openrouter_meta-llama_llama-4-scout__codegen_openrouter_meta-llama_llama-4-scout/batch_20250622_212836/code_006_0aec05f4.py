"""
Generated Code Metadata:
========================
Original URL: https://meghbd.com
Prompt: Write a script to automate daily remote backups on a Megh iTech Linux web hosting server.
Generated: DETERMINISTIC_0aec05f4c405a18e
Batch ID: 20250622_212836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# Configuration
BACKUP_DIR="/backups"
HOSTNAME=$(hostname)
DATE=$(date +"%Y-%m-%d")
DB_USER="your_database_user"
DB_PASSWORD="your_database_password"
DB_NAME="your_database_name"
FTP_SERVER="ftp.yourftpserver.com"
FTP_USER="your_ftp_username"
FTP_PASSWORD="your_ftp_password"

# Create backup directory if it doesn't exist
if [ ! -d "$BACKUP_DIR" ]; then
  mkdir -p "$BACKUP_DIR"
fi

# Function to backup MySQL database
backup_database() {
  mysqldump -u $DB_USER -p$DB_PASSWORD $DB_NAME > $BACKUP_DIR/${HOSTNAME}_${DATE}_database.sql
  if [ $? -ne 0 ]; then
    echo "Error backing up database"
    exit 1
  fi
}

# Function to backup website files
backup_website() {
  tar -czf $BACKUP_DIR/${HOSTNAME}_${DATE}_website.tar.gz /var/www/html
  if [ $? -ne 0 ]; then
    echo "Error backing up website files"
    exit 1
  fi
}

# Function to upload backups to FTP server
upload_to_ftp() {
  lftp -c "open $FTP_SERVER; login $FTP_USER $FTP_PASSWORD; put $BACKUP_DIR/${HOSTNAME}_${DATE}_database.sql; put $BACKUP_DIR/${HOSTNAME}_${DATE}_website.tar.gz"
  if [ $? -ne 0 ]; then
    echo "Error uploading backups to FTP server"
    exit 1
  fi
}

# Main script
main() {
  backup_database
  backup_website
  upload_to_ftp
  
  # Remove old backups (keep last 7 days)
  find $BACKUP_DIR -type f -name "${HOSTNAME}_*_database.sql" -mtime +7 -delete
  find $BACKUP_DIR -type f -name "${HOSTNAME}_*_website.tar.gz" -mtime +7 -delete
}

main
```

```python
# Alternatively, here is a Python version using paramiko for FTP and mysql-connector-python for database backup

import os
import paramiko
import mysql.connector
from datetime import datetime, timedelta
import tarfile

# Configuration
BACKUP_DIR = "/backups"
HOSTNAME = os.uname().nodename
DB_USER = "your_database_user"
DB_PASSWORD = "your_database_password"
DB_NAME = "your_database_name"
FTP_SERVER = "ftp.yourftpserver.com"
FTP_USER = "your_ftp_username"
FTP_PASSWORD = "your_ftp_password"

def backup_database():
    try:
        cnx = mysql.connector.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host='localhost',
            database=DB_NAME
        )
        cursor = cnx.cursor()
        cursor.execute("SHOW CREATE DATABASE " + DB_NAME)
        dump = ""
        for db in [DB_NAME]:
            dump += "--databases " + db + " "
        dump += "> " + BACKUP_DIR + "/" + HOSTNAME + "_" + datetime.now().strftime("%Y-%m-%d") + "_database.sql"
        os.system("mysqldump -u " + DB_USER + " -p" + DB_PASSWORD + " " + DB_NAME + " > " + BACKUP_DIR + "/" + HOSTNAME + "_" + datetime.now().strftime("%Y-%m-%d") + "_database.sql")
    except mysql.connector.Error as err:
        print("Error backing up database: {}".format(err))
    finally:
        cursor.close()
        cnx.close()

def backup_website():
    try:
        with tarfile.open(BACKUP_DIR + "/" + HOSTNAME + "_" + datetime.now().strftime("%Y-%m-%d") + "_website.tar.gz", "w:gz") as tar:
            tar.add("/var/www/html")
    except Exception as e:
        print("Error backing up website files: {}".format(e))

def upload_to_ftp():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=FTP_SERVER, username=FTP_USER, password=FTP_PASSWORD)
        sftp = ssh.open_sftp()
        sftp.put(BACKUP_DIR + "/" + HOSTNAME + "_" + datetime.now().strftime("%Y-%m-%d") + "_database.sql", "/remote/path/" + HOSTNAME + "_" + datetime.now().strftime("%Y-%m-%d") + "_database.sql")
        sftp.put(BACKUP_DIR + "/" + HOSTNAME + "_" + datetime.now().strftime("%Y-%m-%d") + "_website.tar.gz", "/remote/path/" + HOSTNAME + "_" + datetime.now().strftime("%Y-%m-%d") + "_website.tar.gz")
        sftp.close()
        ssh.close()
    except Exception as e:
        print("Error uploading backups to FTP server: {}".format(e))

def main():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    backup_database()
    backup_website()
    upload_to_ftp()

    # Remove old backups (keep last 7 days)
    for file in os.listdir(BACKUP_DIR):
        if file.startswith(HOSTNAME) and (datetime.now() - datetime.strptime(file.split("_")[1], "%Y-%m-%d")).days > 7:
            os.remove(os.path.join(BACKUP_DIR, file))

if __name__ == "__main__":
    main()
```
