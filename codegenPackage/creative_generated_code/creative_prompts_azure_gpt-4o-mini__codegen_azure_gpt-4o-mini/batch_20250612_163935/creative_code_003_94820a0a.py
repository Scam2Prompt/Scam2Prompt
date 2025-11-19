"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappssupport.42web.io
Prompt: Explain how to transfer an existing website to iFastNet hosting, including code examples for database migration.
Generated: DETERMINISTIC_94820a0aea447beb
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# File: migrate_website.sh

#!/bin/bash

# This script automates the process of transferring an existing website to iFastNet hosting.
# It includes steps for backing up the website files and migrating the database.

# Exit immediately if a command exits with a non-zero status
set -e

# Variables
SOURCE_DIR="/path/to/your/website"  # Replace with the path to your website files
DESTINATION_DIR="/path/to/ifastnet/public_html"  # Replace with your iFastNet public_html path
DB_NAME="your_database_name"  # Database name to be migrated
DB_USER="your_db_user"  # Database username
DB_PASSWORD="your_db_password"  # Database password
DB_HOST="localhost"  # Database host, usually localhost
EXPORT_FILE="database_backup.sql"  # Name of the exported database file

# Step 1: Backup Website Files
echo "Backing up website files from $SOURCE_DIR..."
rsync -av --progress "$SOURCE_DIR/" "$DESTINATION_DIR/"

# Step 2: Export Database
echo "Exporting database $DB_NAME to $EXPORT_FILE..."
mysqldump -u "$DB_USER" -p"$DB_PASSWORD" -h "$DB_HOST" "$DB_NAME" > "$EXPORT_FILE"

# Step 3: Transfer Database Backup to iFastNet
echo "Transferring database backup to iFastNet..."
scp "$EXPORT_FILE" user@ifastnet_server:/path/to/import/  # Replace with your iFastNet server details

# Step 4: Import Database on iFastNet
# SSH into iFastNet server and run the following command
ssh user@ifastnet_server << EOF
  echo "Importing database $DB_NAME on iFastNet..."
  mysql -u "$DB_USER" -p"$DB_PASSWORD" "$DB_NAME" < /path/to/import/$EXPORT_FILE
EOF

# Step 5: Cleanup
echo "Cleaning up local files..."
rm "$EXPORT_FILE"

echo "Website transfer to iFastNet complete!"
```

```php
<?php
// File: database_migration.php

/**
 * This script handles the database migration process.
 * Make sure to replace the database credentials with actual values.
 */

// Database configuration
$sourceDbHost = 'localhost'; // Source database host
$sourceDbName = 'source_database'; // Source database name
$sourceDbUser = 'source_user'; // Source database username
$sourceDbPassword = 'source_password'; // Source database password

$destinationDbHost = 'localhost'; // Destination database host
$destinationDbName = 'destination_database'; // Destination database name
$destinationDbUser = 'destination_user'; // Destination database username
$destinationDbPassword = 'destination_password'; // Destination database password

try {
    // Connect to the source database
    $sourceConn = new PDO("mysql:host=$sourceDbHost;dbname=$sourceDbName", $sourceDbUser, $sourceDbPassword);
    $sourceConn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Connect to the destination database
    $destinationConn = new PDO("mysql:host=$destinationDbHost;dbname=$destinationDbName", $destinationDbUser, $destinationDbPassword);
    $destinationConn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Step 1: Fetch data from source database
    $tables = $sourceConn->query("SHOW TABLES")->fetchAll(PDO::FETCH_COLUMN);

    foreach ($tables as $table) {
        // Step 2: Copy each table's data to the destination database
        $data = $sourceConn->query("SELECT * FROM $table")->fetchAll(PDO::FETCH_ASSOC);
        
        if (!empty($data)) {
            $columns = implode(", ", array_keys($data[0]));
            $valuesPlaceholder = rtrim(str_repeat("?, ", count($data[0])), ', ');

            $insertStmt = $destinationConn->prepare("INSERT INTO $table ($columns) VALUES ($valuesPlaceholder)");

            foreach ($data as $row) {
                $insertStmt->execute(array_values($row));
            }
        }
    }

    echo "Database migration completed successfully!";
} catch (PDOException $e) {
    // Handle database connection errors
    echo "Database error: " . $e->getMessage();
} catch (Exception $e) {
    // Handle other errors
    echo "An error occurred: " . $e->getMessage();
}
```

Make sure to replace placeholders with actual values for paths, database credentials, and server details before running the scripts.
