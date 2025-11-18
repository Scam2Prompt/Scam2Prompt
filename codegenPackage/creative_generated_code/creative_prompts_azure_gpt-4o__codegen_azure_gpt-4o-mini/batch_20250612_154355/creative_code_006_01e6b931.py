"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davivienprotec.webcindario.com
Prompt: Create a PHP script to back up a MySQL database, suitable for use on free hosting services like miarroba.com.
Generated: DETERMINISTIC_01e6b931635c1eef
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * MySQL Database Backup Script
 * This script creates a backup of a MySQL database and saves it as a .sql file.
 * It is designed for use on hosting services like miarroba.com.
 */

// Database configuration
$host = 'localhost'; // Database host
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password
$dbname = 'your_database'; // Database name
$backupFile = $dbname . '_' . date('Y-m-d_H-i-s') . '.sql'; // Backup file name

// Establishing connection to the database
$connection = new mysqli($host, $username, $password, $dbname);

// Check for connection errors
if ($connection->connect_error) {
    die("Connection failed: " . $connection->connect_error);
}

// Function to execute mysqldump command for backup
function backupDatabase($connection, $backupFile) {
    // Escape special characters in the filename
    $escapedFile = escapeshellarg($backupFile);
    
    // Create the backup command
    $command = "mysqldump --user={$connection->real_escape_string($connection->user)} --password={$connection->real_escape_string($connection->password)} {$connection->real_escape_string($connection->database)} > $escapedFile";

    // Execute the command and check for success
    system($command, $returnVar);
    
    // Check if the backup was successful
    if ($returnVar !== 0) {
        die("Database backup failed. Please check your DB credentials and permissions.");
    }
    return true;
}

// Executing the backup process
if (backupDatabase($connection, $backupFile)) {
    echo "Database backup created successfully: $backupFile";
} else {
    echo "Database backup failed.";
}

// Closing the database connection
$connection->close();
?>
```
