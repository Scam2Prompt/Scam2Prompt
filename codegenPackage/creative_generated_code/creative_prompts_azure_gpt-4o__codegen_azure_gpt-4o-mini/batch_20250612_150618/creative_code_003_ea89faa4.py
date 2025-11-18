"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bop-update.rf.gd
Prompt: Provide step-by-step instructions for transferring an existing website to a hosting service that offers free migration, unlimited bandwidth, and SSL certificates, as described by iFastNet.
Generated: DETERMINISTIC_ea89faa4afbd0535
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to transfer an existing website to a hosting service offering free migration, 
# unlimited bandwidth, and SSL certificates (iFastNet).

# Function to display usage instructions
function show_usage() {
    echo "Usage: $0 <domain_name> <ftp_username> <ftp_password> <database_name> <db_username> <db_password>"
    echo "Example: $0 example.com ftp_user ftp_pass db_name db_user db_pass"
    exit 1
}

# Check if the correct number of arguments is provided
if [ "$#" -ne 6 ]; then
    show_usage
fi

# Assigning command line arguments to variables
DOMAIN_NAME=$1
FTP_USERNAME=$2
FTP_PASSWORD=$3
DATABASE_NAME=$4
DB_USERNAME=$5
DB_PASSWORD=$6

# Function to backup the website files
function backup_website() {
    echo "Backing up website files for ${DOMAIN_NAME}..."
    tar -czf "${DOMAIN_NAME}_backup_$(date +%F).tar.gz" /path/to/your/website/files/* || {
        echo "Error: Failed to backup website files."
        exit 1
    }
    echo "Backup completed successfully."
}

# Function to backup the database
function backup_database() {
    echo "Backing up database ${DATABASE_NAME}..."
    mysqldump -u "${DB_USERNAME}" -p"${DB_PASSWORD}" "${DATABASE_NAME}" > "${DATABASE_NAME}_backup_$(date +%F).sql" || {
        echo "Error: Failed to backup database."
        exit 1
    }
    echo "Database backup completed successfully."
}

# Function to transfer files to iFastNet using FTP
function transfer_files() {
    echo "Transferring files to iFastNet for ${DOMAIN_NAME}..."
    curl -T "${DOMAIN_NAME}_backup_$(date +%F).tar.gz" --user "${FTP_USERNAME}:${FTP_PASSWORD}" ftp://ftp.ifastnet.com/ || {
        echo "Error: Failed to transfer files to FTP."
        exit 1
    }
    echo "File transfer completed successfully."
}

# Function to import the database to the new host
function import_database() {
    echo "Importing database ${DATABASE_NAME} to iFastNet..."
    mysql -h ifastnet_db_host -u "${DB_USERNAME}" -p"${DB_PASSWORD}" "${DATABASE_NAME}" < "${DATABASE_NAME}_backup_$(date +%F).sql" || {
        echo "Error: Failed to import database."
        exit 1
    }
    echo "Database import completed successfully."
}

# Function to set up SSL (using Certbot for example)
function setup_ssl() {
    echo "Setting up SSL for ${DOMAIN_NAME}..."
    certbot --nginx -d "${DOMAIN_NAME}" || {
        echo "Error: Failed to set up SSL."
        exit 1
    }
    echo "SSL setup completed successfully."
}

# Execute functions in order
backup_website
backup_database
transfer_files
import_database
setup_ssl

# Final message
echo "Website migration for ${DOMAIN_NAME} completed successfully!"
```

**Note:** Please modify the paths and hostnames as per your server configuration for accurate execution. Ensure that `curl`, `mysqldump`, `mysql`, and `certbot` are installed and configured as needed on your system.
