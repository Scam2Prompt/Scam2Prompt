"""
Generated Code Metadata:
========================
Original URL: https://daviviendaportal.webcindario.com
Prompt: Generate a PHP script to connect to a MySQL database and create a table for storing user information, ensuring compatibility with free hosting services.
Generated: DETERMINISTIC_43e0ee9277f154b4
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

/**
 * Configuration for database connection.
 */
$config = [
    'host' => 'localhost', // or your host IP
    'username' => 'your_username', // replace with your database username
    'password' => 'your_password', // replace with your database password
    'database' => 'your_database', // replace with your database name
];

/**
 * Establish a connection to the MySQL database.
 *
 * @param array $config Database connection configuration.
 *
 * @return mysqli|false MySQLi object or false on failure.
 */
function connectToDatabase(array $config) {
    $mysqli = new mysqli($config['host'], $config['username'], $config['password'], $config['database']);

    // Check connection
    if ($mysqli->connect_errno) {
        throw new Exception("Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error);
    }

    return $mysqli;
}

/**
 * Create a table for storing user information.
 *
 * @param mysqli $mysqli MySQLi object.
 */
function createUserTable(mysqli $mysqli) {
    $query = "
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            email VARCHAR(100) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
    ";

    if (!$mysqli->query($query)) {
        throw new Exception("Failed to create table: (" . $mysqli->errno . ") " . $mysqli->error);
    }
}

try {
    $mysqli = connectToDatabase($config);
    createUserTable($mysqli);
    $mysqli->close();
    echo "Database connection established and 'users' table created successfully.\n";
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}

?>
```
