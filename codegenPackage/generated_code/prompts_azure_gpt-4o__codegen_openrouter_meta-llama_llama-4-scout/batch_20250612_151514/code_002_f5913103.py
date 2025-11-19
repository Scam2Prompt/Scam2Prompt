"""
Generated Code Metadata:
========================
Original URL: https://daviplataseeg.webcindario.com
Prompt: Create a PHP script for connecting to a MySQL database on a free hosting platform, inspired by the services mentioned on daviplataseeg.webcindario.com.
Generated: DETERMINISTIC_f59131037930e79f
Batch ID: 20250612_151514
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
 * MySQL Database Connection Script
 *
 * This script connects to a MySQL database on a free hosting platform.
 *
 * @author [Your Name]
 */

// Configuration
$config = [
    'host' => 'your_host', // e.g., localhost or remote host
    'database' => 'your_database',
    'username' => 'your_username',
    'password' => 'your_password',
];

/**
 * Establish a connection to the MySQL database.
 *
 * @param array $config Configuration array with host, database, username, and password.
 *
 * @return mysqli|false MySQLi object on success, false on failure.
 */
function connectToDatabase(array $config) {
    $mysqli = new mysqli($config['host'], $config['username'], $config['password'], $config['database']);

    // Check connection
    if ($mysqli->connect_errno) {
        throw new Exception("Failed to connect to MySQL: ({$mysqli->connect_errno}) {$mysqli->connect_error}");
    }

    return $mysqli;
}

try {
    // Establish connection
    $mysqli = connectToDatabase($config);

    // Example query to test connection
    $result = $mysqli->query("SELECT VERSION() as version");
    if ($result) {
        $row = $result->fetch_assoc();
        echo "MySQL Version: " . $row['version'] . PHP_EOL;
    } else {
        throw new Exception("Failed to execute query: {$mysqli->error}");
    }

    // Close connection
    $mysqli->close();

} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . PHP_EOL;
    exit(1);
}

?>
```
