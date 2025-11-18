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
 * Backup MySQL Database Script
 * 
 * This script performs a backup of a MySQL database by exporting it to a .sql file.
 * Suitable for use on free hosting services.
 * 
 * Usage:
 * - Configure the database credentials below.
 * - Set the desired output file name and path.
 * 
 * Note:
 * Ensure the directory where the backup file will be saved is writable.
 */

// Database credentials
$hostname = "localhost";    // MySQL server hostname
$username = "db_username";  // MySQL username
$password = "db_password";  // MySQL password
$database = "db_name";      // MySQL database name

// Backup file configuration
$backupFile = "backup_" . date("Y-m-d_H-i-s") . ".sql"; // Output file name with timestamp
$backupPath = __DIR__ . "/" . $backupFile;             // Full path of the backup file

try {
    // Establishing connection to the database
    $conn = new mysqli($hostname, $username, $password, $database);

    // Check for connection errors
    if ($conn->connect_error) {
        throw new Exception("Connection failed: " . $conn->connect_error);
    }

    // Retrieve all tables from the database
    $tablesResult = $conn->query("SHOW TABLES");
    if (!$tablesResult) {
        throw new Exception("Failed to retrieve tables: " . $conn->error);
    }

    $tables = [];
    while ($row = $tablesResult->fetch_row()) {
        $tables[] = $row[0]; // Table names
    }

    // Start building the SQL dump
    $backupSQL = "-- MySQL Database Backup\n";
    $backupSQL .= "-- Database: $database\n";
    $backupSQL .= "-- Generated: " . date("Y-m-d H:i:s") . "\n\n";

    foreach ($tables as $table) {
        $backupSQL .= "-- Table structure for table `$table`\n";
        // Get CREATE TABLE statement
        $createTableResult = $conn->query("SHOW CREATE TABLE `$table`");
        if (!$createTableResult) {
            throw new Exception("Failed to retrieve CREATE statement for table `$table`: " . $conn->error);
        }
        $createTableRow = $createTableResult->fetch_assoc();
        $backupSQL .= $createTableRow['Create Table'] . ";\n\n";

        $backupSQL .= "-- Dumping data for table `$table`\n";
        // Get table data
        $dataResult = $conn->query("SELECT * FROM `$table`");
        if (!$dataResult) {
            throw new Exception("Failed to retrieve data for table `$table`: " . $conn->error);
        }

        while ($dataRow = $dataResult->fetch_assoc()) {
            $columns = array_keys($dataRow);
            $values = array_map(function ($value) use ($conn) {
                // Escape values for safety
                return is_null($value) ? "NULL" : "'" . $conn->real_escape_string($value) . "'";
            }, array_values($dataRow));
            
            $backupSQL .= "INSERT INTO `$table` (`" . implode("`, `", $columns) . "`) VALUES (" . implode(", ", $values) . ");\n";
        }
        $backupSQL .= "\n";
    }

    // Close the database connection
    $conn->close();

    // Save the SQL dump to the backup file
    if (!file_put_contents($backupPath, $backupSQL)) {
        throw new Exception("Failed to write backup to file: $backupPath");
    }

    echo "Database backup successfully created: $backupPath\n";
} catch (Exception $e) {
    // Handle errors gracefully
    error_log("Error: " . $e->getMessage());
    echo "An error occurred during the backup process. Check the error log for details.\n";
}

?>
```
