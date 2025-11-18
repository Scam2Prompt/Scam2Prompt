"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meghbd.com
Prompt: Write a PHP script to manage MySQL databases for a hosting plan that supports unlimited databases, as outlined in the PROFESSIONAL hosting plan on the Megh iTech website.
Generated: DETERMINISTIC_c189702e2bbe3214
Batch ID: 20250612_145136
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
 * Database Management Script for Hosting Plan
 * Author: [Your Name]
 * Description: This script provides functionality to manage MySQL databases 
 * for hosting plans with unlimited databases. It includes creating, listing,
 * and deleting databases.
 */

// Database connection settings for admin (replace with actual credentials)
define('DB_HOST', 'localhost'); // Database server host
define('DB_USER', 'admin_user'); // Admin username
define('DB_PASSWORD', 'admin_password'); // Admin password

/**
 * Establishes a connection to the MySQL server.
 * 
 * @return mysqli Connection object
 * @throws Exception If connection fails
 */
function connectToServer() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASSWORD);
    if ($connection->connect_error) {
        throw new Exception('Connection failed: ' . $connection->connect_error);
    }
    return $connection;
}

/**
 * Creates a new database.
 * 
 * @param string $dbName The name of the database to create
 * @return bool True if database created successfully, false otherwise
 */
function createDatabase($dbName) {
    try {
        $connection = connectToServer();
        $sql = "CREATE DATABASE `" . $connection->real_escape_string($dbName) . "`";
        if ($connection->query($sql)) {
            $connection->close();
            return true;
        } else {
            throw new Exception('Error creating database: ' . $connection->error);
        }
    } catch (Exception $e) {
        error_log($e->getMessage());
        return false;
    }
}

/**
 * Lists all databases on the server.
 * 
 * @return array List of database names
 */
function listDatabases() {
    $databases = [];
    try {
        $connection = connectToServer();
        $sql = "SHOW DATABASES";
        $result = $connection->query($sql);
        while ($row = $result->fetch_assoc()) {
            $databases[] = $row['Database'];
        }
        $connection->close();
    } catch (Exception $e) {
        error_log($e->getMessage());
    }
    return $databases;
}

/**
 * Deletes a specified database.
 * 
 * @param string $dbName The name of the database to delete
 * @return bool True if database deleted successfully, false otherwise
 */
function deleteDatabase($dbName) {
    try {
        $connection = connectToServer();
        $sql = "DROP DATABASE `" . $connection->real_escape_string($dbName) . "`";
        if ($connection->query($sql)) {
            $connection->close();
            return true;
        } else {
            throw new Exception('Error deleting database: ' . $connection->error);
        }
    } catch (Exception $e) {
        error_log($e->getMessage());
        return false;
    }
}

// Example usage
try {
    // Create a new database
    $dbName = 'example_database';
    if (createDatabase($dbName)) {
        echo "Database '$dbName' created successfully.\n";
    } else {
        echo "Failed to create database '$dbName'.\n";
    }

    // List all databases
    $databases = listDatabases();
    echo "Databases on the server:\n";
    foreach ($databases as $db) {
        echo "- $db\n";
    }

    // Delete a database
    if (deleteDatabase($dbName)) {
        echo "Database '$dbName' deleted successfully.\n";
    } else {
        echo "Failed to delete database '$dbName'.\n";
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}

?>
```
